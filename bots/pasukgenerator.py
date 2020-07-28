#its a BIGGEST pasuk bot ever

import os
import telebot
import time
import random
import threading
from emoji import emojize
from telebot import types
from pymongo import MongoClient
import traceback
import requests
import info
from bs4 import BeautifulSoup

#-----------------Greatest Funcs--------------------------------
def medit(message_text,chat_id, message_id,reply_markup=None,parse_mode=None):
    return bot.edit_message_text(chat_id=chat_id,message_id=message_id,text=message_text,reply_markup=reply_markup,
                                 parse_mode=parse_mode)
def hello():
    try:
        t=threading.Timer(3600, reload)
        t.start()
        global allw
        allw=words.find_one({})
        pasuki=['Брит уебло']
        tts = random.choice(pasuki)
        tts = 'Мое настроение: ' + tts
        bot.send_message(-1001405019571, tts)
    except:
        pass    
#--------------------Variables------------------------


token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token)
endsymbols=['!', '.', '?', ')'] #Символы для цепей Маркова.
odmens=[441399484, 512006137, 268486177] #Bot admins.
evalist = [512006137]
polls={}
drochka_pisosa = 0 #Chat id for ugadaika fixing.
number=0
deystviya = ['ПОЛУНИН ТУПОЙ ЕБАК'] # List for /pasukgo.
triggers={}
x=triggers
randlist=['Пасюк №']#List for ugadaika's nicks.
ban=[]
try:
    client = MongoClient(os.environ['database']) #Connceting to Mongo
    db=client.aiwordgen #Database of Markov Chains
    words=db.words #Collection for Markov Chains
    pasuki2=db.pasuki2 #Pasuk's phrases
    pasuki2=pasuki2.find_one({}) #Importing from Mongo
    twowords=0
    allw={}
except Exception as e:
    print('Ошибка:\n', traceback.format_exc())
    bot.send_message(512006137, traceback.format_exc())
    
    
#----------------Simple Commands----------------
@bot.message_handler(commands=["eval"])
def ebal(m):
    try:
        if m.from_user.id in evalist:
            txt = m.text.split(" ", 1)[1]
            eval(txt)
            bot.send_message(m.chat.id, "Source:\n"+txt)
    except:
        bot.send_message(m.chat.id, "Source:\n"+txt+'\nErrors:\n'+traceback.format_exc())
@bot.message_handler(commands=["help"])
def helpach(m):
    sss='Это бот с огромезным функционалом!\n/bunt <кол-во> - бунтануть\n/here - получить айди чата в лс\n//golos <текст> - поговорить от лица бота(не анонимно)\n/ptalk <текст> - написать от лица Пасюка\n/findpasuk - сыграть в игру "найди пасюка"\n/randompasuk - фраза Пасюка\n/cohelp - помощь по /convert\n/ugadai - игра про поиск пасюка.\nАдминам:\n/ban <время> - бан юзера на определенное время\n/mute <время> - мут юзера на определенное время'
    bot.send_message(m.chat.id, sss)

@bot.message_handler(commands=["ptalk"])
def gandoni(m):
    if m.from_user.id in ban:   #Cheking if user id in ban(dont working)
        return
    try:
        bot.delete_message(m.chat.id, m.message_id)    #Deleting msg with command
        text = m.text.split(' ', 1)[1]  
        if text == 'laguh':
            bot.send_sticker(m.chat.id, 'CAADAgADAwAD-ZeEHnikVOwYHk14Ag', reply_to_message_id = m.reply_to_message.message_id)
            trace = m.from_user.first_name + ' ' + text
            bot.send_message(512006137, trace)
        elif text == 'cat':
            bot.send_sticker(m.chat.id, 'CAADAgADCwAD-ZeEHn8PdFdXHqZJAg', reply_to_message_id = m.reply_to_message.message_id)  
            trace = m.from_user.first_name + ' ' + text
            bot.send_message(512006137, trace)
        else:
            bot.send_message(m.chat.id, text, reply_to_message_id = m.reply_to_message.message_id)
            trace = m.from_user.first_name + ' ' + text
            bot.send_message(512006137, trace)
    except:
        try:
            text = m.text.split(' ', 1)[1]
            if text == 'laguh':
                bot.send_sticker(m.chat.id, 'CAADAgADAwAD-ZeEHnikVOwYHk14Ag')
                trace = m.from_user.first_name + ' ' + text
                bot.send_message(512006137, trace)
            elif text == 'cat':
                bot.send_sticker(m.chat.id, 'CAADAgADCwAD-ZeEHn8PdFdXHqZJAg')
                trace = m.from_user.first_name + ' ' + text
                bot.send_message(512006137, trace)
            else:
                bot.send_message(m.chat.id, text)
                trace = m.from_user.first_name + ' ' + text
                bot.send_message(512006137, trace)
        except:
            bot.send_message(512006137, traceback.format_exc())
