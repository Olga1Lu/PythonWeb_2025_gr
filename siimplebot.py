# Бот
from gc import callbacks

import telebot
from PIL.ImageMath import lambda_eval
from telebot import types
token = ''  # обычно в отд.файле

import  telebot

kb = types.ReplyKeyboardMarkup(row_width=2)  # по две кнопки в ряду
btn1 = types.KeyboardButton('/url')
btn2 = types.KeyboardButton('/help')
btn3 = types.KeyboardButton('Как дела?')
kb.add(btn1, btn2,btn3)  # добавили кнопки на клавиатуру

bot = telebot.TeleBot(token)  # создали бот, который будет запускаться по команде /start  в TG
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я запущен и буду повторять за вами', reply_markup=kb)


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'Я пока всего лишь Ваше эхо и умею немного')

@bot.message_handler(commands=['url'])
def url_message(message):
    markup = types.InlineKeyboardMarkup() # инлайн клавиатура
    btn = types.InlineKeyboardButton(text='сайт Яндекса', url='https://ya.ru')  # кнопка
    markup.add(btn)
    bot.send_message(message.chat.id, 'перейти на сайт Яндекса',
                    reply_markup=markup)




@bot.message_handler(content_types=['text'])  #попугай
def parrot(message):
    if message.text.strip().lower() == 'привет':
        bot.send_message(message.chat.id, 'Ну здорово !')
    elif message.text.strip().lower() == 'Как дела?':
        # bot.send_message(message.chat.id, '👍')
        answer = types.InlineKeyboardMarkup(row_width=2)
        btn_good = types.InlineKeyboardButton('Хорошо', callback_data='good')
        btn_bad = types.InlineKeyboardButton('Плохо', callback_data='bad')
        answer.add( btn_good, btn_bad)
        bot.send_message(message.chat.id, 'У меня-то хорошо, а у тебя', reply_markup=answer)
    else:
        bot.send_message(message.chat.id, message.text)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'good':
        bot.send_message(call.message.chat.id, 'О, круто, рад!!!')
    if call.data == 'bad':
        bot.send_message(call.message.chat.id, 'Не переживай, всё наладится!!!')

bot.infinity_polling(non_stop=True)  # сам не остановится, пока бот не уберем сами


