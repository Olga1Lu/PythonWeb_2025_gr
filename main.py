# Исключения, обработка ошибок (run time)
#полная конструкция:
# try:
#     что пытаемся сделать
#except:
#    обрабатываем исключения, т.е. может быть несколько "except"
#else:
#    если исключения не было
#finally:
#    выполняется в любом случае
from logging import exception

#Пример полной конструкции (обычно finally и else не используется)
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

# если исключение не известно заранее
#print('Остаток от деления:')

# try:
#     value = int(input('На что делим число 10: '))
#     res = 10 % value
#     print(f'Остаток от деления 10 на {value} = {res}')
# except ZeroDivisionError:
#     print('На ноль делить нельзя!')
# # except ValueError:
# #     print('Надо вводить только целые числа')
# except Exception as exp :  # все остальные исключения
#     print('Произошло исключение:', exp.__class__.__name__, exp)  # универсальное сообщение

# пока не введем правильно, предлагается ввод
# loop = true
# while loop:
#     try:
#         value = int(input('На что делим число 10: '))
#         res = 10 % value
#         print(f'Остаток от деления 10 на {value} = {res}')
#     except ZeroDivisionError:
#         print('На ноль делить нельзя!')
# # except ValueError:
# #     print('Надо вводить только целые числа')
#     except Exception as exp :  # все остальные исключения
#         print('Произошло исключение:', exp.__class__.__name__, exp)
#     else:
#         loop = False

# бросаемся исключениями - raise (throw - для большинства др.ЯП)
# max_val = 10
# min_val = 1
#
# try:
#     val = int(input(f'Введите целое число от {min_val} до {max_val} : '))
#     if not min_val < val < max_val :
#         raise  ValueError('введенной число вне диапазона')
#     print(f'Введенное число {val} находится в заданном диапазоне')
# except ValueError as exp:
#     print('Надо быть внимательнее:', exp)

# Утверждения (assertion) нужен для проверки/тестирования программы, в продакшн не идет, их убирают
# try:
#     text = input('введите текст :')
#     assert  len(text) >3  # это утверждение
# except AssertionError :
#     print('Слишком короткий текст')

# Задача 1

lst = [1,2,3,4,5,6,7,8,9]
# fl = True
# while fl :
#
#     try:
#         ind = int(input(f'Введите индекс от 0 до {len(lst)} : '))
#         print(f'Число по индексу "{ind}": {lst[ind]}')
#     except ValueError :
#         print('Надо вводить только целые числа')
#     except IndexError :
#         print (f'Число должно быть в диапазоне от 0 до {len(lst)}')
#     except Exception as exp :  # все остальные исключения
#         print('Произошло исключение:', exp.__class__.__name__, exp)
#     else:
#         fl = False

# try:
#         ind = int(input('Введите индекс '))
#         if not -len(lst) < ind < len(lst) - 1:
#             raise ValueError('Индекс вне диапазона')
#         res = lst[ind]
#         print(f'Число по индексу "{ind}": {res}')
#
#     except Exception as exp :  # все остальные исключения
#         mess = exp.args
#         if mess.startwith('invalid literal') :   #в коммитек
#         print('вводить надо числа')
#     else:
#         print(exp)

# задача 2
# сделали с if - else
# while True:
#     a = input('введите первое число: ')
#     b = input('введите второе число: ')
#
#     if a.isdigit() and b.isdigit() :
#         if int(b) == 0:
#             print('На ноль делить нельзя.')
#         else:
#             print(int(a)/int(b))
#             break
#     else:
#         print('Вводить надо только числа.')

#  через исключения
# while True:
#     a = input('введите первое число: ')
#     b = input('введите второе число: ')
#     try:
#       res = int(a)/int(b)
#     except ZeroDivisionError :
#         print('На ноль делить нельзя')
#     except ValueError :
#         print('Необходимо ввести числа')
#         print(f'А введено : {a} и {b}')
#     else:
#         print(res)
#         break