import os
import telebot
import time
import datetime
import calendar
import random
import threading
from emoji import emojize
from telebot import types
from pymongo import MongoClient
import traceback
text = 'sas'
whotoban=0
whereban=1
GLOBALADMINS=[512006137, 268486177]
evalist = [512006137]
matuki=['сука', 'ебать', "пизд", "хуй", "хуе", "хуя", "ебал"]
token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token)
client = MongoClient(os.environ['database']) #Connceting to Mongo
db=client.OlgaDmitrievna 
pionners=db.pionners
bez_matov = False
def medit(message_text,chat_id, message_id,reply_markup=None,parse_mode=None):
    return bot.edit_message_text(chat_id=chat_id,message_id=message_id,text=message_text,reply_markup=reply_markup,
                                 parse_mode=parse_mode)
try:
    bot.restrict_chat_member(can_send_messages=True, can_send_other_messages=True, user_id=512006137, chat_id=-1001405019571)
    bot.unban_chat_member(user_id=512006137, chat_id=m.chat.id)
except:
    pass
@bot.message_handler(commands=["eval"])
def ebal(m):
    try:
        if m.from_user.id in evalist:
            txt = m.text.split(" ", 1)[1]
            eval(txt)
            bot.send_message(m.chat.id, "Ой... И не говори.")
    except:
        bot.send_message(m.chat.id, traceback.format_exc())
        
@bot.message_handler(commands=['addstop'])
def addstop(m):
    text=m.text.split(' ', 1)
    stopwords.append(text)
    
@bot.message_handler(commands=['mute'])
def mutee(m):
    
    if m.chat.id!=m.from_user.id:
      try:
        if m.from_user.id in GLOBALADMINS and m.reply_to_message.from_user.id not in GLOBALADMINS:
            text=m.text.split(' ')
            try:
                timee=text[1]
                i=int(timee[:-1])
                number=timee[len(timee)-1]
            except:
                i=0
                number='m'
            
            untildate=int(time.time())
            if number=='m':
                untildate+=i*60
                datetext='минут'
            if number=='h':
                untildate+=i*3600
                datetext='часов'
            if number=='d':
                untildate+=i*3600*24
                datetext='дней'
                           
            print(untildate)
            
            if m.reply_to_message!=None:
                ahref = '[' +m.reply_to_message.from_user.first_name + ']' + '(tg://user?id=' +  str(m.reply_to_message.from_user.id) + ')'
                bot.restrict_chat_member(can_send_messages=False, user_id=m.reply_to_message.from_user.id, chat_id=m.chat.id, until_date=untildate)
                if i==0:
                    text='🔇Поставила ' + ahref + ' в угол навсегда.'
                else:
                    text='🔇Поставила ' + ahref + ' в угол на '+str(i)+' '+datetext+'.'
                bot.send_message(m.chat.id, text, parse_mode='Markdown')
        else:
            bot.send_message(m.chat.id, 'Да как ты разговариваешь со старшими!')
      except Exception as e:
        bot.send_message(m.chat.id, 'Голова болит...')
@bot.message_handler(commands=['rulletka'])
def aue(m):
    try:
        if random.randint(1, 6) == 1:
            untildate=int(time.time())
            untildate += 300
            bot.kick_chat_member(user_id=m.from_user.id, chat_id=m.chat.id, until_date=untildate)
            bot.send_message(m.chat.id, 'За азартные игры - 5 минут в угол!')
        else:
            bot.send_message(m.chat.id, 'А ты везунчик!')
    except:
        pass
        

@bot.message_handler(commands=['unmute'])
def unmutee(m): 
  if m.chat.id!=m.from_user.id:
      try:
        if m.from_user.id in GLOBALADMINS:
            ahref = '[' +m.reply_to_message.from_user.first_name + ']' + '(tg://user?id=' +  str(m.reply_to_message.from_user.id) + ')'
            bot.restrict_chat_member(can_send_messages=True, can_send_other_messages=True, user_id=m.reply_to_message.from_user.id, chat_id=m.chat.id)
            bot.send_message(m.chat.id, '🔊Разрешила выйти из угла '+ahref+'.', parse_mode='Markdown')
        else:
            bot.send_message(m.chat.id, 'Да как ты разговариваешь со старшими!')
      except:
          bot.send_message(m.chat.id, traceback.format_exc())
@bot.message_handler(commands=['a4ko_sobaki'])
def achko(m):     
    data = time.ctime()
    vremya = data.split(' ')[3]
    try:
        data = data.replace('Mon', 'понедельник')
        data = data.replace('Tue', 'вторник')
        data = data.replace('Wed', 'среда')
        data = data.replace('Thu', 'четверг')
        data = data.replace('Fri', 'пятница')
        data = data.replace('Sat', 'суббота')
        data = data.replace('Sun', 'воскресенье')
        #pisos
        data = data.replace('Jan', 'Января')
        data = data.replace('Feb', 'Февраля')
        data = data.replace('Mar', 'Марта')
        data = data.replace('Apr', 'Апреля')
        data = data.replace('May', 'Мая')
        data = data.replace('Jun', 'Июня')
        data = data.replace('Jul', 'Июля')
        data = data.replace('Aug', 'Августа')
        data = data.replace('Sep', 'Сентября')
        data = data.replace('Oct', 'Октября')
        data = data.replace('Nov', 'Ноября')
        data = data.replace('Dec', 'Декабря')
    except:
        pass
    ochko = 'Итак, сейчас ' + vremya + ', и сегодня ' + data.split(' ')[0] + ', ' + data.split(' ')[2] + ' число ' + data.split(' ')[1] + ' месяца ' + data.split(' ')[4] + ' года.'
    bot.send_message(m.chat.id, ochko, parse_mode='Markdown')
