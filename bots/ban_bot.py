# simple banner. SIMPLE AHAHAHHAHA SIMPLE

import os
import telebot
import time
import random
import threading
from emoji import emojize
from telebot import types
from pymongo import MongoClient
import traceback

client1=''
client=MongoClient(client1)
db = client.bpl
chats = db.chats
users = db.users

token = ''
bot = telebot.TeleBot(token)
mainchat = -100148807
mainadmin = 72
bot_id = 9088
log_id = -1

adminos_telebotos=['administrator', 'creator']

@bot.message_handler(commands=['ban'])
def ban(m):
    if m.chat.id!=m.from_user.id:
      try:
        chat_member = bot.get_chat_member(m.chat.id, m.from_user.id)
        reply_member = bot.get_chat_member(m.chat.id, m.reply_to_message.from_user.id)
        if bot.get_chat_member(m.chat.id, m.from_user.id).status in adminos_telebotos and bot.get_chat_member(m.chat.id, m.reply_to_message.from_user.id).status not in adminos_telebotos:
            text=m.text.split(' ')
            try:
                timee=text[1]
                i=int(timee[:-1])
                number=timee[len(timee)-1]
            except:
                i=0
                number='m'
            
            untildate=int(time.time())
            if number=='m':
                untildate+=i*60
                datetext='минут'
            if number=='h':
                untildate+=i*3600
                datetext='часов'
            if number=='d':
                untildate+=i*3600*24
                datetext='дней'
                           
            print(untildate)
            
            if m.reply_to_message!=None:
                ahref = '[' +m.reply_to_message.from_user.first_name + ']' + '(tg://user?id=' +  str(m.reply_to_message.from_user.id) + ')'
                bot.kick_chat_member(user_id=m.reply_to_message.from_user.id, chat_id=m.chat.id, until_date=untildate)
                if i==0:
                    text='Пользователь ' + ahref + ' заблокирован навсегда.'
                else:
                    text='Пользователь ' + ahref + ' заблокирован на '+str(i)+' '+datetext+'.'
                bot.send_message(m.chat.id, text, parse_mode='Markdown')
                log(' заблокирован на ', ahref, ' '+str(i)+' '+datetext)
        else:
            bot.send_message(m.chat.id, 'Возможно, вы не администратор, или пытаетесь заблокировать такового (в будущем будет наказуемо).')
      except Exception as e:
        bot.send_message(m.chat.id, 'Ошибка. Не удалось заблокировать пользователя.')
        print(traceback.format_exc())        
#exec(open("test2.py").read());
@bot.message_handler(commands=['anounce'])
def anons(m):
    bot.send_message('@bpl_log', m.text.split()[1])
    
@bot.message_handler()
def hand(m):
    print(m.chat.id)
def log(act, ahref, data):
    tts = 'Пользователь ' + ahref + act + data   
    bot.send_message(log_id, tts)
bot.send_message(mainchat, 'Бот был перезагружен!')
print('7777')
bot.polling(none_stop=True,timeout=600)
