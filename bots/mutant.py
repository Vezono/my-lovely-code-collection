# its a mutantic code of two bots... dont touch that

import os
import telebot
import time
import random
import threading
from emoji import emojize
from telebot import types
from pymongo import MongoClient
import traceback
from requests.exceptions import ReadTimeout
from requests.exceptions import ConnectionError
from variables import *
from minesurv.minesurvp import *

#fm_token = os.environ['fm_token']
#fm_bot = telebot.TeleBot(fm_token)
mine_token = os.environ['mine_token']
mine_bot = telebot.TeleBot(mine_token)

client=MongoClient(os.environ['fm_db'])
#fm_db=client.fabricamanagers
#fm_users=fm_db.users
#fm_world=fm_db.world
boottext = 'Succseed! Yeah!'
admin = 792414733
vip = [792414733]

craftable = ['Бутерброд с рыбой', 'Приготовленное мясо', 'Печь', 'Колодец', 'Хлеб', 'Удочка', '', '', '', '', '', '',
             '', '', '', '', '', '']
recipes = ['furnance', 'cookedmeat', 'fountain', 'bread', 'fishingrod', 'fishhamburger', 'woodsword', 'farm', 'hoe',
           'bucket', 'battery',
           'autobur']
x = 0
mine_users = client.farmer.users
class minesurvdefs(object):
    def __init__(self, color, doors, tires):
        print('Minesurv')

    def recipetoname(x):
        text = 'У рецепта нет названия, сообщите об этом разработчику.'
        if x == 'furnance':
            text = 'Печь'
        if x == 'cookedmeat':
            text = 'Приготовленное мясо'
        if x == 'fountain':
            text = 'Колодец'
        if x == 'bread':
            text = 'Хлеб'
        if x == 'fishingrod':
            text = 'Удочка'
        if x == 'fishhamburger':
            text = 'Бутерброд с рыбой'
        if x == 'woodsword':
            text = 'Деревянный меч'
        if x == 'farm':
            text = 'Ферма'
        if x == 'bucket':
            text = 'Ведро'
        if x == 'hoe':
            text = 'Мотыга'
        if x == 'battery':
            text = 'Батарейка'
        if x == 'autobur':
            text = 'Автобур'
        return text

    def recipetocraft(x):
        text = 'Рецепта нет! Обратитесь к разработчику.'
        if x == 'furnance':
            text = '*Печь:* 100 (Камень), 10 (Дерево), 30 (Голод) (/furnance).\n'
        if x == 'cookedmeat':
            text = '*Приготовленное мясо:* 1 (Мясо), 1 (Уголь) (/meat).\n'
        if x == 'fountain':
            text = '*Колодец:* 150 (Камень), 40 (Дерево), 1 (Ведро), 50 (Голод) (/fountain).\n'
        if x == 'bread':
            text = '*Хлеб:* 10 (Пшено) (/bread).\n'
        if x == 'fishingrod':
            text = '*Удочка:* 40 (Дерево), 10 (Нитки) (/rod).\n'
        if x == 'fishhamburger':
            text = '*Бутерброд с рыбой:* 15 (Рыба), 10 (Хлеб) (/fishburger).\n'
        if x == 'woodsword':
            text = '*Деревянный меч:* 40 (Дерево), 15 (Голод) (/woodsword).\n'
        if x == 'farm':
            text = '*Ферма:* 600 (Дерево), 250 (Камень), 20 (Вода), 1 (Мотыга), 70 (Голод) (/farm).\n'
        if x == 'hoe':
            text = '*Мотыга:* 50 (Дерево), 25 (Камень), 10 (Голод) (/hoe).\n'
        if x == 'bucket':
            text = '*Ведро:* 25 (Железо), 5 (Уголь), 5 (Голод) (/bucket).\n'
        if x == 'battery':
            text = '*Батарейка:* 70 (Железо), 20 (Медь), 500 (Электричество) (/battery).\n'
        if x == 'autobur':
            text = '*Автобур:* 5 (Иридий), 130 (Железо), 5 (Батарея), 6 (Алмазы) (/autobur).\n'
        return text

    def mtext(m):
        if m.from_user.id == m.chat.id:
            x = mine_users.find_one({'id': m.from_user.id})
            if x != None:
                if x['tutorial'] == 1:
                    if m.text == '👷🏻Добыча':
                        kb = types.ReplyKeyboardMarkup()
                        kb.add(types.KeyboardButton('🌲Лес'))
                        mine_bot.send_message(m.chat.id, 'Куда вы хотите направиться?', reply_markup=kb)
                    elif m.text == '🌲Лес' and x['tforest'] == 0:
                        mine_users.update_one({'id': m.from_user.id}, {'$set': {'tforest': 1}})
                        mine_bot.send_message(m.chat.id,
                                              'Вы отправились в лес. Вернётесь через минуту (Минута вашего времени = 15 минут жизни на острове).')
                        t = threading.Timer(60, tforest, args=[m.from_user.id])
                        t.start()
                    elif m.text == '🔨Постройка':
                        kb = types.ReplyKeyboardMarkup()
                        kb.add(types.KeyboardButton('⛺️Дом'))
                        mine_bot.send_message(m.chat.id, 'Что вы хотите построить?', reply_markup=kb)
                    elif m.text == '⛺️Дом' and x['thouse'] == 0:
                        mine_users.update_one({'id': m.from_user.id}, {'$set': {'thouse': 1}})
                        mine_bot.send_message(m.chat.id, 'Вы отправились строить дом. Вернётесь через 2 минуты.')
                        t = threading.Timer(120, thouse, args=[m.from_user.id])
                        t.start()
                else:
                    if m.text == '❓Обо мне':
                        mine_bot.send_message(m.chat.id, 'Привет, ' + x['name'] + '!\n' +
                                              'Голод: ' + str(x['hunger']) + '/' + str(x['maxhunger']) + '🍗\n' +
                                              'Уровень: ' + str(x['level']) + '\n' +
                                              'Опыт: ' + str(x['exp']) + '\n' +
                                              'Инвентарь: /inventory\n' +
                                              'Еда: /food')

                    elif m.text == '👷Добыча':
                        kb = types.ReplyKeyboardMarkup()
                        kb.add(types.KeyboardButton('🌲Лес'))
                        kb.add(types.KeyboardButton('🕳Пещера'))
                        kb.add(types.KeyboardButton('🐖Охота'))
                        if 'fountain' in x['buildings']:
                            kb.add('💧Колодец')
                        kb.add(types.KeyboardButton('↩️Назад'))
                        mine_bot.send_message(m.chat.id, 'Куда хотите отправиться?', reply_markup=kb)

                    elif m.text == '⛺️Дом':
                        kb = types.ReplyKeyboardMarkup()
                        kb.add(types.KeyboardButton('⚒Крафт'))
                        kb.add(types.KeyboardButton('↩️Назад'))
                        mine_bot.send_message(m.chat.id,
                                              'Дома вы можете крафтить полезные вещи и строить дополнительные строения.',
                                              reply_markup=kb)

                    elif m.text == '⚒Крафт':
                        x = mine_users.find_one({'id': m.from_user.id})
                        text = 'Список того, что вы можете скрафтить:\n'
                        for ids in x['recipes']:
                            text += recipetocraft(ids)
                        if text == 'Список того, что вы можете скрафтить:\n':
                            text = 'У вас пока что нет рецептов. Получить их можно, добывая ресурсы в любой локации.'
                        mine_bot.send_message(m.chat.id, text, parse_mode='markdown')

                    elif m.text == '🌲Лес':
                        x = mine_users.find_one({'id': m.from_user.id})
                        if x['farming'] == 0:
                            mine_users.update_one({'id': m.from_user.id}, {'$set': {'farming': 1}})
                            mine_bot.send_message(m.chat.id, 'Вы отправились в лес. Вернётесь через 5 минут.')
                            battle = random.randint(1, 100)
                            ids = mine_users.find({'id': {'$ne': m.from_user.id}})
                            idss = []
                            for i in ids:
                                idss.append(i)

                            if battle <= 20:
                                if len(idss) > 0:
                                    user = random.choice(idss)
                                    mine_users.update_one({'id': m.from_user.id}, {'$set': {'huntedby': user['id']}})
                                    mine_users.update_one({'id': user['id']}, {'$set': {'huntingto': m.from_user.id}})
                                    try:
                                        if m.from_user.id not in vip:
                                            mine_bot.send_message(user['id'],
                                                                  'Вы заметили ' + m.from_user.first_name + ', добывающего ресурсы около вашего дома! Чтобы попробовать ограбить его, нажмите /hunt.')
                                    except:
                                        print('oshibka')
                            if m.from_user.id in vip:
                                forest(m.from_user.id)
                            else:
                                t = threading.Timer(300, forest, args=[m.from_user.id])
                                t.start()
                        else:
                            mine_bot.send_message(m.chat.id, 'Вы уже заняты добычей ресурсов, попробуйте позже.')

                    elif m.text == '🕳Пещера':
                        x = mine_users.find_one({'id': m.from_user.id})
                        if x['farming'] == 0:
                            mine_users.update_one({'id': m.from_user.id}, {'$set': {'farming': 1}})
                            mine_bot.send_message(m.chat.id, 'Вы отправились в пещеру. Вернётесь через 5 минут.')
                            battle = random.randint(1, 100)
                            ids = mine_users.find({'id': {'$ne': m.from_user.id}})
                            idss = []
                            for i in ids:
                                idss.append(i)

                            if battle <= 20:
                                if len(idss) > 0:
                                    user = random.choice(idss)
                                    mine_users.update_one({'id': m.from_user.id}, {'$set': {'huntedby': user['id']}})
                                    mine_users.update_one({'id': user['id']}, {'$set': {'huntingto': m.from_user.id}})
                                    try:
                                        if m.from_user.id not in vip:
                                            mine_bot.send_message(user['id'],
                                                                  'Вы заметили ' + m.from_user.first_name + ', добывающего ресурсы около вашего дома! Чтобы попробовать ограбить его, нажмите /hunt.')
                                    except:
                                        print('oshibka')
                            if m.from_user.id in vip:
                                cave(m.from_user.id)
                            else:
                                t = threading.Timer(300, cave, args=[m.from_user.id])
                                t.start()

                        else:
                            mine_bot.send_message(m.chat.id, 'Вы уже заняты добычей ресурсов, попробуйте позже.')

                    elif m.text == '🐖Охота':
                        x = mine_users.find_one({'id': m.from_user.id})
                        if x['farming'] == 0:
                            mine_users.update_one({'id': m.from_user.id}, {'$set': {'farming': 1}})
                            mine_bot.send_message(m.chat.id, 'Вы отправились на охоту. Вернётесь через 5 минут.')
                            battle = random.randint(1, 100)
                            ids = mine_users.find({'id': {'$ne': m.from_user.id}})
                            idss = []
                            for i in ids:
                                idss.append(i)

                            if battle <= 20:
                                if len(idss) > 0:
                                    user = random.choice(idss)
                                    mine_users.update_one({'id': m.from_user.id}, {'$set': {'huntedby': user['id']}})
                                    mine_users.update_one({'id': user['id']}, {'$set': {'huntingto': m.from_user.id}})
                                    try:
                                        if m.from_user.id not in vip:
                                            mine_bot.send_message(user['id'],
                                                                  'Вы заметили ' + m.from_user.first_name + ', добывающего ресурсы около вашего дома! Чтобы попробовать ограбить его, нажмите /hunt.')
                                    except:
                                        print('oshibka')
                            if m.from_user.id in vip:
                                hunt(m.from_user.id)
                            else:
                                t = threading.Timer(300, hunt, args=[m.from_user.id])
                                t.start()

                        else:
                            mine_bot.send_message(m.chat.id, 'Вы уже заняты добычей ресурсов, попробуйте позже.')

                    elif m.text == '💧Колодец':
                        x = mine_users.find_one({'id': m.from_user.id})
                        if x['farming'] == 0:
                            if 'fountain' in x['buildings']:
                                mine_users.update_one({'id': m.from_user.id}, {'$set': {'farming': 1}})
                                mine_bot.send_message(m.chat.id, 'Вы отправились к колодцу. Вернётесь через 3 минуты.')
                                if m.from_user.id in vip:
                                    water(m.from_user.id)
                                else:
                                    t = threading.Timer(300, water, args=[m.from_user.id])
                                    t.start()
                            else:
                                mine_bot.send_message(m.chat.id, 'У вас нет колодца!')
                        else:
                            mine_bot.send_message(m.chat.id, 'Вы уже заняты добычей ресурсов, попробуйте позже.')

                    elif m.text.lower() == 'тест':
                        if m.from_user.id in vip:
                            mine_bot.send_message(m.chat.id, 'Вы отправились в пещеру. Вернётесь через 3 секунды.')
                            mine_users.update_one({'id': m.from_user.id}, {'$set': {'farming': 1}})
                            t = threading.Timer(3, cave, args=[m.from_user.id])
                            t.start()

                    elif m.text == '🐔Ферма' and m.from_user.id == m.chat.id:
                        if 'farm' in x['buildings']:
                            kb = types.ReplyKeyboardMarkup()
                            kb.add('Посадить семена')
                            kb.add('Животные')
                            kb.add('↩️Назад')
                            mine_bot.send_message(m.chat.id, 'Вы на своей ферме! Выберите действие.', reply_markup=kb)
                        else:
                            mine_bot.send_message(m.chat.id, 'У вас нет фермы!')


                    elif m.text == 'Посадить семена' and m.from_user.id == m.chat.id:
                        if 'farm' in x['buildings']:
                            kb = types.ReplyKeyboardMarkup()
                            mine_bot.send_message(m.chat.id, 'Отправьте количество семян, которое хотите посадить',
                                                  reply_markup=kb)
                            mine_users.update_one({'id': x['id']}, {'$set': {'seeding': 1}})
                            t = threading.Timer(30, seed0, args=[m.from_user.id])
                            t.start()

                    elif m.text == '↩️Назад':
                        kb = types.ReplyKeyboardMarkup()
                        kb.add('👷Добыча')
                        kb.add('⛺️Дом')
                        if 'farm' in x['buildings']:
                            kb.add('🐔Ферма')
                        kb.add('❓Обо мне')
                        mine_bot.send_message(m.chat.id, 'Добро пожаловать домой!', reply_markup=kb)

                    else:
                        if x['seeding'] == 1:
                            if x['farming'] != 1:
                                try:
                                    z = int(m.text)
                                    if x['seeds'] >= z and z > 0:
                                        if x['water'] > 0:
                                            mine_users.update_one({'id': m.from_user.id}, {'$set': {'farming': 1}})
                                            mine_bot.send_message(m.chat.id,
                                                                  'Вы отправились сажать семяна. Вернётесь через 3 минуты.')
                                            t = threading.Timer(180, seeding, args=[m.from_user.id, z])
                                            t.start()
                                        else:
                                            mine_bot.send_message(m.chat.id,
                                                                  'Для этого вам не хватает 1 (Вода)! (требуется: 1)')
                                    else:
                                        mine_bot.send_message(m.chat.id,
                                                              'У вас недостаточно семян, или вы указали отрицательное число.')
                                except:
                                    pass
                            else:
                                mine_bot.send_message(m.chat.id, 'Вы уже заняты добычей ресурсов.')

    def forest(id):
        woodtexts = ['Вы вернулись из леса. В этот раз удалось добыть:\n']
        wood = random.randint(1, 100)
        rock = random.randint(1, 100)
        meat = random.randint(1, 100)
        seeds = random.randint(1, 100)
        cow = random.randint(1, 100)
        gwood = 0
        grock = 0
        gmeat = 0
        gseeds = 0
        gcow = 0
        if wood <= 90:
            wood = 1
            gwood = random.randint(4, 15)
        else:
            wood = 0
        if rock <= 15:
            rock = 1
            grock = random.randint(1, 8)
        else:
            rock = 0
        if meat <= 20:
            meat = 1
            gmeat = random.randint(1, 3)
        else:
            meat = 0
        if seeds <= 30:
            seeds = 1
            gseeds = random.randint(3, 8)
        else:
            seeds = 0
        if cow <= 1:
            cow = 1
            gcow = 1
        else:
            cow = 0
        recources = ''
        text = random.choice(woodtexts)
        if wood == 1:
            recources += '⚪️Дерево: ' + str(gwood) + '\n'
        if rock == 1:
            recources += '🔵Камень: ' + str(grock) + '\n'
        if meat == 1:
            recources += '🔵Мясо: ' + str(gmeat) + '\n'
        if seeds == 1:
            recources += '🔵Семена: ' + str(gseeds) + '\n'
        if cow == 1:
            recources += '🔶Телёнок: ' + str(gcow) + '\n'
        x = mine_users.find_one({'id': id})
        grecipe = random.randint(1, 100)
        if grecipe <= 15:
            recipe = random.choice(recipes)
            if len(x['recipes']) < len(recipes):
                while recipe in x['recipes']:
                    recipe = random.choice(recipes)
                mine_users.update_one({'id': id}, {'$push': {'recipes': recipe}})
                recources += '🔴Рецепт: ' + recipetoname(recipe)
        text = random.choice(woodtexts)
        if wood == 0 and rock == 0 and meat == 0 and grecipe > 15 and seeds == 0 and cow == 0:
            text = 'В этот раз ничего добыть не удалось. Зато вы прогулялись по лесу и хорошо отдохнули!'
        if x['huntedby'] != None:
            y = mine_users.find_one({'id': x['huntedby']})
            if y['hunting'] == 1:
                if y['huntwin'] == 1:
                    mine_bot.send_message(x['id'], 'Когда вы возвращались из леса, на вас напал ' + y[
                        'name'] + '!\n.............\nОн оказался сильнее, и всю добычу пришлось отдать.')
                    mine_bot.send_message(y['id'], 'Когда ' + x[
                        'name'] + ' возвращался из леса, вы напали на него из засады.\n.............\nВы победили, и забрали всю его добычу себе!')
                    mine_users.update_one({'id': y['id']}, {'$inc': {'wood': gwood}})
                    mine_users.update_one({'id': y['id']}, {'$inc': {'meat': gmeat}})
                    mine_users.update_one({'id': y['id']}, {'$inc': {'rock': grock}})
                    mine_users.update_one({'id': y['id']}, {'$inc': {'seeds': gseeds}})
                    mine_users.update_one({'id': y['id']}, {'$inc': {'cow': gcow}})
                    mine_bot.send_message(y['id'], 'Полученные ресурсы:\n' + recources)
                    mine_bot.send_message(id, 'Ресурсы, которые у вас отняли:\n' + recources)
                else:
                    mine_bot.send_message(x['id'], 'Когда вы возвращались из леса, на вас напал ' + y[
                        'name'] + '!\n.............\nВы одержали победу! Враг уходит ни с чем.')
                    mine_bot.send_message(y['id'], 'Когда ' + x[
                        'name'] + ' возвращался из леса, вы напали на него из засады.\n.............\nВраг оказался слишком сильным, и вам пришлось отступить.')
                    mine_users.update_one({'id': id}, {'$inc': {'wood': gwood}})
                    mine_users.update_one({'id': id}, {'$inc': {'meat': gmeat}})
                    mine_users.update_one({'id': id}, {'$inc': {'rock': grock}})
                    mine_users.update_one({'id': id}, {'$inc': {'seeds': gseeds}})
                    mine_users.update_one({'id': id}, {'$inc': {'cow': gcow}})
                    mine_bot.send_message(x['id'], 'Ваши добытые ресурсы:\n' + recources)
                    mine_bot.send_message(y['id'], 'Ресурсы, которые нёс враг:\n' + recources)
                    mine_users.update_one({'id': id}, {'$set': {'huntedby': None}})
                    mine_users.update_one({'id': y['id']}, {'$set': {'huntingto': None}})
                    mine_users.update_one({'id': id}, {'$set': {'farming': 0}})
                    mine_users.update_one({'id': y['id']}, {'$set': {'hunting': 0}})
        else:
            mine_users.update_one({'id': id}, {'$inc': {'wood': gwood}})
            mine_users.update_one({'id': id}, {'$inc': {'meat': gmeat}})
            mine_users.update_one({'id': id}, {'$inc': {'rock': grock}})
            mine_users.update_one({'id': id}, {'$inc': {'seeds': gseeds}})
            mine_users.update_one({'id': id}, {'$inc': {'cow': gcow}})
            mine_users.update_one({'id': id}, {'$set': {'huntedby': None}})
            mine_users.update_one({'id': y['id']}, {'$set': {'huntingto': None}})
            mine_users.update_one({'id': y['id']}, {'$set': {'hunting': 0}})
            mine_users.update_one({'id': id}, {'$set': {'farming': 0}})
            try:
                mine_bot.send_message(id, text + recources)
            except:
                pass
            try:
                mine_bot.send_message(y['id'], 'Вы решили не атаковать, и цель ушла с ресурсами.')
            except:
                pass

    else:
        mine_users.update_one({'id': id}, {'$inc': {'wood': gwood}})
        mine_users.update_one({'id': id}, {'$inc': {'meat': gmeat}})
        mine_users.update_one({'id': id}, {'$inc': {'rock': grock}})
        mine_users.update_one({'id': id}, {'$inc': {'seeds': gseeds}})
        mine_users.update_one({'id': id}, {'$inc': {'cow': gcow}})
        mine_users.update_one({'id': id}, {'$set': {'farming': 0}})
    try:
        mine_bot.send_message(id, text + recources)
    except:
        pass


