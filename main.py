####################
#Документы
# Word - DOCX
# from docx import Document
# from docx.enum.text import WD_ALIGN_PARAGRAPH
# from docx.shared import Cm, Inches, Mm, Pt  # для размеров
# doc = Document()  # создали конструктор, создание экземпляра документа
from itertools import count

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
with open('info.txt', 'rt', encoding='utf-8') as fo :
    text = fo.read()
    lst = text.splitlines()
    print(lst)
# менеджер конт. проследит, чтбы файл закрылся
