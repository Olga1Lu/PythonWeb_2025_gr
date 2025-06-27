# Коллекции
# Множества, списки, словари, коллекции

# множества

s = set()  # Пустое
s = {'3' , '5' , '7' , 3 , 10, '3'}
# print(s)
# s.add('8.5')
# print(s)
# print('Есть ли 3 ?')
# if str(3) in s:
#     print('Да')
# for item in s :
#     if item == '3' :
#         print(item)
# print(f'Число элементов: {len(s)}')

# print(dir(s))

#'add', 'clear', 'copy', 'difference', 'difference_update', 'discard',
 #'intersection', 'intersection_udate'
# 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference',
# 'symmetric_difference_update','union', 'update']

#удаление эл-тов  из множества
s.remove('3')  # вызывает ошибку, если эл-та нет
s.discard('3')  # удаляет вслепую
temp = s.pop()  # удаляет случайный эл-т и вовращает его, если пустое мн-во, то er
print(temp)
# s.clear()  # очистка полностью
for item in s :
    print(item)






