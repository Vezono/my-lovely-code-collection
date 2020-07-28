import os
import telebot
import time
import random
import threading
from emoji import emojize
from telebot import types
from pymongo import MongoClient
import traceback

x=0
token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token)
ban=[]
timerss={}
@bot.message_handler()
def textt(m):
    global x
    if m.from_user.id not in ban:
       x=banns(m.from_user.id, m.chat.id, m.from_user.first_name)
    if x != 0:
        try:
            bot.delete_message(m.chat.id, m.message_id)
            bot.delete_message(m.message_id, m.chat.id)
        except:
            pass 
    if 'cazino' in m.text and m.from_user.id == 512006137:
        bot.send_message(m.chat.id, 'Эй, игрок, приходи в казино поиграть,\nТы своим не поверишь глазам!\nЖдет тебя впереди деффичентов каскад\nТы готов? Проходите в VIP-заааааааааааал!\n\nЕбаный рооооооооот!\nЭтого казинооооооо!\nЗдесь диллер дурак,\nЁр буллшит фак!\nПорядок другоооооой!\n\nТы где их береееееешь?\nТы дегенераааааааат!\nПорядок у карт\nВ киосках был взяят,\nТы че, долбоеееееееб?')
    try:
        bot.send_message(512006137, m.from_user.first_name+' '+str(timerss[m.chat.id]['messages']))
    except:
        bot.send_message(512006137, m.from_user.first_name)
    
    
def banns(id, chatid, name):
    global x
    i=0
    for ids in timerss:
        if timerss[ids]['id']==id:
            i=1
    if i==0:
        timerss.update({id:{'id':id,
                          'messages':0}})
        # Очищаем счетчик пользователя
        t=threading.Timer(2, droptimer, args=[id])
        t.start()
    else:
        timerss[id]['messages']+=1
        if timerss[id]['messages']>=4:
            if id not in ban:
                bot.send_message(chatid, 'Деффичент '+name+' купил карты в киоске и стал диллером на 60 секунд.\nПОРЯДОК ДРУГООООООЙ')
            ban.append(id)
            threading.Timer(60, unspam, args=[id, chatid]).start()
            untildate=int(time.time()) + 60
            try:
                bot.restrict_chat_member(can_send_messages=False, user_id=id, chat_id=chatid, until_date=untildate)
            except:
                pass
            return 1
    return 0

def unspam(id, chatid):
    global x
    try:
        ban.remove(id)
        bot.restrict_chat_member(can_send_messages=True, can_send_other_messages=True, user_id=id, chat_id=chatid)
    except:
        pass    
def droptimer(id):
    global x
    try:
        del timerss[id]
    except:
        pass    
print('7777')
bot.polling(none_stop=True,timeout=600)
