# trying to fuck dyno hours in heroku

import os
import telebot
import time
import telebot
import random
import threading
from emoji import emojize
from telebot import types
from pymongo import MongoClient
from emoji import emojize
from requests.exceptions import ReadTimeout
from requests.exceptions import ConnectionError

pokewars_token = os.environ['pokewars_token']
pokewars = telebot.TeleBot(pokewars_token)
bot = pokewars
trigger_token = os.environ['trigger_token']
triggerbot = telebot.TeleBot(trigger_token)
mongo_http=os.environ['mongo_http']
client = MongoClient(mongo_http)
db = client.pokewars
users = db.users
chats = db.chats
vip = [512006137]
brit_id=512006137
games = {}
skills = []
timerss = {}
ban = []
timers = []
idlist=[]
testtriggers={}
i = 0
lol = 0
testmod=0
pokeban = []
symbollist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z',
              'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
              'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я',
              '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
def medit(message_text, chat_id, message_id, reply_markup=None, parse_mode='Markdown'):
    return bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=message_text, reply_markup=reply_markup,
                                 parse_mode=parse_mode)
triggers= {'лошадкин': '@loshadkin', 'соси': 'как Булат', 'бот упал': '@LOSHADKIN ИДИ ЧИНИТЬ БОТА, ХВАТИТ ДРОЧИТЬ', 'loshadkin': '@loshadkin', 'ваши покемоны': 'это ваши покемоны', 'sasatt': 'lezhat', 'сасать член': 'пасюка', 'булат': 'сосатт', 'бт': 'плясатт', 'бизарр': 'лучшая тима', 'bulat': 'sosatt', 'ослик': 'сосет у себя', 'пасюк': 'пидор', 'слава': ' СЛАВА УКРАИНЕ ГЕРОЯМ СЛАВА', 'россия': 'сасатт', 'аниме': 'Ты что смотришь аниме? Соси хуй тогда🍆', 'винко': 'Уберите этого говноеда от меня, блядб', 'huntall': 'Все равно они не придут', 'нет': 'пидора ответ', 'да': 'пизда', 'бунт': 'CAADAgADDwADIcYAARAiXXInVZNiUAI', 'не приходят': 'CAADAgADDgYAAiVUQBNcQhf8905GbwI', 'кто': 'CAADAQADSgIAAtg_5wk5IXNJogXh9gI', 'дизайнер': 'CAADAgADCAADIcYAARBfFBmUxB9V3gI', 'украин': 'CAADAgADFgADIcYAARAPkK3cV1pXTwI', 'монга': '@gbball', 'brit': '@gbball', 'аргумент': 'аргумент не нужен пидор обнаружен', 'пидор обнаружен': 'Пидор засекречен твой анал не вечен', 'твоя': 'твоя', 'моя': 'головка от хуя'}


#-----------Release-Code------------------
@triggerbot.message_handler(commands=['gettriggers'])
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
    triggerbot.send_message(m.chat.id, text)  
@triggerbot.message_handler(commands=['addtrigger'])
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
        triggerbot.send_message(message.chat.id, '@gbball новый триггер ебать иди копируй в код ты же ебан монгу не можешь юзать ггагагга')
    except:
        triggerbot.send_message(message.chat.id, 'Триггер добавляется так:\nтекст/ответ(айди стикера, текст)')
@triggerbot.message_handler(commands=['deltrigger']) 
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

@triggerbot.message_handler(content_types=["text"])
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
                triggerbot.send_sticker(message.chat.id, tts, reply_to_message_id = message.message_id)
                i = 1
            except:
                report(message)
            if i != 1:
                triggerbot.send_message(message.chat.id, tts, reply_to_message_id = message.message_id)
            else:
                pass
            lol = 300
        else:
            pass


#SUKA ACHKO RAZDELITEL-------------------------------------------------------------
@pokewars.message_handler(commands=['evol'])
def evol(m):
    if m.from_user.id == brit_id:  
        txt = m.text.split(' ', 1)
        eval(txt)
@pokewars.message_handler(commands=['pokerub'])
def poketyigfh(m):
    users.update_one({'id': brit_id}, {'$set': {'pokemons2.rubenis': createruby('rubenis', 0)}})

@pokewars.message_handler(commands=['update'])
def spammm(m):
    if m.from_user.id == brit_id:
        #   users.update_many({},{'$set':{'ruby':0}})
        # users.update_many({},{'$set':{'pokemons2':{}}})
        x = users.find({})
        for ids in x:
            for idss in ids['pokemons']:
                try:
                    zzz = ids['pokemons'][idss]['golden']
                except:
                    users.update_one({'id': ids['id']}, {'$unset': {'pokemons.' + idss: 1}})
        print('yes')
 

@pokewars.message_handler(commands=['pokemon'])
def statssss(m):
    kb = types.InlineKeyboardMarkup()
    x = users.find_one({'id': m.from_user.id})
    if x != None:
        for ids in x['pokemons']:
            kb.add(types.InlineKeyboardButton(text=pokemons[ids]['name'],
                                              callback_data=str(m.from_user.id) + ' stats' + ids))
        for ids in x['pokemons2']:
            kb.add(types.InlineKeyboardButton(text=rubypokemons[ids]['name'],
                                              callback_data=str(m.from_user.id) + ' stats' + ids))
        pokewars.send_message(m.chat.id, m.from_user.first_name + ', Статы какого покемона хотите посмотреть?',
                         reply_markup=kb)
    else:
        pokewars.send_message(m.chat.id, 'Ошибка!')
                              

@pokewars.message_handler(commands=['tests'])
def tests(m):
    if m.from_user.id == brit_id:
        i = 0
        z = 0
        x = 400000
        while i < x:
            i += 1
            z += 2
            g = random.randint(1, 100)
            if g != 1:
                i -= 1
        print(z)


