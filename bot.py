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

# @bot.message_handler(content_types=['photo'])
# def handle_photo(message):
#     print(message)
class Factory:
    def __init__(self):
        self.flag = False

    def get_flag(self):
        return self.flag


f = Factory()

@bot.message_handler(content_types=['text', 'photo'])
def handle_button_nastya(message):
    if message.content_type == 'text':
        if message.text == "Кнопка Насти":
            f.flag = True
            bot.send_message(text="Кнопка нажата", chat_id=message.chat.id)
    elif message.content_type == 'photo':
        if f.flag:
            fileID = message.photo[-1].file_id
            file_info = bot.get_file(fileID)
            downloaded_file = bot.download_file(file_info.file_path)
            # json = api(downloaded_file)
            # name_of_plant = json.plant.name
            # bot.send_message(text=f"{name_of_plant}", chat_id=message.chat.id)
            f.flag = False
    else:
        f.flag = False
        # with open("image.jpg", 'wb') as new_file:
        #     new_file.write(downloaded_file)
        # bot.send_photo(message.chat.id, downloaded_file)



bot.polling(none_stop=True)
