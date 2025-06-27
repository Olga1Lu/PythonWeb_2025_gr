# Коллекции
# Множества, списки, словари, коллекции
# Таблица симолов, зашифровка, расшифровка
from operator import index

s = '\xB0'  # назначили заранее спец.символ
u = '\u2603'  # знак снеговика в 16-ричной системе
# print('25' + s + 'C°')
# print(u)
# print(f'Код снеговика в unic: {ord('☃')}')
# print(chr(176))
#удобные ф-ции
# ord(символ) - возвращает код символа в Unicode
# chr(код) - возвращает символ по коду в Unicode

# word = input('введите фразу для зашифровки: ')
# s = set()
# for ch in word :
#      s.add(ord(ch))
# print(s)
# f = ''
# for ch in s :
#     f += chr(ch)
# print(f)

 # Задача Шифр  Цезаря ДЗ

 #Методы строк
#abc = 'абвгдеёжзиклмнопрстуфхцчшщъыьэюя'
# 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
#pf = 'Язык Python'
# print(pf.lower())
# print(pf.upper())
# print(pf.capitalize()) #только в первом слове заглавная буква
# print(pf.title()) # в каждом слове заглавная буква
# print('Ура ' * 3)
# print('Телевизор'.count('е')) # сколько раз фрагмент "e" входит в исх.строку
# print('Телевизор'.index('е')) # номер символа в строке

s = input('Введите слово: ')

for i in range (len(s)) :
    print(s[i]*(i+1), end='')








