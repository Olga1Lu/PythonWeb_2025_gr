#import math
# def num_to_word(num) :
#     e_d = ['один', 'два', 'три','четыре', 'пять', 'шесть','семь', 'восемь', 'девять',
#            'десять', 'одиннадцать', 'двенадцать', 'тринадцать','четырнадцать', 'пятнадцать',
#            'шестнадцать', 'семнадцать',  'восемнадцать', 'девятнадцать', '']
#     d_d = ['двадцать', 'тридцать', 'сорок', 'пятьдесят','шестьдесят', 'семьдесят',
#            'восемьдесят', 'девяносто']
#
from itertools import count

# DZ V-control + функция с аннотацией
# def num_to_word(n: int)  -> str :
#     """
#     Функция, принимающая число и возвращающая ее словами
#     :param n: двухзначное число
#     :return: это число словами
#     """
#     num_to_str = {0: 'ноль', 1:'один', 2:'два', 3:'три', 4:'четыре', 5:'пять', 6:'шесть',
#               7:'семь', 8:'восемь', 9: 'девять', 10: 'десять', 11: 'одиннадцать', 12: 'двенадцать',
#               13: 'тринадцать', 14: 'четырнадцать', 15: 'пятнадцать', 16: 'шестнадцать',
#               17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать',
#               20: 'двадцать', 30: 'тридцать', 40: 'сорок', 50: 'пятьдесят',
#               60: 'шестьдесят', 70: 'семьдесят', 80: 'восемьдесят', 90: 'девяносто'}
#     if len(str(n)) > 2 :
#         return 'введите двухзначное число'
#     if  len(str(n)) == 1 and n in num_to_str:
#         return  num_to_str[int(n)]
#     return num_to_str[int(str(n)[0] + '0')] + ' ' + num_to_str[int(str(n)[1])]


# Аннотирование функций
# def print_array(array: list) -> None :
#     for item in array :
#         print(item)
#
# words = ['привет', 'мир']
#
# print_array(words)
# print_array(['a', 'b', 'c'])


# def greet(name: str) -> None:
#     print('Привет', name)
#     name = 'друг'
#     print('Здравствуй', name)
#
#
# greet('Петр')


# способ определения глобальных переменных для функций - "главная функция"
# def main() :  # эту функцию пишем ниже всех функций
#      area = 'Дворцовая площадь'
#      print('встретимся, где', area)
#      square_area(200, 158)
#      print('встречаемся', area, '?')
#      circle_length(5)

#main()


# return vs yield

# def generate_list():  #генератор
#     for i in range(5):
#         yield i  # возвращает значение, но не завершает работу
#
#
# array = list(generate_list())
# print(array)

#main() и ее применение
# def print_goodbye() :
#     print('Goodbye', end=' ')
#
#
# def print_cruel() :
#     print('cruel', end=' ')
#
#
# def print_world() :
#     print('world',end=' ')
#
#
# def main():
#     print_goodbye()
#     print_cruel()
#     print_world()


#main()

#############################################
# Оператор is : a is b - когда а и в один и тот же объект (адрес совпадает)
# здесь адреса разные
# my_refreg = ['колбаса', 'сыр', 'масло']
# # his_refreg =  ['колбаса', 'сыр', 'масло']
# his_refreg = my_refreg.copy()  # то же что и [:]
# my_refreg += ['мясо']
# print(his_refreg)
# print(my_refreg is his_refreg)
# print(my_refreg == his_refreg)
# print(id(my_refreg) == id(his_refreg))
#
# temp = None
# print(type(temp))
# print(temp is None)
#
# # d = {'a': 1}
# # print(id(d))
# # d['a'] += 1
# # print(id(d))

# def print_array(array: list, start=None):
#     if start is None and start > len(array) :
#         return
#     if start is None :
#         start = 0
#     else :
#         for i in range(start, len(array)) :
#             print(array[i])
#
#
# a = [1,2,3]
# print_array(a, 1)