@bot.message_handler(commands=["google"])
def google(m):
    text = m.text.split(' ', 1)[1]
    r = requests.get('http://google.com/search?q={}'.format(text[1]))
    soup = BeautifulSoup(r.text, features="lxml")
    try:
        items = soup.find_all('div', {'class': 'g'})
    except:
        bot.send_message(m.chat.id, 'Ответов на ваш запрос нет')
        return
    text = ''
    i = 1
    for item in items:
        print(item)
        link = item.find('h3', {'class': 'r'}).find('a').get('href')[7:]
        txt = item.find('h3', {'class': 'r'}).find('a').text
        try:
            desc = item.find('span', {'class': 'st'}).text
            text += '<a href="{}">{}</a>\n' \
                    '{}\n\n'.format(link, txt, desc)
        except:
            text += '<a href="{}">{}</a>\n\n'.format(link, txt)
        if i == 5:
            break
        i += 1
    if i == 1:
        bot.send_message(m.chat.id, 'Ответов на ваш запрос нет')
        return
    bot.send_message(m.chat.id, text.encode('UTF-8'), parse_mode='HTML')
@bot.message_handler(commands=["piska"])
def gandonik(m):
    if m.from_user.id in ban:   
        return
    try:
        bot.delete_message(-1001405019571, m.message_id)
        text = m.text.split(' ', 1)[1]
        if text == 'laguh':
            bot.send_sticker(-1001405019571, 'CAADAgADAwAD-ZeEHnikVOwYHk14Ag', reply_to_message_id = m.reply_to_message.message_id)
        elif text == 'cat':
            bot.send_sticker(-1001405019571, 'CAADAgADCwAD-ZeEHn8PdFdXHqZJAg', reply_to_message_id = m.reply_to_message.message_id)    
        else:
            bot.send_message(-1001405019571, text, reply_to_message_id = m.reply_to_message.message_id)
    except:
        try:
            text = m.text.split(' ', 1)[1]
            if text == 'laguh':
                bot.send_sticker(-1001405019571, 'CAADAgADAwAD-ZeEHnikVOwYHk14Ag')
            elif text == 'cat':
                bot.send_sticker(-1001405019571, 'CAADAgADCwAD-ZeEHn8PdFdXHqZJAg')
            else:
                bot.send_message(-1001405019571, text)
        except:
            bot.send_message(512006137, traceback.format_exc())
    
@bot.message_handler(commands=["admin"])
def start(message):
    if message.from_user.id in ban:   
        return
    bot.send_message(message.chat.id, "@p0lunin")
    bot.send_message(message.chat.id, "@loshadkin")
    bot.send_message(message.chat.id, "@gbball")
    bot.send_message(message.chat.id, "канец и делу винец")
       
@bot.message_handler(commands=["golos"])
def gandon(m):
    if m.from_user.id in ban:   
        return
    try:
        bot.delete_message(m.chat.id, m.message_id)
        text = m.from_user.first_name
        text += ': '
        text += m.text.split(' ', 1)[1]
        bot.send_message(m.chat.id, text)
    except:
        pass
@bot.message_handler(commands=["bunt"])
def bunt(m):
    if m.from_user.id != 512006137:
        pass
    try:
        bunts = int(m.text.split(' ')[1])
        for i in range(bunts):
            bot.send_message(-1001405019571, "ЧУНГАЧАНГА ПОХОДУ ТЫ ЕБЛО\nЧУНГАЧАНГА БОТА РАЗНЕСЛО\nЧУНГАЧАНГА МОДЕРОВ БОМБИТ\nЧУНГАЧАНГА ИХ ПИЗДАК ГОРИТ")
    except:
        bot.send_message(-1001405019571, "ЧУНГАЧАНГА ПОХОДУ ТЫ ЕБЛО\nЧУНГАЧАНГА БОТА РАЗНЕСЛО\nЧУНГАЧАНГА МОДЕРОВ БОМБИТ\nЧУНГАЧАНГА ИХ ПИЗДАК ГОРИТ")
