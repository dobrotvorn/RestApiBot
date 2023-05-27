import os
import telebot
from telebot import types

token = os.getenv("TOKEN")

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])  # теперь если мы напишем боту /start - он ответит -'привет'
def start_message(message):
    bot.send_message(message.chat.id, 'Привет')


@bot.message_handler(commands=['button'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Кнопка Насти")
    item2 = types.KeyboardButton("Кнопка Коли")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(message.chat.id, 'Нажмите на понравившуюся кнопку', reply_markup=markup)

bot.polling(none_stop=True)
