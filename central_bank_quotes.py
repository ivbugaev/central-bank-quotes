# Автор модуля: Бугаев Иван / Telegram: @ivtmn72 / E-mail: iustum1@ya.ru
# Модуль для импорта котировок с Центрального банка легальным (официальным) способом
# https://cbr.ru/development/SXML/

import time
import xml.etree.ElementTree as et
import urllib.request
import json

# Класс для импорта котировок с Центрального банка легальным (официальным) способом
class CentralBankQuotes():
    # Метод инициализации
    def __init__(self):
        self.hidden_now = time
        self.hidden_day = self.hidden_now.strftime("%d")
        self.hidden_month = self.hidden_now.strftime("%m")
        self.hidden_year = self.hidden_now.strftime("%Y")
        self.quotes_num_code_dict = {}
        self.quotes_char_code_dict = {}
        self.quotes_num_code_json = json.dumps({}, indent=4)
        self.quotes_char_code_json = json.dumps({}, indent=4)

    # День за который нужно получить котировки
    def set_date(self, day, month, year):
        '''
        Задаём пользовательскую дату
        '''
        self.hidden_day = day
        self.hidden_month = month
        self.hidden_year = year

    # Отображение пользовательской даты
    def get_date(self):
        '''
        Получаем текущую дату
        '''
        print(f'Текущая дата: {self.hidden_day}.{self.hidden_month}.{self.hidden_year}')

    # Загрузка котировок с ресурса и сохранение их в JSON
    def load_quotes(self):
        '''
        Инициализируем получение котировок с официального источника и формирование словарей
        '''
        link = f'https://cbr.ru/scripts/XML_daily.asp?date_req={self.hidden_day}/{self.hidden_month}/{self.hidden_year}'
        tree = et.ElementTree(file=urllib.request.urlopen(link))
        root = tree.getroot()
        for valute in root.findall('Valute'):
            num_code = int(valute.find('NumCode').text)
            char_code = valute.find('CharCode').text
            nominal = int(valute.find('Nominal').text)
            name = valute.find('Name').text
            value = float(valute.find('Value').text.replace(',','.'))
            vunit_rate = float(valute.find('VunitRate').text.replace(',','.'))

            # справочник для определенной валюты
            quote_dict = {'num_code': num_code, 'char_code': char_code, 'nominal': nominal, 'name': name, 'value': value, 'vunit_rate': vunit_rate}

            # справочник валют (ключ: код валюты цифрой, например 978 для EUR)
            self.quotes_num_code_dict[num_code] = quote_dict
            # справочник валют (ключ: код валюты символами, например EUR)
            self.quotes_char_code_dict[char_code] = quote_dict

    # Возвращает справочник валют (ключ: код валюты цифрой, например 978 для EUR)
    def get_quotes_by_num_dict(self):
        return self.quotes_num_code_dict
    
    # Возвращает справочник валют (ключ: код валюты символами, например EUR)
    def get_quotes_by_char_dict(self):
        return self.quotes_char_code_dict

    # Возвращает справочник валют (ключ: код валюты цифрой, например 978 для EUR) в формате JSON
    def get_quotes_by_num_json(self):
        return json.dumps(self.quotes_num_code_dict, indent=4)
    
    # Возвращает справочник валют (ключ: код валюты символами, например EUR) в формате JSON
    def get_quotes_by_char_json(self):
        return json.dumps(self.quotes_char_code_dict, indent=4)
