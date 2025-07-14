# ООП/OOP
# encapsulation
# a = 3
# print(a.__class__.__name__)  # класс и имя класса
# создание класса
# class Fruit:
#
# #свойства классов
# #создание экземпляра класса
#     a = Fruit()
#     b = Fruit()
#     c = Fruit()
# #создание объекта, определяем свойства
#     a.name = 'Яблоко'
#     a.weight = 120
#     print(a.name)
#     print(a.weight)
#
#     b.name = 'Груша'
#     b.weight = 180

# Методы классов
# class Greater:
#     def hello(self, name='Noname')-> None:
#         print('Привет, ', name)
#
#     def bye(self):
#         print('Пока!')
#
#
# # создадим объект
# g = Greater()  # объект g
# g.hello()
#
# c = Greater()
# c.bye()

# методы, анализ предыдущих  вызовов
# class Car:
#     def __init__(self, brand='Noname', model='NoModel', color='Nocolor'):
#         self.engine_on = False  # прописываем свойства
#         self.brand = brand  #'Skoda'
#         self.model =  model  #'Oktavia'
#         self.color = color #'red'
#
#
#     def start_engine(self):
#         self.engine_on = True  # self. - делает аналог глобальной переменной
#
#
#     def drive_to(self, place):
#         if self.engine_on:
#             print(f'Едем в {place} на {self.brand}{self.model}')
#         else:
#             print('Двигатель не заведен, не едем')
# from lib import Car  # описание класса в отдельной библиотеке (файл lib.py)
#
#
# car = Car('Skoda', 'Oktavia', 'red')
# car.start_engine()
# car.drive_to('город')
#
# car2 = Car()
# car2.start_engine()
# car2.drive_to('город')

# class Person:
#     def __init__(self, name='Bill', age=1):
#         self._name = name
#         self._age = age
#
#     def set_name(self, new_name):  # setter - устанавливает значение свойств (полей класса)
#         if new_name:
#             self._name = new_name
#
#     def set_age(self, new_age):
#         if 0 < new_age < 150 :
#             self._age = new_age
#         else:
#             print('Некорректный возраст - ', new_age)
#
#     def get_name(self):  # getter - возвращает значение поля класса
#         return self._name
#
#     def get_age(self):
#         return self._age
#
#     def person_info(self):
#         print(f'Человек с именем {self._name} .  Возраст :{self._age}')

# from lib import Car
# from lib import Clicker
# from lib import Separator
# from lib import Sorter
# from lib import Balance

# car1 = Car()
# car2 = Car()
# car3 = Car()
#
# print('В парке машин: ', Car.get_counter())
#
# from lib import Person
# p = Person()
# p.set_age(789)
# print(p._age)
# print(p._name)


# cl = Clicker()
#
# cl.click()
# cl.click()
# cl.click()
#
# print(cl.get_counter())
#
# cl.reset()
# print(cl.get_counter())

# s = Separator()
# for i in range(20) :
#     s.add_num(i)
#
# print(s.get_even())


# s = Sorter()
# s.add_word(('привет'))
# s.add_word(('пока'))
# s.add_word(('здорово'))
# print(s.result())


# b = Balance()
#
# b.add_left(5)
# b.add_right(4)
# b.add_left(3)
# b.add_right(5)
# b.add_left(6)
# b.add_right(7)
# b.add_left(2)
# b.add_right(4)
#
# print(b.result())

################################
# полиморфизм
# method override; operator overloading

# пример - перегрузка оператора " + ", он полиморфный
# print(1+2)
# print(1+2.0)
# print('abc' + 'def')
# print([1,2] + [3,4])
#
# def fun1(x,y):
#     return  x + y
#
# print(fun1(2 , 3.0))

# from lib import Book
#
#
# book = Book('Язык C++', 'Бьярн Страупструп')  # отлич. книга по C++
#
# print(f'{book.get_title(), book.get_author()}')

# полиморфизм, пример - переопределение метода
#from math import pi

