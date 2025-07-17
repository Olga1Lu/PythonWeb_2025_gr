from flask_wtf import FlaskForm  # импорт форм
from wtforms import StringField, PasswordField, BooleanField, SubmitField  # импорт элементов форм
from wtforms.validators import  DataRequired  # пустое поле обязат. к заполнению

class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')