import os
import telebot
import time
import random
import threading
from emoji import emojize
from telebot import types
from pymongo import MongoClient
import traceback
from pyrogram import Client
from pyrogram import Filters

bot = Client("my_account")
aaa = "Что смешного? Ладно, неважно. Все поняли правила? Отлично! Для регистрации в турнире нужно подойти ко мне, и сказать"
ol = "К сожалению, заданий для тебя сейчас нет"
sis = "Встречайте победителя турнира:"
pisun = 'тличная работа'
ded = 891466545


@bot.on_message()
def suka(pisos, message):
    try:
        toprin = str(message.from_user.id) +' - '+ message.text
        print(toprin) 
    except:
        pass
    try:
        if "Нашла для тебя занятие, Брит!" in message.text and message.from_user.id == 636658457:
            message.reply("Я готов!")
        elif aaa in message.text and message.from_user.id == 609648686:
            message.reply("Хочу принять участие в турнире!")
            '''
        elif ol in message.text and message.from_user.id == 636658457:
            bot.send_message(636658457, "/work")
        elif pisun in message.text and message.from_user.id == 636658457:
            bot.send_message(636658457, "/work")
            '''
        elif sis in message.text and message.from_user.id == 609648686:
            bot.send_message(636658457, "/cards")
        elif "Так как ты у нас ответственный пионер, Брит" in message.text and message.from_user.id == 636658457:
            message.reply("Я готов!")
        elif "работа" in message.text and message.from_user.id == 636658457:
            message.reply("Я готов!")
        elif "Вы сдохли" in message.text and message.from_user.id == ded:
            message.reply("/start")
    except:
        pass
bot.run()

print('7777')