###############################################
# Возврат нескольких значений из функции
# При распаковке * может быть только одна
# def coordin() -> tuple:
#     return 5.4, 3.2, 3.8, 7.2, 4.6  # возвращает кортеж
#
# x, *rest, y = coordin()  # распаковка кортежа
# print(f'x= {x}, y={y}, rest={rest}')
#
# *names, surname = 'Остап Сулейман Бендер'.split()
# print(names, surname)
# names = 'Остап Сулейман Бендер'.split()
# print(*names)

#########################################
# Функции с переменным числом входных аргументов

# def multy(*args) :  # перемножение чисел
# #print(len(args))  # делает подсчет числа аргументов
# #print(args)   #по индексу или перебором
# #
# #
# # multy(1,2)
#     #if args == 0:
#     if not args :
#         return 0
#     result = 1
#     for arg in args :
#         result *= arg
#     return result

# первый агр-т определенный (позиционный - должен быть на первой позиции, остальные - неизвестно скоько и какие
#def multy(*args, first) :  # перемножение чисел
#print(len(args))  # делает подсчет числа аргументов
#print(args)   #по индексу или перебором
#
#
# multy(1,2)
    #if args == 0:
#     if not args :
#         return first
#     result = first
#     for arg in args :
#         result *= arg
#     return result
#
# def fio(name, surname):
#     return f'{name} {surname}'


# print(multy(2, 3,4, first=5))
#
# print((fio('Остап', 'Бендер')))

#вариант 1
# def math_op(*args, operator) :
#     if operator != '+' and operator != '*' :
#         return 'Операция не поддерживается !'
#     if operator == '+' :
#         result = 0
#         for arg in args :
#             result += arg
#     else:
#         result = 1
#         for arg in args :
#             result *= arg
#
#     return result


# вариант с использованием match
# def calc(*args, operator) :
#     match operator :
#         case '+' :
#             result = 0
#             for i in args :
#                 result += i
#         case '*' :
#             result = 1
#             for i in args:
#                 result *= i
#         case _:  # случай по дефолту
#             return  -float('inf')
#     return result
#
#
# print(calc(1, 2, 4, operator='*'))

#print(math_op(2, 4, operator='*'))

# def sandwich(type_of_meal, with_onion=False, with_tomato=False) :
#     print('Булочка')
#     if with_onion :
#         print('Лук')
#     print(type_of_meal)
#     if with_tomato :
#         print('Томаты')
#     print('Булочка')
#
#
# sandwich('Котлета', with_onion=True)
# переменное кол-во позиционных и именованных аргументов
# def print_any(*args, **kwargs) :  # параметр с ** можно интерпретировать как словарь(ключ: значение)
#     for i in args :
#         print(i)
#     for k,v in kwargs.items() :
#         print(k, '=', v)

# создание профиля человека
# def profile(name, surname, city, *children, **additional):
#     print(f'Имя: {name}')
#     print(f'Фамилия: {surname}')
#     print(f'Из города: {city}')
#     if len(children) > 0 :
#         print('Дети:', ','.join(children))
#     if 'hobbie' in additional :
#         print('Хобби:', ', ' .join(additional['hobbie']))
#     print(additional)


#profile('Дмитрий', 'Колесов', 'Волгоград',
#         'Мария', 'Петр', hobbie=['Филателия', 'шахматы'])


#print(print_any('Дмитрий', 'Колесов', city='Москва', age=27))

###################################
# Функция как объект
# передается в другие функции: эти функции называются функции высшего порядка

# печатник = print # печатник указывает на объект print и умеет все то же самое, что и print
# печатник('Привет, мир')

# Функция критерия отбора эд-тов списка
# Критерий - длина строки(слова)
# def is_longer_six(word) :
#     return len(word) > 6  # True or False
#
# words = ['В', 'этом', 'списке', 'останутся', 'слова', 'длина', 'которых', 'больше', 'шести']
#
# result = list(filter(is_longer_six, words))
# print(result)
#
# for word in filter(is_longer_six, words) :
#      print(word)


