# Циклы:
# while
# for
counter = 0  # обнуляем счетчик
# цикл из 5 итераций
while counter < 5 :
    print(f'Итерация номер: {counter}')
    # counter = counter + 1 # инкремент
    counter +=  1  # инкремент (краткая завпись)
# др. операторы: *=  /=   -=

print(f'Итого уже {counter}')
print('обратный отсчет:')

while counter > 0 :
    print(f'Итерация номер: {counter}')
    counter -=  1  # декремент (краткая завпись)
print(f'Итого уже {counter}')
