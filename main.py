
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

