import time
from datetime import datetime
from fast_bitrix24 import Bitrix


def write_data(data: list):
    bitrix = Bitrix("https://dubrovnik.su/rest/86/yil3pl7b3c1ooeo5")
    """Записивые полученные данные в справочник СУД"""
    bitrix.call('lists.element.add',
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


if __name__ == '__main__':
    write_data(['06.10.2021 08:34:35', 'Коньков Виктор Александрович', 'ВХОД ОИТ'])