def huntt(id, chatid, pokemon):
    x = users.find_one({'id': id})
    if pokemon not in rubypokes:
        earned = 0
        i = 0
        try:
            zz = x['pokemons'][pokemon]['golden']
            i = 1
        except:
            pass
        if i == 1:
            users.update_one({'id': id}, {'$set': {'pokemons.' + pokemon + '.hunting': 0}})
        i = 0
        chances = 0
        win = 0
        pokemon = x['pokemons'][pokemon]
        print(pokemon)
        while i < pokemon['cool']:
            i += 1
            chances += 1
            z = random.randint(1, 100)
            if z <= 30 + (pokemon['atk'] * 2):
                win += 1
                earned += 1
            z = random.randint(1, 100)
            if z <= 5 + pokemon['agility']:
                earned += 1
            z = random.randint(1, 100)
            if pokemon['def'] >= 100:
                pokemon['def'] = 99
            if z <= pokemon['def']:
                i -= 1
        z = random.randint(1, 100)
        level = 'нет'
        if z <= 100:
            if pokemon['golden'] == 1:
                earned = earned * 2
                level = 'да'
        pupa = ''
        if pokemon['code'] == 'pupa':
            f = random.randint(1, 100)
            if f <= 35:
                earned += 25000
                pupa = 'Пупа и Лупа ходили за голдой. Но Пасюк перепутал их крутость, и Лупа принес голду за Пупу, а Пупа ЗА ЛУПУ!!! Получено 25к голды.'
        pokewars.send_message(chatid, 'Покемон ' + pokemon['name'] + ' пользователя ' + x[
            'name'] + ' вернулся с охоты!\nПринесённое золото: ' + str(earned) + '\n' +
                         'Умножено ли золото на 2 (только для золотых): ' + level + '\n' + pupa)
        users.update_one({'id': id}, {'$inc': {'money': earned}})

    else:
        earned = 0
        i = 0
        try:
            zz = x['pokemons2'][pokemon]['golden']
            i = 1
        except:
            pass
        if i == 1:
            users.update_one({'id': id}, {'$set': {'pokemons2.' + pokemon + '.hunting': 0}})
        i = 0
        pokemon = x['pokemons2'][pokemon]
        print(pokemon)
        while i < (pokemon['atk'] + int(pokemon['cool'] / 1000)):
            i += 1
            z = random.randint(1, 100)
            if z <= 25 + pokemon['agility']:
                earned += 1
            z = random.randint(1, 100)
            if z <= pokemon['def']:
                i -= 1
        z = random.randint(1, 100)
        level = 'нет'
        if z <= 100:
            if pokemon['golden'] == 1:
                earned = earned * 2
                level = 'да'
        v = random.randint(1, 100)
        gold = 0
        if v <= 20:
            gold = earned * 100000

        pokewars.send_message(chatid, 'Покемон ' + pokemon['name'] + ' пользователя ' + x[
            'name'] + ' вернулся с охоты!\nПринесённые рубины: ' + str(earned) + '\n' + 'Принесённое золото: ' + str(
            int(gold / 1000)) + 'к\n'
                                'x2: ' + level)
        users.update_one({'id': id}, {'$inc': {'ruby': earned}})
        users.update_one({'id': id}, {'$inc': {'money': gold}})
            

@pokewars.message_handler(commands=['huntal'])
def huntallll(m):
    if m.from_user.id not in ban:
        x = banns(m.from_user.id, m.from_user.id, m.from_user.first_name)
        if x == 0:
            x = users.find_one({'id': m.from_user.id})
            if x != None:
                pisos=[]
                for ids in x['pokemons']:
                    if x['pokemons'][ids]['hunting'] == 0:
                        users.update_one({'id': m.from_user.id}, {'$set': {'pokemons.' + ids + '.hunting': 1}})
                        t = threading.Timer(1800, huntt, args=[m.from_user.id, m.from_user.id, ids])
                        t.start()
                        pisos.append(x['pokemons'][ids]['code'])
                for ids2 in x['pokemons2']:
                    if x['pokemons2'][ids2]['hunting'] == 0:
                        users.update_one({'id': m.from_user.id}, {'$set': {'pokemons2.' + ids2 + '.hunting': 1}})
                        t = threading.Timer(1800, huntt, args=[m.from_user.id, m.from_user.id, ids2])
                        t.start()
                        pisos.append(x['pokemons'][ids]['code'])
                if len(pisos) > 0:        
                    pokewars.send_message(m.chat.id, 'Вы отправили всех готовых покемонов на охоту. Вернутся через 30 минут.')
                else:
                    pokewars.send_message(m.chat.id, 'Все покемоны уже на охоте!')

@pokewars.message_handler(commands=['testhuntal'])
def huntallll(m):
    if m.from_user.id == brit_id:
        x = users.find_one({'id': m.from_user.id})
        if x != None:
            for ids in x['pokemons']:
                if x['pokemons'][ids]['hunting'] == 0:
                    users.update_one({'id': m.from_user.id}, {'$set': {'pokemons.' + ids + '.hunting': 1}})
                    t = threading.Timer(10, huntt, args=[m.from_user.id, m.from_user.id, ids])
                    t.start()
                    pisos.append(x['pokemons'][ids]['code'])
            for ids2 in x['pokemons2']:
                if x['pokemons2'][ids2]['hunting'] == 0:
                    users.update_one({'id': m.from_user.id}, {'$set': {'pokemons2.' + ids2 + '.hunting': 1}})
                    t = threading.Timer(10, huntt, args=[m.from_user.id, m.from_user.id, ids2])
                    t.start()
                    pisos.append(x['pokemons'][ids]['code'])
            if len(pisos) > 0:        
                pokewars.send_message(m.chat.id, 'Вы отправили всех готовых покемонов на охоту. Вернутся через 10 сек.')
            else:
                pokewars.send_message(m.chat.id, 'Все покемоны уже на охоте!')


