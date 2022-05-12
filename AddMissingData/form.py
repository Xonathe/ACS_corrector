# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(265, 205)
        Widget.setMinimumSize(QSize(265, 205))
        Widget.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(Widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.main_page = QWidget()
        self.main_page.setObjectName(u"main_page")
        self.verticalLayout_3 = QVBoxLayout(self.main_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.title = QLabel(self.main_page)
        self.title.setObjectName(u"title")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.title, 0, Qt.AlignHCenter)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.base_label = QLabel(self.main_page)
        self.base_label.setObjectName(u"base_label")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.base_label.sizePolicy().hasHeightForWidth())
        self.base_label.setSizePolicy(sizePolicy)
        self.base_label.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_3.addWidget(self.base_label)

        self.base = QComboBox(self.main_page)
        self.base.setObjectName(u"base")

        self.horizontalLayout_3.addWidget(self.base)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.person = QCheckBox(self.main_page)
        self.person.setObjectName(u"person")
        sizePolicy.setHeightForWidth(self.person.sizePolicy().hasHeightForWidth())
        self.person.setSizePolicy(sizePolicy)
        self.person.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_4.addWidget(self.person)

        self.person_line = QLineEdit(self.main_page)
        self.person_line.setObjectName(u"person_line")
        self.person_line.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.person_line)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.s_label = QLabel(self.main_page)
        self.s_label.setObjectName(u"s_label")
        sizePolicy.setHeightForWidth(self.s_label.sizePolicy().hasHeightForWidth())
        self.s_label.setSizePolicy(sizePolicy)
        self.s_label.setMinimumSize(QSize(20, 0))

        self.horizontalLayout_2.addWidget(self.s_label)

        self.time1 = QDateTimeEdit(self.main_page)
        self.time1.setObjectName(u"time1")
        self.time1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.time1)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.po_label = QLabel(self.main_page)
        self.po_label.setObjectName(u"po_label")
        sizePolicy.setHeightForWidth(self.po_label.sizePolicy().hasHeightForWidth())
        self.po_label.setSizePolicy(sizePolicy)
        self.po_label.setMinimumSize(QSize(20, 0))

        self.horizontalLayout.addWidget(self.po_label)

        self.time2 = QDateTimeEdit(self.main_page)
        self.time2.setObjectName(u"time2")
        self.time2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.time2)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.add = QPushButton(self.main_page)
        self.add.setObjectName(u"add")

        self.verticalLayout_3.addWidget(self.add)

        self.stackedWidget.addWidget(self.main_page)
        self.log_page = QWidget()
        self.log_page.setObjectName(u"log_page")
        self.verticalLayout_2 = QVBoxLayout(self.log_page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.log = QListWidget(self.log_page)
        self.log.setObjectName(u"log")

        self.verticalLayout_2.addWidget(self.log)

        self.ok = QPushButton(self.log_page)
        self.ok.setObjectName(u"ok")

        self.verticalLayout_2.addWidget(self.ok)

        self.stackedWidget.addWidget(self.log_page)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.retranslateUi(Widget)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.title.setText(QCoreApplication.translate("Widget", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0432 Bitrix24 \u043d\u0435\u0434\u043e\u0441\u0442\u0430\u044e\u0449\u0438\u0435 \u0434\u0430\u043d\u043d\u044b\u0435 \u0421\u041a\u0423\u0414", None))
        self.base_label.setText(QCoreApplication.translate("Widget", u"\u0411\u0430\u0437\u0430", None))
        self.person.setText(QCoreApplication.translate("Widget", u"\u0424\u0418\u041e", None))
        self.s_label.setText(QCoreApplication.translate("Widget", u"\u0421", None))
        self.po_label.setText(QCoreApplication.translate("Widget", u"\u041f\u043e", None))
        self.add.setText(QCoreApplication.translate("Widget", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.ok.setText(QCoreApplication.translate("Widget", u"\u041e\u041a", None))
    # retranslateUi