def hunt(id):
    hunttexts = ['Вы вернулись с охоты. В этот раз удалось добыть:\n']
    meat = random.randint(1, 100)
    eggs = random.randint(1, 100)
    mushroom = random.randint(1, 100)
    fish = random.randint(1, 100)
    gmeat = 0
    geggs = 0
    gfish = 0
    gmushroom = 0

    if meat <= 60:
        meat = 1
        gmeat = random.randint(3, 8)
    else:
        meat = 0

    if eggs <= 25:
        eggs = 1
        geggs = random.randint(1, 4)
    else:
        eggs = 0

    if mushroom <= 1:
        mushroom = 1
        gmushroom = 1
    else:
        mushroom = 0

    if fish <= 40:
        fish = 1
        gfish = random.randint(2, 6)
    else:
        fish = 0

    recources = ''
    text = random.choice(hunttexts)
    if meat == 1:
        recources += '⚪️Мясо: ' + str(gmeat) + '\n'
    if fish == 1:
        recources += '⚪️Рыба: ' + str(gfish) + '\n'
    if eggs == 1:
        recources += '🔵Яйца: ' + str(geggs) + '\n'
    if mushroom == 1:
        recources += '🔶Грибы: ' + str(gmushroom) + '\n'
    x = mine_users.find_one({'id': id})
    grecipe = random.randint(1, 100)
    if grecipe <= 15:
        recipe = random.choice(recipes)
        if len(x['recipes']) < len(recipes):
            while recipe in x['recipes']:
                recipe = random.choice(recipes)
            mine_users.update_one({'id': id}, {'$push': {'recipes': recipe}})
            recources += '🔴Рецепт: ' + recipetoname(recipe)

    text = random.choice(hunttexts)
    if meat == 0 and fish == 0 and eggs == 0 and mushroom == 0 and grecipe > 15:
        text = 'В этот раз никого поймать не удалось - добыча была слишком быстрой.'

    if x['huntedby'] != None:
        y = mine_users.find_one({'id': x['huntedby']})
        if y['hunting'] == 1:
            if y['huntwin'] == 1:
                mine_bot.send_message(x['id'], 'Когда вы возвращались с охоты, на вас напал ' + y[
                    'name'] + '!\n.............\nОн оказался сильнее, и всю добычу пришлось отдать.')
                mine_bot.send_message(y['id'], 'Когда ' + x[
                    'name'] + ' возвращался с охоты, вы напали на него из засады.\n.............\nВы победили, и забрали всю его добычу себе!')
                mine_users.update_one({'id': y['id']}, {'$inc': {'meat': gmeat}})
                mine_users.update_one({'id': y['id']}, {'$inc': {'fish': gfish}})
                mine_users.update_one({'id': y['id']}, {'$inc': {'egg': geggs}})
                mine_users.update_one({'id': y['id']}, {'$inc': {'mushroom': gmushroom}})
                mine_bot.send_message(y['id'], 'Полученные ресурсы:\n' + recources)
                mine_bot.send_message(id, 'Ресурсы, которые у вас отняли:\n' + recources)
            else:
                mine_bot.send_message(x['id'], 'Когда вы возвращались с охоты, на вас напал ' + y[
                    'name'] + '!\n.............\nВы одержали победу! Враг уходит ни с чем.')
                mine_bot.send_message(y['id'], 'Когда ' + x[
                    'name'] + ' возвращался с охоты, вы напали на него из засады.\n.............\nВраг оказался слишком сильным, и вам пришлось отступить.')
                mine_users.update_one({'id': id}, {'$inc': {'meat': gmeat}})
                mine_users.update_one({'id': id}, {'$inc': {'fish': gfish}})
                mine_users.update_one({'id': id}, {'$inc': {'egg': geggs}})
                mine_users.update_one({'id': id}, {'$inc': {'mushroom': gmushroom}})
                mine_users.update_one({'id': id}, {'$set': {'farming': 0}})
                mine_bot.send_message(x['id'], 'Ваши добытые ресурсы:\n' + recources)
                mine_bot.send_message(y['id'], 'Ресурсы, которые нёс враг:\n' + recources)
            mine_users.update_one({'id': id}, {'$set': {'huntedby': None}})
            mine_users.update_one({'id': y['id']}, {'$set': {'huntingto': None}})
            mine_users.update_one({'id': id}, {'$set': {'farming': 0}})
            mine_users.update_one({'id': y['id']}, {'$set': {'hunting': 0}})
        else:
            mine_users.update_one({'id': id}, {'$inc': {'meat': gmeat}})
            mine_users.update_one({'id': id}, {'$inc': {'fish': gfish}})
            mine_users.update_one({'id': id}, {'$inc': {'egg': geggs}})
            mine_users.update_one({'id': id}, {'$inc': {'mushroom': gmushroom}})
            mine_users.update_one({'id': id}, {'$set': {'farming': 0}})
            mine_users.update_one({'id': id}, {'$set': {'huntedby': None}})
            mine_users.update_one({'id': y['id']}, {'$set': {'huntingto': None}})
            mine_users.update_one({'id': id}, {'$set': {'farming': 0}})
            mine_users.update_one({'id': y['id']}, {'$set': {'hunting': 0}})
            try:
                mine_bot.send_message(id, text + recources)
            except:
                pass
            try:
                mine_bot.send_message(y['id'], 'Вы решили не атаковать, и цель ушла с ресурсами.')
            except:
                pass
    else:
        mine_users.update_one({'id': id}, {'$inc': {'meat': gmeat}})
        mine_users.update_one({'id': id}, {'$inc': {'fish': gfish}})
        mine_users.update_one({'id': id}, {'$inc': {'egg': geggs}})
        mine_users.update_one({'id': id}, {'$inc': {'mushroom': gmushroom}})
        mine_users.update_one({'id': id}, {'$set': {'farming': 0}})
        try:
            mine_bot.send_message(id, text + recources)
        except:
            pass


