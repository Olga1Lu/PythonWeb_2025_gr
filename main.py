# Flask
# MVC-(Model View Controller)
#JINJA - шаблонизатор: переменные, условия, циклы
import os.path
from fileinput import filename

from flask import Flask, url_for, request, render_template
from openpyxl.styles.builtins import title
from werkzeug.utils import secure_filename  # проверка, что имя файла безопасно
import sqlite3

from urllib3.util.proxy import connection_requires_http_tunnel

app = Flask(__name__)  # регистрируем приложение
app.config['UPLOAD_FOLDER'] = 'uploads/'
ALLOWED_EXTENSIONS = ['txt', 'pdf', 'zip', 'jpg', 'png']
debug = False


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS  # анализируем только расширение файла


@app.route('/')  # связь с браузером, регистрируем пути
@app.route('/index')
def index():
    params = {}
    params['user'] = 'слушатель'
    params['title'] = 'приветствие'
    params['weather'] = 'Сегодня хорошая погода'
    return render_template('index.html',
                           **params)


@app.route('/about')
def about():
    print('Вызвана функция about')
    return 'О нас'


@app.route('/countdown')
def cd():
    lst = [str(x) for x in reversed(range(10))]
    lst.append('Полетели!')
    return '<br>'.join(lst)


@app.route('/image')
def show_image():
    return f'<img src="{url_for('static', filename='images/piton.jpg')}">'


@app.route('/sample-page')
def sample_page():
    return f"""
    <!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Картинка</title>
</head>
<body>
  <img = src="{url_for('static', filename='images/piton.jpg')}" alt="Python">
</body>
</html>
    """


@app.route('/sample-page2')
def sample_page2():
    with open('temp.html', 'r', encoding='utf-8') as html:
        return html.read()


###################
# не рекомендуется
# x = 5
# @app.route('/1')
# def show_num():
#     global x
#     x += 1
#     return str(x)
###################

# типы конверторов - по умолчанию всегда строка
# <string> по умолчанию строка
# <int:number> - целое
# <float:number> - вещ.числа
# <path:p> - может содержать слэши для указания пути
# <uuid:id> - строка идентификатор (16 байт в HEX-формате)

# передать данные, определяемые пользователем
@app.route('/greeting/<user>/<int:id_num>')  # вместо <> м.подставить любое слово
def greeting(user, id_num):
    return f'Привет, {user} c id= {id_num}'


# обращение к базе данных
@app.route('/get-user/')
@app.route('/get-user/<int:id_num>')  # вместо <> м.подставить любой номер для вывода опрюзаписи из БД
def get_user(id_num=None):  # если не введен порядковый номер записи
    if id_num is None:
        return 'Нет номера записи'
    con = sqlite3.connect('db/movies.sqlite')
    cur = con.cursor()
    query = f'SELECT name, city FROM users WHERE trip_id={id_num}'
    response = cur.execute(query)
    result = response.fetchone()
    name, city = result  # распаковка кортежа name, city
    # print(result)  # получили объект

    cur.close()  # подтверждение
    con.close()  # закрываем подключение
    return f"""<table border="1">  # вывод в табличной форме
    <tr>
    <td>ФИО</td>
    <td>Город</td>
    </tr>
    <tr>
    <td>{name}</td>
    <td>{city}</td>
    </tr>
    </table>
    """


@app.route('/form-test', methods=['POST', 'GET'])
def form_test():
    if request.method == 'GET':
        with open('form.html', 'r', encoding='utf-8') as html:
            return html.read()
    elif request.method == 'POST':
        print(request.form['gender'])
        print(request.form['email'])

        return 'Форма успешно отправлена'


@app.route('/upload', methods=['POST', 'GET'])  # загрузка файла на сервер
def file_upload():
    if request.method == 'GET':
        with open('upload.html', 'r', encoding='utf-8') as html:
            return html.read()
    elif request.method == 'POST':
        if 'file' not in request.files:
            return 'Файл не был выбран.'
        file = request.files['file']
        if file.filename == '':
            return 'Файл без имени.'
        if file and allowed_file(file.filename):
            new_name = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], new_name))
            return f'Файл {new_name} загружен успешно.'
    return 'Ошибка загрузки.'
@app.route('/numbers/')
@app.route('/numbers/<int:id_num>')
if num is None# загрузка файла на сервер
def odd_even(id_num):
    return render_template('numbers.html', title='Чет-нечет', number=id_num)

@app.route('/deals')  # загрузка файла на сервер
def printlist():
    deal = ['Помыть посуду', 'Выгулять собаку', 'Снять счетчик', 'Сходить в магазин']
    return render_template('printlist.html', deals=deal)

@app.route('/queue')  # загрузка файла на сервер
def queue():

    return render_template('wars.html', title='Стоим в очереди')

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=debug)
