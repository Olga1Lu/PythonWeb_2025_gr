# Коллекции
# Множества, списки, словари, коллекции
from operator import index

from pyexpat.errors import messages

#Создание аббревиатур
# lst = []
# while (word := input('Введите слово: ').strip()) != '' :
#     lst.append((word[0].upper))
#
# print('Получилась аббревиатура', end=':')
# print(*lst, sep=' ') # выведет перечень аргументов с разделителем пробел

# Кортеж (tuple) список не изменяемый
# множ-ва, списки, строки можно преобразовать в кортежи
# t = (1,) создание кортежа из одного элемента
# t = 36,6 тоже создание кортежа из одного элемента
# BLACK = (0, 0, 0)
# empty = ()
# s = 'Python'
# t = tuple(s)
# print(t)
# t1 = tuple(s) + ('.',)
# print(t1)
#
# # методы кортежей
# #count', 'index
#
# cards = [(7, 'червей'), ('туз', 'пик')]
#
# print( (7>2)) # кортежи можно сравнивать
# print((1,2) == (1,2))
# print((1,2) < (1,3))
# a = 3
# b = 4
# a,b = b,a переприсвоение

#chanels = ['red', 'green', 'blue']
#chanels = [1,2,3]
#r,g,b = chanels # распаковка: кол-во переменных должно равняться кол-ву эл-тов, строки и мн-ва тоже поддерживают
#r, *g = chanels # частичная распаковка, r=red, все остальное в список "g"
#print(g)
# a, b = input(), input() #присваивание через ввод
# a, b, c = 1, 2, 3  # прямое присваивание
# a, b = [1, 2], 3 # упаковка

# chanels = [128,200,155]
# r, g, b = chanels
# print((r, g, b))

#Студент и средний балл
#spis = []
# while(fname := input('введите фамилию студента: ')) != '' :
#     ball = float(input('его средний балл? '))
#     spis.append((fname, ball))
# N = 3
# studs = []
# for i in range (N) :
#     stud, aver = input('Введите фамилию:'), float(input('Средний балл ? '))
#     studs.append((stud, aver))
#
# print(studs)
#
# for st in studs :
#     stud, aver = st
#     print('студент: ', stud)
#     print('Средний балл: ', aver)

# Функция sorted()
# s = {'Иванов', 'Петров', 'Сидоров'}
# # lst = list(s)
# # lst.sort()
# r = False
# lst = sorted(s, reverse=r)  #возвращает сортированный список, можно сразу применить к s
# print(*lst, sep=', ')

# enumerate () - в цикле  for возвращает пару (i, v)
fio = ['Иванов', 'Петров', 'Сидоров']

# for item in enumerate(fio) :
#     print(item)

# for i, v in enumerate(fio) :
#     print(f'{i+1}. {v}.')

# Продолжим методы строки: split(), join()

# text = 'один два три четыре'
# ip = '192.168.0.1'
# # split -  разделяет строку по какому-либо разделителю (фрагменту строки), возвращает список
# lst = ip.split('.')
# print(lst)
# txt2 = '-'.join(lst)
# print(txt2)
#
# #['192', '168', '0', '1']

# DZ 30_06

# V1.
# stop_lst = ['зима', 'газ', 'свежий', 'темно']
# temp = []
#
# while (word:= (input('Введите фразу: ')).lower()) != '' :
#     lst = message.split()
# for ch in lst :
#     if ch not in stop_lst :
#         temp.append(ch)
# res = sorted(temp)
#
# for i, v in enumerate(res, 1) :
#     print(f'{i}. {v}')

# V2
############################################
# списочные выражения (list comprehension)
# создадим список из квадратов чисел от 1 до 9
# 1 способ
# squares = []
# for i in range (10) :
#     squares.append(i**2)
# print(*squares, sep=', ')
#
# # 2 теперь исп списочные выражения :
# squares = [i**2 for i in range(10)]
# print(*squares, sep=', ')

#список квадратов четных чисел
# squares = [i**2 for i in range(10) if i % 2 == 0]
# print(*squares, sep=', ')

# два цикла внутри
# произведения  i * j
#1 станд.способ, получится не список
# for i in range(3) :
#     for j in range(3):
#         print(i*j)
# 2 способ получится список
#print([i*j for i in range(3) for j in range(3)])

# n = '500 600 700 800'
# approved = [500, 800]
# print([int (i) for i in n.split() if int(i) in approved])  # сделать список целых чисел

# задачи
#каждое третье слово на экран
text = 'Списочные выражения применяются для эффективности кода'
#print([ch for ch in text.split() if (text.index(ch)+1) % 3])  # не получается каждое 3 слово - почему?

res = [ch for ch in text.split()[2::3]]  # используем срез от text
print(res)

# если не ставить кв.скобки снаружи, то получится итератор
# можно преобр-ть во множество




















