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

# break
# continue

# num = 3  # надо угадать его
# var = ''
#
# print('Угадайте число')
#
# while True :
#     var = int( input('Ваше значение: '))
#     if var == num :
#         print('угадали!')
#         break  # фцикл прерван
#     elif var > num :
#         print('Число больше загаданного')
#     else:
#         print('Число меньше загаданного')
#
# print('Приходи еще')
count = 0
while count < 5 :
    count += 1
    if count == 3 :
        continue  # прервать текущую итерацию и начать следующую
    print(f'Итерация номер: {count}')