@pokewars.message_handler(commands=['mygold'])
def goldd(m):
    x = users.find_one({'id': m.from_user.id})
    if x != None:
        pokewars.send_message(m.chat.id,
                         m.from_user.first_name + ', ваше золото: ' + str(x['money']) + '\nРубины: ' + str(x['ruby']))


@pokewars.message_handler(commands=['suckdick'])
def suckdick(m):
    if m.from_user.id not in ban:
        x = banns(m.from_user.id, m.chat.id, m.from_user.first_name)
        if x == 0:
            try:
                users.update_one({'id': m.from_user.id}, {'$inc': {'money': -1}})
                bot.send_message(m.chat.id, 'Вы успешно отсосали хуйца и потратили 1 монету.')
                z = random.randint(1, 100)
                if z <= 1:
                    pokewars.send_message(m.chat.id, 'Ебаный рот этого казино блять!')
            except:
                pass


@pokewars.message_handler(commands=['gextra'])
def gextra(m):
    if m.from_user.id == brit_id:
        gold = 1
        if gold == 1:
            gold = '(золотой!!!) '
            pokemon = 'gold'
        else:
            gold = ''
            pokemon = ''
        i = 0
        for ids in pokemons:
            i += 1
        pokechance = 40 / (i * 0.06)
        come = []
        for ids in elita:
            come.append(ids)
        if len(come) > 0:
            poke = random.choice(come)
        else:
            poke = random.choice(basepokes)
        kb = types.InlineKeyboardMarkup()
        kb.add(types.InlineKeyboardButton(text='Поймать', callback_data=pokemon + poke))
        me = pokewars.send_message(m.chat.id,
                             'Обнаружен *' + gold + '*покемон ' + pokemons[poke]['name'] + '! Его крутость: ' + str(
                                 pokemons[poke]['cool']) + '. Жмите кнопку ниже, чтобы попытаться поймать.',
                             reply_markup=kb, parse_mode='markdown')
        pokewars.pin_chat_message(me.chat.id, me.message_id, disable_notification=True)
@pokewars.message_handler(commands=['extra'])
def extra(m):
    if m.from_user.id == brit_id:
        gold = 1
        if gold == 1:
            gold = '(золотой!!!) '
            pokemon = 'gold'
        else:
            gold = ''
            pokemon = ''
        i = 0
        for ids in pokemons:
            i += 1
        pokechance = 40 / (i * 0.06)
        come = []
        for ids in elita:
            come.append(ids)
        if len(come) > 0:
            poke = random.choice(come)
        else:
            poke = random.choice(basepokes)
        kb = types.InlineKeyboardMarkup()
        kb.add(types.InlineKeyboardButton(text='Поймать', callback_data=pokemon + poke))
        me = pokewars.send_message(m.chat.id,
                             'Обнаружен *' + gold + '*покемон ' + pokemons[poke]['name'] + '! Его крутость: ' + str(
                                 pokemons[poke]['cool']) + '. Жмите кнопку ниже, чтобы попытаться поймать.',
                             reply_markup=kb, parse_mode='markdown')
        pokewars.pin_chat_message(me.chat.id, me.message_id, disable_notification=True)
@pokewars.message_handler(commands=['hunt'])
def hunt(m):
    if m.from_user.id not in ban:
        x = banns(m.from_user.id, m.chat.id, m.from_user.first_name)
        if x == 0:
            kb = types.InlineKeyboardMarkup()
            x = users.find_one({'id': m.from_user.id})
            if x != None:
                for ids in x['pokemons']:
                    if x['pokemons'][ids]['hunting'] != 1:
                        kb.add(types.InlineKeyboardButton(text=pokemons[ids]['name'],
                                                          callback_data=str(m.from_user.id) + ' earn' + ids))
                pokewars.send_message(m.chat.id, m.from_user.first_name + ', какого покемона вы хотите отправить на охоту?',
                                 reply_markup=kb)
            else:
                pokewars.send_message(m.chat.id, 'Ошибка!')


@pokewars.message_handler(commands=['gфve'])
def give(m):
    if m.from_user.id == brit_id:
        x = m.text.split(' ')
        try:
            golden = ''
            i = 0
            if len(x) > 2:
                if x[2] == 'gold':
                    golden = '*золотой* '
                    i = 1
            users.update_one({'id': m.reply_to_message.from_user.id},
                             {'$set': {'pokemons.' + x[1]: createpoke(x[1], i)}})
            pokewars.send_message(m.chat.id, 'Покемон ' + golden + pokemons[x[1]]['name'] + ' успешно выдан!',
                             parse_mode='markdown')
        except:
            pass


def banns(id, chatid, name):
    i = 0
    for ids in timerss:
        if timerss[ids]['id'] == id:
            i = 1
    if i == 0:
        print('1')
        timerss.update({id: {'id': id,
                             'messages': 0}})
        t = threading.Timer(15, unwarn, args=[id])
        t.start()
    else:
        print('2')
        timerss[id]['messages'] += 1
        if timerss[id]['messages'] >= 4:
            if id not in ban:
                pokewars.send_message(chatid, 'Пользователь ' + name + ' много спамил и был заблокирован на 20 секунд.')
            ban.append(id)
            tt = threading.Timer(20, unbannn, args=[id])
            tt.start()
            print(ban)
            return 1
    return 0


def unwarn(id):
    try:
        del timerss[id]
        print('UNWARN!!!!!')
    except:
        pass


def unbannn(id):
    print('unbanlaunch')
    try:
        ban.remove(id)
        print('UNBAN!')
    except:
        pass


pokemonlist = eval(os.environ['pokemonlist'])

basepokes = eval(os.environ['basepokes'])

elita = ['pikachu', 'pedro', 'bulbazaur', 'psyduck', 'moxnatka', 'charmander', 'diglet', 'golem', 'sidot', 'traxer',
         'tyxlomon', 'morzh',
         'penisdetrov', 'gandonio', 'spermostrel', 'yebator', 'egg', 'graveler', 'tirog', 'eldro4illo', 'vyper',
         'sizor', 'myavs', 'bulatpidor', 'ebusobak',
         'slagma', 'pupa', 'lupa']

