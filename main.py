#Flask
#MVC-(Model View Controller)
from fileinput import filename
from http.cookiejar import debug

from flask import Flask, url_for

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

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=debug)