# def start_a(word) :
#
#     return word[0] == 'а'  # True or False
#
#words = ['арбуз', 'ананас', 'банан', 'ежевика', 'малина']
#
# result = list(filter(start_a, words))
# print(result)

# def sq(num) :
#     return num**2

#nums = [1,2,3,4,5,6,7,8,9] # -> 123456789
# sqwares = map(sq, nums)
# print(list(sqwares))

#DZ
# res = ', '.join(map(str, nums))
# print(res)

# в частности "ан"
# def srt_cont(s) :
#     return 'ан' in s
# res = list(filter(str_cont, words))

# анонимные ф-ции (однострочники, безымянные)
# lambda - функции
# lambda <аргументы> : <выражение>

# is_l_six = lambda word: len(word) > 6
# result = list(filter(lambda word: len(word) > 6, words))

# is_first_l_a = lambda st: word[0] == 'a'
#res = list(filter(lambda s: s[0] == 'a', word))

# str_con = lambda s: 'ан' in s
# res = list(filter(lambda s: 'ан' in s, words))

# в одну строку квадраты чисел от 1 до 16
# res = list (map(lambda y: y**2, range(3,16)))  # c lambda
#res = [y**2 for y in range (3,16)]  # однострочник

# word1 = ['В', 'этом', 'списке', 'останутся', 'слова', 'длина', 'которых', 'больше', 'шести']
# long_words = [w for w in word1 if len(w) > 6] # однострочник

# Практика

# ENG_ABC = [chr(ch) for ch in range(ord('a'), ord('z')+1)]
# RUS_ABC = [chr(ch) for ch in range(ord('а'), ord('я')+1)] +['ё']
# # print(ENG_ABC)
# # print(RUS_ABC)
# ABC = set(ENG_ABC )^ set(RUS_ABC) ^ set(map(str.upper, ENG_ABC)) ^  set([ch.upper for ch in RUS_ABC]) #симметричная
# # разность и два способа преобразования набора символов из маленьких в большие - два последних члена выражения
#
# txt = 'Cказали что , но . сегодня'
# text = ''.join(filter(lambda x: x in  ABC ^ {' '}, txt)) # убрали все знаки препинания, т.к. их нет в ABC
# # print(text)
# #
# def remove_punct(text) :
#     return ''.join(filter(lambda x: x in  ABC ^ {' '}, text))
#
#
# def get_words(text: str) -> list:
#     return remove_punct(text).split()
#
# def long_words (text, lengh=4)-> list :
#     return list(filter(lambda word: len(word) > lengh, get_words(text)))

# print(long_words(txt, 6))

# numb = [1,2,3,4,5]  # list(range(1,6))
# squar = {n: n**2 for n in numb}  # создание словаря squar = {n: n**2 for n in numb}
# squar1 = {n: n**2 for n in range(1,11) if n % 2 == 0}
# print(squar1)

# source_dict = {
#     'x': 1,
#     'y': 2,
#     'z': 3,
# }
#
# dest_dict = {k: v*2 for k,v in source_dict.items()}
# print(dest_dict)

# Частотный анализ
# txt = 'Я знаю, что ничего незнаю. Но другие не знают и этого. А значит, я знаю больше , чем они.'
# d = {}
# words = get_words(txt)
# print(words)
#
# for word in words:
#     if word in d:
#         d[word] += 1
#     else :
#         d[word] = 1
#
# for k,v in d.items():
#     print(k,v)

#fruits = ['ананас', 'банан', 'ежевика', 'малина', 'арбуз']
# fruits.sort()
# print(fruits)
# print(sorted(fruits, key=lambda ch: ch[1]))  # сортировка по ключу "вторая буква"
# print(sorted(fruits, key=lambda ch: len(ch))) # сортировка по ключу "длина слова"


################################################
# ключ сортировки

# fruits = ['ананас', 'банан', 'ежевика', 'малина', 'арбуз']
# print(sorted(fruits, key= lambda s: (len(s), s[-1])))  # сортировка по нескольким ключам, приоритет ключей задается
# в виде кортежа - сначала по первому усл-ю,  затем по второму

