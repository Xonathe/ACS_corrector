from form import *
from auth import *
import sys
import pypyodbc
from fast_bitrix24 import Bitrix
import fdb
from datetime import datetime
from threading import Thread


class Form(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("AddMissingData")
        self.add.released.connect(self.add_action)
        self.ok.released.connect(self.ok_action)
        now = QDate.currentDate()
        self.time1.setDate(now)
        self.time2.setDate(now)
        bases = ["MsSQL", "Firebird"]
        self.base.addItems(bases)
        self.person_line.setEnabled(False)
        self.ok.setEnabled(False)
        self._list = []
        self.bitrix = Bitrix(webhook)
        self.person.toggled.connect(lambda: self.person_action(self.person))

    def add_action(self):
        self.add.setEnabled(False)
        my_time = self.time1.dateTime().toString("yyyy-MM-dd hh:mm:ss")
        my_time2 = self.time2.dateTime().toString("yyyy-MM-dd hh:mm:ss")
        self.stackedWidget.setCurrentIndex(1)
        self.resize(750, 500)
        get_base = self.base.currentText()
        if get_base == "MsSQL":
            # p = Process(target=self.get_data_mssql(my_time, my_time2))
            # p.start()
            # p.join()
            self.get_data_mssql(my_time, my_time2)
        elif get_base == "Firebird":
            self.get_data_firebird()

    def person_action(self, check):
        if check.isChecked():
            self.person_line.setEnabled(True)
        else:
            self.person_line.setEnabled(False)

    def ok_action(self):
        self.resize(265, 205)
        self.stackedWidget.setCurrentIndex(0)
        self.add.setEnabled(True)
        self.ok.setEnabled(False)

    def get_data_mssql(self, tm1, tm2):
        self.con_mssql = pypyodbc.connect(
            f'DRIVER=SQL Server;SERVER={mssql_server};DATABASE={sql_db};UID={sql_login};PWD={sql_pass}')
        cursor = self.con_mssql.cursor()
        cursor.execute(
            f"""
            select * from Journals WHERE dateadd(SECOND, (SystemDate / 10000000) - 11644473600, convert(datetime, '1970-1-1 03:00:00')) < convert(datetime, '{tm2}')
            and dateadd(SECOND, (SystemDate / 10000000) - 11644473600, convert(datetime, '1970-1-1 03:00:00')) > convert(datetime, '{tm1}')
            AND UserName IS NOT NULL
            AND CardNo != '0'
            AND EmployeeUID IN (SELECT UID FROM Employees where DepartmentUID IS NOT NULL)
            """
        )
        for row in cursor:
            if self.person.isChecked() == True:
                fio = self.person_line.text()
                if row[14] == fio:
                    app_time = datetime.fromtimestamp((row[13] // 10000000) - 11644473600)
                    self._list.append([app_time.strftime('%d.%m.%Y %H:%M:%S'), row[14], row[9]])
            else:
                app_time = datetime.fromtimestamp((row[13] // 10000000) - 11644473600)
                self._list.append([app_time.strftime('%d.%m.%Y %H:%M:%S'), row[14], row[9]])
        Thread(target=self.set_log, daemon=True).start()
        # self.set_log()

    def set_log(self):
        count = 1
        for u in sorted(self._list):
            # self.write_data(u)
            elem = self.check_entry(u)
            if elem != ([],):
                self.log.addItems([f"{count}. Добавлено => {u[0]} {u[1]} {u[2]}"])
                self.log.scrollToBottom()
                count += 1
        if len(self._list) != 0:
            self.log.addItems([f"-----===== Всего добавлено {count - 1} =====-----"])
        else:
            self.log.addItems(["Ничего не найдено"])
        self.ok.setEnabled(True)
        self.con_mssql.close()
        self._list.clear()

    def get_data_firebird(self):
        self.my_time = self.time1.dateTime().toString("yyyy-MM-dd hh:mm:ss")
        self.my_time2 = self.time2.dateTime().toString("yyyy-MM-dd hh:mm:ss")
        self.con_fbd = fdb.connect(host=fb_host_ip, database=fb_db_path, user=fb_login, password=fb_pass,
                                   charset='none')

        self.con_fbd.close()

    def write_data(self, data: list):
        """Записивые полученные данные в справочник СУД"""
        self.bitrix.call('lists.element.add',
                         [
                             {
                                 'IBLOCK_TYPE_ID': 'bitrix_processes',
                                 'IBLOCK_ID': '153',
                                 'ELEMENT_CODE': f'{data[1]} {data[0]}',
                                 'FIELDS': {
                                     'NAME': f'{data[1]} {data[0]}',
                                     'PROPERTY_812': f'{data[1]}',
                                     'PROPERTY_815': f'{data[0]}',
                                     'PROPERTY_793': f'{data[2]}',
                                     'PROPERTY_814': 'Импортировано',
                                 }
                             }
                         ]
                         )

    def check_entry(self, data: list):
        """Проверяет записана ли запись в Битрикс"""
        element = self.bitrix.call('lists.element.get',
                                   [
                                       {
                                           'IBLOCK_TYPE_ID': 'bitrix_processes',
                                           'IBLOCK_ID': '153',
                                           'ELEMENT_CODE': f'{data[1]} {data[0]}'
                                       }
                                   ]
                                   )
        return element


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Form()
    window.show()
    sys.exit(app.exec_())
