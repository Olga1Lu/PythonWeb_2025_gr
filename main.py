prompt =  """ Витязь на распутье 
Налево (L) пойдешь, вольну-волю обретешь
Направо (R) пойдешь, коня потеряешь 
Прямо(F) пойдешь, сыт и весел будешь """

print(prompt)
choice = input('Куда идем (L, R или F): ')


if choice == 'L' or choice == 'l':
    print('Вольну-волю обретешь')

elif choice == 'R' or choice == 'r':
    print('Коня потеряешь')

elif choice == 'F' or choice == 'f':
    print('Сыт и весел будешь')

else:
    print('Подумай еще, да не прогадай!')


print('Конец!')