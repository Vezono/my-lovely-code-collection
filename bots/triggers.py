import os
import telebot
import time
import random
import threading
from emoji import emojize
from telebot import types
from pymongo import MongoClient
import traceback
idlist=[]
testtriggers={}
i = 0
lol = 0
testmod=0

token = ''
bot = telebot.TeleBot(token)
client1=''

client=MongoClient(client1)
db=client.vsevihs
triggerscol=db.triggerscol





triggers= {'лошадкин': '@loshadkin', 'соси': 'как Булат', 'бот упал': '@LOSHADKIN ИДИ ЧИНИТЬ БОТА, ХВАТИТ ДРОЧИТЬ', 'loshadkin': '@loshadkin', 'ваши покемоны': 'это ваши покемоны', 'sasatt': 'lezhat', 'сасать член': 'пасюка', 'булат': 'сосатт', 'бт': 'плясатт', 'бизарр': 'лучшая тима', 'bulat': 'sosatt', 'ослик': 'сосет у себя', 'пасюк': 'пидор', 'слава': ' СЛАВА УКРАИНЕ ГЕРОЯМ СЛАВА', 'россия': 'сасатт', 'аниме': 'Ты что смотришь аниме? Соси хуй тогда🍆', 'винко': 'Уберите этого говноеда от меня, блядб', 'huntall': 'Все равно они не придут', 'нет': 'пидора ответ', 'да': 'пизда', 'бунт': 'CAADAgADDwADIcYAARAiXXInVZNiUAI', 'не приходят': 'CAADAgADDgYAAiVUQBNcQhf8905GbwI', 'кто': 'CAADAQADSgIAAtg_5wk5IXNJogXh9gI', 'дизайнер': 'CAADAgADCAADIcYAARBfFBmUxB9V3gI', 'украин': 'CAADAgADFgADIcYAARAPkK3cV1pXTwI', 'монга': '@gbball', 'brit': '@gbball', 'аргумент': 'аргумент не нужен пидор обнаружен', 'пидор обнаружен': 'Пидор засекречен твой анал не вечен', 'твоя': 'твоя', 'моя': 'головка от хуя'}


#-----------Release-Code------------------
@bot.message_handler(commands=['gettriggers'])
def gettriggers(m):        
    text = 'Тригерры:\n'
    lisrer = str(triggers).replace('{', '').replace('}', '').split(',')
    luntr = 0
    lentr = len(lisrer)
    while lentr != luntr:
        text += '[' + str(luntr) + '] ' + lisrer[luntr] + '\n'
        luntr += 1
    text.replace("'", '').replace(':', ' - ')
    text = text.split("'")
    text = ''.join(text)
    text = text.replace(': ', ' - ')
    print("ZALUPA\n" + text)    
    bot.send_message(m.chat.id, text)  
@bot.message_handler(commands=['add'])
def addtrigger(message):         
    try:
        if message.from_user.id == 0:
            return
        text=message.text.split(' ', maxsplit = 1)
        text=text[1]
        text=text.split('/')
        if ',' in text[1]:
            bot.send_message(message.chat.id, 'Запятые нельзя!')
            return
        triggers.update({text[0]:text[1]})
        bot.send_message(message.chat.id, '@gbball новый триггер ебать иди копируй в код ты же ебан монгу не можешь юзать ггагагга')
    except:
        bot.send_message(message.chat.id, 'Триггер добавляется так:\nтекст/ответ(айди стикера, текст)')
@bot.message_handler(commands=['del']) 
def deltrigger(message):        
    try:
        if message.from_user.id != 512006137:
            return
        text=message.text.split(' ', maxsplit = 1)
        text=text[1]
        text=text.split('/')
        del triggers[text[0]]
    except Exception as e:
        print("kek")

@bot.message_handler(content_types=["text"])
def triggi(message):
    m = message          
    i = 0
    lol = 0
    text = message.text.lower()
    print(str(triggers))
    for trigger in triggers:
        if trigger in text and lol != 300:
            tts = triggers[trigger]
            try:
                bot.send_sticker(message.chat.id, tts, reply_to_message_id = message.message_id)
                i = 1
            except:
                report(message)
            if i != 1:
                bot.send_message(message.chat.id, tts, reply_to_message_id = message.message_id)
            else:
                pass
            lol = 300
        else:
            pass
def report(m):
    return

   #bot.send_message(m.chat.id, traceback.format_exc())


bot.send_message(-1001110170305, '7777')       
print('7777')
bot.polling(none_stop=True,timeout=600)
