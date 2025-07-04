import math
# def num_to_word(num) :
#     e_d = ['один', 'два', 'три','четыре', 'пять', 'шесть','семь', 'восемь', 'девять',
#            'десять', 'одиннадцать', 'двенадцать', 'тринадцать','четырнадцать', 'пятнадцать',
#            'шестнадцать', 'семнадцать',  'восемнадцать', 'девятнадцать', '']
#     d_d = ['двадцать', 'тридцать', 'сорок', 'пятьдесят','шестьдесят', 'семьдесят',
#            'восемьдесят', 'девяносто']
#


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

#import math as m  #тогда можно обращаться через новое имя "m", импорт всей библиотеки, но вся она в память не выгружается
# from  math import pi, sqrt  # импортируем только нужные функции - это правильноб если н.только несколько ф-ций
from  math import sin, radians  # можно в несколько строк, если много ф-ций
# from  math import *  # импорт всей библиотеки, но это грубый способ, т.к. все вытягивается в память, засоряется
# пространство имен, лучше "import math"

#print('Число Пи: ' , math.e)

# print(dir(m))   # вызов списка всех ф-ций модуля
# print(help(m.cos))  # вызов описания конкретной ф-ции
print('Синус 30:', round(sin(radians(30)),2))