def cave(id):
    cavetexts = ['Вы вернулись из пещеры. В этот раз удалось добыть:\n']
    iron = random.randint(1, 100)
    gold = random.randint(1, 100)
    diamond = random.randint(1, 1000)
    ruby = random.randint(1, 1000)
    rock = random.randint(1, 100)
    coal = random.randint(1, 100)
    giron = 0
    grock = 0
    ggold = 0
    gdiamond = 0
    gcoal = 0
    gruby = 0
    x = mine_users.find_one({'id': id})

    if iron <= 20:
        iron = 1
        giron = random.randint(2, 10)
    else:
        iron = 0

    if rock <= 75:
        rock = 1
        grock = random.randint(5, 14)
    else:
        rock = 0

    if gold <= 5:
        gold = 1
        ggold = random.randint(1, 5)
    else:
        gold = 0

    if diamond <= 2:
        diamond = 1
        gdiamond = random.randint(1, 6)
    else:
        diamond = 0

    if coal <= 40:
        coal = 1
        gcoal = random.randint(1, 15)
    else:
        coal = 0

    if ruby <= 1:
        ruby = 1
        gruby = random.randint(1, 3)
    else:
        ruby = 0

    recources = ''
    text = random.choice(cavetexts)
    if rock == 1:
        recources += '⚪️Камень: ' + str(grock) + '\n'
    if coal == 1:
        recources += '⚪️Уголь: ' + str(gcoal) + '\n'
    if iron == 1:
        recources += '🔵Железо: ' + str(giron) + '\n'
    if gold == 1:
        recources += '🔴Золото: ' + str(ggold) + '\n'
    if diamond == 1:
        recources += '🔶Алмазы: ' + str(gdiamond) + '\n'
    if ruby == 1:
        recources += '🔶Рубины: ' + str(gruby) + '\n'

    grecipe = random.randint(1, 100)
    if grecipe <= 15:
        recipe = random.choice(recipes)
        if len(x['recipes']) < len(recipes):
            while recipe in x['recipes']:
                recipe = random.choice(recipes)
            mine_users.update_one({'id': id}, {'$push': {'recipes': recipe}})
            recources += '🔴Рецепт: ' + recipetoname(recipe)
        else:
            grecipe = 100

    text = random.choice(cavetexts)
    if rock == 0 and iron == 0 and coal == 0 and gold == 0 and diamond == 0 and ruby == 0 and grecipe > 15:
        text = 'В этот раз ничего добыть не удалось - пещера оказалось слишком опасной, и вы решили не рисковать.'

    if x['huntedby'] != None:
        y = mine_users.find_one({'id': x['huntedby']})
        if y['hunting'] == 1:
            if y['huntwin'] == 1:
                mine_bot.send_message(x['id'], 'Когда вы возвращались из пещеры, на вас напал ' + y[
                    'name'] + '!\n.............\nОн оказался сильнее, и всю добычу пришлось отдать.')
                mine_bot.send_message(y['id'], 'Когда ' + x[
                    'name'] + ' возвращался из пещеры, вы напали на него из засады.\n.............\nВы победили, и забрали всю его добычу себе!')
                mine_users.update_one({'id': y['id']}, {'$inc': {'rock': grock}})
                mine_users.update_one({'id': y['id']}, {'$inc': {'coal': gcoal}})
                mine_users.update_one({'id': y['id']}, {'$inc': {'iron': giron}})
                mine_users.update_one({'id': y['id']}, {'$inc': {'gold': ggold}})
                mine_users.update_one({'id': y['id']}, {'$inc': {'diamond': gdiamond}})
                mine_users.update_one({'id': y['id']}, {'$inc': {'ruby': gruby}})
                mine_users.update_one({'id': y['id']}, {'$set': {'farming': 0}})
                mine_bot.send_message(y['id'], 'Полученные ресурсы:\n' + recources)
                mine_bot.send_message(id, 'Ресурсы, которые у вас отняли:\n' + recources)
            else:
                mine_bot.send_message(x['id'], 'Когда вы возвращались из пещеры, на вас напал ' + y[
                    'name'] + '!\n.............\nВы одержали победу! Враг уходит ни с чем.')
                mine_bot.send_message(y['id'], 'Когда ' + x[
                    'name'] + ' возвращался из пещеры, вы напали на него из засады.\n.............\nВраг оказался слишком сильным, и вам пришлось отступить.')
                mine_users.update_one({'id': id}, {'$inc': {'rock': grock}})
                mine_users.update_one({'id': id}, {'$inc': {'coal': gcoal}})
                mine_users.update_one({'id': id}, {'$inc': {'iron': giron}})
                mine_users.update_one({'id': id}, {'$inc': {'gold': ggold}})
                mine_users.update_one({'id': id}, {'$inc': {'diamond': gdiamond}})
                mine_users.update_one({'id': id}, {'$inc': {'ruby': gruby}})
                mine_users.update_one({'id': id}, {'$set': {'farming': 0}})
                mine_bot.send_message(x['id'], 'Ваши добытые ресурсы:\n' + recources)
                mine_bot.send_message(y['id'], 'Ресурсы, которые нёс враг:\n' + recources)
            mine_users.update_one({'id': id}, {'$set': {'huntedby': None}})
            mine_users.update_one({'id': y['id']}, {'$set': {'huntingto': None}})
            mine_users.update_one({'id': id}, {'$set': {'farming': 0}})
            mine_users.update_one({'id': y['id']}, {'$set': {'hunting': 0}})
        else:
            mine_users.update_one({'id': id}, {'$inc': {'rock': grock}})
            mine_users.update_one({'id': id}, {'$inc': {'coal': gcoal}})
            mine_users.update_one({'id': id}, {'$inc': {'iron': giron}})
            mine_users.update_one({'id': id}, {'$inc': {'gold': ggold}})
            mine_users.update_one({'id': id}, {'$inc': {'diamond': gdiamond}})
            mine_users.update_one({'id': id}, {'$inc': {'ruby': gruby}})
            mine_users.update_one({'id': id}, {'$set': {'farming': 0}})
            mine_users.update_one({'id': id}, {'$set': {'huntedby': None}})
            mine_users.update_one({'id': y['id']}, {'$set': {'huntingto': None}})
            mine_users.update_one({'id': id}, {'$set': {'farming': 0}})
            mine_users.update_one({'id': y['id']}, {'$set': {'hunting': 0}})
            try:
                mine_bot.send_message(id, text + recources)
            except:
                pass
            try:
                mine_bot.send_message(y['id'], 'Вы решили не атаковать, и цель ушла с ресурсами.')
            except:
                pass
    else:

        mine_users.update_one({'id': id}, {'$inc': {'rock': grock}})
        mine_users.update_one({'id': id}, {'$inc': {'coal': gcoal}})
        mine_users.update_one({'id': id}, {'$inc': {'iron': giron}})
        mine_users.update_one({'id': id}, {'$inc': {'gold': ggold}})
        mine_users.update_one({'id': id}, {'$inc': {'diamond': gdiamond}})
        mine_users.update_one({'id': id}, {'$inc': {'ruby': gruby}})
        mine_users.update_one({'id': id}, {'$set': {'farming': 0}})
        try:
            mine_bot.send_message(id, text + recources)
        except:
            pass

    mobs = ['Червя-камнееда']
    text = ''
    enemy = random.randint(1, 100)
    recources = ''
    if enemy <= 20:
        mob = random.choice(mobs)
        text = 'По пути назад вы встретили ' + mob + '!\n.............\n'
        y = random.randint(1, 100)
        if 'woodsword' in x['craftable']:
            x['strenght'] += 8
        if y - x['strenght'] <= 1:
            gleither = 0
            if mob == 'Червя-камнееда':
                leither = random.randint(1, 100)
                if leither <= 50:
                    gleither = random.randint(1, 5)
                    recources += '⚪️Чешуя: ' + str(gleither) + '\n'
            text2 = 'Вы оказались сильнее, и убили врага. Полученные ресурсы:\n' + recources
            mine_users.update_one({'id': id}, {'$inc': {'squama': gleither}})
            breakk = random.randint(1, 100)
            if breakk <= 3 and x['craftable']['woodsword'] > 0:
                mine_users.update_one({'id': id}, {'$inc': {'craftable.woodsword': -1}})
                text2 += 'Ваш деревянный меч сломался!'
        else:
            text2 = 'Враг был силён, и вам пришлось отступить.'
        mine_bot.send_message(id, text + text2)