# goods = [
#     ['Утюг', 1500, 2],
#     ['Фен', 1000, 5],
#     ['Телевизор',  8000, 3]
# ]
#
# print(sorted(goods, key=lambda s: (s[1], s[2], s[0] )))

######################
# проверка коллекций: any(), all() удобно для анализа больших массивов, и поиска флуктуаций
# any - любой эл-т коллекции вернет True
# all - все эл-ты коллекции вернет True
# print(all([1,2,3]))  # True -  все эл-ты ненулевые
# print(all([1,2,0]))  # False - один эл-т нулевой
#
# print(all([]))

# words2 = 'один два три'.split()
# ls_for_analyz = list(map(lambda ch: len(ch) > 2, words2))
# print(ls_for_analyz)
# print(all(list(map(lambda ch: len(ch) > 3, words2))))
# print(any(list(map(lambda ch: len(ch) > 3, words2))))

########################
# потоковый ввод sys.stdin - элементы это строки, к-рые вводит пользователь (Ctrl + D)
#import  sys

# data =  sys.stdin.readlines()  # потоковый ввод , окончание Ctrl+D
# data = [d.strip('\n') for d in data]  # можно все в одну строку data = [d.strip('\n') for d in sys.stdin.readlines()]
# print(data) # это результат

# data = ['раз два три', 'ёлочка гори']
# temp = []  # индекс строки в data и число слов в виде кортежей
# for i, s in enumerate (data):
#     temp.append((i, len(s.split())))
# print(temp)
# temp.sort(key=lambda ch: ch[1])
# print(temp)
# index = temp[0][0]
# res = sorted(data[index].split())
# print(*res, sep='-')

##############################

#  Рекурсия - функция вызывает сама себя, глубина стека для интерпретатора Python = 1000, лучше рекурсию не использовать
# обязательно первым шагом прописать условие выхода из рекурсии

# def factr(count) :
#     res = 1
#     for i in range (2, count + 1) :
#         res *= i
#     return res
#
# for x in range(10):
#     print (x, factr(x))


# def factr1 (n) :
#     if n ==1 or x == 0 :
#         return 1
#     else:
#         n *= factr1(n-1)

############################
# черепашья графика
#import turtle
# import turtle as t # замена на короткое название для удобства вызова
# начало координат в середине (600 х800)
# turtle.goto(-100,-200) # переход в точку начала рисования
# turtle.penup()  # оторвались от "земли"
# turtle.pendown() # вернулись на "землю"
#turtle.speed(0)  # скорость от 0 до 10, 0 - самая быстрая

# colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
# turtle.bgcolor('black')  # общий фон
# angle = 360 // len(colors) - 1
#
# for x in range(200):
#     turtle.pencolor(colors[x % len(colors)])
#     turtle.width(x // 100+1)
#     turtle.forward(x)
#     turtle.left(angle)

# for i in range(4) :
#     turtle.forward(100)  # вперед в пикселях
#     turtle.right(90)  # поворот на угол()
#
# for i in range(3) :
#     turtle.forward(100)  # вперед в пикселях
#     turtle.right(120)
#
#     turtle.forward(100)  # вперед в пикселях
# n = 5
# for i in range(n):
#     turtle.right(360 // n)
#     turtle.circle(50)
# turtle.circle(50)  #радиус

# N = 5
# for _ in range(N) :
#     for _ in range(4):
#         turtle.forward(100)
#         turtle.right(90)
#     turtle.right(360//5)

# def qv(a):
#     for _ in range(4):
#         turtle.forward(a)
#         turtle.right(90)
#     return
# #
# def flow(n):
#     for i in range(n) :
#       turtle.circle(50)
#       turtle.right(10)
#     return
# flow(36)


# N = 5
# for _ in range(N) :
#     qv(100)
#     turtle.right(360//5)

# def tree (lent):  # фрактал, используем рекурсию
#     if lent < 10 :
#         return
#     turtle.forward(lent)
#     turtle.left(30)
#     tree(lent*0.7)
#     turtle.right(60)
#     tree(lent * 0.7)
#     turtle.left(30)
#     turtle.backward(lent)
#
#
# turtle.left(90)
# tree(100)
#
# turtle.mainloop()  # откроется графическое окно

