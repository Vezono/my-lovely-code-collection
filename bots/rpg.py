# kek
import os
import telebot
import time
import telebot
import random
import info
import threading
from emoji import emojize
from telebot import types



token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token)




@bot.message_handler(commands=['begin'])
def once(message):
    bot.send_message(message.chat.id, 'Добро пожаловать в игру "Блядские животные"!')
    if "/begin" in message.text:
        bot.send_message(message.chat.id, 'Выберите рассу: Осел, Брит или Пасюк!')
        if "Осел" in message.text:
            bot.send_message(message.chat.id, "Вы теперь Осел!")
        elif "Пасюк" in message.text:
            bot.send_message(message.chat.id, "Вы теперь Пасюк!")
        elif "Брит" in message.text:
            bot.send_message(message.chat.id, "Вы теперь Брит!")
        else:
             bot.send_message(message.chat.id, "Нет такой рассы!")
    else:
        bot.send_message(message.chat.id, "Ошибка"!)
        
if True:
   print('7777')
   bot.polling(none_stop=True,timeout=600)