@bot.message_handler(commands=["print"])    
def printf(m):
    printef = m.text.split(' ', 1)[1]
    print(printef)
    bot.send_message(-1001405019571, "ok")
  
@bot.message_handler(commands=["here"])
def here(m):
    if m.from_user.id in ban:   
        return
    text = m.chat.id
    bot.send_message(m.from_user.id, text)

@bot.message_handler(commands=["convert"])
def conva(m):    
    conf = m.text.split(' ', 1)
    conf = conf[1]
    conf = conf.split('"')
    vid = conf[0]
    vid=vid[:len(vid)-1]
    el = conf[1]
    el = el.split('^')
    query = conf[2]
    query = query.split(' ')[1]
    print('vid: '+vid)
    print('query: '+query)
    try:
        if vid == 'replace':
            query = query.split(el[0])
            query = el[1].join(query)
            bot.send_message(m.chat.id, query)
        else:
            bot.send_message(m.chat.id, 'ERR')
    except:
        bot.send_message(512006137, traceback.format_exc())


@bot.message_handler(commands=["cohelp"])
def cohelpach(m):
    sss='/convert replace "<символы, которые заменять>^<на что заменять>" <текст>'
    bot.send_message(m.chat.id, sss)
    
    
#---------------------Ugadaikas code---------------------


@bot.message_handler(commands=['ugadai'])
def m(m):
    global drochka_pisosa
    if m.chat.id not in info.lobby.game and m.chat.id != m.from_user.id:
        info.lobby.game.update(createroom(m.chat.id))
        drochka_pisosa = m.chat.id
        t=threading.Timer(300, del2, args=[m.chat.id])
        t.start()
        info.lobby.game[m.chat.id]['timer']=t
        bot.send_message(512006137, 'Угадайка началася где-то!')
        Keyboard=types.InlineKeyboardMarkup()          
        Keyboard.add(types.InlineKeyboardButton(text='Искать пасюка', callback_data='join'))
        info.lobby.game[m.chat.id]['startm']=bot.send_message(m.chat.id, 'Начинаем! жмите на кнопку, чтобы присоединиться', reply_markup=Keyboard)
    else:
      try:
        bot.reply_to(info.lobby.game[m.chat.id]['startm'], 'Угадайка уже идёт, или вы уебас!')
      except:
        pass
@bot.message_handler(commands=['stop'])
def s(m):
  for ids in info.lobby.game:
    if m.from_user.id in info.lobby.game[ids]['players']:
        bot.send_message(ids, 'Угадыватель пасючка вышел!')
        t=threading.Timer(0.1, delplayer, args=[ids, m.from_user.id])
        t.start()    
                 
def del2(id):
    try:
      for suchki in info.lobby.game[id]['players']:
        bot.send_message(id, suchki)
        Keyboard=types.InlineKeyboardMarkup()
        Keyboard.add(types.InlineKeyboardButton(text=str(suchki), callback_data='js'))      
      bot.send_message(id, 'И кто пaсюк?', reply_markup=Keyboard)
      del info.lobby.game[id]
    except:
      bot.send_message(512006137, traceback.format_exc())
def delplayer(id, id2):
    try:
        del info.lobby.game[id]['players'][id2]
    except:
        bot.send_message(512006137, traceback.format_exc())            
def deleter(id):
  try:
    del info.lobby.game[id]
  except:
    bot.send_message(512006137, traceback.format_exc())    
def namechoice(id):
    x=random.choice(randlist)
    while x in info.lobby.game[id]['nicks']:
        x=random.choice(randlist)
        x += str(random.randint(1,10))
    info.lobby.game[id]['nicks'].append(x)
    return x               
def begin(id):
    pass
    for ids in info.lobby.game[id]['players']:
        try:
            bot.send_message(ids, 'Пишите сюда что то')
        except:
            bot.send_message(id, 'Какой то пидорас не открыл диалог с ботом!')     
def createroom(id):
  return{id:{
      'nicks':[],
      'startm':None,
      'timer':None,
    'players':{
    }
     }
      }           
def createuser(id, chatid):
    return{id:{
           'name':namechoice(chatid)
          }
          }   


#-----------------------FindPasuk--------------------------

