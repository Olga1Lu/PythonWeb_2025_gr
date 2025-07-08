
# Пишем свои модули
#from . lib import summ - из текущей директории, из текущего файла
#from .. lib import summ - из директории уровнем выше
#from .lib import summ - импорт относительно текущего файла, т.е. в той же директории, что и текущий файл
# подключаем свой модуль
#V1
# import  lib
# c = lib.diff(7,3)
#
# #V2
# from lib import diff
#
# print(diff(7,3))
#
#
# print(__name__)
# def main():
#     from lib import diff, summ
#     print(summ(7,3))
#
# if __name__ == '__main__':   # пишем main и нажимаем 'tab'
#    print('Это main')
#    main()

#################
# пакеты (директория, где есть неск.модулей и файл _init_.py, в котором записаны связи, указано разграничение прав
# либо просто указывает, что это пакет)

# from package1.module import  greet  # если init пустой
# print(greet('Мир'))

# from package1 import  greet , add1  # если в init прописана связь, возможно и доступ
# print(greet('Мир'))
# print(add1(7,3))
# print('Автор', autor) - как распечатать ?

# from package1 import *  # для всех
# print(package1.module_hidden_function())

#############################
# Файлы

# name.<расширение>
# типы файлов доступные для Python: txt, html, xml, бинарные
# doc,xls - гибридные

# t - текстовые файлы (txt, html, xml)
# b -  бинарные файлы (jpg, avi, mp3)
# к одной из этих литер добавляется:
# w - открываем файл на запись (при этом все что было стирается, если файла не было, то он создастся)
# a - открываем файл на запись (при этом все добавляется в конец, если файла не было, то он создастся)
# r - чтение

# Текстовые файлы

#fo = open('info.txt', 'wt', encoding='utf-8')  # создание объекта
# print(fo)  # если encoding='cp1251', то надо перекодировать: encoding='utf-8' - это стандарт для Pycharm
# print(fo.mode)
# print(fo.name)
# print(fo.encoding)
#
# count = fo.write('Этот текст будет в файле !')
# print('В файл записано ', count, 'байт')

#fo.close()

# Чтение из файла
# fo = open('info.txt', 'rt', encoding='utf-8')
# text = fo.read(4)  # в скобках можно указать (цифрами) сколько байт читать
# text = fo.read(10)
# print(text)
#
# fo.close()

# fo = open('info.txt', 'rt', encoding='utf-8')
# text = fo.read(11)  # остановка в том месте где остановилось чтение, след.чтение с этого места
# fo.read(6)
# text += fo.read(7)
# print('вот что в файле', end=': ')
# print(text)
# fo.close()

# Добавление в файл (в конец и там останавливается)
# fo = open('info.txt', 'at', encoding='utf-8')
# fo.write(' Хороший текст')
# print('вот что в файле', end=': ')
# fo.close()

# печать внутрь файла (в конец)
# fo = open('info.txt', 'at', encoding='utf-8')
# print('\nА вот это будет уже с новой строки', file=fo)
# print('\nА вот еще одна строка', file=fo)
# fo.close()



# # построчное чтение V1
#fo = open('info.txt', 'rt', encoding='utf-8')
# while text := fo.readlines() :
#     print(text.rstrip('\n'))
# fo.close()

# # построчное чтение V2
# lst = fo.readlines()
# lst = list(map(lambda  x: x.str('\n'), lst))
# print(lst)

# построчное чтение V3
# text = fo.read()
# lst = text.splitlines()
# print(lst)

# открытие с менеджером контекста
# with open('info.txt', 'rt', encoding='utf-8') as fo :
#     text = fo.read()
#     lst = text.splitlines()
#     print(lst)
# менеджер конт. проследит, чтбы файл закрылся

#####################################

import  os  # модуль управления операционной системой

# os.mkdir('libs')  # создание директории, если директория уже существует, тогда ошибка
#
# os.makedirs('libs', exist_ok=True)  # если директория уже существует, ошибки не будет
# if os.path.exists('libs') :  # проверка существования пути
#       os.rmdir('libs')  # удаление директории

# Переключение директорий
# path = os.getcwd()  # узнать, где находимся (текущая)
# print(path)
#
# os.chdir(path + '/imges')
# print(os.getcwd())
#
# os.chdir('..')
# os.chdir(path + '/Fonts')
# print(os.getcwd())

# список всех файлов в директории
# path = os.getcwd()
# os.chdir(path + '/imges')
# #all_files = [f for f in os.listdir('.')]
# #all_files = [f for f in os.listdir('.') if f.endswith('.jpg')]  # список с фильтрацией
# all_files = [f for f in os.listdir('.') if f.startswith('pi')]  # список с фильтрацией
# print(all_files)
# os.chdir('..')  # вернулись в корневую директорию
#res = []
# with open('info1.txt', 'r') as f:
# #f = open('info1.txt', 'rt', encoding='utf-8')
#     while temp := f.readline():
#         res += temp.split(', ')
# print(type(res))
# res = list(map(lambda x : x.rstrip('\n'), res))
# print(res)
# res = set(res)
# res = sorted(int(x) for x in res)
# print(res)
# f.close()

# Или др. вариант короче:
# with open('info1.txt', 'r') as f:
#     while temp := f.readline().rstrip('\n'):
#         res += temp.split(', ')
#
# res = sorted(int(x) for x in set(res))
# print(res)
# f.close()

###################################
# сохранение сложных структур "сериализация и десериализация"

# 1 способ: pickle
# import pickle
# import pprint
# d = {
#     'стол': 'table' ,
#     'стул': 'chair'
# }

#сериализация
# with open ('dictfile.dat', 'wb') as p:
#     pickle.dump(d, p)  #d - что сериализуем, p - куда сериализуем
# p.close()

# десериализация
# with open ('dictfile.dat', 'rb') as p:
#     d = pickle.load(p)
# pprint.pprint(d, width=15)
# p.close()

# организация путей /см. файл pathlib.py
# from pathlib import *
# print(img_dir)
# print(font_dir)

###############################

# исключения, обработка ошибок (run time)
#полная конструкция:
# try:
#     что пытаемся сделать
#except:
#    обрабатываем исключения, т.е. может быть несколько "except"
#else:
#    если исключения не было
#finally:
#    выполняется в любом случае

# flag = False  # открывался ли файл на запись
# try:
#     fo = open('info3.txt', 'rt', encoding='utf-8')
#
# except FileNotFoundError :  # если не указать какое, то будет действовать для любого исключения
#     fo = open('info3.txt', "wt", encoding='utf-8')
#     flag = True
#     print('файл не обнаружен и создан с параметрами по умолчанию')
#     # with open('info3.txt', "wt", encoding='utf-8') as fo :
#     #     fo.write('по умолчанию')
# else:
#     print('Файл открыт успешно. Читаем и закрываем')
#     print(fo.read())
#     fo.close()
# finally:
#     if flag:  #если файл был открыт на запись
#     # print('продолжаем работать')
#         fo.write('по умолчанию')
#         fo.close()