#DZ 03_07, control V

# string = [d.strip('\n') for d in sys.stdin.readlines()]
# length = len(string) # сколько строк
# rem = length % 3

# if rem:
#     string = strings[:length - rem] # берем только кратные 3
#
# for x in range(0, length - rem, 3) :
#     summ = sum (len(a) for a in strings[x:x+3]) # вычисляем сумму эл-тов списка, если все эл-ты  -  числа (min и max)
#     result = []
#     for s in strings[x:x+3] :
#         temp = s.lower().split()
#         result += filter(lambda a: len(a) % 2 == summ % 2, temp)
#     result = sorted(set(map(lambda b: b.capitalize(), result)))[:5]
#     print(*result, sep='.')

# функции sum, max, min

# sum -принимает кортеж или список
# res = sum([1,2,3])
# print(res)
#
# lst = [1,2,3]
# res = sum(lst)
# min_lst = min(lst)
# max_lst = max(lst)
# print(res, max_lst, min_lst)

#################################
# Встроенные библиотеки

# PyPi - хранилище внешних библиотек Python (pupi.org)

# модуль math
#import math as m  #тогда можно обращаться через новое имя "m", импорт всей библиотеки, но вся она в память не выгружается
# from  math import pi, sqrt  # импортируем только нужные функции - это правильноб если н.только несколько ф-ций
#from math import sin, radians, hypot  # можно в несколько строк, если много ф-ций
# from  math import *  # импорт всей библиотеки, но это грубый способ, т.к. все вытягивается в память, засоряется
# пространство имен, лучше "import math"

#print('Число Пи: ' , math.e)

# print(dir(m))   # вызов списка всех ф-ций модуля
# print(help(m.cos))  # вызов описания конкретной ф-ции
#print('Синус 30:', round(sin(radians(30)),2))

# модуль random

#import random as r
#from random import sample

#num = r.randint(0,10)  # случайное число в опр.диапазоне
# for _ in range(10) :
#     print(r.randint(0,10))
#     print(r.randrange(0,10,2))  # только четные случ.  числа

# ф-ция choice - выбирает эл-т случайным образом, не работает с множествами и словарями
# lst = [1,2,3,4,5,6,7,8,9]
# res = r.choice(lst)
# print(res)
# print(r.choice(['орел', 'решка']))  # подбрасывание монеты
# print(r.choice('орел'))

# d = {'a': 1, 'b': 2, 'c': 3}  # как обработать словарь с помощью choice
# keys = list(d.keys())
# key = r.choice(keys)
# print(d[key])


# бросание кубика zara
# zara = ['\u2680', '\u2681','\u2682','\u2683','\u2684','\u2685']
# for i in range(10) :
#     print((r.choice(zara), r.choice(zara)))

# sample - случайный выбор без повторов, можно указать кол-во выборов

# lst = [1,2,3,4,5,6,7,8,9]
# print(r.sample(lst, k = 5))
#
# for _ in range(10) :
#     print((r.sample(lst, k = 5)))

# shuffle - перетасовать, работает со списками

#генерация случайного пароля, из 8 знаков, чтобы была хотя бы одна цифра, один спец знак и одна большая буква
# N = 8
# abc = 'qwertyyutyuukpipkasfgjkghlghj'
# num = '1,2,3,4,5,6,7,8,9,0'
# spec = '#@$'
# abc = list(abc)
# num = list(num)
# spec = list(spec)
# r.shuffle(abc)
# temp = abc[:N - 3]
# temp.append(r.choice(abc).upper())
# temp.append(r.choice(num))
# temp.append(r.choice(spec))
# r.shuffle(temp)
# res = ''.join(temp)
# print(res)

# функция random()
# r.seed()
# print(r.random())

# datetime - берет данные из системного времени (компа..)

# import datetime as dt
# from calendar import weekday

