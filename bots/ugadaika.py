import os
import telebot
import time
import random
import threading
from emoji import emojize
from telebot import types
from pymongo import MongoClient
import traceback


token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token)

polls={}
number=0
deystviya = ['ебет слона', 'ебет корову']

try:
    pass

except Exception as e:
    print('Ошибка:\n', traceback.format_exc())
    bot.send_message(512006137, traceback.format_exc())

def medit(message_text,chat_id, message_id,reply_markup=None,parse_mode=None):
    return bot.edit_message_text(chat_id=chat_id,message_id=message_id,text=message_text,reply_markup=reply_markup,
                                 parse_mode=parse_mode)   
    
@bot.message_handler(commands=['findpasuk'])
def dd(m):
    global number
    text='Угадайте, в какой коробке пасюк!.'
    kb=types.InlineKeyboardMarkup(3)
    buttons1=[]
    buttons2=[]
    buttons3=[]
    amount=random.randint(0,9)
    i=0
    dicks=[]
    govno=[]
    while i<amount:
        x=random.randint(0,9)
        while x in dicks:
            x=random.randint(0,9)
        dicks.append(x)
        govn=random.randint(0,9)
        while govn in govno:
            govn=random.randint(0,9)
        govno.append(govn)
        i+=1
    i=1
    while i<=9:
        randoms=random.randint(0,1000)
        if i in dicks:
            callb='penis'
        elif i in govno:
            callb='gavno'
        else:
            callb=str(random.randint(0,100))
        if i<=3:
            buttons1.append(types.InlineKeyboardButton(text='📦', callback_data=callb+' '+str(number)+' '+str(randoms)))
        elif i<=6:
            buttons2.append(types.InlineKeyboardButton(text='📦', callback_data=callb+' '+str(number)+' '+str(randoms)))
        elif i<=9:
            buttons3.append(types.InlineKeyboardButton(text='📦', callback_data=callb+' '+str(number)+' '+str(randoms)))
        i+=1
    kb.add(*buttons1)
    kb.add(*buttons2)
    kb.add(*buttons3)
    kb.add(types.InlineKeyboardButton(text='И где же пасюк?', callback_data='endgame '+str(number)))
    polls.update({number:{
        'users':{},
        'dicks':dicks,
        'kb':kb,
        'govno':govno
        
    }}
                )
    bot.send_message(m.chat.id, text, reply_markup=kb)
    number+=1
    
    

@bot.callback_query_handler(func=lambda call:True)
def inline(call):
  try:
    user=call.from_user
    try:
        game=polls[int(call.data.split(' ')[1])]
    except:
        game=None
    govnarstvo = None
    if game!=None:
        if user.id not in game['users'] and call.data!='xyi':
            if 'penis' in call.data:
                dick=True
                bot.answer_callback_query(call.id, '🐴|Ура! Вы выбрали ящик с пасюком!', show_alert=True)
            elif 'gavno' in call.data:
                dick="kakashka"
                bot.answer_callback_query(call.id, '💩|Блядь, долбоеб! Вы выбрали ящик с кукива... Ой, с говном!', show_alert=True)
            else:
                dick=False
                bot.answer_callback_query(call.id, '💨|О нет! Вы выбрали ящик без пасюка!', show_alert=True)
            
            game['users'].update({user.id:{'name':call.from_user.first_name,
                                          'dick':dick}})
            kb=types.InlineKeyboardMarkup(3)
            
            medit(editmsg(game), call.message.chat.id, call.message.message_id, reply_markup=game['kb'])
        
        elif 'endgame' not in call.data:
            bot.answer_callback_query(call.id, 'Вы уже походили!')
        
    if 'endgame' in call.data:
        kb2=types.InlineKeyboardMarkup()
        buttons1=[]
        buttons2=[]
        buttons3=[]
        sasole = random.randint(1, 100000)
        i=1
        while i<=9:
            if i in game['dicks']:
                emoj='🐴'
            elif i in game['govno']:
                if sasole == 1:
                    emoj='💎'
                else:
                    emoj='💩'
            else:
                emoj='💨'
            if i<=3:
                buttons1.append(types.InlineKeyboardButton(text=emoj, callback_data='xyi'))
            elif i<=6:
                buttons2.append(types.InlineKeyboardButton(text=emoj, callback_data='xyi'))
            elif i<=9:
                buttons3.append(types.InlineKeyboardButton(text=emoj, callback_data='xyi'))
            i+=1
        kb2.add(*buttons1)
        kb2.add(*buttons2)
        kb2.add(*buttons3)
        result=editmsg(game, True)
        medit('Игра обкончена ебланом '+call.from_user.first_name+'! Результаты:\n'+result, call.message.chat.id, call.message.message_id, reply_markup=kb2)

  except Exception as e:
    bot.send_message(512006137, traceback.format_exc())
    
def editmsg(game, end=False):
    if end==False:
        text='Угадайте, в какой коробке пасюк.\n\n'
    else:
        text=''
    for ids in game['users']:
        if game['users'][ids]['dick']==True:
            text+=game['users'][ids]['name']+': 🐴нашёл(ла) пасюка\n'
        elif game['users'][ids]['dick']=="kakashka":
            text+=game['users'][ids]['name']+': 💩нашёл(ла) кукивар... ой, говно\n'
        else:
            text+=game['users'][ids]['name']+': 💨открыл(а) пустую коробку\n'
    return text
    
@bot.message_handler(commands=['pasukgo'])
def pasukandiy(m):
    ttts = random.choice(deystviya)
    ttts = "Пасюк " + ttts + "!"
    bot.send_message(m.chat.id, ttts)
    
@bot.message_handler(commands=['addgo'])
def addpasukandiy(m):   
    try:
        addgo=m.text.split(' ', maxsplit = 1)
        deystviya.append(addgo[1])
    except:
        bot.send_message(m.chat.id, "ебак тупой")
        
print('7777')
bot.polling(none_stop=True,timeout=600)
