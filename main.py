# Mathc Case (3.10)
from re import match

print('Возможные ходы:\n\tL - влево\n\tR - вправо\n\tF - прямо')

while True :
    ch = input('ваш выбор: ')
    match ch:
        case 'L' | 'l' | 'д' | 'Д' :
            print('Свернули влево')
        case 'К' | 'k' | 'к' | 'К':
            print('Свернули вправо')
        case 'F' | 'f' | 'ф' | 'Ф':
            print('Свернули влево')
        case 'F' | 'f' | 'ф' | 'Ф':
            print('До свидания!')
            break
        case _:
            print('Свернули влево')