@bot.message_handler(commands=['findpasuk'])
def dd(m):
    if m.from_user.id in ban:   
        return
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

#-------------GREAT HANDLERS------------
@bot.callback_query_handler(func=lambda call:True)
def inline(call):
    if call.data=='join':        
      try:
        if call.from_user.id not in info.lobby.game[call.message.chat.id]['players']:
              z=0
              for ids in info.lobby.game:
                  if call.from_user.id in info.lobby.game[ids]['players']:
                    z+=1    
              if z==0:
               if True:
                  info.lobby.game[call.message.chat.id]['players'].update(createuser(call.from_user.id, call.message.chat.id))
                  bot.send_message(call.message.chat.id, 'Угадыватель пасючка вошел!')
                  info.lobby.alreadyplay.append(call.from_user.id)
                  if call.from_user.id == 441399484:
                    bot.send_message(441399484, 'Ты пасюк! Пытайся быть им!')
                  else:
                    bot.send_message(call.from_user.id, 'Ты не пасюк! Пытайся быть им, что бы тебя выбрали!')
                  
               else:
                   try:
                       bot.send_message(call.from_user.id, 'Достигнуто максимальное число пидоров!')
                   except:
                       pass
                 
               #if len(info.lobby.game[call.message.chat.id]['players'])>len(randlist):
               # bot.send_message(call.message.chat.id, 'Набор окончен!')
               # begin(call.message.chat.id)
      except:
       bot.send_message(512006137, traceback.format_exc())
    '''
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
                emoj='pasuk'
            elif i in game['govno']:
                if sasole == 1:
                    emoj='gold'
                else:
                    emoj='govno'
            else:
                emoj='хуй'
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
    '''
@bot.message_handler()
def addword(m):
    for ids in info.lobby.game:
        if m.from_user.id in info.lobby.game[ids]['players']:
            if m.chat.id == m.from_user.id:
                try:
                    bot.send_message(ids, '_'+info.lobby.game[ids]['players'][m.from_user.id]['name']+'_:\n'+m.text, parse_mode='markdown')
                    info.lobby.game[ids]['timer'].cancel()
                    t=threading.Timer(1500, del2, args=[ids])
                    t.start()
                    info.lobby.game[ids]['timer'].stop()
                    info.lobby.game[ids]['timer']=t
                except:
                    pass
            try:
                for idd in info.lobby.game[ids]['players']:
                    if m.from_user.id!=idd and m.chat.id == m.from_user.id:
                        bot.send_message(idd, '_'+info.lobby.game[ids]['players'][m.from_user.id]['name']+'_:\n'+m.text, parse_mode='markdown')
            except:
                pass
  

