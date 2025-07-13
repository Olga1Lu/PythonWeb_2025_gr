from tkinter import *
from urllib.request import urlopen
from urllib.parse import urlencode
import xml.etree.ElementTree as et


class Map:
    def __init__(self):
        self.root = Tk()
        self.root.title('Поиск места по адресу')
        # иконку приложения добавим позже
        # self.root.call('wm', 'iconphoto', self.root._w, PhotoImage(file='icon.png'))
        # сохранение цвета фона окна в переменную bgnd
        self.bgnd = self.root['bg']
        self.root.geometry('800x600')
        self.canvas = Canvas(self.root, height=450, width=600)
        self.canvas.place(x=100, y=50)  # левый верхний угол
        # назначаем элементы:
        # предустановленный адрес (начальный адрес)
        self.what_to_find = 'Санкт-Петербург, ул. Можайская, 2'
        self.delta = '0.001'  # для изменения spn
        # текстовое поле, надпись и кнопки
        self.entry = Entry(width=60, font=('Verdana 12'))
        self.srch = Button(text="Найти", command=self.show_map)
        self.clear_button = Button(text="Очистить", command=self.clear)
        # добавили кнопки масштаба
        self.plus = Button(text="+", height=2, width=5, command=self.positive_zoom)
        self.minus = Button(text="-", height=2, width=5, command=self.negative_zoom)
        self.header = Label(text="Адрес:", font=('Verdana 12'))
        # размещаем элементы
        self.header.place(x=5, y=0)
        self.entry.place(x=70, y=2)
        self.entry.insert(END, self.what_to_find)
        self.srch.place(x=685, y=0)
        self.clear_button.place(x=735, y=0)
        # добавили кнопки "+" и "-"
        self.plus.place(x=400, y=500)
        self.minus.place(x=350, y=500)
        self.show_map()
        # ожидание действий
        self.root.mainloop()

    # очистка поля ввода адреса и отображаемой карты
    def clear(self):
        # рисуем прямоугольник, залитый цветом фона
        self.canvas.create_rectangle(0, 0, 601, 451,
                                     outline=self.bgnd, fill=self.bgnd)
        self.entry.delete(0, END)  # удаление введенного текста

    # кнопка "+" уменьшает spn
    def positive_zoom(self):
        temp = float(self.delta) / 2
        if temp < 0.00025:
            temp = 0.00025
        self.delta = str(temp)
        self.show_map()

    # кнопка "-" увеличивает spn
    def negative_zoom(self):
        temp = float(self.delta) * 2
        if temp > 32.768:
            temp = 32.768
        self.delta = str(temp)
        self.show_map()

    # показываем карту с предустановленным адресом "Можайская 2"
    def show_map(self):
        self.what_to_find = self.entry.get()  # получаем введенный текст
        # если адрес слишком короткий, вводим предустановленный
        if len(self.what_to_find) < 3:
            self.entry.delete(0, END)
            self.entry.insert(END, 'Санкт-Петербург, ул. Можайская, 2')
            self.what_to_find = self.entry.get()

        # пока пустой перечень параметров запроса
        data = {}
        # ключ выше вводим в кавычках (апострофах)
        data['apikey'] = ''  # в кавычках впишите ключ
        data['geocode'] = 'СПб, Можайская, 2'

        # основная часть ссылки для обращения к геокодеру
        url = 'http://geocode-maps.yandex.ru/1.x/'

        # преобразуем набор параметров в формат URL
        url_values = urlencode(data)
        # формируем полную ссылку
        full_url = '?'.join([url, url_values])
        # получаем ответ по ссылке
        response = urlopen(full_url)

        # полученный ответ преобразуем в XML-формат
        res = response.read().decode('UTF-8')

        # начинаем расшифровывать XML
        root = et.fromstring(res)
        # "вытаскиваем" координаты
        coords = root.find('.//{http://www.opengis.net/gml}pos').text

        # координаты в консоль уже не выводим
        # вновь пустой перечень параметров запроса
        map_data = {}
        # добавляем в запрос все необходимые параметры:
        # широту и долготу
        map_data['ll'] = coords.replace(' ', ',')
        # протяжённость области поиска
        map_data['spn'] = ','.join([self.delta, self.delta])
        # отображаем карту
        map_data['l'] = 'map'
        # добавим значок на карту
        map_data['pt'] = coords.replace(' ', ',') + ',pm2dgl'

        # основная часть ссылки для обращения к
        # статическому контенту Яндекс-карт
        map_url = 'http://static-maps.yandex.ru/1.x/'

        # преобразуем набор параметров в формат URL
        url_values = urlencode(map_data)
        # формируем полную ссылку
        full_url = '?'.join([map_url, url_values])

        # получаем нужный фрагмент
        response = urlopen(full_url)

        # преобразовываем фрагмент в набор пикселей
        self.pict_array = response.read()

        # превращаем набор пикселей в картинку и отображаем её
        self.img = PhotoImage(data=self.pict_array, format='png')
        self.canvas.create_image(0, 0, anchor=NW, image=self.img)


app = Map()  # помещаем приложение в капсулу и запускаем

