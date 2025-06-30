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

# s = 'Дорог Рим '
# t = s.lower()
# cit = t[:5][::-1]  # сначала берем срез, затем его инвертируем
# res = cit + ' ' + t[6:][::-1] + cit
# print(res)

# Списки (list)

# s = {'3','4','5'} # множество, нельзя сортировать и т.д.
# lst = list(s) # превратили в список, можно сортировать и т.д.
#
#
# l = list(range(1,11)) # создали список от 1 до 10

# создание списка (2 варианта)
# lst = [] или lst = [1, 2,3]
# lst = list()  # применяется реже
#lst = list('Python')
# lst = [1,2,3]
#
# print(lst[:2])

# Методы списков
#'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# s = 'сабака'
# lst = list(s)
# lst[1] = 'о'
# print(lst)

# s = []
# for i in range(11) :
#     s.append(i)  # добавляет элемент в конец
# print(s)

# s1 = [1, 2, 3]
# s2 = [4, 5, 6]
# s3 = s1 + ['f']
# s3[0] = 22
# print(s3)
# s = s1.extend(s2)
# s = s1 + s2  #конкатенация списков

#lst = list(range(10)) # создание списка чисел от 1 до 10
# sl = lst[:len(lst):2] # срез
# print(sl)
# for item in range(0, len(lst), 2) :
#     print(lst[item], ' - ', lst[item]**2)

#del lst[2] # удалили цифру 2 и список сдвинулся
# del lst[::2]  # удалили каждый второй элемент
# remove - удаляет первое вхождение значения, если нет этого значения, то выдает ошибку
# pop - удаляет эл-т по индексу, если не задан индекс, то последний
#lst.pop(5)

#list = [1,7,3,5,6,4,2]
# lst.sort()
# lst.reverse()   #  или можно сделать lst.sort(reverse= True)
#print(lst)

# a = ['a', 'b', 'c']
# b = a.copy()  # или a[:]
# b.append('d')
# print((id(a)))
# print(id(b))
# print(a)
# print(b)


#окрошка
sup = []

while (ingr:= input ('Добавьте ингредиент: ')) != '' :
    sup.append(ingr)
temp = set(sup)
sup = list (temp)
sup.sort()
print(f'всего: {len(sup)} ингредиентов')
for i in range (len(sup)) :
    print(f'\t{i+1}. {sup[i]}' )










