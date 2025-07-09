# Регулярные выражения - поиск по паттерну
# Regular expressions (re)
# r-строка -  row-string (игнорирует все управляющие последовательности)
# Квантификаторы (quantity)
# {m} - ровно m раз
# {m,} - m раз и более
# {,n} - не более n раз
# {m,n} - от m до n (пишем без пробелов)
# ? - от нуля до одного (фнфлог {0,1}
# * - от нуля до бесконечности (она равна 32767), соответствует {0,}
# + - от 1 до бесконечности, соответствует {1,}
# import  re
# from os.path import split



# pattern = '20'
# test_str = '10 плюс 20 будет 30'
#
# result = re.search(pattern, test_str)
# print(result)

# pattern = r'\а\п\р'  # регулярное выражение
# test_str = '10 плюс 20 будет 30'
#
# result = re.search(pattern, test_str)
# print(result)

# pattern = r'\b\w{4}\b'  # регулярное выражение (все слова из 4 символов)
# test_str = 'дома было холодно'
#
# #result = re.search(pattern, test_str)  # ищет одно(первое) вхождение
# result = re.findall(pattern, test_str)  # ищет все вхождения
# print(result)


# pattern = r'\d'  # регулярное выражение (все цифры от 0 до 9)
# test_str = '4 тел 45  1256'
#
# #result = re.search(pattern, test_str)  # ищет одно(первое) вхождение
# result = re.findall(pattern, test_str)  # ищет все вхождения
# print(result)

# тернарный if
# pattern = r'\d'  # регулярное выражение (все цифры от 0 до 9)
# test_str = 'телефон 112'
#
# result = re.findall(pattern, test_str)  # ищет все вхождения
# print('Цифры есть') if result else print('Цифр нет')  # тернарный оператор if работает только с выражениями

# pattern = r'\d{3}'  # регулярное выражение (три цифры подряд)
# test_str = 'телефон 112'
#
# result = re.findall(pattern, test_str)  # ищет все вхождения
# print(result)

# pattern = r'начало\Z'  # оканчивается на опр.значение
# test_str = 'Главное - начало'
#
# result = re.findall(pattern, test_str)  # ищет все вхождения
# print(result)


# pattern = r'[0-5][0-9]'  # два числа подряд, одно от 0 до 5, др.- 0-9
# test_str = 'Время - 07:45'
#
# result = re.findall(pattern, test_str)  # ищет все вхождения
# print(result)


# pattern = r'[а-яА-Я]'  # все буквы от а до я и от А до Я
# test_str = 'Время - 07:45'
#
# result = re.findall(pattern, test_str)  # ищет все вхождения
# print(result)

# pattern = '[^ерм]'  # все кроме е,р,м (их исключили)
# вытащить текст из скобок
# pattern = r'\((.+?)\)'  # вытащить текст из скобок (повтор один раз и более), "." - любой символ
# test_str = 'поиск по образцу (pattern)'
#
# result = re.findall(pattern, test_str)  # ищет все вхождения
# print(result)

# pattern = 'o{2,5}'
# test_str = 'Google, Gooogle, Goooogle'
#
# result = re.findall(pattern, test_str)  # ищет все вхождения
# print(result)

# pattern = r'стеклянн?ый'  # вторая "н"может присутствовать , но необязат-но

# "жадный" квантификатор
# pattern = r'<img.*>'  # жадный (greedy quantifiers)
# test_str = 'Картинка<img src="bg.jpg"> в тексте</p>'

# result = re.findall(pattern, test_str)  # ищет все вхождения
# print(result)

# "ленивый" квантификатор (lazy, non-greedy)
# pattern = r'<img.*?>'  # жадный
# test_str = 'Картинка<img src="bg.jpg"> в тексте</p>'
# #pattern = r'<img[^>]+src="([^">])+)"'
# result = re.findall(pattern, test_str)  # ищет все вхождения
# print(result)

# pattern = r'<img[^>]+src="([^">])+)"'  # только путь к картинке
# test_str = 'Картинка<img src="bg.jpg"> в тексте</p>'
# абзац
# test_str = '<b>Вот начало: </b><p>Содержимое</p><i>и т.д.</i>'
# pattern = '<p>(.*?)</p>'  #содержимое абзаца html
# result = re.findall(pattern, test_str)  # ищет все вхождения
# print(result)

# test_str = '<b>Центрируем </b><p align="center">Содержимое</p><i>и т.д.</i>'  # устаревший способ для центровки в html
# #pattern = '<p>(.*?)</p>'  #содержимое абзаца html
# pattern = r'<p[^>]*>(.*?)</p>'  # содержимое абзаца html с атрибутами, без захвата лишнего
# result = re.findall(pattern, test_str)  # ищет все вхождения
# print(result)

# убираем все знаки препинания
# def rem_punct(input_str: str) -> str :
#     """
#     методом sub() заменяем все найденные
#     совпадения пустой строкой и возвращаем очищенную
#     :param input_str:  строка со зн.препинания
#     :return: строка, очищенная от зн.преп-я
#     """
#     return re.sub(r'[^\w\s]', '', input_str)
# test_str = 'Язык Puthon, являясь интуитивно понятным, прост для изучения! Ну и PEP8'
#
# result = rem_punct(test_str)
# print(result)

# разделить по разным признакам сразу
# test_str = '  яблоко, груша. банан ; слива !   абрикос  '
# #test_str = ''.join(test_str.split())  # V1
# print(test_str)
# pattern = r'[,.;:!]'
# result = re.split(pattern, test_str)
# # через map
# #result = list(map(lambda  x: x.strip(), result))
#
# # через строчное выражение с сортировкой
# result = sorted(x.strip() for x in result)
# print(result)

# import requests
# вытащить картинку из текста с сайта
# pattern = r'<img[^>]+src="([^">]+)"'
# test_str = '<img heit="50" width="150" src="images/bg.jpg">'

# html = requests.get('https://skillbox.ru').text
# print(html)
# result = re.findall(pattern, html)
# print(result)
#################################################

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

from lib import Car
from lib import Clicker
from lib import Separator
from lib import Sorter
from lib import Balance

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


b = Balance()

b.add_left(5)
b.add_right(4)
b.add_left(3)
b.add_right(5)
b.add_left(6)
b.add_right(7)
b.add_left(2)
b.add_right(4)

print(b.result())

