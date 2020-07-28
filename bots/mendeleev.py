# sketches...

# -*- coding: utf-8 -*-
import os
import telebot
import time
import random
import threading
from emoji import emojize
from telebot import types
from pymongo import MongoClient
import traceback

dictable={
'кислород':{
    'name':'Кислород',
    'lat':'Oxygenium',
    'chemletter':'O',
    'atomweith':'15,999999',
    'atomnumber':8,
    'group':'VI',
    'period':'2',
    'valency':'II',
    'oxyd':'-'
    },
'платина':{
    'name':'Платина',
    'lat':'Platinum',
    'chemletter':'Pt',
    'atomweith':'195,08',
    'atomnumber':78,
    'group':'VII',
    'valency':'VIII',
    'oxyd':'PtO2'
    },    
}

elements=dictable.keys()
token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token)

@bot.message_handler()
def botmessages(m):
    words = m.text.lower().split(' ')
    for word in words:
        if word in elements:
            sendelement(m, word)
@bot.message_handler(commands=['start'])
def start(m):   
    bot.send_message('Здравствуйте! Напишите имя элемента полностью на русском, и я расскажу про него! Список елементов в боте - /list', m.chat.id)
    
@bot.message_handler(commands=['list'])
def celems(m):
    tts = ''
    for elem in elements:
        tts += elem + ', '
    bot.send_message(tts, m.chat.id)    
def sendelement(m, elem):
    text = dictable[elem]['name'] + ', (лат. ' + dictable[elem]['lat'] + ').'
    bot.send_message(text, m.chat.id)
print('7777')
bot.send_message('7777', 792414733)
bot.polling(none_stop=True,timeout=600)
