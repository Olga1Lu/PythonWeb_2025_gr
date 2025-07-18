from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms import SubmitField
from wtforms.fields.simple import EmailField, TextAreaField
from wtforms.validators import DataRequired

class Register (FlaskForm):
    email = EmailField('Почта', validators=[DataRequired('Введите e-mail')])
    password = PasswordField('Пароль', validators=[DataRequired('Введите пароль')])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired('Подтвердите пароль')])
    name= StringField('Ваше имя', validators=[DataRequired('введите Ваше имя')])
    about = TextAreaField('Напишите о себе')
    submit = SubmitField('Регистрация')