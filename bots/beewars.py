# clone fiswars of egor5q

import os
import telebot
import time
import random
import threading
from emoji import emojize
from telebot import types
from pymongo import MongoClient
import traceback
from datetime import datetime

token = ''
bot = telebot.TeleBot(token)

britmsgs=0
client=MongoClient('')
db=client.beewars
users=db.users
allpasekas=db.pasekas

admin = 930671372
fighthours=[12, 16, 20, 0]
pasekalist=['onepaseka', 'truebees']
officialchat=-1001165918958
rest=False
ban=[]
letters=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

allletters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 
           'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

try:
    pass

except Exception as e:
    print('Ошибка:\n', traceback.format_exc())
    bot.send_message(admin, traceback.format_exc())

@bot.message_handler(commands=['fight'])
def updds(m): 
    if m.from_user.id == admin:
        pasekafight()
@bot.message_handler(commands=['update'])
def updd(m):
    if m.from_user.id==admin:
        users.update_many({},{'$set':{'skills':{}, 'inventory':{}}})
        bot.send_message(admin, 'yes')
            
            
@bot.message_handler(commands=['drop'])
def drop(m):
    if m.from_user.id==admin:
        allpasekas.update_many({},{'$set':{'score':0}})
        bot.send_message(m.chat.id, 'Сбросил очки всем пасекам!')
def pasekatoemoj(paseka=None, emoj=None):
    if paseka=='onepaseka':
        return '🐴🍯'
    if paseka=='truebees':
        return '🌻🍯'
def paseka_ru(paseka):
    if paseka=='onepaseka':
        return '🐴🍯Единая Пасека'
    if paseka=='truebees':
        return '🌻🍯Честные Пчеловоды'
@bot.message_handler(commands=['start'])
def start(m):
    user=users.find_one({'id':m.from_user.id})
    global rest
    if user==None and m.from_user.id==m.chat.id:
        users.insert_one(createuser(m.from_user))
        kb=types.ReplyKeyboardMarkup(resize_keyboard=True)
        al=allpasekas.find({})
        print(al)
        bann=None
        for ids in pasekalist:
                kb.add(types.KeyboardButton(paseka_ru(ids)))
        bot.send_message(m.chat.id, 'Добро пожаловать! Выберите, за какую пасеку вы будете сражаться.', reply_markup=kb)
        try:
            ref=m.text.split(' ')[1]
            u=users.find({})
            friend=None
            for ids in u:
                if ids['referal']==ref:
                    friend=ids
            if friend!=None:
                users.update_one({'id':friend['id']},{'$push':{'friends':m.from_user.id}})
                users.update_one({'id':m.from_user.id},{'$set':{'inviter':friend['id']}})
                bot.send_message(friend['id'], m.from_user.first_name+' зашел в игру по вашей рефералке! Когда он поиграет немного, вы получите +1 к максимальной силе!')
        except Exception as e:
           bot.send_message(admin, traceback.format_exc())

        
def mainmenu(user):
    kb=types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(types.KeyboardButton('💢Атака'), types.KeyboardButton('🛡Защита'))
    kb.add(types.KeyboardButton('🌼Питание'), types.KeyboardButton('ℹ️Инфо по игре'))
    kb.add(types.KeyboardButton('🐝Обо мне'))
    needed=countnextlvl(user['lastlvl'])
    text=''
    text+='🐝Имя пчелы: '+user['gamename']+'\n'
    try:
        text+='🍯Родная пасека: '+paseka_ru(user['paseka'])+'\n'
    except:
        pass
    text+='💪Силы: '+str(user['strenght'])+'/'+str(user['maxstrenght'])+'\n'
    text+='🏅Уровень эволюции: '+str(user['lvl'])+'\n'
    text+='🧬Очки эволюции: '+str(user['evolpoints'])+'/'+str(needed)+'\n'
    text+='💢Атака: '+str(user['stats']['attack'])+'\n'
    text+='🛡Защита: '+str(user['stats']['def'])+'\n'
    text+='Реген сил: 1💪 / '+str(round(20*user['strenghtregencoef'], 2))+' минут\n'
    if user['freestatspoints']>0:
        text+='Доступны очки характеристик! Для использования - /upstats'+'\n'
    bot.send_message(user['id'], 'Главное меню.\n'+text, reply_markup=kb)
        

        
        
