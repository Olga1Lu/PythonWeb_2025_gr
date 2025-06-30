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

# print(pf.lower())
# print(pf.upper())
# print(pf.capitalize()) #только в первом слове заглавная буква
# print(pf.title()) # в каждом слове заглавная буква
# print('Ура ' * 3)
# print('Телевизор'.count('е')) # сколько раз фрагмент "e" входит в исх.строку
# print('Телевизор'.index('е')) # номер символа в строке

# метод  strip
# s = 'ротор'
# print(s.strip())  #уберет пробелы с двух сторон
# print(s.lstrip()) #уберет слева
# print(s.rstrip())  #уберет справа
# print(s.strip('р'))
#
# temp = int(input('Введите слово : ').strip()) # корректировка ввода

# Методы startswith и swith - удобно находить фрагменты текста (сочетания символов в конце или начале слова)

# s = 'Смотреть'
#
# if s.lower().startswith('см') :
#     print('да')
#
# if s.endswith('еть') :
#     print('да')


# метов find() первое вхождение заданной подстроки, если вхождения нет, вернется "-1"
# 1. find ('подстрока')
# 2. find ('подстрока', start)
# 3. find ('подстрока', start, stop)
# s = 'Смотреть, вертеть, видеть'
# index = s.find('ть')  #  ищем с начала строки s
# index = s.find('ть', 10)  #  ищем с позиции start, но номер позиции будет указан с начала  строки s
# index = s.find('ть', 10, 16)  #  ищем с позиции start  до позиции stop, но номер позиции будет указан с начала  строки s

# s = 'синхрофазотрон'
# count = 0
# ch = input('Введите букву')
# ind = ''
# if ch in s :
#     count = s.count(ch)
#     print(f'Буква {ch} встречается в слове "{s}" {count} раз ')
#     print('Ее позиция/позиции:', end = ' ')
#     start = 0
#     for i in range (count) :
#         pos = s.find(ch, start)
#         start += 1
# #дописать
#
# else:
#     print(f'Буквы {ch} нет в слове')

# replace (что, на что) - полная замена
# s = 'тиливизор'
# print(s.replace('и', 'е', 2)) # что на что менять, сколько раз

s = '+7-012-345-67-89' #надо +7 (012) 345-67-89

res = s.replace('-', ' (', 1)
res = res.replace('-', ') ',1)
print(res)

# или в одной строке

print(s.replace('-',
                ' (',
                1).replace('-', ') ',1))