def mine_createuser(id, name):
    return {'id': id,
            'name': name,
            'seeding': 0,
            'huntedby': None,
            'nuntingto': None,
            'huntwin': 0,
            'hunting': 0,
            'strenght': 0,
            'coal': 0,
            'iron': 0,
            'gold': 0,
            'diamond': 0,
            'wood': 0,
            'rock': 0,
            'money': 0,
            'sand': 0,
            'salt': 0,
            'wheat': 0,
            'ruby': 0,
            'shugar': 0,
            'mushroom': 0,
            'meat': 0,
            'fish': 0,
            'egg': 0,
            'cow': 0,
            'seeds': 0,
            'water': 0,
            'iridium': 0,
            'hunger': 100,
            'maxhunger': 100,
            'buildings': [],
            'farm': None,
            'animals': [],
            'exp': 0,
            'level': 1,
            'tutorial': 1,
            'tforest': 0,
            'thouse': 0,
            'building': 0,
            'farming': 0,
            'recipes': [],
            'craftable': {'furnance': 0,
                          'cookedmeat': 0,
                          'fountain': 0,
                          'bread': 0,
                          'fishingrod': 0,
                          'fishhamburger': 0,
                          'woodsword': 0,
                          'hoe': 0,
                          'bucket': 0
                          },
            'squama': 0
            }