@bot.message_handler()
def allmessages(m):
    global rest
    user=users.find_one({'id':m.from_user.id})
    if user!=None:
       if m.from_user.id not in ban:
        if rest==False:
            if m.from_user.id==m.chat.id:
                if user['paseka']==None:
                    if m.text=='🐴🍯Единая Пасека':
                        users.update_one({'id':user['id']},{'$set':{'paseka':'onepaseka'}})
                        bot.send_message(user['id'], 'Теперь вы сражаетесь за территорию 🐴🍯Единой Пасеки!')
                        mainmenu(user)
                    if m.text=='🌻🍯Честные Пчеловоды':
                        users.update_one({'id':user['id']},{'$set':{'paseka':'truebees'}})
                        bot.send_message(user['id'], 'Теперь вы сражаетесь за территорию 🌻🍯Честных пчеловодов!')
                        mainmenu(user)
                if m.text=='🛡Защита':
                    users.update_one({'id':user['id']},{'$set':{'battle.action':'def'}})
                    bot.send_message(user['id'], 'Вы вылетели в оборону своей пасеки! Ждите следующего сражения.')
                if m.text=='💢Атака':
                    kb=types.ReplyKeyboardMarkup(resize_keyboard=True)
                    for ids in pasekalist:
                        if ids!=user['paseka']:
                            users.update_one({'id':user['id']},{'$set':{'battle.action':'attack', 'battle.target':ids}})
                            bot.send_message(user['id'], 'Вы приготовились к атаке на пасеку '+paseka_ru(ids)+'! Ждите начала битвы.')
                        mainmenu(user)
                if m.text=='ℹ️Инфо по игре':
                    bot.send_message(m.chat.id, 'Выбирайте пасеку и сражайтесь за нее, '+
                                     'получая для него очки, повышать уровень и улучшать свои характеристики. Битвы в 12:00, 16:00, 20:00 и 24:00 по МСК.')
                    
                if m.text=='/menu':
                    mainmenu(user)
                    
                if m.text=='/upstats':
                    if user['freestatspoints']>0:
                        text='Свободные очки: '+str(user['freestatspoints'])+'.\nВыберите характеристику для прокачки.'
                        kb=types.ReplyKeyboardMarkup(resize_keyboard=True)
                        kb.add(types.KeyboardButton('💢'), types.KeyboardButton('🛡'))
                        bot.send_message(user['id'], text, reply_markup=kb)
                    else:
                        bot.send_message(user['id'], 'Нет свободных очков!')
                        
                if m.text=='💢':
                    if user['freestatspoints']>0:
                        users.update_one({'id':user['id']},{'$inc':{'freestatspoints':-1, 'stats.attack':1}})
                        bot.send_message(user['id'], 'Вы стали сильнее!')
                    else:
                        bot.send_message(user['id'], 'Нет свободных очков!')
                    user=users.find_one({'id':m.from_user.id})
                    mainmenu(user)
                        
                if m.text=='🛡':
                    if user['freestatspoints']>0:
                        users.update_one({'id':user['id']},{'$inc':{'freestatspoints':-1, 'stats.def':1}})
                        bot.send_message(user['id'], 'Вы стали сильнее!')
                    else:
                        bot.send_message(user['id'], 'Нет свободных очков!')
                    user=users.find_one({'id':m.from_user.id})
                    mainmenu(user)
                    
                if m.text=='/referal':
                    if user['referal']==None:
                        ref=genreferal(user)
                        users.update_one({'id':user['id']},{'$set':{'referal':ref}})
                    else:
                        ref=user['referal']
                    bot.send_message(user['id'], 'Вот ваша ссылка для приглашения друзей:\n'+'https://telegram.me/' + bot.get_me().username + '?start='+ref)
                    
                if m.text=='🌼Питание':
                    kb=types.ReplyKeyboardMarkup(resize_keyboard=True)
                    kb.add(types.KeyboardButton('🔛Поле'), types.KeyboardButton('🔜Далекие места'))
                    kb.add(types.KeyboardButton('⬅️Назад'))
                    bot.send_message(m.chat.id, 'Выберите, где будете пытаться искать пищу. Чем больше вы питаетесь, тем быстрее идёт развитие!', reply_markup=kb)
                    
                if m.text=='🔛Поле':
                    strenght=1
                    if user['strenght']>=strenght:
                        if user['status']=='free':
                            users.update_one({'id':user['id']},{'$set':{'status':'eating'}})
                            users.update_one({'id':user['id']},{'$inc':{'strenght':-strenght}})
                            bot.send_message(m.chat.id, 'Вы отправились искать пищу в поле.')
                            t=threading.Timer(random.randint(60, 90), coastfeed, args=[user])
                            t.start()
                        else:
                            bot.send_message(user['id'], 'Вы уже заняты чем-то!')
                    else:
                        bot.send_message(user['id'], 'Недостаточно сил - даже пчолам нужен отдых!')
                    user=users.find_one({'id':m.from_user.id})
                    mainmenu(user)
                    
                if m.text=='🔜Далекие места':
                    strenght=2
                    if user['strenght']>=strenght:
                        if user['status']=='free':
                            users.update_one({'id':user['id']},{'$set':{'status':'eating'}})
                            users.update_one({'id':user['id']},{'$inc':{'strenght':-strenght}})
                            bot.send_message(m.chat.id, 'Вы отправились искать пищу в далекие места.')
                            t=threading.Timer(random.randint(60, 90), depthsfeed, args=[user])
                            t.start()
                        else:
                            bot.send_message(user['id'], 'Вы уже заняты чем-то!')
                    else:
                        bot.send_message(user['id'], 'Недостаточно сил - даже пчолам нужен отдых!')
                    user=users.find_one({'id':m.from_user.id})
                    mainmenu(user)
                    
                if '/fishname' in m.text:
                    try:
                        if user['changename']>0:
                            no=0
                            name=m.text.split(' ')[1]
                            if len(name)<=20 and len(name)>1:
                                for ids in name:
                                    if ids.lower() not in allletters:
                                        no=1
                            else:
                                no=1
                            if no==0:
                                users.update_one({'id':user['id']},{'$set':{'gamename':name}})
                                users.update_one({'id':user['id']},{'$inc':{'changename':-1}})
                                bot.send_message(m.chat.id, 'Вы успешно сменили имя на "*'+name+'*"!', parse_mode='markdown')
                            else:
                                bot.send_message(m.chat.id, 'Длина ника должна быть от 2х до 20 символов и содержать только русские и английские буквы!')
                        else:
                            bot.send_message(m.chat.id, 'Попытки сменить ник закончились!')
                    except:
                        pass
                    
                if m.text=='🐟Обо мне' or m.text=='⬅️Назад':
                    mainmenu(user)
                    
            if m.text=='/score':
                pasekas=allpasekas.find({})
                text=''
                for ids in pasekas:
                    text+=paseka_ru(ids['name'])+' море: '+str(ids['score'])+' очков\n'
                bot.send_message(m.chat.id, text)
        else:
            if m.chat.id==m.from_user.id:
                bot.send_message(m.chat.id, 'В данный момент идёт битва пасек!')
                
                
