# Коллекции
# Множества, списки, словари, коллекции

# множества
#города
s = set()  # Пустое

city =

while  (city := input('назовите город: ')) != '' :

     if city in s :
         print('Такой город уже есть')
     else:
         s.add(city)
print(f'Итого названо : {len(s)} городов')
for item in s :
    print('\t' , item)



s.remove('3')  # вызывает ошибку, если эл-та нет
s.discard('3')  # удаляет вслепую
temp = s.pop()  # удаляет случайный эл-т и вовращает его, если пустое мн-во, то er
print(temp)
# s.clear()  # очистка полностью
for item in s :
    print(item)