# print(dt.datetime.now())  # дата в м/нар. формате
# print(dt.datetime.now().date()) # только дата
# print(dt.datetime.now().time())  # только время
# print(type(dt.datetime.now().time()))

# strftime # преобразует дату в формат строки
# tim = dt.datetime.now()
# ftim = tim.strftime('%d/%m/%y')  # только день/месяц/год, если "Y" , то будет "2025"
# print(ftim)
# print('Время:', tim.strftime('%H:%M'))  # вывели время

# назначить свое время, какой-то опр.момент
# my_time = dt.time(15, 27, 32)
# print(my_time)
# my_day = dt.date(2025, 7, 4)
# print(my_day)
# my_d_t = dt.datetime.combine(my_day, my_time)
# print(my_d_t)

# матем. операции для дат
#dat1 = dt.date(2025, 6,15)
# dat2 = dt.date(2025, 7, 3)
# delta = dat2 - dat1
# print(delta)

# from pprint import pprint # красивый вывод данных
#
# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
# ]
#
# print(matrix)
# pprint(matrix)

####################
# Внешние библиотеки
#ГРАФИКА
# установка библиотеки PIL - Python Imagine Library - для обработки растровых изображений (м.передать реалистичную картину)
# описание , какие внеш библиотеки установлены:
#1 способ  pip freeze > requirements.txt
# установка списка библиотек: pip install -r  requirements.txt
# цветовая модель RGB

#thumbnail  #сделать уменьшенную копию картинку, ее помещают в спец.директорию

# from PIL import Image, ImageDraw
# базовые действия с изображением
# imag = Image.open('imges/piton.jpg')
# print(imag.size)  # свойства объекта - размер
# x,y = imag.size  # на первом месте ширина, затем высота
# print(f'Ширина = {x}, Длина = {y}')
# # нулевая точка в левом верхнем углу экрана
# mode = imag.mode  # свойства объекта - режим
#
# pixels = imag.load()  #метод для загрузки таблицы пикселей
# print(f'Цветовая схема: {mode}')
# Инверсия
# for i in range(x) :
#     for j in range(y):
#         r,g,b = pixels[i, j]
#         pixels[i, j] = r, b, g
# imag.save('imges/piton2.jpg')  # создание копии файла

# Негатив
# for i in range(x) :
#     for j in range(y):
#         r,g,b = pixels[i, j]
#         pixels[i, j] = 255 - r, 255 - b, 255 - g

# оттенки серого, перевод в черный-белое
# for i in range(x) :
#     for j in range(y):
#         r,g,b = pixels[i, j]
#         average = (r+g+b) // 3
#         pixels[i, j] = average, average, average
# imag.save('imges/piton2.jpg')


#поворот изображения
# img_rot = imag.rotate(90)
#
# img_rot.save('imges/piton2.jpg')

# отразить
# img_flip = imag.transpose(Image.Transpose.FLIP_LEFT_RIGHT)  # вправо влево , можно вверх-вниз
# img_flip.save('imges/piton2.jpg')

# вырезка изображения
# сначала рисуем прямоугольник
# cropped = imag.crop((270,0,540,300))
# cropped.save('imges/piton2.jpg')

# resize
#resized = imag.resize((400,300))  # если неизвестно заранее размер, надо что-то взять за единицу, затем делать
# пропорционально - из пропорций первоначального изображения

#################################
# создание изображений

# imag = Image.new('RGB', (600,400),(0,0,255))  # создание синего квадрата
# imag.save('imges/piton2.jpg')
# draw = ImageDraw.Draw(imag)  # создали холст
#
# draw.line((0,0,600,400), fill=(255,0,0), width=5)  # линия/отрезок
# imag.save('imges/blue.jpg')
#
# draw.line((600,0,0,400), fill=(255,0,0), width=5)  # линия/отрезок
# imag.save('imges/blue.jpg')
#
# draw.rectangle((10,10, 590, 390),outline=255, width=10)
# imag.save('imges/blue.jpg')
#
# draw.ellipse((10,10, 590, 390),outline=255, width=10)
# imag.save('imges/blue.jpg')
#
# # текст
# draw.text((100,100), 'Туапр', fill=255)
# imag.save('imges/blue.jpg')
#
# # полигон
# RED = (255,0,0)
# POLY = [(50,50), (150,50), (180,120)]
# draw.polygon(POLY, outline='green', width=15)
# imag.save('imges/blue.jpg')

