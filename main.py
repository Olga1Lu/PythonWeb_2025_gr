# ключевое слово in

# word = 'поток'
# if 'ток' in word
#     print('Есть')

# цикл for
# for <переменная> in <итерируемый объект>> :
#     команды

# word = 'поток'

# for ch in word :
#     print(ch)

# итератор  range(start, stop, step)
# for i in range (0,3,1) :
#     print(i)
# промежуток: старт включается, финиш - нет
# по умолч.: старт=0б шаг=1

# for _ in range (2,13,2) :  # переменная i не используется.
#     print(i)

for i in range (1,101) :
    if i % 10 == 5 :
        if i == 15 :
            continue
        print(i)