try:
    pass

except Exception as e:
    print('Ошибка:\n', traceback.format_exc())
    fm_bot.send_message(admin, traceback.format_exc())

@mine_bot.message_handler(commands=['update'])
def upd(m):
    if m.from_user.id in vip:
        mine_users.update_many({}, {'$set': {'craftable.battery': 0}})
        print('yes')



@fm_bot.message_handler(commands=['reset_units'])
def resetunits(m):
    if m.from_user.id==admin:
        u=fm_users.find({})
        for ids in u:
            for idss in ids['units']:
                unit=ids['units'][idss]
                fm_users.update_one({'id':ids['id']},{'$set':{'units.'+unit['name']+str(unit['number'])+'.status':'free'}})
                fm_users.update_one({'id':ids['id']},{'$set':{'units.'+unit['name']+str(unit['number'])+'.items':[]}})
                fm_users.update_one({'id':ids['id']},{'$set':{'units.'+unit['name']+str(unit['number'])+'.deliver_time':None}})
        fm_bot.send_message(m.chat.id, 'ready')
                
    
@fm_bot.message_handler(commands=['start'])
def start(m):
    tutorial=0
    if m.from_user.id==m.chat.id:
        if fm_users.find_one({'id':m.from_user.id})==None:
            fm_users.insert_one(fm_createuser(m.from_user))
            tutorial=1
        user=fm_users.find_one({'id':m.from_user.id})
        if tutorial==1:
            fm_bot.send_message(m.chat.id, 'Добывай ресурсы, строй механизмы на своей фабрике, шпионь, кради ресурсы у других, и участвуй в '+
                            'ежедневных битвах роботов!')
        mainmenu(user)
    

@fm_bot.message_handler(commands=['world_addres'])
def addresourcestoworld(m):
    if m.from_user.id==441399484:
        try:
            resource=m.text.split(' ')[1]
            amount=int(m.text.split(' ')[2])
            try:
                fm_world.update_one({},{'$inc':{'res.'+resource:amount}})
            except:
                fm_world.update_one({},{'$set':{'res.'+resource:amount}})
            current=fm_world.find_one({})['res'][resource]
            fm_bot.send_message(m.chat.id, 'Мировой ресурс "'+resource+'" увеличен на '+str(amount)+'! Текущее количество: '+str(current)+'.')
        except Exception as e:
            fm_bot.send_message(441399484, traceback.format_exc())
    
    
@fm_bot.message_handler()
def messages(m):
    kb=types.ReplyKeyboardMarkup(resize_keyboard=True)
    if m.from_user.id==m.chat.id:
        try:
            user=fm_users.find_one({'id':m.from_user.id})
            
            if m.text=='🏢Главное меню':
                mainmenu(m.from_user)
                
            if m.text=='❓Обо мне':
                fm_bot.send_message(m.chat.id, aboutme(user))
                
            if m.text=='👷‍♂️Месторождения ресурсов':
                recource_fields(user)
                
            if m.text=='🛢Нефть':
                distance=user['distances']['oil']
                text='Из нефти делается топливо для любых видов техники. Ближайшее месторождение нефти находится в '+str(distance)+' км от вашей фабрики.\n'
                builds=False
                if len(user['buildings']['oil'])>0:
                    builds=True
                if builds==False:
                    text+='У вас здесь ещё нет строений.\n'
                else:
                    text+='Ваши постройки здесь:\n'
                    text+=buildingslist(user, 'oil')
                    text+='\n'
                kb.add(types.KeyboardButton('⚒Стройка: нефть'))
                kb.add(types.KeyboardButton('🏢Главное меню'))
                fm_bot.send_message(m.chat.id, text, reply_markup=kb)
                
            if m.text=='⚒Стройка: нефть':
                buildmenu(user, 'oil')
                
            if m.text=='🚚Транспортировка ресурсов':
                transportmenu(user)
                
        except Exception as e:
            fm_bot.send_message(441399484, traceback.format_exc())
    
    
@fm_bot.callback_query_handler(func=lambda call:True)
def inline(call):
    user=fm_users.find_one({'id':call.from_user.id})
    kb=types.InlineKeyboardMarkup()
    if 'info' in call.data:
        if 'stock' in call.data:
            text=buildinginfo('stock')
            kb.add(types.InlineKeyboardButton(text='🔨Построить', callback_data='build stock '+call.data.split(' ')[2]))
            kb.add(types.InlineKeyboardButton(text='Закрыть меню', callback_data='close'))
            medit(text, call.message.chat.id, call.message.message_id, reply_markup=kb)
            
        if 'truck' in call.data:
            unit=call.data.split(' ')[1]
            text=unitinfo(user['units'][unit])
            kb.add(types.InlineKeyboardButton(text='Отправить за ресурсами', callback_data='sendto '+unit))
            medit(text, call.message.chat.id, call.message.message_id, reply_markup=kb)
            
    if 'sendto' in call.data:
        unit=call.data.split(' ')[1]
        places=['oil', 'forest', 'ores']
        oil_time=round((user['distances']['oil']/user['units'][unit]['speed'])*2, 2)
        forest_time=round((user['distances']['forest']/user['units'][unit]['speed'])*2, 2)
        ores_time=round((user['distances']['ore']/user['units'][unit]['speed'])*2, 2)
        for ids in places:
            kb.add(types.InlineKeyboardButton(text=field_ru(ids), callback_data='send '+unit+' '+ids))
        medit('Выберите, куда отправить транспорт. Он заберёт столько ресурсов со склада, сколько уместится.\n'+
                         'Примерное время доставки от точек:\n'+
                        '  Нефть: '+str(oil_time)+' час(ов)\n'+
                        '  Лес: '+str(forest_time)+' час(ов)\n'+
                        '  Руды: '+str(ores_time)+' час(ов)\n', call.message.chat.id, call.message.message_id, reply_markup=kb)
        
    if 'send ' in call.data:
        unit=call.data.split(' ')[1]
        to=call.data.split(' ')[2]
        if user['units'][unit]['status']=='free':
            sendto(user, unit, to)
            medit('Транспорт отправлен!', call.message.chat.id, call.message.message_id)
        else:
            medit('Этот транспорт занят!', call.message.chat.id, call.message.message_id)
            
    if 'build' in call.data:
        if 'stock' in call.data:
            resources={}
            place=call.data.split(' ')[2]
            resources.update(addres('wood', 100000))
            resources.update(addres('iron', 40000))
            nores=False
            try:
                for ids in resources:
                    if user['resources'][ids]<resources[ids]:
                        nores=True
            except:
                nores=True
                
            if nores==False:
                b=build(stock, user, place, False, time=21600) 
                for ids in resources:
                    fm_users.update_one({'id':user['id']},{'$inc':{'resources.'+ids:-resources[ids]['amount']}})
                fm_users.update_one({'id':user['id']},{'$set':{'buildings.'+place+'.'+b['name']+str(b['number']):b}})
                medit('Вы начали постройку склада! Стройка закончится примерно через 6 часов.', call.message.chat.id, call.message.message_id)
            else:
                medit('Не хватает ресурсов!', call.message.chat.id, call.message.message_id)
            
    if call.data=='close':
        medit('Меню закрыто.', call.message.chat.id, call.message.message_id, reply_markup=kb)
    
    
def sendto(user, unit, to):
    fm_users.update_one({'id':user['id']},{'$set':{'units.'+unit+'.status':'busy'}})
    timee=round((user['distances'][to]/user['units'][unit]['speed'])*2, 2)
    timee=timee*3600
    inv=[]
    count=0
    for ids in user['buildings'][to]:
        building=user['buildings'][to][ids]
        if building['name']=='stock':
            for ids in building['items']:
                c=building['items'][ids]
                if count+c>user['units'][unit]['capacity']:
                    c=user['units'][unit]['capacity']-count
                    if c!=0:
                        inv.append({ids:c})
                        count+=c
                        fm_users.update_one({'id':user['id']},{'$inc':{'buildings.'+to+'.'+building['name']+building['number']+'.items.'+ids:-c}})
    fm_users.update_one({'id':user['id']},{'$set':{'units.'+unit+'.deliver_time':time.time()+timee}})
    fm_users.update_one({'id':user['id']},{'$set':{'units.'+unit+'.inventory':inv}})
    
        
    
    
    
def transportmenu(user):
    text='Здесь находится весь ваш свободный транспорт. Он нужен для того, чтобы перевозить ресурсы со складов на главную фабрику. Нажмите кнопку '+\
    'для просмотра информации.'
    alltransport=[]
    kb=types.InlineKeyboardMarkup()
    for ids in user['units']:
        unit=user['units'][ids]
        if unit['type']=='transport' and unit['status']=='free':
            alltransport.append(unit)
    for ids in alltransport:
        kb.add(types.InlineKeyboardButton(text=unit_ru(ids['name']), callback_data='info '+unit['name']+str(unit['number'])))
    kb.add(types.InlineKeyboardButton(text='Закрыть меню', callback_data='close'))
    fm_bot.send_message(user['id'], text, reply_markup=kb)
    
                                            
                                             
def addres(res, amount):
    return {
        res:{'amount':amount
            }
    }
    