####################
#DZ 04_07_25

# from PIL import Image
# from PIL import ImageFont
# from PIL import ImageDraw

#V1  прямоугольник с белой окантовкой

# sky1 = Image.new('RGB', (600,400),(50,155,205))  # создание голубого квадрата
# sky1.save('imges/sanday.jpg')
#
# words = Image.open("imges/sanday.jpg")
# draw = ImageDraw.Draw(words)
# draw.rectangle((0,0, 600, 400),outline=(255,255,255), width=10)
#
# font = ImageFont.truetype('arial.ttf', 36)
# draw.text((200, 160), 'SANNY DAY', (255,224,32), font=font)
#
# draw.pieslice( (480,-100, 700, 120),start=90, end=180, fill=(255,224,32))
#
# words.save('imges/sanday.jpg')


#V2 закругл.прямоугольник с белой окантовкой

# sky1 = Image.new('RGB', (600,400),(0, 0, 0))  # создание черного квадрата
# sky1.save('imges/sanday1.jpg')
#
# words = Image.open("imges/sanday1.jpg")
# draw = ImageDraw.Draw(words)
#
# draw.rounded_rectangle((0, 0, 600, 400), radius=40, fill=(50,155,205), outline=(255,255,255), width=4)
# font = ImageFont.truetype('arial.ttf', 36)
# draw.text((200, 160), 'SANNY DAY', (255,224,32), font=font)
#
# draw.pieslice( (480,-112, 712, 120),start=90, end=180, fill=(255,224,32))
#
# words.save('imges/sanday1.jpg')

# https:/fontsforyou.com/ru/specific-fonts/ttf-fonts/languageru
# font = 'fonts/Domb.ttf' - назначить пользовательский шрифт
# _, _, w< h = draw.textbbox((0,0), text, font=font) - определяем высшту и ширину надписи для последующей центровки
from PIL import  Image, ImageFilter, ImageEnhance
from docx.enum.text import WD_ALIGN_PARAGRAPH

# orig = Image.open('imges/sanday.jpg').convert('RGB') # конвертируем в RGB-формат на всякий случай
# up = orig.crop((0,0,600,200))
# down = orig.crop((0,200,600,400))
# new = Image.new('RGB', (600,400))
#
# new.paste(down, (0,0))
# new.paste(up,(0,200))
# new.show()

orig = Image.open('imges/piton.jpg').convert('RGB') # конвертируем в RGB-формат на всякий случай,
# если используем фильтры - обязательно это сделать
#размытие
# blur_image = orig.filter(ImageFilter.GaussianBlur(radius=8))
# blur_image.show()

#усиление резкости
# enchancer = ImageEnhance.Sharpness(orig)
# sharpened_image = enchancer.enhance(4.0)  # степень резкости
# sharpened_image.show()

#получить контуры изображения
####################
#Документы
# Word - DOCX
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Cm, Inches, Mm, Pt  # для размеров
doc = Document()  # создали конструктор, создание экземпляра документа

# Добавление заголовка
doc.add_heading('Отчет за месяц', 1)  # заголовок первого уровня
paragraf = doc.add_paragraph() # отступ чтобы начать новый абзац
paragraf = doc.add_paragraph('В отчете представлены') # с лед.уровень
paragraf.add_run('  ключевые показатели').bold = True  # можно что-то добавить в абзац, приклеиться с конца
# run - это что-то внутри абзаца, текс, картинка и т.п.

#добавление маркированного списка
paragraf = doc.add_paragraph()
paragraf_format = paragraf.paragraph_format
paragraf_format.alignment = WD_ALIGN_PARAGRAPH.LEFT

