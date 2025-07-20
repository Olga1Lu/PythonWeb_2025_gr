# Введение во Flask
# MVC-(Model View Controller)
# GET - запрашивает данные (read)
# POST - отправляет данные на сервер (submit)
# PUT - заменяет всё на сервере из контекста запроса ("заменить")
# DELETE - удаляет указанные данные ("удалить")
# PATCH - частичное изменение данных
# JINJA - переменные, условия, циклы и т.д.
# ORM - Object Relational Mapping
import os.path
from sqlite3 import Error

from openpyxl.styles.builtins import title
from pyexpat.errors import messages

from forms.loginform import LoginForm
from forms.user import Register
from flask import Flask, url_for, request, render_template, redirect
from flask_login import LoginManager, login_user, logout_user
from werkzeug.utils import secure_filename
from data import db_session
from data.users import User
from data.news import News
import sqlite3

app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)

app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['SECRET_KEY'] = 'just_secret_key'
ALLOWED_EXTENSIONS = ['txt', 'pdf', 'zip', 'jpg', 'png']
debug = False


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)



@app.errorhandler(404)
def not_found(e):
    return render_template('404.html', title='Не найдено')


@app.route('/')
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
    return render_template('about.html',
                           title='Про нас')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html',
                           title='Свяжитесь с нами')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query((User).filter(User.email == form.email.data))
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect('/')
        return render_template('login.html', title='Ошибка вторизации',
                               message="Неверный логин или пароль", form=form)

    return render_template('login.html', title='Авторизация', form=form)

@app.route('/logout')  #  выход пользователя
def logout():
    logout_user()
    return  redirect('/')

@app.route('/register', methods=['POST', 'GET'])  #регистрация пользователя
def register():
    form = Register()
    if form.validate_on_submit(): # то же самое что и request.method == 'POST'
        # если пароли не совпали, то:
        if form.password.data != form.password_again.data :
            return render_template('register.html', title='регистрация',
                                   message='Пароли не совпадают', form=form)
        db_sess = db_session.create_session()
        # если поль с таким е-мейлом уже есть
        if db_sess.query(User).filter(User.email==form.email.data).first():
           return render_template('register.html', title='регистрация',
                                       message='Такой пользователь уже есть', form=form)
        user = User(name=form.name.data,
                    email=form.email.data,
                    about=form.about.data
                    )
        user.set_password(form.password.data)
        db_sess.add(user)  # добавили польз в БД
        db_sess.commit()
        return  redirect('/login')
    return render_template('register.html', title='регистрация',
                                    form=form)




@app.route('/countdown')
def cd():
    lst = [str(x) for x in reversed(range(10))]
    lst.append('Полетели!!!')
    return '<br>'.join(lst)


@app.route('/image')
def show_image():
    return f'<img src="{url_for('static', filename='images/python.jpg')}">'


@app.route('/sample-page')
def sample_page():
    return f"""<!DOCTYPE html>
            <html lang="ru">
            <head>
                <meta charset="UTF-8">
                <title>Картинка Питона</title>
            </head>
            <body>
                <img src="{url_for('static', filename='images/python.jpg')}" alt="Python">
            </body>
            </html>
    """


@app.route('/sample-page2')
def sample_page2():
    with open('temp.html', 'r', encoding='utf-8') as html:
        return html.read()


# Так делать мы не будем
# x = 5
# @app.route('/1')
# def show_num():
#     global x
#     x += 1
#     return str(x)

# <string> - по умолчанию строка
# <int:number> - целое
# <float:number> - дес. дробь
# <path:p> - может содержать слэши для указания пути
# <uuid:id> - строка-идентификатор (16-байт в HEX-формате)
@app.route('/greeting/<string:user>/<int:id_num>')
def greeting(user, id_num):
    return f'Привет, {user} c id={id_num}'


@app.route('/get-user/')
@app.route('/get-user/<int:id_num>')
def get_user(id_num=None):
    try:
        # Подключение к базе данных
        con = sqlite3.connect('db/movies.sqlite')
        cur = con.cursor()

        if id_num is None:
            # Получение списка всех пользователей
            query = 'SELECT trip_id, name FROM users'
            response = cur.execute(query)
            result = response.fetchall()
            return render_template('get_user.html', users=result)

        # Получение информации о конкретном пользователе
        query = 'SELECT name, city, date_first FROM users WHERE trip_id=?'
        response = cur.execute(query, (id_num,))
        result = response.fetchone()

        if result:
            name, city, date_first = result
            return render_template('get_user.html',
                                   name=name,
                                   city=city,
                                   start=date_first)
        else:
            return "Пользователь не найден", 404

    except Error as e:
        return f"Произошла ошибка: {str(e)}", 500

    finally:
        # Гарантированное закрытие соединения
        if con:
            cur.close()
            con.close()


