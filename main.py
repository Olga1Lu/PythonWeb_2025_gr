
total = 0
total_suc = 0
# total_ensuc = 0
min_v = float('inf')
max_v = float ('-inf')
num =
# while (num := int(input('Введите рост: '))) != -1 :
    if 150 <= num <= 180:
        total_suc += 1
        if num < min_v :
            min_v = num
        if num > max_v :
            max_v = num

    total += 1
print(f'Всего кандидатов: {total}')
print(f'Успешных: {total_suc}, неуспешных: {total - total_suc}')
print(f'Макс.рост: {max_v}')
print(f'Мин.рост: {min_v}')

# три монеты
# coin1 = int(input('Вес первой монеты '))
# coin2 = int(input('Вес второй монеты '))
# coin3 = int(input('Вес третьей монеты '))
#
# if coin1 == coin2 :
#     print('Фальшивая монета - третья')
# elif coin1 == coin3 :
#     print('Фальшивая монета - вторая')
# else:
#     print('Фальшивая монета - первая')
#
# print('Конец.')

# много монет

coin1 = int(input('Введите вес монеты '))
coin2 = int(input('Введите вес монеты '))
coin3 = int(input('Введите вес монеты '))

if coin3 == coin1 and coin3 == coin2 :
      nom = coin3

      while nom == coin3 :
           coin3 = int(input('Введите вес монеты '))

      print('Эта монета фальшивая')
else :

     if coin1 == coin3 :
         print('Вторая монета фальшивая')
     elif  coin1 == coin2:
         print('Третья монета фальшивая')
     else :
         print('Первая монета фальшивая')

print('Конец.')