# первый способ добавления имен для фигур, второй см. в lib.py
# class Circle:
#     def __init__(self, radius, name):
#         self.radius = radius
#         self.name = 'круг'
#
#     def perimetr(self):
#         return 2 * pi * self.radius
#
#     def area(self):
#         return pi * self.radius ** 2
#
#     def get_name(self):
#         return self.name
#
#
# class Square:
#     def __init__(self, side, name):
#         self.side = side
#         self.name = 'квадрат'
#
#     def perimetr(self):
#         return 4 * self.side
#
#     def area(self):
#         return self.side ** 2
#
#     def get_name(self):
#         return self.name
#
#
# class Rectangle:
#     def __init__(self, widt, long, name):
#         self.widt = widt
#         self.long = long
#         self.name = 'прямоугольник'
#
#     def perimetr(self):
#         return 2 * (self.widt + self.long)
#
#     def area(self):
#         return self.widt * self.long
#
#     def get_name(self):
#         return self.name
#
#
# def shape_info(shape: object):
#     print(f'Объект {shape.get_name()}а :\n Площадь : {shape.area()},  Периметр: {shape.perimetr()}')
#
#
# s = Square(10)
# shape_info(s)
#
# cr = Circle(10)
# shape_info(cr)
#
# rc = Rectangle(5, 10)
# shape_info(rc)

# print(dir(s))
# print(dir(cr))

##########################################
# from lib import Student, Employee, Person
# people = [
#     Person('Александр', 27),
#     Student('Дмитрий', 'ГУАП'),
#     Employee('Пётр', 'Авангард'),
# ]
#
# for person in people:
#     if isinstance(person, Student):
#         print(person.get_univercity())
#     if isinstance(person, Employee):
#         print(person.get_company())
#     else:
#         print(person.get_name())

############################
# lst = list(range(1,15))
#
# class Stat:
#     def __init__(self, lst1):
#         self.lst1 = lst1[:]
#
#     def is_int(self):  # проверяет, все ли числа целые, иначе None
#         return all(isinstance(item, int) for item in self.lst1 )
#
#
#     def get_min(self):
#         if is_int():
#             return min(self.lst1)
#         else:
#             return None
#
#     def get_max(self):
#         if self.is_int():
#             return max(self.lst1)
#         return None
#
#     def get_avg(self):
#         if self.is_int():
#             return sum(self.lst1)  / len(self.lst1) # среднее
#         return None
#
#
# class Selector:
#     def __init__(self, lst1):
#         self.lst1 = lst1[:]
#
#     def get_odd(self):
#         return [x for x in self.lst1  if x % 2]
#
#     def get_even(self):
#         return [x for x in self.lst1  if x % 2 == 0]

############################################

# s = Selector(lst)
# print(s.get_odd())
# print(s.get_even())

# s = Stat(lst)
# print(s.get_min())
# print(s.get_max())
# print(s.get_avg())

############################################
# from math import hypot
# # Special methods
# # переопределение метода
# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):  # переопределили метод
#         return f'<Point: ({self.x}, {self.y})>'
#
#     def __repr__(self):
#         return f'<List of Point: ({self.x}, {self.y})>'  # представление объекта для
#         # читабельности (как лучше представлять информацию)
#
#     def __sub__(self, other):
#         return Point(self.x - other.x, self.y - other.y)
#
#     def __add__(self, other):
#         # hypot = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2)**(1 / 2)
#         # return hypot
#         return hypot((self.x - other.x), (self.y - other.y))  # др. способ со станд. ф-цией
# p = Point()
# p = [Point(),Point()]
# print(p)

# вычесть две точки
# p1 = Point(5,7)
# p2 = Point(9, 12)
# print(p1 - p2)

# расстояние между двумя точками
# p1 = Point(5,7)
# p2 = Point(9, 12)
# print(p1 - p2)
# print(p1 + p2)

# class MyTime:
#     def __init__(self, minutes, seconds):
#         if 0 <= minutes <= 60:
#             self.minutes = minutes
#         if 0 <= seconds <= 60:
#             self.seconds = seconds
#
#     def __str__(self):
#         return f'<Time {self.minutes:02}:{self.seconds:02}>'
#
#
#     def __add__(self, other):
#         m = self.minutes + other.minutes
#         s = self.seconds + other.seconds
#         m += s //60
#         s += s % 60
#         m = m % 60
#         return MyTime(m,s)


# t = MyTime(13, 15)
# print(t)
# t1 = MyTime(20,10)
# print(t + t1)
########################################################################
# список спецметодов - см. док.
# спецметод метод  __call__ - позволяет экземпляру класса вести себя как функция, т.е. становится вызываемым

# class SquareFunction:
#     def __init__(self, a, b, c) :
#         self.a = a
#         self.b = b
#         self.c = c
#     def __call__(self, x) :
#         return self.a * x ** 2 + self.b * x + self.c  # считает квадратичную функцию
#
# s = SquareFunction(1,2,3)
# print(s(2))

