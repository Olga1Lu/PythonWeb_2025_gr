# min , max, average , summ , production
# N = 5
# total = 0
# prod = 1
# min_val = float('inf')  # плюс бесконечность
# max_val = float('-inf')  # минус бесконечность
# for _ in range (N) :
#     num = int (input('введите целое число: '))
#     if num < min_val:
#         min_val = num
#     if num > max_val:
#         max_val = num
#     total += num
#     aver = total / N
#     prod *=num
#
# print(f'Сумма: {total}')
# print(f'Произведение = {prod}')
# print(f'Среднее арифм.: {aver}')
# print(f'мин= {min_val}')
# print(f'мах= {max_val}')
#  N = 5
#  fact = 1
#  for i in range (1,N+1):
#      fact *= i
# print(fact)

# вложенные циклы

for i in range (1, 10) :
    for j in range (1, 10) :
        print(f'Элемент {i}*{j} = {i*j}', end='\t')
    print()