@app.route('/form-test', methods=['POST', 'GET'])
def form_test():
    if request.method == 'GET':
        with open('form.html', 'r', encoding='utf-8') as html:
            return html.read()
    elif request.method == 'POST':
        print(request.form)
        return 'Форма успешно отправлена'


@app.route('/upload', methods=['POST', 'GET'])
def file_upload():
    if request.method == 'GET':
        with open('upload.html', 'r', encoding='utf-8') as html:
            return html.read()
    elif request.method == 'POST':
        # print(request.files)
        if 'file' not in request.files:
            return 'Файл не был выбран!!!'

        file = request.files['file']

        if file.filename == '':
            return 'Файл не был выбран!!!'

        if file and allowed_file(file.filename):
            new_name = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], new_name))
            return f'Файл {new_name} успешно загружен!'
    return "Ошибка загрузки"


@app.route('/numbers/')
@app.route('/numbers/<int:num>')
def odd_even(num=None):
    if num is None:
        return render_template('numbers.html',
                               title='Нет числа', number='')
    return render_template('numbers.html',
                           title='Чет-нечёт', number=num)


@app.route('/deals')
def printlist():
    deal = ['Помыть посуду', 'Выгулять собаку',
            'Снять показания счётчика', 'Сходить в магазин']
    return render_template('printlist.html', deals=deal)


@app.route('/queue')
def queue():
    # loop.index - номер итерации, начиная с 1
    # loop.index0 - номер итерации, начиная с 0
    # loop.first - True, если первая итерация
    # loop.last - True, если последняя итерация
    return render_template('vars.html', title='Стоим в очереди')

# вывод все публичных новостей, т.е. is_private == False
@app.route('/news')
def news():
    db_sess = db_session.create_session()
    all_news = db_sess.query(News).filter(News.is_private != True).all()
    #print(all_news)
    return render_template('news.html', title='Новости',news=all_news )


if __name__ == '__main__':
    db_session.global_init('db/news.sqlite')
    app.run(host='127.0.0.1', port=5000, debug=debug)
    #user = User()
    # db_sess = db_session.create_session()
    # user = db_sess.query(User).filter(User.id == 1).first()
    # news = News(title='First News', content='News Content', user_id=user.id, is_private=False)  # добавление данных в таблицу News
    # db_sess.add(news)

    # db_sess = db_session.create_session()  # другой способ добавления новости
    # user = db_sess.query(User).filter(User.id == 1).first()
    # news = News(title='First News', content='Third Content',
    #             is_private=False)  # добавление данных в таблицу News
    # user.news.append(news)


    # user = db_sess.query(User).filter(User.id == 2).first()
    # news2 = News(title='Second News', content='News Content', user_id=user.id,
    #             is_private=False)  # добавление данных в таблицу News
    # db_sess.add(news2)



    # db_sess = db_session.create_session()
    # user = db_sess.query(User).filter(User.id == 1).first()
    # for news in user.news:
    #     print(news)

   # db_sess = db_session.create_session()  #

    # user = db_sess.query(User).filter(User.id == 2).first()
    # user.set_username('John')  # изменили имя через сеттер
    # user = db_sess.query(User).filter(User.id == 2).delete()  # удаление записи с id=2
    # user = db_sess.query(User).filter(User.id == 2).first()  # удаление записи с id=2 второй способ
    # db_sess.delete(user)  # удаление записи с id=2 второй способ

    # first = db_sess.query(User).first()  # вывод первой записи в таблице
    # alls = db_sess.query(User).all()  # вывод всех записи в таблице
    # first1 = db_sess.query(User).filter(User.name.not_ilike('%1%')).all()  # фильтр для выбора значений
    # first2 = db_sess.query(User).filter(User.id !=1 , User.email.not_ilike('%a%')).all()
    # first3 = db_sess.query(User).filter((User.id != 1) | (User.email.not_ilike('%a%'))).all()
    # print(first3)
    # user.name = 'User2'
    # user.about = 'Данные о User2'
    # user.email = 'ggg@.ru'
    # db_sess = db_session.create_session()
    # db_sess.add(user)

    # db_sess.commit()
    # print(user)