def buildinginfo(b):
    text='Неизвестно'
    if b=='stock':
        text='На склад поступают все ресурсы с месторождений. Чтобы ресурсы можно было использовать, их нужно отвезти со '+\
        'склада на вашу главную фабрику. Время перевозки зависит от расстояния между двумя точками.\n\n'
        text+='Характеристики строения:\n'
        text+='Вместимость: 1000 ед. любых ресурсов\n'
        text+='📦Требуемые ресурсы:\n'
        text+='  Доски: 100 000\n'
        text+='  Железо: 40 000\n'
        text+='  ⏰Время: 6ч.\n'
    return text
        
    
def unitinfo(unit):
    text=unit_ru(unit['name'])+':\n'
    if unit['type']=='transport':
        text+='Скорость: '+str(unit['speed'])+' км/ч\n'
        text+='Вместимость: '+str(unit['capacity'])+'\n'
    return text
    
    
def buildingslist(user, recource):
    text=''
    for ids in user['buildings'][recource]:
        text+=building_ru(ids)+'\n'
    return text
    

def buildmenu(user, resource):
    kb=types.InlineKeyboardMarkup()
    str1=[]
    str1.append(types.InlineKeyboardButton(text='Склад', callback_data='info stock '+resource))
    str1.append(types.InlineKeyboardButton(text='Нефтяная вышка', callback_data='info oilfarmer '+resource))
    kb.add(*str1)
    fm_bot.send_message(user['id'], 'Выберите строение для просмотра информации.', reply_markup=kb)
    
    

def recource_fields(user):
    kb=types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(types.KeyboardButton('🛢Нефть'),types.KeyboardButton('🌲Деревья'),types.KeyboardButton('💎Руды'))
    kb.add(types.KeyboardButton('🏢Главное меню'))
    fm_bot.send_message(user['id'], 'Выберите интересующий вас ресурс.', reply_markup=kb)
    
    
    
def aboutme(user):
    text=''
    text+='Имя: '+user['name']+'\n'
    text+='Ресурсы:\n'
    for ids in user['resources']:
        text+=recource_ru(ids)+': '+str(user['resources'][ids]['count'])+'\n'
    text+='\n'
    text+='Рубли: '+str(user['money'])+'\n'
    text+='Уровень главной фабрики: '+str(user['fabricalvl'])+'\n'
    return text
    
  
def createunit(user, unit):
    speed=60            # km/h
    typee=None
    if unit=='truck':
        typee='transport'
    count=1
    try:
        for ids in user['units']:
            if unit in ids:
                count+=1
    except:
        pass
    return {unit+str(count):{
        'name':unit,
        'speed':speed,
        'capacity':1000,
        'type':typee,
        'number':count,
        'status':'free',
        'inventory':[],
        'deliver_time':None    # Время, когда ресурсы из inventory попадут на общий склад.
    }
           }


def build(building, user, place, built, time=None):   # if built==False, time required
    count=1
    try:
        for ids in user['buildings'][place]:
            if building in ids:
                count+=1
    except:
        pass
    gentime=600               # В секундах
    amount=10                # Кол-во ресурса
    if building=='stock':
        capacity=1000
        gentime=0
    else:
        capacity=100
    return {building+str(count):{
        'items':{},
        'lvl':1,
        'capacity':capacity,
        'generate_time':gentime,
        'amount':amount,                 # Добываемое кол-во ресурса
        'nextgen':None,                  # Время следующей добычи ресурса (в unix)
        'name':building,
        'number':count,
        'place':place,
        'built':built,
        'buildtime':time                 # unix - когда строение будет построено
    }
               }


def building_ru(x):
    if 'stock' in x:
        return 'Склад'
    if 'oilfarmer' in x:
        return 'Нефтяная вышка'
    if 'forestcutter' in x:
        return 'Автолесоруб'
    
    return 'Неизвестное строение'

                                    
                                              
def resource_ru(x):
    if x=='oil':
        return 'Нефть'
    return 'Неизвестный ресурс'
    
                                              
def unit_ru(unit):
    if unit=='truck':
        return 'Грузовик'
    return 'Неизвестный юнит'
                                              
                                              
def field_ru(x):
    if x=='oil':
        return 'Нефть'
    if x=='forest':
        return 'Лес'
    if x=='ores':
        return 'Шахта'
    return 'Неизвестное место'
        
                                              
    
def addresource(building, user):
    error=25             # Погрешность добычи ресурса (в %).
    place=building['place']
    w=fm_world.find_one({})
    if building['name']=='oilfarmer':
        resource='oil'
    elif building['name']=='forestcutter':
        resource='wood'
    amount=building['amount']
    if random.randint(1,100)<=50:
        amount-=amount*(random.randint(0, error)/100)
    else:
        amount+=amount*(random.randint(0, error)/100)
    try:
        if w['res'][resource]<amount:
            amount=w['resources'][resource]
    except:
        return False
    stocks=[]
    for ids in user['buildings'][place]:
        bld=user['buildings'][place][ids]
        if bld['name']=='stock':
            stocks.append(bld)
    currentstock=None
    for ids in stocks:
        count=0
        for idss in ids['items']:
            count+=ids['items'][idss]
        if count+amount<=ids['capacity']:
            currentstock=ids['name']+str(ids['number'])
    if currentstock!=None:
        try:
            fm_users.update_one({'id':user['id']},{'$inc':{'buildings.'+place+'.'+currentstock+'.'+'items.'+resource:amount}})
        except:
            fm_users.update_one({'id':user['id']},{'$set':{'buildings.'+place+'.'+currentstock+'.'+'items.'+resource:amount}})
        fm_users.update_one({'id':user['id']},{'$set':{'buildings.'+place+'.'+building['name']+str(building['number'])+'.nextgen':int(time.time())+building['generate_time']}})
        fm_world.update_one({},{'$inc':{'res.'+resource:-amount}})
        
    
    
def fm_createuser(user):
    summ=80     # Сколько всего км будет распределено между всеми ресурсными точками
    d_ore=random.randint(1,summ)
    summ-=d_ore
    d_forest=random.randint(1,summ)
    summ-=d_forest
    d_oil=summ
    oil={}
    forest={}
    oil.update(build('stock', user, 'oil', True))
    oil.update(build('oilfarmer', user, 'oil', True))
    forest.update(build('stock', user, 'forest', True))
    forest.update(build('forestcutter', user, 'forest', True))
    units={}
    units.update(createunit(user, 'truck'))
    return {
        'id':user.id,
        'name':user.first_name,
        'username':user.username,
        'resources':{},
        'buildings':{
            'oil':oil,
            'forest':forest,
            'ore':{}
        },
        'units':units,
        'money':0,
        'fabricalvl':1,
        'distances':{
            'oil':d_oil,
            'forest':d_forest,
            'ore':d_ore
        }
    }
    
    
def mainmenu(user):
    kb=types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(types.KeyboardButton('❓Обо мне'), types.KeyboardButton('👷‍♂️Месторождения ресурсов'), types.KeyboardButton('🚚Транспортировка ресурсов'))
    try:
        fm_bot.send_message(user['id'], '🏡Главное меню.', reply_markup=kb)
    except:
        fm_bot.send_message(user.id, '🏡Главное меню.', reply_markup=kb)
 
def medit(message_text,chat_id, message_id,reply_markup=None,parse_mode=None):
    return fm_bot.edit_message_text(chat_id=chat_id,message_id=message_id,text=message_text,reply_markup=reply_markup,
                                 parse_mode=parse_mode)  

def finishbuild(user, building):
    path='buildings.'+building['place']+'.'+building['name']+building['number']
    fm_users.update_one({'id':user['id']},{'$set':{path+'.built':True, path+'.buildtime':None}})
    fm_bot.send_message(user['id'], 'Строение "'+building_ru(building['name'])+'": стройка завершена!')

def finishdelivery(user, unit):
    allres={}
    for ids in unit['inventory']:
        for idss in ids:
            try:
                fm_users.update_one({'id':user['id']},{'$inc':{'resources.'+idss:ids[idss]}})
            except:
                fm_users.update_one({'id':user['id']},{'$set':{'resources.'+idss:ids[idss]}})
            try:
                allres[idss]+=ids[idss]
            except:
                allres.update({
                    idss:ids[idss]
                })
    fm_users.update_one({'id':user['id']},{'$set':{'units.'+unit['name']+str(unit['number'])+'.inventory':[]}})
    fm_users.update_one({'id':user['id']},{'$set':{'units.'+unit['name']+str(unit['number'])+'.status':'free'}})
    fm_users.update_one({'id':user['id']},{'$set':{'units.'+unit['name']+str(unit['number'])+'.deliver_time':None}})
    return allres
            

def timecheck():
    t=threading.Timer(60, timecheck)
    t.start()
    timee=int(time.time())
    u=fm_users.find({})
    for ids in u:
        cuser=fm_users.find_one({'id':ids['id']})
        for idss in cuser['buildings']:
            for idsss in cuser['buildings'][idss]:
                building=cuser['buildings'][idss][idsss]
                if building['built']==True:
                    ctime=building['nextgen']
                    if ctime!=None:
                        if timee>=ctime:
                            addresource(building, cuser)
                    else:
                        addresource(building, cuser)
                        
                else:
                    ctime=building['buildtime']
                    if timee>=ctime:
                        finishbuild(cuser, building)
                    
        for idss in cuser['units']:
            unit=cuser['units'][idss]
            if unit['type']=='transport':
                ctime=unit['deliver_time']
                if ctime!=None:
                    if timee>=ctime:
                        text=''
                        resources=finishdelivery(cuser, unit)
                        for ids in resources:
                            text+=resource_ru(ids)+': '+str(resources[ids])+'\n'
                        fm_bot.send_message(cuser['id'], 'Ваш транспорт приехал! Полученные ресурсы:\n'+text)