def genreferal(user):
    u=users.find({})
    ref=''
    allref=[]
    for ids in users.find({}):
        allref.append(ids['referal'])
    while len(ref)<32:
        ref+=random.choice(letters)
    while ref in allref:
        ref=''
        while len(ref)<32:
            ref+=random.choice(letters)
    return ref


def coastfeed(user):
    luckytexts=['Вы нашли большую поляну цветов! Вы можете покормится и принести мед в улей.']
    falsetexts=['Пока вы летали по полю в поисках цветов, вы увидели медведя. Вы решили не нападать на него и улетели.']
    chance=70*user['agility']
    if 'slow' in user['skills']:
        chance+=user['skills']['slow']['lvl']*0.5
    coef=1
    if random.randint(1,100)<=chance:
        i=user['recievepoints']*user['pointmodifer']*coef
        bottompoints=int(i*0.8)
        toppoints=int(i*1.2)
        points=random.randint(bottompoints, toppoints)
        if points<=0:
            points=1
        text=random.choice(luckytexts)
        text+='\nПолучено:\n'+'*Очки эволюции*: '+str(points)+'🧬'
        bot.send_message(user['id'], text, parse_mode='markdown')
        recieveexp(user, points)
    else:
        text=random.choice(falsetexts)
        bot.send_message(user['id'], text, parse_mode='markdown')
    users.update_one({'id':user['id']},{'$set':{'status':'free'}})
    
    
    
