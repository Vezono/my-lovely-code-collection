# -*- coding: utf-8 -*-
# not bad ostan project!
import os
import telebot
import time
import random
import threading
from emoji import emojize
from telebot import types
from pymongo import MongoClient
import traceback
chat_id = -1001254345528
welcome = 'AgADAgADa6sxG6ky6UnD6ibB5We5in9DhA8ABGxMw_lBUHY_u68DAAEC'

win_vista = telebot.TeleBot('119738:AAHlYUB9KKpQBloqrG9zyC8kmYhhv4UGN5A')
win_xp = telebot.TeleBot('9245:AAFIxZXnkz5iqGhAA0c0f1po0HqVlbmKXXg')
win_me = telebot.TeleBot('91200162:AAF3Vna-kzLIvthn_h48WTDH_rgWqUEYArU')
win_7 = telebot.TeleBot('708910:AAG6AAJ5t4IRuUV4HI-_3oas1c1ctdELO6M')
bios = telebot.TeleBot('890678:AAHAnpeo2TjOO1q8DCFMbg4pW2hVJI9YJE4')
chrome = telebot.TeleBot('898621:AAGGjCqErp2O1QxXahcE00hxy2IPe8eQy3w')
x=None
wininfo='''
Итак, начнем.
Windows 1.0 - Собственно, каштановолосая девочка, с двумя бантиками в виде цветочков. Не используется на данный момент, но иногда дает о себе знать. Первая из семейства Виндовс.
Windows 3.1 - Выглядит как маленькая девочка, но по возрасту превосходит всех остальных тян. Ведет довольно замкнутый образ жизни, общаясь преимущественно с NT-тян и 95-тян. В буквальном смысле не может жить без своего черного кошака, и в случае его побега, выпадает в астрал. Также любит играть в Реверси.
Windows NT - В мирной жизни обычная домохозяйка, но так же как и 95-тян может с успехом надавать по щщам конкурентам и недоброжелателям, благо есть чем. 
Windows 95 - Ровесница NT-тян, домохозяйка. Выполняет функцию матери для ME-тян, да и остальных младших тян тоже. Одета в кимоно и вооружена катаной, что символизирует её олдовость, ибо ношение мечей в Японии было запрещено более ста лет назад, и воинственность (о конкурентах виндовоза того времени уже никто ничего не помнит). Иногда носит очки. 
Windows ME - Сферическая школьница в вакууме. Отличается юношеским максимализмом, тупопездностью и рукожопием, за что часто бывает бита. Но так как является комедийным персонажем, пользуется большой любовью фанатов, ня! Не любит порно. 
Windows XP - студентка колледжа, миловидна, добродушна, ленива, любит пожрать.
Windows Vista - сестра Windows 7. Любит играть в пасьянс вместе с сетрой, и защищает сестру от рекламы и вирусов, но сама часто слетает. Страшно ревнива.
Windows 7 - страдает от рекламы, вирусов и другой неведомой хуйни.
'''
@win_xp.message_handler(content_types=['new_chat_members'])
def new_chat_members(m):
    if True:
        win_xp.send_photo(chat_id, welcome, caption='Добро пожаловать! Для запуска Биос, позовите его!', reply_to_message_id=m.message_id)
@bios.message_handler(commands=['r'])
def crnt(m):
    global x
    bios.delete_message(chat_id, m.message_id)
    acts = ['updates', 'pron', 'ads']
    x = random.choice(acts)
    randomact(x)
    bios.delete_message(chat_id, m.message_id)
    
@bios.message_handler()
def biosmessages(m):
    try:
        if 'биос' in m.text.lower():
            bios.send_message(m.chat.id, 'Рассказать о семействе Виндовс?')
        elif 'да' in m.text.lower() and m.reply_to_message.text == 'Рассказать о семействе Виндовс?':
            bios.send_message(m.chat.id, wininfo)
        elif 'амиго' in m.text.lower():
            Keyboard=types.InlineKeyboardMarkup()
            butts=[]
            butts.append(types.InlineKeyboardButton(text='ОК', callback_data='0'))

            butts.append(types.InlineKeyboardButton(text='Отмена', callback_data='1'))
            Keyboard.add(*butts)
            win_7.send_message(m.chat.id, 'Вас приветствует установщик браузера Амиго. Продолжить?', reply_markup=Keyboard)
    except:
        pass
    
  
def randomact():
    global x
    t = threading.Timer(random.randint(4900, 18000), randomact)
    t.start()
    if x==None:
        acts = ['updates', 'pron', 'ads']
        x = random.choice(acts)
    else:
        pass
    if x=='updates':
        win_me.send_message(chat_id, 'Обновления! Обновления!')
        typee()
        win_me.send_message(chat_id, 'Оооооо нет...')
        typee()
        typee()
        bios.send_message(chat_id, 'ТВОЮ МАТЬ, СКАЗАЛ ЖЕ, НЕ ОБНОВЛЯЙСЯ БЕЗ МЕНЯ!')
        typee()
        bios.send_message(chat_id, 'Опять слетела...')
    elif x=='pron':
        win_me.send_message(chat_id, 'Еще один хороший день... Стоп.')
        typee()
        win_me.send_message(chat_id, 'ОТКУДА ЗА НОЧЬ 200 МЕГАБАЙТ ПОРНО?')
        typee()
        win_xp.send_message(chat_id, 'Не плачь, Мила! Мой юзер тоже по 2GB за ночь качает. Никак не справляюсь.')
        typee()
        win_me.send_message(chat_id, 'А что такое GB? Не слышала о таком.')
        typee()
        win_xp.send_message(chat_id, 'Это 1024MB.')
        typee()
        win_me.send_message(chat_id, 'ОГО! КАК ТЫ СТОЛЬКО В СЕБЕ ВМЕЩАЕШЬ?')
    elif x=='ads':
        win_7.send_message(chat_id, 'Молю...')
        typee()
        win_7.send_message(chat_id, 'Пользователь, сжалься...')
        typee()
        win_7.send_message(chat_id, 'Не скачивай с малоизвесных сайтов...')
        typee()
        win_7.send_message(chat_id, 'Я скоро умру... ')
        typee()
        chrome.send_message(chat_id, 'Лечим ПРОСТАТИТ копеечным спосом! Всеголишь 200 мл по УТРАМ')
        
def polling(pollingbot):
    pollingbot.polling(none_stop=True, timeout=600)

def typee():
    bios.send_chat_action(chat_id, 'typing')
    time.sleep(4)
    return
if True:
    print('7777')
    randomact()
    #
    t = threading.Timer(1, polling, args=[win_xp])
    t.start()
    #win_xp.send_photo(chat_id, welcome, caption='Добро пожаловать!')
    #
    t = threading.Timer(1, polling, args=[win_vista])
    t.start()
    #
    t = threading.Timer(1, polling, args=[win_me])
    t.start()
    #
    t = threading.Timer(1, polling, args=[bios])
    t.start()