@mine_bot.message_handler(commands=['sendm'])
def sendmes(message):
    if message.from_user.id in vip:
        x = mine_users.find({})
        tex = message.text.split('/sendm')
        for one in x:
            try:
                mine_bot.send_message(one['id'], tex[1])
            except:
                pass


@mine_bot.message_handler(commands=['food'])
def sendmes(m):
    x = mine_users.find_one({'id': m.from_user.id})
    text = ''
    if x['meat'] > 0:
        text += 'Мясо (восполняет: 1🍗) (/eatmeat): ' + str(x['meat']) + '\n'
    if x['craftable']['cookedmeat'] > 0:
        text += 'Приготовленное мясо (восполняет: 5🍗) (/eatcookedmeat): ' + str(x['craftable']['cookedmeat']) + '\n'
    mine_bot.send_message(m.chat.id, text)


@mine_bot.message_handler(commands=['eatmeat'])
def eatm(m):
    x = mine_users.find_one({'id': m.from_user.id})
    if x['meat'] > 0:
        if x['hunger'] <= x['maxhunger'] - 1:
            mine_users.update_one({'id': m.from_user.id}, {'$inc': {'meat': -1}})
            mine_users.update_one({'id': m.from_user.id}, {'$inc': {'hunger': 1}})
            mine_bot.send_message(m.chat.id, 'Вы съели Мясо и восстановили 1🍗!')
        else:
            mine_bot.send_message(m.chat.id, 'Вы не достаточно голодны!')
    else:
        mine_bot.send_message(m.chat.id, 'У вас нет этого!')


@mine_bot.message_handler(commands=['eatcookedmeat'])
def eatcm(m):
    x = mine_users.find_one({'id': m.from_user.id})
    if x['craftable']['cookedmeat'] > 0:
        if x['hunger'] <= x['maxhunger'] - 5:
            mine_users.update_one({'id': m.from_user.id}, {'$inc': {'craftable.cookedmeat': -1}})
            mine_users.update_one({'id': m.from_user.id}, {'$inc': {'hunger': 5}})
            mine_bot.send_message(m.chat.id, 'Вы съели Приготовленное мясо и восстановили 5🍗!')
        else:
            mine_bot.send_message(m.chat.id, 'Вы не достаточно голодны!')
    else:
        mine_bot.send_message(m.chat.id, 'У вас нет этого!')


@mine_bot.message_handler(commands=['start'])
def start(m):
    if mine_users.find_one({'id': m.from_user.id}) == None and m.chat.id == m.from_user.id:
        mine_users.insert_one(mine_createuser(m.from_user.id, m.from_user.first_name))
        kb = types.ReplyKeyboardMarkup()
        kb.add(types.KeyboardButton('👷🏻Добыча'))
        mine_bot.send_message(m.chat.id, '''Здраствуй, ты попал в игру "Minesurv"!
*Предыстория:*
На земле появился вирус, превращающий людей в зомби, передающийся через укус. В скором времени почти всё
население земли было заражено, и оставшимся в живых ничего не оставалось, кроме переселения на необитаемые острова.
Так как все, кого вы знали, были заражены, вы в одиночку построили плот, взяли минимум необходимых вещей, и отправились в плавание.
Через 3 дня плавания, в 5 часов утра, вы увидели берег какого-то острова. Первым делом, после высадки, вы решили, что нужно построить дом.
Для этого нужно дерево. Чтобы начать добывать его, нажмите кнопку "👷Добыча", а затем - кнопку "🌲Лес".''',
                              parse_mode='markdown', reply_markup=kb)


@mine_bot.message_handler(commands=['inventory'])
def inventory(m):
    x = mine_users.find_one({'id': m.from_user.id})
    if x != None:
        text = ''
        if x['coal'] > 0:
            text += 'Уголь: ' + str(x['coal']) + '\n'
        if x['iron'] > 0:
            text += 'Железо: ' + str(x['iron']) + '\n'
        if x['gold'] > 0:
            text += 'Золото: ' + str(x['gold']) + '\n'
        if x['diamond'] > 0:
            text += 'Алмазы: ' + str(x['diamond']) + '\n'
        if x['wood'] > 0:
            text += 'Дерево: ' + str(x['wood']) + '\n'
        if x['rock'] > 0:
            text += 'Камень: ' + str(x['rock']) + '\n'
        if x['money'] > 0:
            text += 'Деньги: ' + str(x['money']) + '\n'
        if x['sand'] > 0:
            text += 'Песок: ' + str(x['sand']) + '\n'
        if x['salt'] > 0:
            text += 'Соль: ' + str(x['salt']) + '\n'
        if x['ruby'] > 0:
            text += 'Рубины: ' + str(x['ruby']) + '\n'
        if x['iridium'] > 0:
            text += 'Иридий: ' + str(x['iridium']) + '\n'
        if x['shugar'] > 0:
            text += 'Сахар: ' + str(x['shugar']) + '\n'
        if x['mushroom'] > 0:
            text += 'Грибы: ' + str(x['mushroom']) + '\n'
        if x['meat'] > 0:
            text += 'Мясо: ' + str(x['meat']) + '\n'
        if x['fish'] > 0:
            text += 'Рыба: ' + str(x['fish']) + '\n'
        if x['egg'] > 0:
            text += 'Яйца: ' + str(x['egg']) + '\n'
        if x['water'] > 0:
            text += 'Вода: ' + str(x['water']) + '\n'
        if x['squama'] > 0:
            text += 'Чешуя: ' + str(x['squama']) + '\n'
        if x['seeds'] > 0:
            text += 'Семена: ' + str(x['squama']) + '\n'
        if x['cow'] > 0:
            text += 'Телёнок: ' + str(x['cow']) + '\n'
        if x['craftable']['cookedmeat'] > 0:
            text += 'Приготовленное мясо: ' + str(x['craftable']['cookedmeat']) + '\n'
        if x['craftable']['woodsword'] > 0:
            text += 'Деревянный меч: ' + str(x['craftable']['woodsword']) + '\n'
        if x['craftable']['hoe'] > 0:
            text += 'Мотыга: ' + str(x['craftable']['hoe']) + '\n'
        if x['craftable']['bucket'] > 0:
            text += 'Ведро: ' + str(x['craftable']['bucket']) + '\n'
        if text == '':
            text = 'Инвентарь пуст!'
        mine_bot.send_message(m.chat.id, text)




@mine_bot.message_handler(commands=['furnance'])
def furnance(m):
    x = mine_users.find_one({'id': m.from_user.id})
    if 'furnance' in x['recipes']:
        if x['craftable']['furnance'] <= 0:
            if x['rock'] >= 100 and x['wood'] >= 10 and x['hunger'] >= 30:
                mine_users.update_one({'id': m.from_user.id}, {'$inc': {'rock': -100}})
                mine_users.update_one({'id': m.from_user.id}, {'$inc': {'wood': -10}})
                mine_users.update_one({'id': m.from_user.id}, {'$inc': {'hunger': -30}})
                mine_users.update_one({'id': m.from_user.id}, {'$inc': {'craftable.furnance': 1}})
                mine_bot.send_message(m.chat.id, 'Вы успешно скрафтили Печь!')
            else:
                mine_bot.send_message(m.chat.id, 'Недостаточно ресурсов!')
        else:
            mine_bot.send_message(m.chat.id, 'У вас уже есть Печь!')
    else:
        mine_bot.send_message(m.chat.id, 'У вас нет этого рецепта!')


@mine_bot.message_handler(commands=['meat'])
def meat(m):
    x = mine_users.find_one({'id': m.from_user.id})
    if 'cookedmeat' in x['recipes']:
        if x['craftable']['furnance'] >= 1:
            if x['meat'] >= 1 and x['coal'] >= 1:
                mine_users.update_one({'id': m.from_user.id}, {'$inc': {'coal': -1}})
                mine_users.update_one({'id': m.from_user.id}, {'$inc': {'meat': -1}})
                mine_users.update_one({'id': m.from_user.id}, {'$inc': {'craftable.cookedmeat': 1}})
                mine_bot.send_message(m.chat.id, 'Вы успешно скрафтили Приготовленное мясо!')
            else:
                mine_bot.send_message(m.chat.id, 'Недостаточно ресурсов!')
        else:
            mine_bot.send_message(m.chat.id, 'Для крафта вам нужно: Печь.')
    else:
        mine_bot.send_message(m.chat.id, 'У вас нет этого рецепта!')


