# Коллекции
# Множества, списки, словари, коллекции

# множества
#города
# s = set()  # Пустое
#
# while  (city := input('назовите город: ')) != '' :
#
#      if city in s :
#          print('Такой город уже есть')
#      else:
#          s.add(city)
# print(f'Итого названо : {len(s)} городов')
# for item in s :
#     print('\t' , item)



# s.remove('3')  # вызывает ошибку, если эл-та нет
# s.discard('3')  # удаляет вслепую
# temp = s.pop()  # удаляет случайный эл-т и вовращает его, если пустое мн-во, то er
# print(temp)
# # s.clear()  # очистка полностью
# for item in s :
#     print(item)



# cards = {3,7,'туз','валет','дама'}
# for item in cards :
#     if  item != 'туз'
#     print(f'Удален: {cards.pop()})
#     print(cards.pop())

# a = {1,2,3}
# b = {1,2,4}

 # объединение
#с = a.union(b)  #операнды можно менять местами, сложили, повторы убрали
 # c = a / b

# пересечение
#c = a.intersection(b) #операнды можно менять местами
# c = a & b

#разность
#c = b.difference(a)  # есть в "в" но нет в "а"
# c = b - a
# симметричная разность
#c = a.symmetric_difference (b) # есть только в одном или только в другом
# c = b ^ a
#print(c)

ss = {3,7,'дама','туз','валет'}
# вариант 1 - использвание операции вычитания
# st = {'туз'}
# sbt = ss - st
# print(sbt)

# вариант 2 - использование "pop"
# fl = False
# while ss :
#     s = ss.pop()
#     if s == 'туз'
#         ss.add(s)
#         fl = True
#     else:
#         print(s)
#     if fl and len(ss) == 1
#         break




