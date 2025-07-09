# from itertools import count
class Balance:
    def __init__(self):
        self.right = 0
        self.left = 0
        self.str = ''

    def add_left(self, weigt):
        self.left += weigt


    def add_right(self, weigt):
        self.right += weigt

    def result(self) -> str:
        if self.left > self.right:
            self.str = 'левая чаша тяжелее'
        elif self.left < self.right:
            self.str = 'правая чаша тяжелее'
        else:
            self.str = 'чаши уравновешены'

        return  self.str


class Sorter:
    def __init__(self):
        self.words = []

    def add_word(self, word):
        self.words.append((word))

    def result(self):
        return sorted(self.words, key=lambda x: len(x))  # список слов отсортированных по длине


class Separator:
    def __init__(self):
        self.odd = []
        self.even = []  # четные

    def add_num(self, num):
        if num % 2 == 0:
            self.even.append(num)
        else:
            self.odd.append(num)

    def get_odd(self):
        return self.odd

    def get_even(self):
        return self.even


class Clicker:
    def __init__(self):
        self._counter = 0

    def click(self):
        self._counter += 1

    def get_counter(self):
        return self._counter

    def reset(self):
        self._counter = 0


class Car:
    counter = 0  # статичное свойство (счетчик кол-ва машин)

    def __init__(self, brand='Noname', model='NoModel', color='Nocolor'):
        self.engine_on = False  # прописываем свойства
        self.brand = brand  # 'Skoda'
        self.model = model  # 'Oktavia'
        self.color = color  # 'red'
        Car.counter += 1  # при каждом создании новой машины счетчик увеличивается

    def get_brand(self):  # getter - возвращает значение поля класса
        return self.brand

    def get_model(self):  # getter -
        return self.model

    def get_color(self):  # getter -
        return self.color

    def set_color(self, new_color):  # setter
        if new_color:
            self.color = new_color

    def set_brand(self, new_brand):  # setter
        if new_brand:
            self.brand = new_brand

    def set_model(self, new_model):  # setter
        if new_model:
            self.model = new_model

    def start_engine(self):
        self.engine_on = True  # self. - делает аналог глобальной переменной

    def drive_to(self, place):
        if self.engine_on:
            print(f'Едем в {place} на {self.brand}{self.model}')
        else:
            print('Двигатель не заведен, не едем')

    @staticmethod
    def get_counter():
        return Car.counter


class Person:
    def __init__(self, name='Bill', age=1):
        self._name = name
        self._age = age

    def set_name(self, new_name):  # setter - устанавливает значение свойств (полей класса)
        if new_name:
            self._name = new_name

    def set_age(self, new_age):
        if 0 < new_age < 150:
            self._age = new_age
        else:
            print('Некорректный возраст - ', new_age)

    def get_name(self):  # getter - возвращает значение поля класса
        return self._name

    def get_age(self):
        return self._age

    def person_info(self):
        print(f'Человек с именем {self._name} .  Возраст :{self._age}')


def summ(a, b):
    return a + b


def diff(a, b):
    return a - b


print(__name__)

# if __name__ != '__main__':
#    print('Это библиотека, а исполняемый - main.py')
