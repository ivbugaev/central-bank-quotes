# Автор модуля: Бугаев Иван / Telegram: @ivtmn72 / E-mail: iustum1@ya.ru
# Модуль для импорта котировок с Центрального банка легальным (официальным) способом
# https://cbr.ru/development/SXML/

from central_bank_quotes import CentralBankQuotes

# Создаем объект класса
quotes = CentralBankQuotes()

# Строки документации
# print(quotes.set_date.__doc__)


# Получаем дату для импорта котировок (по умолчанию задается текущая)
quotes.get_date()

# Задаём свою дату (день, месяц, год)
quotes.set_date('10','05','2025')

# Получаем дату для импорта котировок
quotes.get_date()

# Инициализируем получение котировок с официального источника и формирование словарей
quotes.load_quotes()

# Получаем справочник котировок по коду валюты (цифрами)
quotes_by_num = quotes.get_quotes_by_num_dict()
#print(quotes_by_num)
# Получаем котировку для валюты с кодом 978
print(quotes_by_num[978]);

# Получаем справочник котировок по коду валюты (символами)
quotes_by_char = quotes.get_quotes_by_char_dict()
#print(quotes_by_char)
# Получаем котировку для валюты с кодом EUR
print(quotes_by_char['EUR']);

# Получаем справочник котировок по коду валюты (цифрами) в формате JSON
quotes_by_num_json = quotes.get_quotes_by_num_json()
#print(quotes_by_num_json)

# Получаем справочник котировок по коду валюты (символами) в формате JSON
quotes_by_char_json = quotes.get_quotes_by_char_json()
print(quotes_by_char_json)
