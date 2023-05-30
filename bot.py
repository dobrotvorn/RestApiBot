import os
import requests
import telebot
from telebot import types

token = os.getenv("TOKEN")
weed_token = os.getenv("WEED_TOKEN")
project = "all"
api_endpoint = f"https://my-api.plantnet.org/v2/identify/{project}?api-key={weed_token}"

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])  # теперь если мы напишем боту /start - он ответит -'привет'
def start_message(message):
    bot.send_message(message.chat.id, 'Привет')


@bot.message_handler(commands=['buttons'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Кнопка Насти")
    item2 = types.KeyboardButton("Кнопка Коли")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(message.chat.id, 'Нажмите на понравившуюся кнопку', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def handle_button_nastya(message):
    if message.text == "Кнопка Насти":
        bot.send_message(text="Кнопка нажата", chat_id=message.chat.id)


bot.polling(none_stop=True)