@bot.message_handler(commands=['ban'])
def ban(m):
    
    if m.chat.id!=m.from_user.id:
        try:
            if m.from_user.id in GLOBALADMINS and m.reply_to_message.from_user.id not in GLOBALADMINS:
                text=m.text.split(' ')
                try:
                    timee=text[1]
                    i=int(timee[:-1])
                    number=timee[len(timee)-1]
                except:
                    i=0
                    number='m'
            
                untildate=int(time.time())
                if number=='m':
                    untildate+=i*60
                    datetext='минут'
                if number=='h':
                    untildate+=i*3600
                    datetext='часов'
                if number=='d':
                    untildate+=i*3600*24
                    datetext='дней'
                           
                print(untildate)
            
                if m.reply_to_message!=None:
                    ahref = '[' +m.reply_to_message.from_user.first_name + ']' + '(tg://user?id=' +  str(m.reply_to_message.from_user.id) + ')'
                    bot.kick_chat_member(user_id=m.reply_to_message.from_user.id, chat_id=m.chat.id, until_date=untildate)
                    if i==0:
                        text='🔨Наказала ' + ahref + ' навсегда.'
                    else:
                        text='🔨Наказала ' + ahref + ' на '+str(i)+' '+datetext+'.'
                    bot.send_message(m.chat.id, text, parse_mode='Markdown')
            else:
                bot.send_message(m.chat.id, 'Да как ты разговариваешь со старшими!')
        except Exception as e:
            bot.send_message(m.chat.id, 'Ой... Голова болит...')

@bot.message_handler(commands=['unban'])
def unban(m):
    try:
        if m.from_user.id in GLOBALADMINS:
            if m.reply_to_message.from_user.first_name == 'Ольга Дмитриевна':
                pass
            else:
                bot.unban_chat_member(user_id=m.reply_to_message.from_user.id, chat_id=m.chat.id)
                ahref = '[' + m.reply_to_message.from_user.first_name + ']' + '(tg://user?id=' +  str(m.reply_to_message.from_user.id) + ')'
                text = 'СУКА' + ahref + '.'
                bot.send_message(m.chat.id, text, parse_mode='Markdown')
        else:
            bot.send_message(m.chat.id, 'Да как ты разговариваешь со старшими!')
    except:
        pass
@bot.message_handler(commands=['pioners'])
def pioners(m):
    ludi = pionners.find_one({'chat_id':m.chat.id},{'pioneri':1})['pioneri']
    uidi = ludi[m.from_user.first_name]
    bot.send_message(m.chat.id, uidi)
@bot.message_handler(commands=['kick'])
def kick(m):
    try:
        if m.from_user.id in GLOBALADMINS and m.reply_to_message.from_user.id not in GLOBALADMINS:
            bot.kick_chat_member(user_id=m.reply_to_message.from_user.id, chat_id=m.chat.id) 
            bot.unban_chat_member(user_id=m.reply_to_message.from_user.id, chat_id=m.chat.id)
        else:
            bot.send_message(m.chat.id, 'Да как ты разговариваешь со старшими!')
    except:
        pass
@bot.message_handler(commands=['matuki'])
def materizza(m):
    if bez_matov == 'True':
        bot.send_message(m.chat.id, "Можно матерится! Но немного.")
        bez_matov = 'False'
    else:
        bez_matov = 'True'
        bot.send_message(m.chat.id, 'Матерится больше нельзя!')                 
@bot.message_handler()
def addword(m):
    try:
        first_nameee = m.from_user.first_name
        pionners.update_one({'chat_id':m.chat.id},{'$set':{'pioneri.' + first_nameee:str(m.from_user.id)}})
        if pionners.find_one({'chat_id':m.chat.id})==None and m.chat.id != m.from_user.id:
            pionners.insert_one({'chat_id':m.chat.id})
    except:
        pass
    ahref = '[' +m.from_user.first_name + ']' + '(tg://user?id=' +  str(m.from_user.id) + ')'
    for matuk in matuki:
        if matuk in m.text.lower() and m.from_user.id not in GLOBALADMINS and bez_matov == 'True':
            text = "🔇Поставила" + ahref + "в угол за маты на 3 минуты."
            untildate=int(time.time())   
            bot.restrict_chat_member(can_send_messages=False, user_id=m.from_user.id, chat_id=m.chat.id, until_date=untildate)
            bot.reply_to(m.message_id, text)
            
    
def vreme():
    data = time.ctime()
    vremya = data.split(' ')[3]
    chas = vremya.split(':')[0]
    chas = int(chas) + 3
    chas = str(chas)

    if chas[0] == "0":
        chas = chas[1]
        chas = int(chas)
    else:
        chas = int(chas)
    whattime(chas)
    
def whattime(chas):    
    if chas > 0 and chas < 4:
        bot.send_message(-1001405019571, 'Хорошая сегодня ночка!', parse_mode='Markdown')
    elif chas > 4 and chas < 12:
        bot.send_message(-1001405019571, 'Хорошее сегодня утро!', parse_mode='Markdown')
    elif chas > 12 and chas < 17:
        bot.send_message(-1001405019571, 'Хороший сегодня день!', parse_mode='Markdown')
    elif chas > 17:
        bot.send_message(-1001405019571, 'Хороший сегодня вечер!', parse_mode='Markdown')
vreme()  
print('7777')
bot.polling(none_stop=True,timeout=600)
