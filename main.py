# Коллекции
# Множества, списки, словари, коллекции

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
#fio = ['Иванов', 'Петров', 'Сидоров']

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
#text = 'Списочные выражения применяются для эффективности кода'
#print([ch for ch in text.split() if (text.index(ch)+1) % 3])  # не получается каждое 3 слово - почему?

# res = [ch for ch in text.split()[2::3]]  # используем срез от text
# print(res)

# если не ставить кв.скобки снаружи, то получится итератор
# можно преобр-ть во множество
#############################################
# вложенные списки
# создание влож.списков
# 1 способ
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],  # висячая запятая, нужна, если что-то надо добавить, лучше ставить
# ]  # это называется таблица или матрица
# print(matrix)
#
# # распечатать/обойти двухмерную таблицу
# for row in range (len(matrix)) :
#     for col in range(len(matrix(row))):
#         print(matrix[row][col])

# Единственный способ создания
# N = 5
# matrix = [[1] * N for _ in range(N)]
# print(matrix)

#Создать матрицу и наполнить ее числами от 1 до 9
# N = 3
# ind = 0
# matrix = [[0] * N for _ in range(N)]  #можно без этого, а сразу создать в цикле ниже, но с указанием размерности через N
# print(matrix)
# for row in range (len(matrix)) :
#     for col in range(len(matrix[row])):
#         ind += 1
#         matrix[row][col] += ind
#         print(matrix[row][col])
# print(matrix)
# Другой вариант
# N = 3
# matrix = [[i+j for j in range(N)] for i in range (1,10,3)]
# print(matrix)
################################################

# словари
# создание
# пустой словарь
# 1. d = {}
# 2. d = dict()  # используется реже

# предзаполненный словарь
# d = {'table': ['таблица', 'стол'],
#      'well': ['хорошо', 'колодец'],
#      'chair': 'стул',
#      'apple': 'яблоко',
#      1: 'один',
#      (55.75, 37.5): 'Москва',   # всегда ставим запятую в конце
#      }
#обращение к элементу словаря
# print(d['table'])
# print(d['well'][0])


# добавление эл-тов в словарь - это будет пара: "ключ - значение"
#d['plum'] = 'слива'
#print(d['plum'])  # по окончании программы предзаполненный словарь останется без изменений, эта запись не войдет

#print(d['well'])
#d['well'].append('скважина')  # добавили элемент по ключу 'well' в список
#if type(d['well']) == list :  # проверка типа
#print(d)

# удаление эл-тов

# способ 1
#del d['well']  # если элемента нет, то будет ошибка
#print(d)  # выод как есть


"""
Методы словаря
'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
"""

# второй способ удаления
# deleted_item = d.pop('apple')  # если элемента нет, то будет ошибка
# print('удалился элемент: ', deleted_item)

# проверка наличия эл-та в словаре по ключу
# print('Есть ли 'стул' в словаре')
# if 'chair' in d :
#     print('да')

#перебор словаря по умолчанию
# for key in d :
#     print(key, '->', d[key])

# print(d.keys())  #возвращает набор ключей, но это не список!
#
# print(list(d.keys()))
# for key in d.keys() :
#     print(key, '->', d[key])

#print(d.values())  # возвращает набор значений

# перебор всех значений
# for value in d.values() :
# #     print(value)

# print(d.items())  # возвращает набор пар в виде кортежей "ключ : значение"
# for k,v in d.items() :
#     print(k, '->', v)



# теперь проверка наличия эл-та в словаре по ключу
# print('Есть ли стул в словаре')
# if 'стул' in d.values() :
#     print('да')

# print('Доступ к несуществующему ключу без "исключений"')
# pear = d.get('pear', 'груши нет')
# print('Где груша : ', pear)
#
# print(d[(55.75, 37.5)])  # ключ является кортежем

#Задача Частотный анализ
text = """Завтра ожидается теплая погода без осадков,
температура воздуха комфортная, осадков не наблюдается. Так рассказал главный метеоролог
"""
# res = {}
# commas = (',', '!', '.', ':', '-')
#
# for ch in commas :
#     fr = text.replace(ch, '')
#
# lst = sorted(fr.strip().lower().split())
#
# for item in lst :
#     if iten in res: #  по умолчанию ищется среди ключей, иначе пишем res.key или res.value
#         res[item] += 1
#     else :
#         res[item] = 1
#
# print('частотный анализ слов:')
# for k,v in res.items() :
#      print(f'\t{k}: {v}')

##########################################

# Функции
# Scope (local or global)  лучше меньше глобальных переменных
#это область видимости ф-ции, локальн.переменные - это внутри ф-ции, глобальные - снаружи в программе
# Синтаксис
# def <имя функции> имя - все с маленькой буквы и можно пользоваться нижним подчеркиванием

# def <имя функции>([параметры]) :
#   команды
#  Return value - необязательно, могут быть просто действия
# person = 'Петр'  # глобальная переменная "person"
# def greet_to_name(name='noname') :
#     print('Hello,', name)  # локальная переменная "name"
#     print((count))
#
#
# greet_to_name('Lusie')
# count = 0
#
#
# def increment() :
#     global count  # разрешили функции изменять значение и манипулировать с глобальной переменной (
#     count += 1
#
#
# increment()
# greet_to_name('Lusie')
#
#
# def print_list(array=None) :
#     if array is None :
#         array = []
#     for item in array :
#         print(item)
#
# greet_to_name()