elitaweak = ['moxnatka', 'diglet', 'traxer', 'penis', 'gandonio', 'egg', 'sizor', 'ebusobak', 'ultrapoke']

rubypokes = ['rubenis', 'crystaler', 'blyadomon', 'moldres', 'pupitar', 'aron', 'sfil']

pokemons = eval(os.environ['pokemons'])
rubypokemons = eval(os.environ['rubypokemons'])


# @pokewars.message_handler(commands=['evolve'])
# def evolve(m):
#    x=users.find_one({'id':m.from_user.id})
#    if x!=None:
#     if x['money']>=500:
#      kb=types.InlineKeyboardMarkup()
#      for ids in x['pokemons']:
#        kb.add(types.InlineKeyboardButton(text=pokemons[ids]['name'], callback_data=str(m.from_user.id)+' evolve'+ids))
#      pokewars.send_message(m.chat.id, m.from_user.first_name+', какого покемона вы хотите попытаться эволюционировать? Цена: 500 голды. Шанс: 15%.', reply_markup=kb)


@pokewars.message_handler(commands=['upgrade'])
def upgradee(m):
    word = m.text.split('"')
    if len(word) != 3:
        x = users.find_one({'id': m.from_user.id})
        if x != None:
            if x['money'] >= 200:
                kb = types.InlineKeyboardMarkup()
                star = emojize(':star:', use_aliases=True)
                for ids in x['pokemons']:
                    gold = ''
                    if x['pokemons'][ids]['golden'] == 1:
                        gold = ' (' + star + ')'
                    kb.add(types.InlineKeyboardButton(text=pokemons[ids]['name'] + gold,
                                                      callback_data=str(m.from_user.id) + ' upgrade' + ids))
                for ids in x['pokemons2']:
                    kb.add(types.InlineKeyboardButton(text=rubypokemons[ids]['name'] + ' (♦️)',
                                                      callback_data=str(m.from_user.id) + ' upgrade' + ids))
                pokewars.send_message(m.chat.id,
                                 m.from_user.first_name + ', какого покемона вы хотите попытаться улучшить? Цена: 200 голды + крутость покемона/3. Шанс: 40%.',
                                 reply_markup=kb)
            else:
                pokewars.send_message(m.chat.id, 'Недостаточно золота!')
        else:
            pokewars.send_message(m.chat.id, 'Ошибка!')
    else:
        x = users.find_one({'id': m.from_user.id})
        if x != None:
            try:
                yes = 0
                print(word[1])
                for ids in x['pokemons']:
                    if word[1] == x['pokemons'][ids]['name']:
                        yes = 1
                        number = ''
                        pokemon = ids
                if yes == 0:
                    for ids in x['pokemons2']:
                        if word[1] == x['pokemons2'][ids]['name']:
                            yes = 1
                            number = '2'
                            pokemon = ids
                if yes != 0:
                    print('yes!=0')
                    if number == '':
                        cost = int(200 + (x['pokemons' + number][pokemon]['cool'] / 3))
                    elif number == '2':
                        cost = int(15 + (x['pokemons' + number][pokemon]['cool'] / 1000))
                    z = int(word[2])
                    i = 0
                    if z > 100:
                        bot.send_message(m.chat.id, 'Больше ста нельзя, сасамба!')
                        return
                    finalcost = 0
                    while i < z:
                        i += 1
                        finalcost += cost
                    if number == '':
                        zz = 'money'
                        constt = 40
                        valuta = 'голды'
                    elif number == '2':
                        zz = 'ruby'
                        constt = 60
                        valuta = 'рубинов'
                    if x[zz] >= finalcost:
                        i = 0
                        atk = 0
                        deff = 0
                        agility = 0
                        cool = 0
                        success = 0
                        while i < z:
                            i += 1
                            g = random.randint(1, 100)
                            bonus = 0
                            abc = ['atk', 'def', 'agility', 'cool']
                            attribute = random.choice(abc)
                            if attribute == 'atk':
                                bonus = random.randint(1, 2)
                                name = 'Атака'

                            elif attribute == 'def':
                                bonus = random.randint(2, 3)
                                name = 'Защита'

                            elif attribute == 'agility':
                                bonus = random.randint(2, 3)
                                name = 'Ловкость'

                            elif attribute == 'cool':
                                if number == '':
                                    bonus = random.randint(5, 15)
                                elif number == '2':
                                    bonus = random.randint(200, 800)
                                name = 'Крутость'

                            if g <= constt:
                                success += 1
                                if attribute == 'atk':
                                    atk += bonus
                                elif attribute == 'def':
                                    deff += bonus
                                elif attribute == 'agility':
                                    agility += bonus
                                elif attribute == 'cool':
                                    cool += bonus
                        users.update_one({'id': m.from_user.id},
                                         {'$inc': {'pokemons' + number + '.' + pokemon + '.' + 'atk': atk}})
                        users.update_one({'id': m.from_user.id},
                                         {'$inc': {'pokemons' + number + '.' + pokemon + '.' + 'def': deff}})
                        users.update_one({'id': m.from_user.id},
                                         {'$inc': {'pokemons' + number + '.' + pokemon + '.' + 'agility': agility}})
                        users.update_one({'id': m.from_user.id},
                                         {'$inc': {'pokemons' + number + '.' + pokemon + '.' + 'cool': cool}})
                        pokewars.send_message(m.chat.id, 'Вы улучшили покемона ' + word[1] + ' ' + str(
                            z) + ' раз! Из них успешных попыток было ' + str(
                            success) + '. Улучшенные характеристики:\n' +
                                         'Крутость: ' + str(cool) + '\nАтака: ' + str(atk) + '\nЗащита: ' + str(
                            deff) + '\nЛовкость: ' + str(agility) + '\n\nПотрачено ' + str(
                            finalcost) + ' ' + valuta + '.')
                        users.update_one({'id': m.from_user.id}, {'$inc': {zz: -finalcost}})
                    else:
                        pokewars.send_message(m.chat.id, 'Недостаточно ' + valuta + '! (нужно ' + str(finalcost) + ')')
                else:
                    pokewars.send_message(m.chat.id, 'not')
            except:
                pass