# маркированный
# paragraf = doc.add_paragraph('Первый пункт', style='List Bullet')
# paragraf = doc.add_paragraph('Второй пункт', style='List Bullet')
#
# #нумерованный
# paragraf = doc.add_paragraph('Первый пункт', style='List Number')
# paragraf = doc.add_paragraph('Второй пункт', style='List Number')

# paragraf = doc.add_paragraph()

# добавить таблицу
# table = doc.add_table(rows=3, cols=3)  # можно еще добавить стиль
# # заполнить таблицу
# for i, row in enumerate(table.rows) :
#     for j, cell in enumerate(table.columns) :
#         cell.text = f'Строка {i + 1}, Столбец {j + 1}'

# добавить изображение
# paragraf = doc.add_paragraph()
#
# doc.add_picture('imges/sanday.jpg', width=Mm(105))  # нужны единицы измерения Word
# # (см, мм или точки), поэтому импорт нужен - см.выше
#
# doc.save('docs/report.docx')

# документы по шаблону
# Word - DOCX (docxtpl)

# загрузка шаблона
# from docxtpl import DocxTemplate
# doc = DocxTemplate('docs/template.docx')
#
# # данные для подстановки в шаблон
# content = {
#     'company': 'ООО "Монолит"',
#     'employee': 'Петров Д.И.',
#     'position': 'Менеджер',
#     'date': '01/02/2025'
# }
#
# doc.render(content)  # загрузка данных в шаблон
# doc.save('docs/about.docx')

# count = 1
# for i in content :
#     doc.render(i)
#     doc.save(f'docs/about{count}.docs')
#     count +=1

###############################
# работа с эл.таблицами, Excel (openpyxl)
from docxtpl import DocxTemplate  # для экселя проверить команду в мастер - образце

#пустой файл excel
# from openpyxl import Workbook  #  конструктор
#
# wb = Workbook()  # создали книгу
# ws = wb.active  # обратились к активному листу
# ws.title = 'Отчет' # назвали лист
# wb.save(('docs/report.xlsx'))

# запись данных в существующий файл
from openpyxl import load_workbook  # подключили метод
# wb = load_workbook('docs/report.xlsx')  # открыли/загрузили рабочю книгу
#
#ws = wb.active  # активный лист
# можно и по имени листа
# ws = wb['Отчет']
#######################
#  способы записи
# #V1
# ws['F1'] = 'Привет мир'  # запись данных в ячейку
#
# #V2
# ws.cell(row=1, column=3, value='Hello!')
#
# wb.save('docs/new_table.xlsx')

# Заголовки
# ws['A1'] = 'ФИО'
# ws['B1'] = 'Должность'
# ws['C1'] = 'Отдел'
#
# # Данные
# emploes = [
#     ['Иванов И.И.', 'Менеджер', 'Продажи'],
#     ['Петров П.П..', 'Бухгалтер', 'Финансы'],
#     ['Сидорова С.С.', 'Аналитик', 'IT'],
# ]
#
# for row, data in enumerate(emploes, start=2) :
#     ws.cell(row=row, column=1, value=data[0])
#     ws.cell(row=row, column=2, value=data[1])
#     ws.cell(row=row, column=3, value=data[2])
#
# wb.save('docs/new_table1.xlsx')

# работа с формулами
# ws['A1'] = "=SUM(A1:A10)"  # ввод формулы в ячейку

# Формат
# from openpyxl.styles import  Font, Alignment
# ws['A2'].font = Font(bold=True, size=14)  # назначение шрифтов
# ws['A2'].alignment = Alignment(horizontal='center')  # выравнивание по горизонтали

#######################
# чтение данных из  файла excel

# wb = load_workbook('docs/new_table1.xlsx')  # открыли/загрузили рабочю книгу
# ws = wb.active  # активный лист
#
# rows_count = ws.max_row  # число заполненных строк
# print(rows_count)
#
# for row in ws.iter_rows(values_only=True) :
#     fio, pos, dept = row  # распаковка кортежа
#     print(f'Фамилия: {fio}, Должность {pos}, Отдел {dept}')