# Чистые функции - результат зависит только от аргументов, не влияет на ход выполнения программы

# Возвращение значений
# def square(num) :
#     return num ** 2
#
# t = square(5)
# print(t)

# def even_odd(num):
#     if num % 2 == 0 :
#         return 'Четное'
#     return 'Нечетное'
#
# print((even_odd(5)))


# def print_str(s=None) :
#     if s is None:
#         return  # полезный способ использования return
#     print(s)


# DZ функцию чтобы выводить число словами 56 ->  пятьдесят шесть, число мах 2-значное

# функция, которая записывает двухзначное число словами
# 56 -> пятьдесят шесть

#V1.
# def num_to_word(num) :
#     e_d = {0: '', 1:'один', 2:'два', 3:'три', 4:'четыре', 5:'пять', 6:'шесть',
#            7:'семь', 8:'восемь', 9: 'девять'}
#     tw_d = {11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать',
#             14: 'четырнадцать', 15: 'пятнадцать', 16: 'шестнадцать',
#             17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать'}
#     d_d = {0: '', 1: 'десять', 2: 'двадцать', 3: 'тридцать', 4: 'сорок', 5: 'пятьдесят',
#         6: 'шестьдесят', 7: 'семьдесят', 8: 'восемьдесят', 9: 'девяносто'}
#
#     if len(str(num)) > 2 :
#         print(f'Число {num} имеет больше двух разрядов')
#         return
#     key1 = num % 10
#     key10 = num // 10
#     if key1 + key10 == 0 :
#         print(num, '-> ноль')
#
#     elif key10 == 1 and key1 != 0 :
#         print(num, '->', tw_d[key10*10+key1])
#     else :
#         print(num, '->', d_d[key10], e_d[key1])
#
#
# num_to_word(0)


#V2
# def num_to_word(num) :
#     e_d = ['один', 'два', 'три','четыре', 'пять', 'шесть','семь', 'восемь', 'девять',
#            'десять', 'одиннадцать', 'двенадцать', 'тринадцать','четырнадцать', 'пятнадцать',
#            'шестнадцать', 'семнадцать',  'восемнадцать', 'девятнадцать', '']
#     d_d = ['двадцать', 'тридцать', 'сорок', 'пятьдесят','шестьдесят', 'семьдесят',
#            'восемьдесят', 'девяносто']
#
#     if len(str(num)) > 2 :
#         print(f'Число {num} имеет больше двух разрядов')
#         return
#     if num == 0 :
#         print(num, '-> ноль ')
#     elif num < 20 :
#         print(num, '->', e_d[num - 1])
#     else :
#         print(num, '->',d_d[num // 10-2], e_d[num % 10-1] )
#
#
# num_to_word(11)

# V control + функция с аннотацией
# def num_to_word(n: int)  -> str :
#     """
#     Функция, принимающая число и возвращающая ее словами
#     :param n: двухзначное число
#     :return: это число словами
#     """
#     num_to_str = {0: 'ноль', 1:'один', 2:'два', 3:'три', 4:'четыре', 5:'пять', 6:'шесть',
#             7:'семь', 8:'восемь', 9: 'девять', 11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать',
#             14: 'четырнадцать', 15: 'пятнадцать', 16: 'шестнадцать',
#             17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать',
#             20: 'двадцать', 30: 'тридцать', 40: 'сорок', 50: 'пятьдесят',
#            60: 'шестьдесят', 70: 'семьдесят', 80: 'восемьдесят', 90: 'девяносто'}
#     if len(str(n)) > 2 :
#         return 'введите двухзначное число'
#     if  len(str(n)) == 1 or n in num_to_str:
#         return  num_to_str[int(n)]
#     return num_to_str[int(str(n)[0] + '0')] + ' ' + num_to_str[int(str(n)[1])]  #исправить


#   num_to_word(25)


# Область видимости

# Пример: испортили список
# a = [1, 2]
#
# def change_array() :
#     a[0] = 0
#
# change_array()
# print(a)

# shadows name 'square' from jther scope
#square = 'Дворцовая площадь'

# def square_area (lenth, width) :
#     area = lenth * width
#     print(f' Площадь площади  = {area}')
#
# print('встретимся, где', square)
# square_area(200, 158)
# print('встречаемся', square, '?')


# PI = 3.14
# def circle_length(radius):
#     perimetr = 2 * PI * radius
#     print(f'Длина окружности с радиусом {radius} равна {perimetr:.2f}')

# circle_length(5)


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


# Оператор is : a is b - когда а и в один и тот же объект (адрес совпадает)
# здесь адреса разные
my_refreg = ['колбаса', 'сыр', 'масло']
# his_refreg =  ['колбаса', 'сыр', 'масло']
his_refreg = my_refreg.copy()  # то же что и [:]
my_refreg += ['мясо']
print(his_refreg)
print(my_refreg is his_refreg)
print(my_refreg == his_refreg)
print(id(my_refreg) == id(his_refreg))

temp = None
print(type(temp))
print(temp is None)

# d = {'a': 1}
# print(id(d))
# d['a'] += 1
# print(id(d))