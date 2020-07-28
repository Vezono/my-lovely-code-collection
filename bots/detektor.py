# he is detektor or cooker?

import telebot
import time
import random
import threading
from telebot import types
import traceback
global_admins = [930671372]
main_admin_id = 930671372
main_chat_id = -1001167374930
bot_id = 682665487
bot_token = '980762660:AAFdhztMdsZY8p-V6Czq-EybXGIjoav1Tzg'
bot = telebot.TeleBot(bot_token)
eatable = ['суп', 'картофель', 'торт', 'вода', 'кока кола', 'сок из апельсинов', 'клубника', 'отрава', 'пицца']
cookers={}
def medit(message_text, chat_id, message_id, reply_markup=None, parse_mode='Markdown'):
    return bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=message_text, reply_markup=reply_markup,
                                 parse_mode=parse_mode)
try:
    pass
except Exception as e:
    print('Ошибка:\n', traceback.format_exc())
    bot.send_message(441399484, traceback.format_exc())
@bot.message_handler(commands=['cook'])
def eat(m):
    try:
        meal = m.text.lower().split(' ', 1)[1]
    except:
        bot.send_message(m.chat.id, 'Вы забыли указать, что именно вы хотите приготовить!')
    if m.reply_to_message is None:
        try:
            cookself(m, meal)
        except:
            bot.send_message(m.chat.id, traceback.format_exc())
    else:
        try:
            cookto(m, meal)
        except:
            bot.send_message(m.chat.id, traceback.format_exc())
@bot.message_handler(commands=['append'])
def appendix(m):
    try:
        meal = m.text.lower().split(' ', 1)[1]
        eatable.append(meal)
        bot.send_message(m.chat.id, 'Я научился готовить '+ meal + '!')
        bot.send_message(main_admin_id, str(eatable))
    except:
        bot.send_message(m.chat.id, 'Вы забыли указать, что именно готовить!')
@bot.message_handler(commands=['remove'])
def appendix(m):
    if m.from_user.id != main_admin_id:
        return
    meal = m.text.lower().split(' ', 1)[1]
    eatable.remove(meal)
    bot.send_message(m.chat.id, 'Я разучился готовить '+ meal + '!')
    print(eatable)
          
def cookto(m, meal):
    tts = m.from_user.first_name + ' приготовил(а) пользователю ' + m.reply_to_message.from_user.first_name + ' ' + meal + '!'
    if meal in eatable:
        kb=types.InlineKeyboardMarkup(3) 
        artrits = meal
        buttons1=[types.InlineKeyboardButton(text='Съесть', callback_data='eat '+artrits), 
                  types.InlineKeyboardButton(text='Оставить', callback_data='stay '+artrits), 
                  types.InlineKeyboardButton(text='Выбросить', callback_data='trash '+artrits)]
        kb.add(*buttons1)
        oldm = m
        m = bot.reply_to(m, tts, reply_markup=kb)
    else:
        bot.send_message(m.chat.id, 'Он(а) не может съесть ' + meal + ', потому что я неумею это готовить. Чтобы научить меня - /append еда.')
def cookself(m, meal):
    if meal in eatable:
        bot.send_message(m.chat.id, m.from_user.first_name + ' сьел(а) ' + meal + '!')
    else:
        bot.send_message(m.chat.id, 'Вы не можете съесть ' + meal + ', потому что я неумею это готовить. Чтобы научить меня - /append еда.')
        
@bot.callback_query_handler(func=lambda call:True)
def inline(call):
    calldata = call.data
    attribut = calldata.split()[0]
    userid = call.message.reply_to_message.from_user.id
    meal = calldata.split()[1]
    user_name = call.message.reply_to_message.from_user.first_name
    mid = call.message.message_id
    if userid == call.from_user.id:
        if attribut == 'eat':
            tts = call.from_user.first_name + ' с апетитом сьел(а) блюдо "' + meal + '" от пользователя ' + user_name + '!'
            medit(call.message.chat.id, mid, tts, reply_markup=None)
        elif attribut == 'stay':
            tts = call.from_user.first_name + ' решил(а) не есть блюдо "' + meal + '" от пользователя ' + user_name + '!'
            medit(call.message.chat.id, mid,  tts, reply_markup=None)
        elif attribut == 'trash':
            tts = call.from_user.first_name + ' выбросил(а) блюдо "' + meal + '" от пользователя ' + user_name + '!'
            medit(call.message.chat.id, mid,  tts, reply_markup=None)     
    else:
        bot.answer_callback_query(call.id, 'Это не ваше меню!')
bot.send_message(main_chat_id, 'Деплойнулся!')
print('777')
bot.polling(none_stop=True, timeout=600)

import os
import telebot
import time
import random
import threading
from emoji import emojize
from telebot import types
from pymongo import MongoClient
import traceback
from telebot import types
token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(m):   
    bot.send_message(m.chat.id, 'Здравствуйте! Я подключен к датабазе бога! Задавайте вопросы. /help для помощи')
@bot.message_handler(commands=['help'])
def help(m):
    bot.send_message(m.chat.id, '/yesno Вопрос?\n/question "Вопрос?" ответ1/ответ2')
@bot.message_handler(commands=['yesno'])
def yesno(m):
    random.seed(m.text.split(' ', 1)[1])
    so = random.choice(['Да.', 'Нет.'])
    bot.send_message(m.chat.id, so)
    
@bot.message_handler(commands=['question'])
def question(m):
    try:
        txt = m.text.split(' ', 1)[1].split('"')
        quest = txt[1]
        argss = txt[2][1:].split('/')
        random.seed(quest)
        so = random.choice(argss)
        print(argss)
        print(so)
        so = "Вопрос: " + quest + '\n' + 'Ответ: ' + so
        bot.send_message(m.chat.id, so)
    except:
        bot.send_message(792414733, traceback.format_exc())
    
@bot.inline_handler(func=lambda query: len(query.query) > 0)
def query_text(query):
    try:
        message = query.query
        txt = message.split('"')
        print(txt)
        quest = txt[1]
        argss = txt[2][1:].split('/')
        if False:
            argss=['Да.', 'Нет.']
        else:
            pass
        random.seed(quest)
        so = random.choice(argss)
        print(argss)
        print(so)
        pso = "Вопрос: " + quest + '\n' + 'Ответ: ' + so   
        tts = types.InlineQueryResultArticle(
                id='1', title=quest,
                description=so,
                input_message_content=types.InputTextMessageContent(
                message_text=pso))
        bot.answer_inline_query(query.id, [tts])
    except:
        bot.send_message(792414733, traceback.format_exc())      
print('7777')
bot.send_message(792414733, 'ЩЗА')
bot.polling(none_stop=True,timeout=600)
