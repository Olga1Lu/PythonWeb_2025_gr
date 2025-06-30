# Коллекции
# Множества, списки, словари, коллекции
# Таблица симолов, зашифровка, расшифровка
# s = '\xB0'  # назначили заранее спец.символ
# u = '\u2603'  # знак снеговика в 16-ричной системе
# print('25' + s + 'C°')
# print(u)
# print(f'Код снеговика в unic: {ord('☃')}')
# print(chr(176))
#удобные ф-ции
# ord(символ) - возвращает код символа в Unicode
# chr(код) - возвращает символ по коду в Unicode


 #Методы строк
#abc = 'абвгдеёжзиклмнопрстуфхцчшщъыьэюя'
# 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith',
# 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha',
# 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric',
# 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower',
# 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace',
# 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split',
# 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper',
# 'zfill']

# Срез (есть у строки и др.коллекций, кроме множеств)
# [начало (вкл): окончание(не вкл): шаг]
# s = 'Добрый день'
# print(s[:11])  # от начала до зад.индекса
# print(s[7:])  # от зад. индекса до конца
# print(s[7:11]) # от n до m ( m не вкл)
# print(s[:-6]) # с начала до позиции рассчитанной с конца слова
# print(s[::-1])  #  инверсия

# палиндром или нет?
# s = input('Введите слово: ').strip()
#
# s_n = s[::-1]
# if s.lower() == s[::-1].lower() :
#     print(f'слово "{s}" - палиндром')
# else:
#     print(f'слово "{s}" - не палиндром')

# s = 'Дорог Рим город или дорог Миргород'
#
# print(s[26:] + ' ' + (s[:5].lower() + '...')*2)

s = 'Дорог Рим '
t = s.lower()
cit = t[:5][::-1]  # сначала берем срез, затем его инвертируем
res = cit + ' ' + t[6:][::-1] + cit
print(res)












