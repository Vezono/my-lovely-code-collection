import redis
import os
import telebot
import math
import random
import threading
from telebot import types
from emoji import emojize
token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token)
groups=[]
stopp=0
admins=[512006137]

def spamon(message, group):
    global stopp
    while stopp!=1:
        msg=bot.send_message(group, message)
    
@bot.message_handler(commands=['stop'])
def stopppp(m):
    global stopp
    stopp=1
    bot.send_message(m.chat.id, 'Остановил спам во всех чатах ебать')
        
@bot.message_handler(commands=['start'])
def stopppp(m):
    global stopp
    stopp=0
    bot.send_message(m.chat.id, 'Разрешил спам во всех чатах ебать')
    
@bot.message_handler(commands=['spam'])
def spam(m):
    try:
        msg=m.text.split('/spam')[1]
        spamon(msg, m.chat.id)
    except:
        bot.send_message(m.chat.id, 'Ты долбоеб ебаный')
    
    




def poll():
    try:
        bot.polling(none_stop=True)
    except:
        try:
            bot.stop_polling()
        except:
            pass
        poll()

        
        
poll()
