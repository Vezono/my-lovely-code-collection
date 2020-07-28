# one MORE TRIGGERS

import telebot
import random
import traceback
import config
import datetime
import os
import math
import threading
import calendar
import time
import traceback
import pymongo
from pymongo import MongoClient


bot=telebot.TeleBot(config.token)

db=MongoClient(os.environ['database'])

triggers = db.triggers

x=triggers.find_one({chat_id})

games={}
skills=[]

games={}

timerss={}

ban=[]
timers=[]
pokeban=[]
gimn = "Ще не вмерла України і слава, і воля,\n" \
       "Ще нам, браття молодії, усміхнеться доля.\n" \
       "Згинуть наші воріженьки, як роса на сонці.\n" \
       "Запануєм i ми, браття, у своїй сторонці.\n" \
       "Душу й тіло ми положим за нашу свободу,\n" \
       "І покажем, що ми, браття, козацького роду."


etok = random.choice(["это ко мне", "это к бриту", "это к полунину", "это к пасюку"])




def banns(id, chatid, name):
    i=0
    for ids in timerss:
        if timerss[ids]['id']==id:
            i=1
    if i==0:
        print('1')
        timerss.update({id:{'id':id,
                          'messages':0}})
        t=threading.Timer(15, unwarn, args=[id])
        t.start()
    else:
        print('2')
        timerss[id]['messages']+=1
        if timerss[id]['messages']>=4:
            if id not in ban:
                bot.send_message(chatid, 'Пользователь '+name+' много спамил и был заблокирован на 60 секунд.')
            ban.append(id)
            tt=threading.Timer(60, unbannn, args=[id, chatid])
            tt.start()
            print(ban)
            untildate=int(time.time())
            untildate+=60
            try:
                bot.restrict_chat_member(can_send_messages=False, user_id=id, chat_id=chatid, until_date=untildate)
            except:
                pass
            return 1
    return 0

def unbannn(id, chatid):
      print('unbanlaunch')
      try:
        ban.remove(id)
        bot.restrict_chat_member(can_send_messages=True, can_send_other_messages=True, user_id=id, chat_id=chatid)
        print('UNBAN!')
      except:
           pass
@bot.message_handler(commands=['add'])
def addtrigger(message):
    text=message.text.split(' ', maxsplit = 1)
    text=text[1]
    text=text.split('/')
    triggers.update_one({chat_id:"-1001405019571"}, {'$set': {text[0]:text[1]}})

@bot.message_handler(commands=['del']) 
def deltrigger(message):
    try:
        text=message.text.split(' ', maxsplit = 1)
        text=text[1]
        text=text.split('/')
        del triggers[text[0]]
    except Exception as e:
        print("kek")
              
@bot.message_handler(content_types=["text"])
def triggi(message):
    m = message
    if m.from_user.id not in ban:
       x=banns(m.from_user.id, m.chat.id, m.from_user.first_name)
    if x == 0:
       pass
    else:
       return          
    text = message.text.lower()
    for trigger in x:
       if trigger in text:
          tts = triggers[trigger]
          bot.send_message(message.chat.id, tts, reply_to_message_id = message.message_id)
        





    
   
if __name__ == '__main__':
    bot.polling(none_stop=True)
