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
# from PIL import  Image, ImageFilter, ImageEnhance
# from docx.enum.text import WD_ALIGN_PARAGRAPH

# orig = Image.open('imges/sanday.jpg').convert('RGB') # конвертируем в RGB-формат на всякий случай
# up = orig.crop((0,0,600,200))
# down = orig.crop((0,200,600,400))
# new = Image.new('RGB', (600,400))
#
# new.paste(down, (0,0))
# new.paste(up,(0,200))
# new.show()

#orig = Image.open('imges/piton.jpg').convert('RGB') # конвертируем в RGB-формат на всякий случай,
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
# from docx import Document
# from docx.enum.text import WD_ALIGN_PARAGRAPH
# from docx.shared import Cm, Inches, Mm, Pt  # для размеров
# doc = Document()  # создали конструктор, создание экземпляра документа

# Добавление заголовка
# doc.add_heading('Отчет за месяц', 1)  # заголовок первого уровня
# paragraf = doc.add_paragraph() # отступ чтобы начать новый абзац
# paragraf = doc.add_paragraph('В отчете представлены') # с лед.уровень
# paragraf.add_run('  ключевые показатели').bold = True  # можно что-то добавить в абзац, приклеиться с конца
# run - это что-то внутри абзаца, текс, картинка и т.п.

#добавление списка
# paragraf = doc.add_paragraph()
# paragraf_format = paragraf.paragraph_format
# paragraf_format.alignment = WD_ALIGN_PARAGRAPH.LEFT

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
#from docxtpl import DocxTemplate  # для экселя проверить команду в мастер - образце

#пустой файл excel
# from openpyxl import Workbook  #  подключили метод "конструктор"
#
# wb = Workbook()  # создали книгу
# ws = wb.active  # обратились к активному листу
# ws.title = 'Отчет' # назвали лист
# wb.save(('docs/report.xlsx'))

# запись данных в существующий файл
#from openpyxl import load_workbook  # подключили метод
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
# for row in ws.iter_rows(min_row=2, values_only=True) :
#     fio, pos, dept = row  # распаковка кортежа
#     print(f'Фамилия: {fio}, Должность {pos}, Отдел {dept}')

########################################
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

from package1 import  greet , add1  # если в init прописана связь, возможно и доступ
print(greet('Мир'))
print(add1(7,3))
# print('Автор', autor) - как распечатать ?

# from package1 import *  # для всех
# print(package1.module_hidden_function())