#############################
# ООП Наследование  (Inheritance)

# from math import pi
# from abc import ABC, abstractmethod  #можно использовать для указания абстрактного класса (ниже), но редко применяется
#
#
#
# class Shape(ABC):  #  в данном примере это абстрактный класс
#     def info(self):
#         print(f'Класс:  {self.__class__.__name__}')
#
#     def area(self):
#         pass  # джля абстрактного класс
#
#     def perimetr(self):
#         pass
#
#
#     # фигуры
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def perimetr(self):
#         return 2 * pi * self.radius
#
#     def area(self):
#         return pi * self.radius ** 2
#
#
# class Rectangle(Shape):
#     def __init__(self, widt, long):
#         self.widt = widt
#         self.long = long
#         self.name = 'прямоугольник'
#
#     def perimetr(self):
#         return 2 * (self.widt + self.long)
#
#     def area(self):
#         return self.widt * self.long
#
#     def get_name(self):
#         return self.name
#
#
# class Square(Rectangle):  # производный от класса Rectangle
#     def __init__(self, side):
#         super().__init__(side, side)  # приобретает все свойства родителя
#         self.side = side
#         self.name = 'квадрат'


# все, что ниже, не нужно, т.к. это уже есть в родительком (базовом) классе
##############################################
# def perimetr(self):
#     return 4 * self.side
#
# def area(self):
#     return self.side ** 2
############################################

# class Triangle(Square):
#     def __init__(self, side):
#         super.__init__(self, side)  # если множ.наслед- е, то н. указывать имя род.класса вместо "super"
#         self.side = side
#         self.name = 'треугольник'
#
#     def area(self):
#         return self.side ** 2 * 3**0.5 / 4
#
#     def perimetr(self):
#         return 3 * self.side





# s = Square(5)
# print(s.area())
# print(s.perimetr())
# print(s.name)
# s.info()
#
# t = Triangle(8)
# print(t.area())
# print(t.perimetr())
# print(t.name)
# s.info()

############################################


#task  "банк"
# """
# условия
#
# class: BankAccount(owner, balance)
# методы: deposit(amount), withdrow(amount), get_balance()
#
# """
#
# class BankAcount:
#     def __init__(self, owner, balance=0):
#         self._owner = owner
#         self._balance = balance
#
#     def get_balance(self):
#         return self._balance
#
#     def dep_amount(self, amount):
#         if amount > 0:
#             self._balance += amount
#             print(f'Депозит пополнен на сумму {amount}')
#         else:
#             print(f'Нельзя вносить отрицательную сумму на депозит')
#
#     def with_amount(self, amount):
#         if 0 < amount < self._balance:
#             self._balance -= amount
#             print(f'С депозита снята сумма {amount}')
#         else:
#             print('Не хватает средств. Овердрафт недоступен')
#
#
# client1 = BankAcount('John')
# client1.dep_amount(500)
# client1.with_amount(600)
# print('Остаток: ', client1.get_balance())
##########################################
#Home task  10_07_25

"""
смоделировать зоопарк с разными животными
Условия:
Базовый класс Animal c методом make_sound().
классы-наследники: Dog, Cat, Elephant c переопределением звуков.
Класс Zoo хранит список животных и метод make_all_sounds
"""
# from abc import ABC, abstractmethod
#
#
# class Animal(ABC):
#     def make_sound(self):
#         pass
#
#
#     def make_sound(self):
#         print('Животное издает звуки: "У-р-р"')
#
#
# class Dog(Animal):
#     def  __init__(self, color):
#         self.color = color
#         self.name = 'собака'
#
#     def  make_sound(self):
#         print(f'Животное:  {self.color} {self.name} издает звуки: "Гав-гав-ррр"')
#
#
# class Cat(Animal):
#     def __init__(self, color):
#         #super().__init__(place)
#         self.name = 'кошка'
#         self.color = color
#
#
#     def make_sound(self):
#         print(f'Животное:  {self.color} {self.name} издает звуки: "Мяу-мяу-мурр"')
#
#
# class Elephant(Animal):
#     def __init__(self, color):
#         self.color = color
#         self.name = 'слон'
#
#     def make_sound(self):
#         print(f'Животное {self.color} {self.name} издает звуки: "U-u-u-u"')
#
# class zoo:
#     def __init__(self):
#         self.animals = []  # закончить
#
#     def add_animals(self):
#
#
#
# animal1 = Cat('черная')
# animal2 = Dog('пегая')
# animal3 = Elephant('белый')
# print(animal1.make_sound())
# print(animal2.make_sound())
# print(animal3.make_sound())
# Animal.info(animal1)
#