@bot.message_handler(commands=['sellpoke'])
def sellpoke(m):
    x = users.find_one({'id': m.from_user.id})
    if x != None:
        kb = types.InlineKeyboardMarkup()
        for ids in x['pokemons']:
            kb.add(types.InlineKeyboardButton(text=pokemons[ids]['name'],
                                              callback_data=str(m.from_user.id) + ' sell' + ids))
        bot.send_message(m.chat.id,
                         m.from_user.first_name + ', какого покемона вы хотите продать? Цена=крутость покемона*5 (если золотой, то *50).',
                         reply_markup=kb)
    else:
        bot.send_message(m.chat.id, 'Ошибка!')


@bot.message_handler(commands=['givegold'])
def givegoldd(m):
    x = m.text.split(' ')
    try:
        golden = ''
        i = 0
        if len(x) == 2:
            gold = int(x[1])
            if gold > 0:
                y = users.find_one({'id': m.from_user.id})
                if y != None:
                    if y['money'] >= gold:
                        users.update_one({'id': m.reply_to_message.from_user.id}, {'$inc': {'money': gold}})
                        users.update_one({'id': m.from_user.id}, {'$inc': {'money': -gold}})
                        bot.send_message(m.chat.id, 'Вы успешно передали ' + str(
                            gold) + ' золота игроку ' + m.reply_to_message.from_user.first_name + '!',
                                         parse_mode='markdown')
                    else:
                        bot.send_message(m.chat.id, 'Недостаточно золота!')
                else:
                    bot.send_message(m.chat.id, 'Ошибка!')
            else:
                bot.send_message(m.chat.id, 'Введите число больше нуля!')
    except:
        pass

@bot.message_handler(commands=['ggold'])
def givegolddd(m):
    if m.from_user.id == 512006137:
        pass
    else:
        return
    x = m.text.split(' ')
    try:
        golden = ''
        i = 0
        if len(x) == 2:
            gold = int(x[1])
            if True:
                y = users.find_one({'id': m.from_user.id})
                if y != None:
                    if True:
                        users.update_one({'id': m.reply_to_message.from_user.id}, {'$inc': {'money': gold}})
                        bot.send_message(m.chat.id, 'Выдано ' + str(
                            gold) + ' золота игроку ' + m.reply_to_message.from_user.first_name + '!',
                                         parse_mode='markdown')
                    else:
                        bot.send_message(m.chat.id, 'Недостаточно золота!')
                else:
                    bot.send_message(m.chat.id, 'Ошибка!')
            else:
                bot.send_message(m.chat.id, 'Введите число больше нуля!')
    except:
        pass
@bot.message_handler(commands=['buyruby'])
def traderuby(m):
    x = users.find_one({'id': m.from_user.id})
    if x != None:
        y = m.text.split(' ')
        if len(y) == 2:
            try:
                ruby = int(y[1])
                if ruby > 0:
                    i = ruby * 100000
                    if x['money'] >= i:
                        users.update_one({'id': m.from_user.id}, {'$inc': {'money': -i}})
                        users.update_one({'id': m.from_user.id}, {'$inc': {'ruby': ruby}})
                        bot.send_message(m.chat.id, 'Вы успешно обменяли ' + str(int(i / 1000)) + 'к золота на ' + str(
                            ruby) + ' рубин(ов)!')
                    else:
                        bot.send_message(m.chat.id, 'Недостаточно золота! (курс: 100к золота за 1 рубин).')
                else:
                    bot.send_message(m.chat.id, 'Введите число больше нуля!')
            except:
                bot.send_message(m.chat.id, 'Неверный формат!')


@bot.message_handler(commands=['pokeshop'])
def pokeshopp(m):
    kb = types.InlineKeyboardMarkup()
    for ids in rubypokes:
        kb.add(types.InlineKeyboardButton(
            text=rubypokemons[ids]['name'] + ' (цена: ' + str(rubypokemons[ids]['cost']) + '♦️)',
            callback_data=str(m.from_user.id) + ' buy' + ids))
    bot.send_message(m.chat.id, 'Какого покемона вы хотите приобрести?', reply_markup=kb)


@bot.message_handler(commands=['top'])
def toppp(m):
    x = users.find({})
    cool1 = 0
    cool2 = 0
    cool3 = 0
    top2 = {'name': 'Не определено'}
    top3 = {'name': 'Не определено'}
    for ids in x:
        if ids['id'] != brit_id:
            summ1 = 0
            for idss in ids['pokemons']:
                summ1 += ids['pokemons'][idss]['cool']
            for idsss in ids['pokemons2']:
                summ1 += ids['pokemons2'][idsss]['cool']
            if summ1 > cool1:
                cool1 = summ1
                top1 = ids
    x = users.find({})
    for ids2 in x:
        if ids2['id'] != brit_id:
            summ2 = 0
            for idss2 in ids2['pokemons']:
                summ2 += ids2['pokemons'][idss2]['cool']
            for idsss2 in ids2['pokemons2']:
                summ2 += ids2['pokemons2'][idsss2]['cool']
            if summ2 > cool2 and summ2 != cool1:
                cool2 = summ2
                top2 = ids2
    x = users.find({})
    for ids3 in x:
        if ids3['id'] != brit_id:
            summ3 = 0
            for idss3 in ids3['pokemons']:
                summ3 += ids3['pokemons'][idss3]['cool']
            for idsss3 in ids3['pokemons2']:
                summ3 += ids3['pokemons2'][idsss3]['cool']
            if summ3 >= cool3 and summ3 != cool2 and summ3 != cool1:
                cool3 = summ3
                top3 = ids3

    bot.send_message(m.chat.id,
                     'Топ-3 по крутости:\n\n' + '1 место: ' + top1['name'] + ' - ' + str(cool1) + '\n' + '2 место: ' +
                     top2['name'] + ' - ' + str(cool2) + '\n' + '3 место: ' + top3['name'] + ' - ' + str(cool3) + '\n')


