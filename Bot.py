import os
import telebot
from telebot import types


token = os.getenv("TOKEN")

bot=telebot.TeleBot(token)