def depthsfeed(user):
    luckytexts=['Вы далеко улетели от своего улья, но ваши старания были вознаграждены! Вы прилетели к соседнему улью, и вам дали мед и нектар!']
    falsetexts=['Вы далеко улетели от своего улья, и ничего не нашли. Если бы вы залетели дальше - вы бы просто заблудились.']
    chance=55*user['agility']
    if 'slow' in user['skills']:
        chance+=user['skills']['slow']['lvl']*0.5
    coef=2.5
    if random.randint(1,100)<=chance:
        i=user['recievepoints']*user['pointmodifer']*coef
        bottompoints=int(i*0.8)
        toppoints=int(i*1.2)
        points=random.randint(bottompoints, toppoints)
        if points<=0:
            points=1
        text=random.choice(luckytexts)
        text+='\nПолучено:\n'+'*Очки эволюции*: '+str(points)+'🧬'
        bot.send_message(user['id'], text, parse_mode='markdown')
        recieveexp(user, points)
    else:
        text=random.choice(falsetexts)
        bot.send_message(user['id'], text, parse_mode='markdown')
    users.update_one({'id':user['id']},{'$set':{'status':'free'}})
        
    
    

def recieveexp(user, exp):
    users.update_one({'id':user['id']},{'$inc':{'evolpoints':exp}})
    c=int(countnextlvl(user['lastlvl']))
    if user['evolpoints']+exp>=c:
        users.update_one({'id':user['id']},{'$set':{'lastlvl':c, 'recievepoints':countnextpointrecieve(user['recievepoints'])}})
        users.update_one({'id':user['id']},{'$inc':{'lvl':1, 'freeevolpoints':2, 'freestatspoints':1}})
        bot.send_message(user['id'], 'Поздравляем! Вы эволюционировали!')
        user=users.find_one({'id':user['id']})
        if user['lvl']==3 and user['inviter']!=None:
            users.update_one({'id':user['inviter']},{'$inc':{'maxstrenght':1}})
            bot.send_message(user['inviter'], user['gamename']+' освоился в игре! Вы получаете +1 к выносливости.')
        
            
            


    
def endrest():
    global rest
    rest=False
    
def pasekafight():
    pasekas={}
    cusers=users.find({})
    for ids in pasekalist:
        pasekas.update(createpaseka(ids))
    for ids in cusers:
        if ids['battle']['action']=='def':
            pasekas[ids['paseka']]['defers'].update({ids['id']:ids})
        elif ids['battle']['action']=='attack':
            pasekas[ids['battle']['target']]['attackers'].update({ids['id']:ids})
    
    for ids in pasekas:
        paseka=pasekas[ids]
        print(paseka)
        for idss in paseka['defers']:
            user=paseka['defers'][idss]
            defpower=user['stats']['def']
            if 'fat' in user['skills']:
                defpower+=defpower*user['skills']['fat']['lvl']*0.01
            if 'steelleather' in user['skills']:
                if random.randint(1,1000)<=user['skills']['steelleather']['lvl']*0.5*10:
                    if len(pasekas[ids]['attackers'])>0:
                        trgt=random.choice(pasekas[ids]['attackers'])
                        trgt['attack']=trgt['attack']/2
                        bot.send_message(user['id'], 'Своим жалом вы обезвредили пчолу '+trgt['gamename']+', снизив ее характеристики на 50%!')
            paseka['defpower']+=defpower
        for idss in paseka['attackers']:
            user=paseka['attackers'][idss]
            if 'sharpteeth' in user['skills']:
                user['stats']['attack']+=user['stats']['attack']*user['skills']['sharpteeth']['lvl']*0.01
            paseka['attackerspower']+=user['stats']['attack']
            
        if paseka['defpower']<paseka['attackerspower']:
            paseka['saved']=False
    text=''
    for ids in pasekas:
        paseka=pasekas[ids]
        if paseka['saved']==False:
            paseka['score']+=0
            scores=[]
            for idss in paseka['attackers']:
                atker=paseka['attackers'][idss]
                if atker['paseka'] not in scores:
                    scores.append(atker['paseka'])
                    pasekas[atker['paseka']]['score']+=3
            text+='💢'+paseka_ru(paseka['name'])+'... Пасека потерпела поражение в битве! Топ атакующих:\n'
            who='attackers'
            stat='attack'
            text+=battletext(paseka, who, stat)
            text+='Топ защитников:\n'
            who='defers'
            stat='def'
            text+=battletext(paseka, who, stat)
        else:
            paseka['score']+=8
            text+='🛡'+paseka_ru(paseka['name'])+'... Пасека отстояла свою территорию! Топ защитников:\n'
            who='defers'
            stat='def'
            text+=battletext(paseka, who, stat)
            text+='Топ атакующих:\n'
            who='attackers'
            stat='attack'
            text+=battletext(paseka, who, stat)
    text+='Начисленные очки:\n\n'
    for ids in pasekas:
        text+=paseka_ru(pasekas[ids]['name'])+' пасека: '+str(pasekas[ids]['score'])+' очков\n'
        allpasekas.update_one({'name':pasekas[ids]['name']},{'$inc':{'score':pasekas[ids]['score']}})
    users.update_many({},{'$set':{'battle.target':None, 'battle.action':None}})
    bot.send_message(officialchat, 'Результаты битвы:\n\n'+text)
            
            
         
        