#----------------------Forrero------------------            
hello()
bot.send_message(512006137, 'launched')
bot.delete_webhook()
bot.polling(none_stop=True,timeout=600)
print('7777')
#----------------TRASH----------------------
'''
global twowords
    text = m.text.lower()
    for trigger in x:
        if trigger in text:
            tts = triggers[trigger]
            bot.send_message(m.chat.id, tts, reply_to_message_id = m.message_id)
    if m.from_user.id==441399484:
        try:
            pasuki2.update_one(pasuki2, {'$push': {'pasuki2':m.text}})
        except:
            pass
        try:
            if m.text[0]!='/' and m.text[0]!="@":
                toupdate={}
                allword=words.find_one({})
                textwords=m.text.split(' ')
                i=0
                for ids in textwords:
                  if ids not in endsymbols:
                    currentword=ids
                    if twowords==1:
                        try:
                            currentword=ids+' '+textwords[i+1]
                        except:
                            currentword+=ids+' '+'&end'
                    if currentword=='&start':
                        currentword='start'
                    if i==0:
                        fixids=currentword
                        while fixids[len(fixids)-1]==".":
                            fixids=fixids[:len(fixids)-1]
                        if "." not in fixids:
                            toupdate.update({'&start':{fixids:1}})
                    end=False
                    try:
                        nextword=textwords[i+1]
                        if twowords==1:
                            try:
                                nextword=textwords[i+2]+' '+textwords[i+3]
                            except:
                                nextword=textwords[i+2]+' '+'&end'
                                end=True
                    except:
                        nextword='&end'
                        end=True
                    if '&end' in nextword and end==False:
                        nextword='end'
                    try:
                        if currentword[len(currentword)-1] in endsymbols:
                            nextword='&end'
                    except Exception as e:
                        bot.send_message(512006137, traceback.format_exc())
                    try:
                        while currentword[len(currentword)-1] == '.':
                            currentword=currentword[:len(currentword)-1]
                    except Exception as e:
                        bot.send_message(512006137, traceback.format_exc())
                    try:
                        while nextword[len(nextword)-1]==".":
                            nextword=nextword[:len(nextword)-1]
                    except Exception as e:
                        bot.send_message(512006137, traceback.format_exc())
                    if currentword not in toupdate:     
                        if "." not in currentword and "." not in nextword:
                            toupdate.update({currentword:{nextword:1}})
                    else:
                        if nextword not in toupdate[currentword]:
                            if "." not in currentword and "." not in nextword:
                                toupdate[currentword].update({nextword:1})
                        else:
                            
                            toupdate[currentword][nextword]+=1
                    i+=1
                
                if twowords==1:
                    dic='words2'
                else:
                    dic='words'
                for ids in toupdate:
                    if ids not in allword[dic]: ####
                        for idss in toupdate[ids]:
                            if isinstance(toupdate[ids][idss], int):
                                words.update_one({},{'$set':{dic+'.'+str(ids)+'.'+str(idss):toupdate[ids][idss]}})
                    else:
                        for idss in toupdate[ids]:
                            if idss not in allword['words'][ids]:
                                if isinstance(toupdate[ids][idss], int):
                                    words.update_one({},{'$set':{dic+'.'+str(ids)+'.'+str(idss):toupdate[ids][idss]}})
                            else:
                                if isinstance(toupdate[ids][idss], int):
                                    words.update_one({},{'$inc':{dic+'.'+str(ids)+'.'+str(idss):toupdate[ids][idss]}})
                     
        except Exception as e:
            bot.send_message(512006137, traceback.format_exc())  
@bot.message_handler(commands=["wiki"])
def wiki(m):
    try:
        text = m.text.split(' ', 1)[1]
        text = text.split(' ')
        text = '_'.join(text)    
        text = 'https://ru.wikipedia.org/wiki/'+text
        url = text
        r = requests.get(url)
        print(r)
        c = httplib.HTTPConnection(url)
        c.request("HEAD", '')
        if c.getresponse().status == 200:
            bot.send_message(m.chat.id, text)
        elif c.getresponse().status == 404:
            bot.send_message(m.chat.id, 'Нет такой страницы кста')
    except:
        bot.send_message(m.chat.id, 'Еблан пиши нормально')
        bot.send_message(512006137, traceback.format_exc())
@bot.message_handler(commands=["google"])
def google(m):
    try:
        text = m.text.split(' ', 1)[1]
        text = text.split(' ')
        text = '+'.join(text)    
        text = 'https://www.google.com/search?q='+text
        bot.send_message(m.chat.id, text)
    except:
        bot.send_message(m.chat.id, 'Еблан пиши нормально')
        bot.send_message(512006137, traceback.format_exc())        
    
@bot.message_handler(commands=["droch"])
def droch(m):    
    i=random.randint(1, 1000)
    text = 'Вы увеличели член посюка на "+i+"!"
    i+=i
    bot.send_message(m.chat.id, text)
    megaeblani=[]
    megaeblani.append(m.from_user.id)
    print(megaeblani)
@bot.message_handler(commands=["about"])
def start(message):
    if message.from_user.id in ban:   
        return
    bot.send_message(message.chat.id, "Разработчик: @gbball")
    bot.send_message(message.chat.id, "Родитель: @tiger_trigger_bot")
@bot.message_handler(commands=["aboutchat"])
def start(message):
    if message.from_user.id in ban:   
        return
    bot.send_message(message.chat.id,
                     "Чат с играми в покемонов, где сидят три чокнутых программиста, один из них только косит под "
                     "него. Один пинает их, два работают. админка: /admin")
@bot.message_handler(commands=["brit"])
def start(message):
    if message.from_user.id in ban:   
        return
    bot.send_message(message.chat.id, "@gbball")
    bot.delete_message(message.chat.id, message.message_id)
@bot.message_handler(commands=["pasuk"])
def start(message):
    if message.from_user.id in ban:   
        return
    bot.send_message(message.chat.id, "@loshadkin")
    bot.delete_message(message.chat.id, message.message_id)
@bot.message_handler(commands=["oslik"])
def start(message):
    if message.from_user.id in ban:   
        return
    bot.send_message(message.chat.id, "@p0lunin")
    bot.delete_message(message.chat.id, message.message_id)
    
@bot.message_handler(commands=['pasukgo'])
def pasukandiy(m):
    if m.from_user.id in ban:   
        return
    ttts = random.choice(deystviya)
    ttts = "Пасюк " + ttts + "!"
    bot.send_message(m.chat.id, ttts)
    
@bot.message_handler(commands=['lll'])
def addpasukandiy(m): 
    if m.from_user.id in ban:   
        return
    try:
        bot.delete_message(m.chat.id, message_id)
        addgo=m.text.split(' ', maxsplit = 1)
        deystviya.append(addgo[1])
    except:
        bot.send_message(m.chat.id, "ебак тупой")
    
@bot.message_handler(commands=['randompasyk'])
def pasuka(m):
    if m.from_user.id in ban:   
        return
    try:
        wgat = random.randint(1,2)
        if wgat == 1:
            tts = random.choice(pasuki)
            bot.send_message(m.chat.id, tts)
        else:
            tts = random.choice(pasuki2)
            bot.send_message(m.chat.id, tts)
    except:
        pasuka(m)
    
@bot.message_handler(commands=['addpasuk'])
def addpasuka(m):
    if m.from_user.id in ban:   
        return
    bot.delete_message(m.chat.id, message_id)
    lol=m.text.split(' ', maxsplit = 1)
    lol=lol[1]
    pasuki.append(lol)
    
    
@bot.message_handler(commands=['add'])
def addtrigger(m):
    if m.from_user.id in ban:   
        return
    text=m.text.split(' ', maxsplit = 1)
    bot.delete_message(m.chat.id, m.message_id)
    text=text[1]
    text=text.split('/')
    triggers.update({text[0]:text[1]})
    
SUKA
@bot.message_handler(commands=['del']) 
def deltrigger(m):
    if m.from_user.id in ban:   
        return
    try:
        text=m.text.split(' ', maxsplit = 1)
        bot.delete_message(m.chat.id, m.message_id)
        text=text[1]
        text=text.split('/')
        del triggers[text[0]]
    except Exception as e:
        print("kek")
              
    
    
    
    
            
def kostory():
    if True:
        try:
            sentences=random.randint(1,3)
            try:
                sentences=int(m.text.split(' ')[1])
            except:
                pass
            csent=0
            ctext=''
            global allw
            allwords=allw
            global twowords
            if twowords==1:
                dic='words2'
            else:
                dic='words'
            while csent<sentences:
                cword=0
                currentword=''
                while '&end' not in currentword:
                    start=None
                    if cword==0:
                        if twowords==0:
                            start=allwords[dic]['&start']
                        else:
                            for idss in allwords[dic]:
                                if '&start' in idss:
                                    start=allwords[dic][idss]
                        items=[]
                        for ids in start:
                            i=0
                            try:
                                while i<start[ids]: 
                                    items.append(ids)
                                    i+=1
                            except:
                                pass
                        start=random.choice(items)
                        i=0
                        cwd=''
                        currentword=start
                        
                        st=0
                        for a in start:
                            if i==0 and a.isupper()==False and st==0:
                                if a!='@':
                                    cwd+=a.upper()
                            else:
                                if a!='@':
                                    cwd+=a
                            st+=1
                        start=cwd
                        ctext+=start+' '
                    else:
                        nextwords=[]
                        for ids in allwords[dic][currentword]:
                            i=0
                           
                             
                            while i<allwords[dic][currentword][ids]:
                                    nextwords.append(ids)
                                    i+=1
                            
                        nextword=random.choice(nextwords)
                        if currentword[len(currentword)-1] in endsymbols:
                            endsent=1
                        else:
                            endsent=0
                        currentword=nextword
                        
                        if '&end' not in nextword:
                            i=0
                            cwd=''
                            for a in nextword:
                                if a!='@':
                                    cwd+=a
                            ctext+=cwd+' '
                        else:
                            if endsent==0:
                                if twowords==1:
                                    ctext=ctext[:len(ctext)-5]
                                else: 
                                    ctext=ctext[:len(ctext)-1]
                                ctext+='.'
                        
                    cword+=1
                csent+=1
                ctext+=' '
            bot.send_message(-1001405019571, ctext)
            t=threading.Timer(5, kostory)
            t.start()
        except Exception as e:
            kostory()
