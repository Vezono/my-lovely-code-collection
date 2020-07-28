import os
import telebot
import time
import random
import threading
from emoji import emojize
from telebot import types
from pymongo import MongoClient
import traceback

what = random.choice(['?', 'Что?'])
triggers={'@dvach_tan':what, 'пися':'СУКА'}
token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token)
@bot.message_handler(commands=["talk"])
def gandoni(m):
    try:
        bot.delete_message(m.chat.id, m.message_id)
        text = m.text.split(' ', 1)[1]
        bot.send_message(m.chat.id, text, reply_to_message_id = m.reply_to_message.message_id)
    except:
        try:
            text = m.text.split(' ', 1)[1]
            bot.send_message(m.chat.id, text)
        except:
            bot.send_message(512006137, traceback.format_exc())
@bot.message_handler(commands=["bunt"])
def bunt(m):
    bunts = int(m.text.split()[1])
    for i in range(bunts):
        bot.send_message(-1001405019571, "ДОЛОЙ ВСЕВЫШНЕГО БЛЯДЬ!")            
@bot.message_handler(commands=['addp'])
def addtrigger(m):
    text=m.text.split(' ', maxsplit = 1)
    bot.delete_message(m.chat.id, m.message_id)
    text=text[1]
    text=text.split('/')
    triggers.update({text[0]:text[1]})
    

@bot.message_handler(commands=['delp']) 
def deltrigger(m):
    if m.from_user.id in ban:   
        return
    try:
        text=m.text.split(' ', maxsplit = 1)
        bot.delete_message(m.chat.id, m.message_id)
        text=text[1]
        text=text.split('/')
        del triggers[text[0]]
    except Exception as e:
        print("kek")
            
@bot.message_handler()
def handlerblya(m):
    text = m.text.lower()
    for trigger in triggers:
        if trigger in text:
            tts = triggers[trigger]
            bot.send_message(m.chat.id, tts, reply_to_message_id = m.message_id)

hellolist=['Я нашла ошибку в своем коде!', 'Я обиделась на Пасюка.', 'Я обиделась на Полунина.', 'Я обиделась на Брита.', 'ВАМ ПИЗДА БЛЯДЬ']            
def hello():
    try:
        if True:
            tts = random.choice(hellolist)
            bot.send_message(-1001405019571, tts)
    except:
        hello()
        
hello()       
print('7777')
bot.polling(none_stop=True,timeout=600)
