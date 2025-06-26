# Циклы:


# цикл до ввода пустой строки
# 1 без моржа
# word = input('Введите слово: ')
#
# while word != '' :
#     print(f'Слово: "{word}')
#     word = input('Введите слово: ')
#
# print('строка пустая')


num = 3  # надо угадать его
flag = True  # флаг
var = ''

print('Угадайте число')

while flag :
    var = int( input('Ваше значение: '))
    if var == num :
        print('угадали!')
        flag = not flag  # флаг инвертирован
    elif var > num :
        print('Число больше загаданного')
    else:
        print('Число меньше загаданного')

print('Приходи еще')