@bot.message_handler(commands=['upchance'])
def upchance(m):
    x = users.find_one({'id': m.from_user.id})
    if x != None:
        z = int((x['chancetocatch'] * 200000) + 20000)
        if x['money'] >= z:
            users.update_one({'id': m.from_user.id}, {'$inc': {'money': -z}})
            users.update_one({'id': m.from_user.id}, {'$inc': {'chancetocatch': 0.1}})
            bot.send_message(m.chat.id, 'Вы потратили ' + str(z) + ' золота. Шанс поймать покемона увеличен на 10%.')
        else:
            bot.send_message(m.chat.id, 'Не хватает золота (нужно ' + str(z) + ').')


@bot.message_handler(commands=['createteam'])
def createteam(m):
    pass


@bot.message_handler(commands=['jointeam'])
def jointeam(m):
    pass


@bot.message_handler(commands=['summon'])
def summon(m):
    # if m.from_user.id not in ban:
    #   x=banns(m.from_user.id, m.from_user.id, m.from_user.first_name)
    #   if x==0:
    y = users.find_one({'id': m.from_user.id})
    if y['money'] >= 100:
        x = random.randint(1, 100)
        users.update_one({'id': y['id']}, {'$inc': {'money': -100}})
        if x <= 20:
            bot.send_message(m.chat.id, 'Вы потратили 100 монет. Вам удалось призвать покемона!!!')
            poke(m.chat.id)
        else:
            bot.send_message(m.chat.id, 'Вы потратили 100 монет. Вам не удалось призвать покемона.')
    else:
        bot.send_message(m.chat.id, 'Недостаточно золота!')


def poke(id):
    gold = random.randint(1, 100)
    if gold == 1:
        gold = '(золотой!!!) '
        pokemon = 'gold'
    else:
        gold = ''
        pokemon = ''
    i = 0
    for ids in elita:
        i += 1
    pokechance = 50 / (i * 0.06)
    come = []
    for ids in elita:
        chance = pokechance / (pokemons[ids]['cool'] * 0.02)
        x = random.randint(1, 100)
        if x <= chance:
            come.append(ids)
    if len(come) > 0:
        poke = random.choice(come)
    else:
        poke = random.choice(elitaweak)
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton(text='Поймать', callback_data=pokemon + poke))
    m = bot.send_message(id, 'Обнаружен *' + gold + '*покемон ' + pokemons[poke]['name'] + '! Его крутость: ' + str(
        pokemons[poke]['cool']) + '. Жмите кнопку ниже, чтобы попытаться поймать.', reply_markup=kb,
                         parse_mode='markdown')
    t = threading.Timer(random.randint(300, 600), runpoke, args=[m.message_id, m.chat.id])
    t.start()
    timers.append('1')
    try:
        bot.pin_chat_message(m.chat.id, m.message_id, disable_notification=False)
    except:
        pass


def dailypoke(id):
    x = random.randint(300, 301)
    t = threading.Timer(x, dailypoke, args=[id])
    t.start()
    gold = random.randint(1, 100)
    if gold == 1:
        gold = '(золотой!!!) '
        pokemon = 'gold'
    else:
        gold = ''
        pokemon = ''
    i = 0
    for ids in pokemons:
        i += 1
    pokechance = 95 / (i * 0.06)
    come = []
    for ids in pokemonlist:
        chance = pokechance / (pokemons[ids]['cool'] * 0.01)
        x = random.randint(1, 100)
        if x <= chance:
            come.append(ids)
    if len(come) > 0:
        poke = random.choice(come)
    else:
        poke = random.choice(basepokes)
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton(text='Поймать', callback_data=pokemon + poke))
    m = bot.send_message(id, 'Обнаружен *' + gold + '*покемон ' + pokemons[poke]['name'] + '! Его крутость: ' + str(
        pokemons[poke]['cool']) + '. Жмите кнопку ниже, чтобы попытаться поймать.', reply_markup=kb,
                         parse_mode='markdown')
    t = threading.Timer(random.randint(300, 600), runpoke, args=[m.message_id, m.chat.id])
    t.start()
    timers.append('1')
    bot.pin_chat_message(m.chat.id, m.message_id, disable_notification=False)


def runpoke(mid, cid):
    medit('Время на поимку покемона вышло.', cid, mid)


@bot.message_handler(commands=['pokes'])
def pokesfgtd(m):
    if m.from_user.id not in ban:
        x = banns(m.from_user.id, m.chat.id, m.from_user.first_name)
        if x == 0:
            x = users.find_one({'id': m.from_user.id})
            if x != None:
                text = ''
                for ids in x['pokemons']:
                    if x['pokemons'][ids]['golden'] == 1:
                        text += '*Золотой* '
                    text += x['pokemons'][ids]['name'] + ' - крутость: ' + str(x['pokemons'][ids]['cool']) + '\n'
                for ids in x['pokemons2']:
                    if x['pokemons2'][ids]['golden'] == 1:
                        text += '*Золотой* '
                    text += x['pokemons2'][ids]['name'] + ' - крутость: ' + str(x['pokemons2'][ids]['cool']) + '\n'
                bot.send_message(m.chat.id, 'Ваши покемоны:\n\n' + text, parse_mode='markdown')
            else:
                bot.send_message(m.chat.id, 'Сначала напишите в чат что-нибудь (не команду!).')


def rebootclick():
    global notclick
    notclick = 0


