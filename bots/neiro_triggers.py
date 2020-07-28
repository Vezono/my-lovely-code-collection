import os
import telebot
import time
import random
import threading
from telebot import types
from pymongo import MongoClient
import traceback
import apiai, json
from api.ai import Agent

token = ''
bot = telebot.TeleBot(token)

neiro = apiai.ApiAI('')
parent=''

agent = Agent(
'cipraded',
'',
'',
)

training = False
teachers = [268486177, 792414733, 441399484]
@bot.message_handler(commands=['train'])
def ctrain(m):
    pass
@bot.message_handler()
def txt(m):
    response = react(m)
    if response:
        bot.reply_to(m, response)
def react(m):
    request = neiro.text_request()
    request.lang = 'ru' # На каком языке будет послан запрос
    request.session_id = 'cipraded' # ID Сессии диалога (нужно, чтобы потом учить бота)
    request.query = m.text.lower() # Посылаем запрос к ИИ с сообщением от юзера
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    response = responseJson['result']['fulfillment']['speech'] # Разбираем JSON и вытаскиваем ответ
    return response
print('7777')
bot.polling(none_stop=True,timeout=600)
