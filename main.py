# prompt =  """ Витязь на распутье
# Налево (L) пойдешь, вольну-волю обретешь
# Направо (R) пойдешь, коня потеряешь
# Прямо(F) пойдешь, сыт и весел будешь """
#
# print(prompt)
# choice = input('Куда идем (L, R или F): ')
#
#
# if choice == 'L' or choice == 'l':
#     print('Вольну-волю обретешь')
#
# elif choice == 'R' or choice == 'r':
#     print('Коня потеряешь')
#
# elif choice == 'F' or choice == 'f':
#     print('Сыт и весел будешь')
#
# else:
#     print('Подумай еще, да не прогадай!')
#
#
# print('Конец!')
# hour = int(input('Который час?  ')) # 0-23
# if hour > 23 :
#     hour = 23
# if hour < 0 :
#     hour = 0
#
# if 7 <= hour < 12 :
#     print ('Доброе утро!')
# elif 12 <= hour < 18 :
#     print('Добрый день!')
# elif hour >= 18 and hour < 22 :
#     print('Добрый вечер!')
# elif hour >= 22 or hour == 0 :
#     print('Доброй ночи!')
# else :
#     print('Доброго времени суток!')
# print('Конец!')

# iterable object
a = input('Введите слово ')
if not a or len(a) < 4 :
    print('Ничего нет или слово слишком короткое')
else :
    print('Вы ввели слово: "' + a + '" его длина', len(a) , 'букв')
# else:
   # print('Вы ввели слово ', a, ' его длина меньше 4 букв')