@bot.callback_query_handler(func=lambda call: True)
def inline(call):
    global notclick
    if notclick == 0:
        if 'earn' not in call.data and 'upgrade' not in call.data and 'sell' not in call.data and 'buy' not in call.data and 'stats' not in call.data:
            notclick = 1
            t = threading.Timer(3, rebootclick)
            t.start()
            if call.from_user.id not in pokeban:
                x = users.find_one({'id': call.from_user.id})
                if x != None:
                    text = call.data
                    golden = 0
                    if call.data[0] == 'g' and call.data[1] == 'o' and call.data[2] == 'l' and call.data[3] == 'd':
                        text = call.data[4:]
                        golden = 1
                    chancetocatch = (100 * (x['chancetocatch'] + 1)) / (pokemons[text]['cool'] * 0.03)
                    z = random.randint(0, 100)
                    if z <= chancetocatch:
                        i = 0
                        for ids in x['pokemons']:
                            print(x['pokemons'][ids])
                            if x['pokemons'][ids]['code'] == text:
                                i = 1
                        if i != 1:
                            givepoke(call.data, call.message.chat.id, call.message.message_id,
                                     call.from_user.first_name, call.from_user.id)
                            try:
                                timers.remove('1')
                            except:
                                pass
                        else:
                            if golden == 1 and x['pokemons'][text]['golden'] == 0:
                                users.update_one({'id': call.from_user.id},
                                                 {'$set': {'pokemons.' + text + '.golden': 1}})
                                medit('Покемона *Золотой* ' + pokemons[text][
                                    'name'] + ' поймал ' + call.from_user.first_name + '! Данный покемон у него уже был, ' +
                                      'но обычный. Теперь он стал золотым!', call.message.chat.id,
                                      call.message.message_id, parse_mode='markdown')
                                timers.remove('1')
                            else:
                                bot.answer_callback_query(call.id, 'У вас уже есть этот покемон!')
                    else:
                        pokeban.append(call.from_user.id)
                        t = threading.Timer(60, unban, args=[call.from_user.id])
                        t.start()
                        bot.send_message(call.message.chat.id,
                                         'Пользователю ' + call.from_user.first_name + ' не удалось поймать покемона!')
                else:
                    bot.answer_callback_query(call.id, 'Сначала напишите в чат что-нибудь (не команду!).')
            else:
                bot.answer_callback_query(call.id, 'Подождите минуту для ловли следующего покемона!')
        elif 'earn' in call.data:
            text = call.data.split(' ')
            if int(text[0]) == call.from_user.id:
                x = users.find_one({'id': call.from_user.id})
                text = text[1]
                text = text[4:]
                if x['pokemons'][text]['hunting'] == 0:
                    users.update_one({'id': call.from_user.id}, {'$set': {'pokemons.' + text + '.hunting': 1}})
                    medit('Вы отправили покемона ' + pokemons[text]['name'] + ' на охоту. Он вернётся через пол часа.',
                          call.message.chat.id, call.message.message_id)
                    t = threading.Timer(1800, huntt, args=[call.from_user.id, call.from_user.id, text])
                    t.start()
                else:
                    medit('Покемон уже на охоте!', call.message.chat.id, call.message.message_id)
            else:
                bot.answer_callback_query(call.id, 'Это не ваше меню!')
        elif 'stats' in call.data:
            text = call.data.split(' ')
            if int(text[0]) == call.from_user.id:
                x = users.find_one({'id': call.from_user.id})
                text = text[1]
                text = text[5:]
                r = ''
                if text in rubypokes:
                    r = '2'
                medit(x['name'] + ', статы покемона ' + x['pokemons' + r][text]['name'] + ':\nКрутость: ' + str(
                    x['pokemons' + r][text]['cool']) + '\nАтака: ' + str(x['pokemons' + r][text]['atk']) + '\n' +
                      'Защита: ' + str(x['pokemons' + r][text]['def']) + '\nЛовкость: ' + str(
                    x['pokemons' + r][text]['agility']), call.message.chat.id, call.message.message_id)
            else:
                bot.answer_callback_query(call.id, 'Это не ваше меню!')
        elif 'sell' in call.data:
            text = call.data.split(' ')
            if int(text[0]) == call.from_user.id:
                x = users.find_one({'id': call.from_user.id})
                text = text[1]
                text = text[4:]
                try:
                    gold = x['pokemons'][text]['cool'] * 5
                    if x['pokemons'][text]['golden'] == 1:
                        gold = x['pokemons'][text]['cool'] * 50
                except:
                    gold = 0
                try:
                    users.update_one({'id': call.from_user.id}, {'$unset': {'pokemons.' + text: 1}})
                    users.update_one({'id': call.from_user.id}, {'$inc': {'money': gold}})
                    medit('Вы продали покемона ' + pokemons[text]['name'] + '!', call.message.chat.id,
                          call.message.message_id)
                except:
                    medit('У вас нет этого покемона!', call.message.chat.id, call.message.message_id)
            else:
                bot.answer_callback_query(call.id, 'Это не ваше меню!')

        elif 'buy' in call.data:
            text = call.data.split(' ')
            if int(text[0]) == call.from_user.id:
                x = users.find_one({'id': call.from_user.id})
                if x != None:
                    text = text[1]
                    text = text[3:]
                    i = 0
                    for ids in x['pokemons2']:
                        if x['pokemons2'][ids]['code'] == text:
                            i = 1
                    if i == 0:
                        if x['ruby'] >= rubypokemons[text]['cost']:
                            users.update_one({'id': x['id']}, {'$inc': {'ruby': -rubypokemons[text]['cost']}})
                            users.update_one({'id': x['id']}, {'$set': {'pokemons2.' + text: createruby(text, 0)}})
                            medit('Вы успешно купили покемона ' + rubypokemons[text]['name'] + '!',
                                  call.message.chat.id, call.message.message_id)
                        else:
                            medit('Недостаточно рубинов!', call.message.chat.id, call.message.message_id)
                    else:
                        medit('У вас уже есть этот покемон!', call.message.chat.id, call.message.message_id)
            else:
                bot.answer_callback_query(call.id, 'Это не ваше меню!')

        elif 'upgrade' in call.data:
            text = call.data.split(' ')
            if int(text[0]) == call.from_user.id:
                text = text[1]
                text = text[7:]
                if text not in rubypokes:
                    x = users.find_one({'id': call.from_user.id})
                    cost = int(200 + (x['pokemons'][text]['cool'] / 3))
                    if x['money'] >= cost:
                        users.update_one({'id': call.from_user.id}, {'$inc': {'money': -cost}})
                        z = random.randint(1, 100)
                        bonus = 0
                        abc = ['atk', 'def', 'agility', 'cool']
                        attribute = random.choice(abc)
                        if attribute == 'atk':
                            bonus = random.randint(1, 2)
                            name = 'Атака'

                        elif attribute == 'def':
                            bonus = random.randint(2, 3)
                            name = 'Защита'

                        elif attribute == 'agility':
                            bonus = random.randint(2, 3)
                            name = 'Ловкость'

                        elif attribute == 'cool':
                            bonus = random.randint(5, 15)
                            name = 'Крутость'

                        if z <= 40:
                            users.update_one({'id': call.from_user.id},
                                             {'$inc': {'pokemons.' + text + '.' + attribute: bonus}})
                            medit('Вы успешно улучшили покемона ' + x['pokemons'][text][
                                'name'] + '! Улучшено:\n\n' + name + ': ' + str(bonus) + '\nПотрачено ' + str(
                                cost) + ' голды.', call.message.chat.id, call.message.message_id)
                        else:
                            medit('У вас не получилось улучшить покемона! Потрачено ' + str(cost) + ' голды.',
                                  call.message.chat.id, call.message.message_id)
                    else:
                        medit('Недостаточно золота (нужно ' + str(cost) + ').', call.message.chat.id,
                              call.message.message_id)
                else:
                    x = users.find_one({'id': call.from_user.id})
                    cost = int(15 + (x['pokemons2'][text]['cool'] / 1000))
                    if x['ruby'] >= cost:
                        users.update_one({'id': call.from_user.id}, {'$inc': {'ruby': -cost}})
                        z = random.randint(1, 100)
                        bonus = 0
                        abc = ['atk', 'def', 'agility', 'cool']
                        attribute = random.choice(abc)
                        if attribute == 'atk':
                            bonus = random.randint(1, 2)
                            name = 'Атака'

                        elif attribute == 'def':
                            bonus = random.randint(2, 3)
                            name = 'Защита'

                        elif attribute == 'agility':
                            bonus = random.randint(2, 3)
                            name = 'Ловкость'

                        elif attribute == 'cool':
                            bonus = random.randint(200, 800)
                            name = 'Крутость'

                        if z <= 60:
                            users.update_one({'id': call.from_user.id},
                                             {'$inc': {'pokemons2.' + text + '.' + attribute: bonus}})
                            medit('Вы успешно улучшили покемона ' + x['pokemons2'][text][
                                'name'] + '! Улучшено:\n\n' + name + ': ' + str(bonus) + '\nПотрачено ' + str(
                                cost) + ' рубинов.', call.message.chat.id, call.message.message_id)
                        else:
                            medit('У вас не получилось улучшить покемона! Потрачено ' + str(cost) + ' рубинов.',
                                  call.message.chat.id, call.message.message_id)
                    else:
                        medit('Недостаточно рубинов (нужно ' + str(cost) + ').', call.message.chat.id,
                              call.message.message_id)
            else:
                bot.answer_callback_query(call.id, 'Это не ваше меню!')


