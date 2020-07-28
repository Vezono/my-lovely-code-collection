import os
import traceback

import telebot
from telebot import types

import datetime
import calendar
import time
import threading

import random

from pymongo import MongoClient



token = 'none'
bot = telebot.TeleBot(token)


global_admins = [268486177, 792414733, 441399484]
group_admins=['administrator', 'creator']

@bot.message_handler(commands=['ping'])
def ping(m):
    bot.reply_to(m, 'Успешно!')
    
@bot.message_handler(commands=['info'])
def ping(m):
    tts = '*Информация о чате*:\nЧат айди: `{}`\nТип чата: `{}`\n\n*Информация о юзере*: \nИмя юзера: `{}`\nАйди юзера: `{}`' # Text To Send
    if m.reply_to_message:
        tts = tts.format(str(m.chat.id), m.chat.type, m.reply_to_message.from_user.first_name, str(m.reply_to_message.from_user.id))
    else:
        tts = tts.format(str(m.chat.id), m.chat.type, m.from_user.first_name, str(m.from_user.id))
@bot.message_handler()
def txt(m):
    pass


def is_admin(user, chat):
    chat_member = bot.get_chat_member(chat, user)
    if chat_member.status in group_admins:
        return True
    else:
        return False
print('7777')
bot.polling(none_stop=True,timeout=600)