@mine_bot.message_handler(commands=['bucket'])
def meat(m):
    x = mine_users.find_one({'id': m.from_user.id})
    if 'bucket' in x['recipes']:
        if x['craftable']['furnance'] >= 1:
            if x['iron'] >= 25 and x['coal'] >= 5 and x['hunger'] >= 5:
                mine_users.update_one({'id': m.from_user.id}, {'$inc': {'coal': -5}})
                mine_users.update_one({'id': m.from_user.id}, {'$inc': {'iron': -25}})
                mine_users.update_one({'id': m.from_user.id}, {'$inc': {'hunger': -5}})
                mine_users.update_one({'id': m.from_user.id}, {'$inc': {'craftable.bucket': 1}})
                mine_bot.send_message(m.chat.id, 'Вы успешно скрафтили Ведро!')
            else:
                mine_bot.send_message(m.chat.id, 'Недостаточно ресурсов!')
        else:
            mine_bot.send_message(m.chat.id, 'Для крафта вам нужно: Печь.')
    else:
        mine_bot.send_message(m.chat.id, 'У вас нет этого рецепта!')


@mine_bot.message_handler(commands=['hoe'])
def hoe(m):
    x = mine_users.find_one({'id': m.from_user.id})
    if 'hoe' in x['recipes']:
        if x['wood'] >= 50 and x['rock'] >= 25 and x['hunger'] >= 10:
            mine_users.update_one({'id': m.from_user.id}, {'$inc': {'wood': -50}})
            mine_users.update_one({'id': m.from_user.id}, {'$inc': {'rock': -25}})
            mine_users.update_one({'id': m.from_user.id}, {'$inc': {'hunger': -10}})
            mine_users.update_one({'id': m.from_user.id}, {'$inc': {'craftable.hoe': 1}})
            mine_bot.send_message(m.chat.id, 'Вы успешно скрафтили Мотыгу!')
        else:
            mine_bot.send_message(m.chat.id, 'Недостаточно ресурсов!')
    else:
        mine_bot.send_message(m.chat.id, 'У вас нет этого рецепта!')


@mine_bot.message_handler(commands=['farm'])
def meat(m):
    x = mine_users.find_one({'id': m.from_user.id})
    if 'farm' in x['recipes']:
        if 'farm' not in x['buildings']:
            if x['wood'] >= 600 and x['rock'] >= 250 and x['water'] >= 20 and x['craftable']['hoe'] >= 1 and x[
                'hunger'] >= 70:
                mine_users.update_one({'id': m.from_user.id}, {'$inc': {'rock': -250}})
                mine_users.update_one({'id': m.from_user.id}, {'$inc': {'wood': -600}})
                mine_users.update_one({'id': m.from_user.id}, {'$inc': {'hunger': -70}})
                mine_users.update_one({'id': m.from_user.id}, {'$inc': {'craftable.hoe': -1}})
                mine_users.update_one({'id': m.from_user.id}, {'$push': {'buildings': 'farm'}})
                mine_bot.send_message(m.chat.id, 'Вы успешно построили Ферму!')
            else:
                mine_bot.send_message(m.chat.id, 'Недостаточно ресурсов!')
        else:
            mine_bot.send_message(m.chat.id, 'У вас уже есть это!')
    else:
        mine_bot.send_message(m.chat.id, 'У вас нет этого рецепта!')


@mine_bot.message_handler(commands=['fountain'])
def meat(m):
    x = mine_users.find_one({'id': m.from_user.id})
    if 'fountain' in x['recipes']:
        if 'fountain' not in x['buildings']:
            if x['wood'] >= 40 and x['rock'] >= 150 and x['craftable']['bucket'] >= 1 and x['hunger'] >= 50:
                mine_users.update_one({'id': m.from_user.id}, {'$inc': {'rock': -150}})
                mine_users.update_one({'id': m.from_user.id}, {'$inc': {'wood': -40}})
                mine_users.update_one({'id': m.from_user.id}, {'$inc': {'hunger': -50}})
                mine_users.update_one({'id': m.from_user.id}, {'$inc': {'craftable.bucket': -1}})
                mine_users.update_one({'id': m.from_user.id}, {'$push': {'buildings': 'fountain'}})
                mine_bot.send_message(m.chat.id, 'Вы успешно построили Колодец!')
            else:
                mine_bot.send_message(m.chat.id, 'Недостаточно ресурсов!')
        else:
            mine_bot.send_message(m.chat.id, 'У вас уже есть это!')
    else:
        mine_bot.send_message(m.chat.id, 'У вас нет этого рецепта!')


@mine_bot.message_handler(commands=['woodsword'])
def wsword(m):
    x = mine_users.find_one({'id': m.from_user.id})
    if 'woodsword' in x['recipes']:
        if x['wood'] >= 40 and x['hunger'] >= 15:
            mine_users.update_one({'id': m.from_user.id}, {'$inc': {'wood': -40}})
            mine_users.update_one({'id': m.from_user.id}, {'$inc': {'hunger': -15}})
            mine_users.update_one({'id': m.from_user.id}, {'$inc': {'craftable.woodsword': 1}})
            mine_bot.send_message(m.chat.id, 'Вы успешно скрафтили Деревянный меч!')
        else:
            mine_bot.send_message(m.chat.id, 'Недостаточно ресурсов!')
    else:
        mine_bot.send_message(m.chat.id, 'У вас нет этого рецепта!')


@mine_bot.message_handler(commands=['help'])
def help(m):
    mine_bot.send_message(m.chat.id, '*Что обозначают значки ⚪️,🔵,🔴,🔶 около добытых ресурсов?*\n' +
                          'Обозначают они редкость материалов:\n' +
                          '⚪️ - обычные;\n' +
                          '🔵 - редкие;\n' +
                          '🔴 - эпические;\n' +
                          '🔶 - легендарные.', parse_mode='markdown')


@mine_bot.message_handler(commands=['hunt'])
def huntt(m):
    x = mine_users.find_one({'id': m.from_user.id})
    if x['huntingto'] != None and x['hunting'] == 0:
        mine_users.update_one({'id': x['id']}, {'$set': {'hunting': 1}})

        y = mine_users.find_one({'id': x['huntingto']})
        chance = random.randint(1, 100)
        sword = 0
        if x['craftable']['woodsword'] > 0:
            sword -= 8
        if y['craftable']['woodsword'] > 0:
            sword += 8
        if chance + sword <= 50:
            mine_users.update_one({'id': x['id']}, {'$set': {'huntwin': 1}})
        else:
            pass
        mine_bot.send_message(m.chat.id, 'Вы решили напасть. Ожидайте результатов...')


@mine_bot.message_handler(content_types=['text'])
def text(m):
    mtext(m)


def seed0(id):
    mine_users.update_one({'id': id}, {'$set': {'seeding': 0}})


def seeding(id, x):
    mine_users.update_one({'id': id}, {'$inc': {'seeds': -x}})
    mine_users.update_one({'id': id}, {'$inc': {'wheat': x}})
    mine_users.update_one({'id': id}, {'$inc': {'water': -1}})
    mine_bot.send_message(id, 'Вы вырастили и собрали ' + str(x) + ' пшена! Потрачено: 1 (Вода).')
    mine_users.update_one({'id': id}, {'$set': {'farming': 0}})


def water(id):
    watertexts = ['Вы набрали воду в колодце. Полученные ресурсы:\n']
    water = random.randint(1, 5)
    recources = ''
    recources += 'Вода: ' + str(water) + '\n'
    text = random.choice(watertexts)
    mine_users.update_one({'id': id}, {'$inc': {'water': water}})
    mine_users.update_one({'id': id}, {'$set': {'farming': 0}})
    try:
        mine_bot.send_message(id, text + recources)
    except:
        pass





def tforest(id):
    kb = types.ReplyKeyboardMarkup()
    kb.add(types.KeyboardButton('🔨Постройка'))
    mine_users.update_one({'id': id}, {'$set': {'wood': 0}})
    try:
        mine_bot.send_message(id,
                         'Прошло пол часа. С помощью топора, который вы взяли с собой в путь, вы добыли 1000 ед. дерева -' +
                         ' Этого должно хватить на постройку дома. Чтобы начать постройку, нажмите кнопку "🔨Постройка", и выберите пункт "⛺️Дом".',
                              reply_markup=kb)
    except:
        pass


def thouse(id):
    kb = types.ReplyKeyboardMarkup()
    kb.add('Добыча')
    kb.add('Дом')
    kb.add('Обо мне')
    try:
        mine_bot.send_message(id,
                         'Поздравляю! Вы построили себе дом! Здесь вы сможете спастись от дикой природы и от холода.' +
                         ' Дальше выживать придётся самостоятельно. Но осторожнее: добывая ресурсы, вы можете встретить других игроков, и если' +
                         ' они будут сильнее вас - добычу придётся отдать.', reply_markup=kb)
    except:
        pass
    mine_users.update_one({'id': id}, {'$set': {'tutorial': 0}})

                     
def polling(pollingbot):
    pollingbot.polling(none_stop=True, timeout=600)  
    
timecheck()
x = mine_users.find({})
for ids in x:
    try:
        mine_bot.send_message(ids['id'], 'Бот был перезагружен! Если вы в этот момент добывали ресурсы, придется начать сначала. Приношу свои извенения за это.')
    except:
        pass
mine_users.update_many({}, {'$set': {
'farming': 0,
'building': 0,
'hunting': 0,
'huntingto': None,
'huntedby': None,
    
} })   
print('Apps seems to be launched.')
print(boottext)


#threading.Timer(1, polling, args=[fm_bot]).start() # Boot fabrica menegers
threading.Timer(1, polling, args=[mine_bot]).start()  #Boot minecraft
