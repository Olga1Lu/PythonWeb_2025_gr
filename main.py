# Регулярные выражения - поиск по паттерну
# Regular expressions (re)
#r-строка -  row-string (игнорирует все управляющие последовательности)
# Квантификаторы (quantity)
# {m} - ровно m раз
# {m,} - m раз и более
# {,n} - не более n раз
# {m,n} - от m до n (пишем без пробелов)
# ? - от нуля до одного (фнфлог {0,1}
# * - от нуля до бесконечности (она равна 32767), соответствует {0,}
# + - от 1 до бесконечности, соответствует {1,}
import  re

# pattern = '20'
# test_str = '10 плюс 20 будет 30'
#
# result = re.search(pattern, test_str)
# print(result)

# pattern = r'\а\п\р'  # регулярное выражение
# test_str = '10 плюс 20 будет 30'
#
# result = re.search(pattern, test_str)
# print(result)

# pattern = r'\b\w{4}\b'  # регулярное выражение (все слова из 4 символов)
# test_str = 'дома было холодно'
#
# #result = re.search(pattern, test_str)  # ищет одно(первое) вхождение
# result = re.findall(pattern, test_str)  # ищет все вхождения
# print(result)


# pattern = r'\d'  # регулярное выражение (все цифры от 0 до 9)
# test_str = '4 тел 45  1256'
#
# #result = re.search(pattern, test_str)  # ищет одно(первое) вхождение
# result = re.findall(pattern, test_str)  # ищет все вхождения
# print(result)

# тернарный if
# pattern = r'\d'  # регулярное выражение (все цифры от 0 до 9)
# test_str = 'телефон 112'
#
# result = re.findall(pattern, test_str)  # ищет все вхождения
# print('Цифры есть') if result else print('Цифр нет')  # тернарный оператор if работает только с выражениями

# pattern = r'\d{3}'  # регулярное выражение (три цифры подряд)
# test_str = 'телефон 112'
#
# result = re.findall(pattern, test_str)  # ищет все вхождения
# print(result)

# pattern = r'начало\Z'  # оканчивается на опр.значение
# test_str = 'Главное - начало'
#
# result = re.findall(pattern, test_str)  # ищет все вхождения
# print(result)


# pattern = r'[0-5][0-9]'  # два числа подряд, одно от 0 до 5, др.- 0-9
# test_str = 'Время - 07:45'
#
# result = re.findall(pattern, test_str)  # ищет все вхождения
# print(result)


# pattern = r'[а-яА-Я]'  # все буквы от а до я и от А до Я
# test_str = 'Время - 07:45'
#
# result = re.findall(pattern, test_str)  # ищет все вхождения
# print(result)

#pattern = '[^ерм]'  # все кроме е,р,м (их исключили)
# вытащить текст из скобок
# pattern = r'\((.+?)\)'  # вытащить текст из скобок (повтор один раз и более)
# test_str = 'поиск по образцу (pattern)'
#
# result = re.findall(pattern, test_str)  # ищет все вхождения
# print(result)

pattern = 'o{2,5}'
test_str = 'Google, Gooogle, Goooogle'

result = re.findall(pattern, test_str)  # ищет все вхождения
print(result)