def unban(id):
    try:
        pokeban.remove(id)
    except:
        pass


def givepoke(pokemon, id, mid, name, userid):
    golden = 0
    if pokemon[0] == 'g' and pokemon[1] == 'o' and pokemon[2] == 'l' and pokemon[3] == 'd':
        z = len(pokemon)
        pokemon = pokemon[(z - (z - 4)):]
        golden = 1
    text = ''
    if golden == 1:
        text = '*Золотой* '
    try:
        medit('Покемона ' + text + pokemons[pokemon]['name'] + ' поймал ' + name + '!', id, mid, parse_mode='markdown')
        users.update_one({'id': userid}, {'$set': {'pokemons.' + pokemon: createpoke(pokemon, golden)}})
    except:
        pass


@bot.message_handler(content_types=['text'])
def textt(m):
    if users.find_one({'id': m.from_user.id}) == None:
        users.insert_one(createuser(m.from_user.id))
    x = chats.find_one({'id': m.chat.id})
    if x == None:
        chats.insert_one(createchat(m.chat.id))
    if users.find_one({'id': m.from_user.id}) != None:
        users.update_one({'id': m.from_user.id}, {'$set': {'name': m.from_user.first_name}})


def createpoke(pokemon, gold):
    return {'name': pokemons[pokemon]['name'],
            'code': pokemon,
            'cool': pokemons[pokemon]['cool'],
            'golden': gold,
            'lvl': 1,
            'atk': 1,
            'def': 1,
            'agility': 1,
            'hunting': 0
            }


def createruby(pokemon, gold):
    return {'name': rubypokemons[pokemon]['name'],
            'code': pokemon,
            'cool': rubypokemons[pokemon]['cool'],
            'golden': gold,
            'lvl': 2,
            'atk': 1,
            'def': 1,
            'agility': 1,
            'hunting': 0
            }


def createchat(id):
    return {'id': id
            }


def createuser(id):
    return {'id': id,
            'name': None,
            'pokemons': {},
            'chancetocatch': 0,
            'money': 0,
            'pokemons2': {},
            'ruby': 0
            }


        
print('7777')
pokewars.polling(none_stop=True,timeout=600)
