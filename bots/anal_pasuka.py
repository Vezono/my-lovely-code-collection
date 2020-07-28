# sketch
import os
import telebot
import time
import random
import threading
from emoji import emojize
from telebot import types
from pymongo import MongoClient
import traceback

client1=os.environ['database']
client=MongoClient(client1)
db=client.analpasuka
users=db.analpasuka
token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token)
try:
    x=users.find({})
    for ids in x:
        try:
            bot.send_message(ids['id'], 'Бот был перезагружен.')
        except:
            pass
    users.update_many({}, {'$set':{'droching':0}})
except:
    pass
@bot.message_handler(commands=['start'])
def start(m):
    if users.find_one({'id':m.from_user.id})==None and m.chat.id==m.from_user.id:
        users.insert_one(createuser(m.from_user.id, m.from_user.first_name))
        if m.chat.id != 441399484:
            bot.send_message(m.from_user.id, 'Привет. Ты новенький, да? Короче, мы охотимся на анал Пасюка. Только не говори пасюку!')
        else:
            bot.send_message(m.from_user.id, 'О, привет Пасюк. Не бойся, все будет хорошо. И твой на твой анал никто не нападет! Брит то обеoает)')
    else:
        pass     
                             
                             
def createuser(id, name):
    return{'id':id,
          'name':name,
          'anals':0,
          'strength':5,
          'hp':100,
          'weapon':'hands',
          'droching':0
          }        
          
print('7777')
bot.polling(none_stop=True,timeout=600)