def battletext(paseka, who, stat):
    top=5
    i=0
    text=''
    alreadyintext=[]
    while i<top:
        intext=None
        maxstat=0
        for idss in paseka[who]:
            user=paseka[who][idss]
            if user['stats'][stat]>maxstat and user['id'] not in alreadyintext:
                maxstat=user['stats'][stat]
                intext=user
        if intext!=None:
            alreadyintext.append(intext['id'])
            text+=intext['gamename']            
            text+=', '                            
        i+=1
    if len(paseka[who])>0:
        text=text[:len(text)-2]
        text+='.'
    text+='\n\n'
    return text
            
            
def createuser(user):
    stats={
        'attack':1,
        'def':1
    }
    battle={
        'action':None,
        'target':None
    }
    return {
        'id':user.id,
        'name':user.first_name,
        'gamename':user.first_name,
        'stats':stats,
        'paseka':None,
        'status':'free',
        'maxstrenght':8,
        'strenght':8,
        'agility':1,                     # 1 = 100%
        'battle':battle,
        'evolpoints':0,
        'lvl':1,
        'inventory':{},
        'freestatspoints':0,
        'freeevolpoints':0,
        'lastlvl':0,
        'strenghtregencoef':1,       # Чем меньше, тем лучше
        'laststrenghtregen':None,
        'recievepoints':1,                # 1 = 1 exp
        'pointmodifer':1,                 # 1 = 100%
        'referal':None,
        'changename':3,
        'skills':{}
    }

def regenstrenght(user):
    users.update_one({'id':user['id']},{'$inc':{'strenght':1}})
    users.update_one({'id':user['id']},{'$set':{'laststrenghtregen':time.time()+3*3600}})


def countnextlvl(lastlvl):
    if lastlvl!=0:
        nextlvl=int(lastlvl*2.9)
    else:
        nextlvl=10
    return nextlvl
        
def countnextpointrecieve(recievepoints):
    return recievepoints*2.1



   
def createpaseka(paseka):
    return {paseka:{
        'name':paseka,
        'defpower':0,
        'attackerspower':0,
        'defers':{},
        'attackers':{},
        'saved':True,
        'score':0
    }
           }

def timecheck():
    globaltime=time.time()+3*3600
    ctime=str(datetime.fromtimestamp(globaltime)).split(' ')[1]
    global rest
    chour=int(ctime.split(':')[0])
    cminute=int(ctime.split(':')[1])
    csecond=float(ctime.split(':')[2])
    csecond=round(csecond, 0)
    if chour in fighthours and rest==False and cminute==0:
        pasekafight()
        rest=True
        t=threading.Timer(120, endrest)
        t.start()
    for ids in users.find({}):
        user=ids
        if user['strenght']<user['maxstrenght']:
            if user['laststrenghtregen']==None:
                regenstrenght(user)
            elif globaltime>=user['laststrenghtregen']+20*60*user['strenghtregencoef']:
                regenstrenght(user)
    if csecond==0:
        global britmsgs
        britmsgs=0
        global ban
        ban=[]
    t=threading.Timer(1, timecheck)
    t.start()
    

timecheck()
    
    
users.update_many({},{'$set':{'status':'free'}})
print('7777')
bot.polling(none_stop=True,timeout=600)
