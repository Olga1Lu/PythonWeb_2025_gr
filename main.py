#########################################
# Протоколы
# TCP, IP - обычная запись: TCP/IP
from tkinter.filedialog import dialogstates

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

#import csv

from PIL.EpsImagePlugin import field
from jinja2.lexer import newline_re
from urllib3 import connection_from_url
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
#import json

#чтение данных
#load - для чтения из файла
#loads - для чтения данных в строковом представлении - данные прямо в этом же файле

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

# d = {
#     'ананас': 300,
#     'банан': 400,
#     'яблоко': 120,
#     'груша': 280,
# }
#
# # with open('fruits.json', 'wt', encoding='utf-8') as f:
#     #json.dump(d,f, indent=4)  #запись в файл с отступом 4, для читабельности
# data = json.dumps(d, indent=4)  #вывод в виде строки
# print(data)
########################
# упражнение Получение прогноза погоды

###################################

# Бфзы данных
#чтение данных

"""
1.Импорт библ. sqlite3
2.подключаемся к БД
3.назначить "курсор"
4.работаем с БД (запросы и ответы)
5.отключаемся от БД
6.подтвердить изменения (commit) - делакется на уровне подключения
"""

import sqlite3
import csv

# подключаемся
connection = sqlite3.connect('db/movies.sqlite')

# курсор
cursor = connection.cursor()

# запрос (с помощью курсора)
# result = cursor.execute(
#     """
#     INSERT INTO users (name, age)
#     VALUES('Sim', 25),
#     ('Rom', 41)
#     """
# )
#print(result)  # получили объект

# fetch
# array =result.fetchall()  # получить все соответствия
# for title, year in array:
#     print(title, year) # распаковка на печать

# array =result.fetchone()  # получить только первое соответствие
# print(array)

# array =result.fetchmany(5)  #  первые 5 соответствий
# print(array)

# connection.commit()  # подтверждение
# connection.close()  # закрываем подключение

#########

#запись данных в БД
# с ошибкой!!
# connection = sqlite3.connect('db/movies.sqlite')
# cursor = connection.cursor()
#
# with open('people.csv', 'r', encoding='utf-8') as f:
#     reader = csv.reader(f, delimiter=',')
#     next(reader)  # пропустить заголовок
#
# for name, age in reader:
#     cursor.execute(
#         """
#         INSERT INTO users (name, age)
#         VALUES(?, ?),
#
#         """, (name, int(age))
#     )
#
# connection.commit()  # подтверждение
# connection.close()  # закрываем подключение

# class Crud:
#     def __init__(self, db_path):
#         self._conn = sqlite3.connect(db_path)
#         self._cur = self._conn.cursor()
#     def create(self, table_name, name, age):
#         self._cur.execute(
#             f"""
#             INSERT INTO {table_name}(name, age)
#             VALUES(?, ?),
#
# #        """, (name, int(age))
#         )
#         self._conn.commit()
#
#
#     def read(self, table_name):
#         res = self._cur.execute(
#             f'SELECT * FROM {table_name}'
#         ).fetchall()
#         for num, name, age in res:
#             print(num, name, age)
#
#     def update(self, table_name, id_num, name=None, age=None):
#
#             query = f'UPDATE {table_name} SET name="{name}", age={age} WHERE id={id_num}'
#
#             self._cur.execute (
#                 query
#             )
#
#             self._conn.commit()
#
#     def delet(self, in_num, table_name):
#         self._cur.execute(
#             f'DELETE  FROM {table_name} WHERE id ={in_num}'
#         )
#         self._conn.commit()
#
#
#     def __del__(self):  # переопределяем метод уничтожения объекта)
#         self._cur.close()
#         self._conn.close()
#
# db = Crud('db/movies.sqlite')
# db.create('users', 'Jull', 18)
# #db.update('users', 8, 'Евгений', 19)
# #db.delet(3, 'users')
# db.read('users')



##################################
# Погода и карта места через API

# import requests
# from PIL import Image
# import io  # базовый интерфейс ввода-вывода
#
# API_KEY = '3cd660f4466f3c3784bd9ca613c0ddaa'
# URL = 'http://api.openweathermap.org/data/2.5/weather'
# CITY = 'Санкт-Петербург'
#
# params = {
#     'q': CITY,   # город
#     'appid': API_KEY,  # ключ
#     'units': 'metric',
#     'lang': 'ru'
#
# }
#
# response = requests.get(URL, params=params)
# result = response.json()
#
# weather = result['weather'][0]['description']
# temperature = result['main']['temp']
# humidity = result['main']['humidity']
# wind = result['wind']['speed']
# print(f'Сегодня в городе {CITY}: {weather}')
# print(f'Температура: {temperature:.1f}\xB0C')
# print(f'Влажность: {humidity}%')
# print(f'Скорость ветра: {wind}m/c')
# data = result['coord']
# ll = f'{data['lon']},{data['lat']}'
# link = f'https://static-maps.yandex.ru/1.x/?ll={ll}&spn=0.005,0.005&l=sat&pt={ll},pm2dgl'  #картинка с местом на карте
# image = requests.get(link).content
# if image:
#     im = Image.open(io.BytesIO(image)).convert('RGB')
#     im.save('map.jpg')
# print(ll)

################################################

# Декораторы
# функция внутри другой функции
# def answer(question):
#     return 'самост'
#
# def dialog():
#     def answer(question):
#         if question.lower().startswith('когда'):
#             return  'Никогда'
#         else:
#             return 'УПППС'
#     question = input()
#     while question !=''
#         print(answer(question))
#         question = input()
#
# dialog()


# def upper_case_print(old_function):
#     def new_function(*args, **kwargs):
#         case = kwargs.pop('case', None)
#         if case == 'U':
#             args = [str(arg).upper() for arg in args]
#         elif case == 'L':
#             args = [str(arg).lower() for arg in args]
#         return old_function(*args, **kwargs)
#     return new_function
#
# new_print = upper_case_print(print)
#
# new_print('Привет, пока', case='L')

# non local
# def outer():
#     x = 5
#
#     def inner():
#         nonlocal x
#         print('Nonlocal x=', x)
#         x = 10
#     inner()
#     print('New x=', x)
#
# outer()

# def logger(func):
#     counter - 0
#
#     def decorated_func(*args, **kwargs):
#         nonlocal  counter
#         counter += 1
#         print(counter, '->', 'Аргументы:' , args,
#               'Именованные аргументы:' , kwargs)
#         result = func(*ar,**kwargs)
#         print('____', 'Результат:' , result)
#         return result
#     return decorated_func
#
# @logger  # ф-ция будет завернута в функцию logger
# def make_burger(meal='говядиной', onion=False, tomato=False):
#     print('Булочка')
#     if onion:
#         print('Луковые кольца')
#     print('Котлета с', meal)
#     if tomato:
#         print('Помидоры')
#     print('Булочка')
#
# make_burger('бараниной', onion=True)

import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        finish = time.time()
        print(f'Функция исполнялась:  {finish - start:.4f} сек.')
        return  result
    return wrapper

@timeit
def test():
    time.sleep(0.8)

test()
