#Flask
#MVC-(Model View Controller)
from fileinput import filename

from flask import Flask, url_for, request
import sqlite3

from urllib3.util.proxy import connection_requires_http_tunnel

app = Flask(__name__)  # регистрируем приложение
debug = False

@app.route('/')  # связь с браузером, регистрируем пути
@app.route('/index')
def index():
    return 'Привет, Flask'
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
    return  f'<img src="{url_for('static', filename='images/piton.jpg')}">'

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
#не рекомендуется
# x = 5
# @app.route('/1')
# def show_num():
#     global x
#     x += 1
#     return str(x)
###################

# типы конверторов - по умолчанию всегда строка
#<string> по умолчанию строка
#<int:number> - целое
#<float:number> - вещ.числа
#<path:p> - может содержать слэши для указания пути
#<uuid:id> - строка идентификатор (16 байт в HEX-формате)

# передать данные, определяемые пользователем
@app.route('/greeting/<user>/<int:id_num>')  # вместо <> м.подставить любое слово
def greeting(user, id_num):
    return f'Привет, {user} c id= {id_num}'

#обращение к базе данных
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
    #print(result)  # получили объект

    cur.close()  # подтверждение
    con.close()  # закрываем подключение
    return  f"""<table border="1">  # вывод в табличной форме
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
    if request.method == 'GET' :
        with open('form.html', 'r', encoding='utf-8') as html :
            return html.read()
    elif request.method == 'POST' :
            print(request.form['gender'])
            print(request.form['email'])

            return 'Форма успешно отправлена'

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=debug)


