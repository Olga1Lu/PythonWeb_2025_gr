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
# count = 0
# while count < 5 :
#     count += 1
#     if count == 3 :
#         continue  # прервать текущую итерацию и начать следующую
#     print(f'Итерация номер: {count}')


h = 0

# while h <= 150 or h >= 180 :
#     h = int(input('Укажите Ваш рост в см: '))
#     if h > 150 and h < 180 :
#         print('Подходит.')
#         break
#     else:
#         print('Не подходит')
# h = int(input('Укажите Ваш рост в см: '))
# while h <= 150 or h >= 180 :
#     print('Не подходит.')
#     h = int(input('Укажите Ваш рост в см: '))
#
# print('Подходит')

h = int(input('Укажите Ваш рост в см: '))

while not (150 <= h <= 180) :
    print(f'Рост {h} не подходит')
    h = int(input('Укажите Ваш рост в см: '))
print('Подходит')
