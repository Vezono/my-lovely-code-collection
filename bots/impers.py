import os
import telebot
import time
import random
import threading
from emoji import emojize
from telebot import types
from pymongo import MongoClient
import traceback
gamerz=[]
yoba=[512006137]
imperias={}
token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start']) 
def start(m):
    if m.from_user.id not in gamerz:
        imperias.update({m.from_user.id:createempire(m)})
        gamerz.append(m.from_user.id) 
        bot.send_message(m.from_user.id, 'Ваша империя создана, и названа в *вашу* честь!', parse_mode = 'markdown')
        nachat(m.from_user.id, m.from_user.first_name)
    else:
        bot.send_message(m.from_user.id, 'Империя *' + imperias[m.from_user.id]['name'] + '* уже существует!', parse_mode = 'markdown')
@bot.message_handler(commands=['me']) 
def me(m):
    if m.from_user.id in gamerz:
        id = m.from_user.id
        sfood = str(imperias[id]['food'])
        swarriors = str(imperias[id]['warriors'])
        sfarmers = str(imperias[id]['farmers'])
        smoney = str(imperias[id]['money'])
        stoday = str(imperias[id]['day'])
        
        text = '📃Доклад о империи *' + m.from_user.first_name + '* состоянием на ' + stoday + ' день:\n'
        text += '💂🏻‍♀️Количевство воинов:' + swarriors + '\n'
        text += '🍎Количевство еды:' + sfood + '\n'
        text += '💰Количевство денег:' + smoney + '\n'
        text += '👨🏻‍🌾Количевство фермеров:' + sfarmers
        bot.send_message(m.from_user.id, text, parse_mode = 'markdown')
    
@bot.message_handler(commands=['burnempire']) 
def burnempire(m):
    if m.from_user.id in gamerz:
        gamerz.remove(m.from_user.id)
        del imperias[m.from_user.id]
        bot.send_message(m.from_user.id, 'Вашей империи больше несуществует.', parse_mode = 'markdown')
    else:
        bot.send_message(m.from_user.id, 'Вам нечего сжигать.', parse_mode = 'markdown')

def nachat(id, name):
    if imperias[id]['food'] > 1:
        food = imperias[id]['food']
        warriors = imperias[id]['warriors']
        farmers = imperias[id]['farmers']
        money = imperias[id]['money']
        
        today = imperias[id]['day'] + 1
        imperias.update({id:{'day':today}})
        text = 'Наступил ' + str(imperias[id]['day']) + ' день существования вашей империи!\n'
        
        todayfood = food - (warriors*5)
        imperias.update({id:{'food':todayfood}})
        text += 'Сегодня ваши воины сьели ' + str(warriors*5) + ' единиц еды.\n'
        
        food = imperias[id]['food']
        todayweed = food+(farmers*2)
        imperias.update({id:{'food':todayweed}})
        text += 'Также, сегодня ваши фермеры произвели ' + str(farmers*2)  + ' единиц еды.\n\n'
        
        food = imperias[id]['food']
        
        text += '📃Доклад о империи *' + name + '* состоянием на ' + str(today) + ' день:\n'
        text += '💂🏻‍♀️Количевство воинов:' + str(warriors) + '\n'
        text += '🍎Количевство еды:' + str(food) + '\n'
        text += '💰Количевство денег:' + str(money) + '\n'
        text += '👨🏻‍🌾Количевство фермеров:' + str(farmers)
        bot.send_message(id, text, parse_mode = 'markdown')
        threading.Timer(120, nachat, args=[id, name]).start()
    else:
        bot.send_message(id, 'Ваша империя мертва. Вы все сьели.', parse_mode = 'markdown')
        gamerz.remove(id)
        del imperias[id]
                                                      
def createempire(m):
    return{'name':m.from_user.first_name,
           'warriors':100,
           'food':1000,
           'money':10000,
           'farmers':1000,
           'day':0}                                                      
for hu in yoba:
    bot.send_message(hu, '777', parse_mode = 'markdown')
print('7777')
bot.polling(none_stop=True,timeout=600)