#########################################
# Протоколы
# TCP, IP - обычная запись: TCP/IP

#############################

# import sys
# print(len(sys.argv))
#
# if len(sys.argv) >= 2:
#     match sys.argv[1]:
#         case 'p':
#             print('Привет')
#         case 'g':
#             print('Пока')
#         case _:
#             print('Пока')
#
#     print('Я', sys.argv[0] , 'и мой аргумент', sys.argv[1])


#########################
# Периодические задачи
# import schedule
# import datetime

####################################
#выполнение задач через опр. интервал времени, по расписанию
# i = 1
#
# def job():  # действия, которые будут выполняться
#     global i
#     print(f'Скрипт запустился {i}-раз')
#     i += 1
#     t = datetime.datetime.now()
#     print('Время', t.strftime('%H:%M:%S'))
#
# schedule.every(3).seconds.do(job)
#
# while True:
#     schedule.run_pending()  # инициализировать выполнение

import csv

from PIL.EpsImagePlugin import field
from jinja2.lexer import newline_re
from urllib3.filepost import writer

# data = [
#     ['name', 'age', 'city'],
#     ['Борис', '25', 'Воронеж'],
#     ['Владимир', '28', 'Тверь'],
#     ['Глеб', '35', 'Москва'],
#]

#with open('people.csv', 'r', encoding='utf-8') as  f:
    # dict_reader = csv.DictReader(f)
    # for row in dict_reader:
    #     print(f'{row['name']} живет в городе {row['city']})

# data = {
#     'name': 'Борис',
#     'age': '27',
#     'city': 'Москва'

#}
# with open('file.csv', 'w', newline='', encoding='utf-8') as f:
#     writer = csv.DictWriter(f, field_names=field_names)
#     writer.writerow(data)
#     # reader = csv.reader(f, delimiter=',', quotechar='"')
#     # for row in reader:
#     #     print(row)

# with open('employee.csv', 'w', newline='', encoding='utf-8') as f:
#     writer = csv.writer(f)
#     writer.writerow(data)

# режимы квотирования
# data = ['name', 25, 'town']
# with open('sample.csv', 'w', newline='', encoding='utf-8') as f:
#     writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)  # надо записать все, но числа в кавычки не заключать
#     writer.writerow(data)
########################################
# Zip
# from zipfile import ZipFile
# import os
#
# csv_files = [f for f in os.listdir() if f.endswith('.csv')]
# # print(csv_files)
# with ZipFile('archive.zip', 'w') as myzip:
#     for file in csv_files:
#         myzip.write(file)
#         os.remove(file)
# with ZipFile('archive.zip', 'r') as zip_obj:
#     zip_obj.extractall()


# file_to_extract = ['people.csv', 'file.csv']
# with ZipFile('archive.zip', 'r') as zip_obj:
#     zip_obj.extractall(members=file_to_extract)  # распаковать только отдельные файлы

# with ZipFile('archive.zip', 'r') as zip_obj:
#     print(zip_obj.namelist())  # список файлов в архиве
########################################

# JSON (Java Script Object Notation)
#load - для чтения из файла
#loads - для чтения данных в строковом представлении - данные прямо в этом же файле
import json

#чтение данных
# with open('dogs.json', 'rt') as d:
#     #data = json.load(d)  # напрямую из файла
#     temp = d.read()  # прочитали файл как строку
#     data = json.loads(temp)  # сделали словарь из строки, читая построчно
#     print(data)
#
# for i in range(len(data)):  # для нескольких, также можно enumerate
#     print(f'i+1')
#     for k, v in data[i].items():
#         if type(v) == list:
#             print(f'\t{k}: {', '.join(v)}')
#         else:
#             print(f'\t{k}: {v}')
#
    # for k,v in data.items():
    #     if type(v) == list:
    #         print(f'{k}: {', '.join(v)}')
    #     else:
    #         print(f'{k}: {v}')



# запись

d = {
    'ананас': 300,
    'банан': 400,
    'яблоко': 120,
    'груша': 280,
}

# with open('fruits.json', 'wt', encoding='utf-8') as f:
    #json.dump(d,f, indent=4)  #запись в файл с отступом 4, для читабельности
data = json.dumps(d, indent=4)  #вывод в виде строки
print(data)




