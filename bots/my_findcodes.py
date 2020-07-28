import random
import threading

from telebot import TeleBot, types

from config import creator

bot = TeleBot('')

games = dict()
roles = {'general': {'cabinet': 300,
                     'actions': ['hear', 'see', 'go_to_cabinet', 'nothing', 'arrest'],
                     'desc': '👨🏻‍✈️Ты генерал. Ты не можешь быть шпионом. Найди его! Твой кабинет: 300.',
                     'spy': '',
                     'no_spy': '',
                     'al': 3
                     },

         'secretar': {'cabinet': 200,
                      'actions': ['hear', 'see', 'steal_a_card', 'go_to_cabinet', 'nothing'],
                      'desc': '👨🏼‍💻Ты секретарь. Ты слышишь все, т.к сидишь на месте секретаря. Твой кабинет: 200.',
                      'spy': '\n\nТы шпион! Слушай все что происходит в здании и ищи коды, которые спрятал генерал!',
                      'no_spy': '\n\nТы не шпион, но если узнаешь кто это - донеси генералу!',
                      'al': 2
                      },
         'cleaner': {'cabinet': 100,
                     'actions': ['hear', 'see', 'steal_a_card', 'go_to_cabinet', 'nothing'],
                     'desc': '👩🏻🧹Ты просто уборщица. У тебя нет способностей.( Твой кабинет (если это можно назвать кабинетом): 100',
                     'spy': '\n\nТы шпион! Убирайся в здании и незаметно ищи коды, которые спрятал генерал!',
                     'no_spy': '\n\nТы не шпион, но если узнаешь кто это - донеси генералу! Хотя ты не любимчик генерала, вряд ли тебе кто поверит.',
                     'al': 1
                     },

         }
rusificate = {
    'general': '👨🏻‍✈️Генерал',
    'secretar': '👨🏼‍💻Секретарь',
    'cleaner': '👩🏻🧹Уборщица',
    'hear': 'Слушать',
    'see': 'Подсматривать',
    'steal_a_key': 'Украсть ключ',
    'go_to_cabinet': 'Прогулятся',
    'nothing': 'Отдыхать',
    'arrest': 'Аррестовать',
    'steal_a_card': 'Украсть AL'
}
emojize = {
    'general': '👨🏻‍✈️',
    'secretar': '👨🏼‍💻',
    'cleaner': '👩🏻🧹'
}
rolelist = ['general', 'secretar', 'cleaner']


@bot.message_handler(commands=['newgame'])
def game(m):
    if m.from_user.id != creator:
        return
    games[m.chat.id] = creategame()
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton('Присоеденится',
                                      url='t.me/' + bot.get_me().username + '?start={}'.format(m.chat.id)))
    bot.send_message(m.chat.id, 'Начался подбор в игру! для регистрации нажмите на кнопку ниже...', reply_markup=kb)


@bot.message_handler(commands=['start'], func=lambda m: m.chat.type == 'private')
def start(m):
    game_id = int(m.text.split()[1])
    game_exists = False
    for i in games.keys():
        if game_id == i:
            game_exists = True
            break
    if not game_exists:
        return
    if len(games[game_id]['players']) > 3:
        bot.send_message(m.chat.id, 'Вы не можете присоединится! Достигнуто маскимальное кол-во игроков.')
        return
    if m.from_user.id in games[game_id]['users']:
        bot.send_message(m.chat.id, 'Вы уже в игре!')
        return
    if games[game_id]['active']:
        bot.send_message(m.chat.id, 'Игра уже началась!')
        return
    temp_roles = games[game_id]['roles']
    try:
        temp_role = rolelist[len(temp_roles)]
    except:
        bot.send_message(m.chat.id, 'Вы не можете присоединится! Достигнуто маскимальное кол-во игроков.')
        return
    if temp_role != 'general' and games[game_id]['spy'] is None:
        spy = random.choice([True, False])
        games[game_id]['spy'] = m.from_user.id
    else:
        spy = False
    games[game_id]['players'].append(createuser(temp_role, m.from_user.id, m.from_user.first_name, spy))
    games[game_id]['roles'].append(temp_role)
    games[game_id]['users'].append(m.from_user.id)
    bot.send_message(m.chat.id, 'Вы присоеденились к игре.')
    bot.send_message(game_id, rusificate[temp_role] + ' ' + m.from_user.first_name + ' присоединился к игре!')


@bot.message_handler(commands=['debug'])
def debuj(m):
    if m.from_user.id == creator:
        bot.send_message(m.chat.id, str(games).replace('{', '\n{\n').replace('}', '\n}\n'))


@bot.message_handler(commands=['пудж'])
def addplayer(m):
    if m.from_user.id != creator:
        return
    try:
        chat = m.chat.id
    except:
        return
    if len(games[chat]['players']) > 3:
        bot.send_message(m.chat.id, 'Он не может присоединится! Достигнуто маскимальное кол-во игроков.')
        return
    if m.reply_to_message.from_user.id in games[chat]['users']:
        bot.send_message(m.chat.id, 'Он уже в игре!')
        # return
    if games[chat]['active']:
        bot.send_message(m.chat.id, 'Игра уже началась!')
        return
    temp_roles = games[chat]['roles']
    try:
        temp_role = rolelist[len(temp_roles)]
    except:
        bot.send_message(m.chat.id, 'Он не можете присоединится! Достигнуто маскимальное кол-во игроков.')
        temp_role = 'None'
    if temp_role != 'general' and games[chat]['spy'] is None:
        spy = random.choice([True, False])
        games[chat]['spy'] = m.reply_to_message.from_user.id
    else:
        spy = False
    games[chat]['players'].append(
        createuser(temp_role, m.reply_to_message.from_user.id, m.reply_to_message.from_user.first_name))
    games[chat]['roles'].append(temp_role)
    games[chat]['users'].append(m.reply_to_message.from_user.id)
    bot.send_message(chat,
                     rusificate[temp_role] + ' ' + m.reply_to_message.from_user.first_name + ' присоединился к игре!')


@bot.message_handler(commands=['kick'])
def addplayer(m):
    if m.from_user.id != creator:
        return
    game_id = m.chat.id
    chat = game_id
    if m.reply_to_message.from_user.id not in games[chat]['users']:
        bot.send_message(m.chat.id, 'Он еще не в игре!')
        return
    im = 0
    for i in range(len(games[game_id]['users'])):
        if games[game_id]['players'][i]['id'] == m.reply_to_message.from_user.id:
            im = i
            break
    temp_role = games[game_id]['players'][im]['role']
    games[chat]['players'].remove(
        createuser(temp_role, m.reply_to_message.from_user.id, m.reply_to_message.from_user.first_name))
    games[chat]['roles'].remove(temp_role)
    games[chat]['users'].remove(m.reply_to_message.from_user.id)
    bot.send_message(chat, rusificate[temp_role] + ' ' + m.reply_to_message.from_user.first_name + ' удалился из игры!')


@bot.message_handler(commands=['startgame'])
def start_game(m):
    if m.from_user.id != creator:
        return
    game_id = m.chat.id
    game_exists = False
    for i in games.keys():
        if game_id == i:
            game_exists = True
            break
    if not game_exists:
        bot.send_message(m.chat.id, 'Игра еще не создана!')
        return
    games[game_id]['active'] = True
    for i in range(len(games[game_id]['users'])):
        desc = roles[games[game_id]['roles'][i]]['desc']
        if games[game_id]['players'][i]['spy']:
            desc += roles[games[game_id]['roles'][i]]['spy']
        else:
            desc += roles[games[game_id]['roles'][i]]['no_spy']
        bot.send_message(games[game_id]['users'][i], desc)
    bot.send_message(m.chat.id, 'Генерал выбирает где спрятать коды, пока работники еще спят...')
    general_id = games[game_id]['players'][0]['id']
    kb = types.InlineKeyboardMarkup()
    btns = list()
    btns2 = list()
    for cab in games[game_id]['cabinets']:
        if cab in [301, 302, 303, 304, 305]:
            btns.append(
                types.InlineKeyboardButton(cab, callback_data='first_hide_code_in {} {}'.format(cab, game_id)))
        elif cab in [201, 202, 203, 204, 205]:
            btns2.append(
                types.InlineKeyboardButton(cab, callback_data='first_hide_code_in {} {}'.format(cab, game_id)))
    kb.add(*btns)
    kb.add(*btns2)
    bot.send_message(general_id, 'Выберете, где спрячете коды...', reply_markup=kb)


@bot.callback_query_handler(lambda c: True)
def callback_handler(c):
    text = c.data.split()
    action = text[0]
    game_id = text[2]
    game_id = int(game_id)
    game_exists = False
    for i in games.keys():
        if game_id == i:
            game_exists = True
        break
    if not game_exists and not games[game_id]['active']:
        return
    if action == 'first_hide_code_in':
        cab_num = int(text[1])
        turn = games[game_id]['turn']
        games[game_id]['turn'] = turn + 1
        games[game_id]['codes'] = cab_num
        bot.edit_message_text('Вы спрятали коды в {} кабинете.'.format(cab_num), c.message.chat.id,
                              c.message.message_id)
        bot.send_message(game_id, 'Генерал ' + c.from_user.first_name + ' спрятал коды!')
        next_turn(game_id)
        return
    elif action == 'nothing':
        bot.edit_message_text('Вы решили сегодня отдыхать.', c.message.chat.id, c.message.message_id)
        return
    elif action == 'steal_a_card':
        kb = types.InlineKeyboardMarkup()
        btns = []
        for i in range(len(games[game_id]['users'])):
            if games[game_id]['players'][i]['name'] != c.from_user.first_name:
                btns.append(types.InlineKeyboardButton(games[game_id]['players'][i]['name'],
                                                       callback_data='2_steal_a_card {} {}'.format(str(i),
                                                                                                   game_id)))
        kb.add(*btns)
        bot.edit_message_text('У кого вы хотите украсть карточку доступа?', c.message.chat.id, c.message.message_id,
                              reply_markup=kb)
        return
    elif action == '2_steal_a_card':
        user = int(text[1])
        im = 0
        for i in range(len(games[game_id]['users'])):
            if games[game_id]['players'][i]['name'] == c.from_user.first_name:
                im = i
                break
        games[game_id]['players'][im]['al'] += games[game_id]['players'][user]['al']
        if games[game_id]['players'][im]['al'] > 3:
            games[game_id]['players'][im]['al'] = 3
        tts = 'Вы украли карточку доступа у {}. Теперь ваш уровень доступа: {}!'.format(
            games[game_id]['players'][user]['name'], str(games[game_id]['players'][im]['al']))
        bot.edit_message_text(tts, c.message.chat.id, c.message.message_id)
        games[game_id]['history'] += 'Сегодня у {} украли карточку доступа!\n'.format(
            games[game_id]['players'][user]['name'])
        games[game_id]['acts'].append(
            'Вы узнали, что {} украл карту доступа у {}!'.format(games[game_id]['players'][im]['name'],
                                                                 games[game_id]['players'][user]['name']))
        return
    elif action == 'see':
        im = 0
        for i in range(len(games[game_id]['users'])):
            if games[game_id]['players'][i]['name'] == c.from_user.first_name:
                im = i
                break
        games[game_id]['players'][im]['see'] = True
        bot.edit_message_text('Сегодня вы решили подсматривать.', c.message.chat.id, c.message.message_id)
        return
    elif action == 'hear':
        im = 0
        for i in range(len(games[game_id]['users'])):
            if games[game_id]['players'][i]['name'] == c.from_user.first_name:
                im = i
                break
        games[game_id]['players'][im]['see'] = True
        bot.edit_message_text('Сегодня вы решили слушать.', c.message.chat.id, c.message.message_id)
        return
    elif action == 'go_to_cabinet':
        im = 0
        for i in range(len(games[game_id]['users'])):
            if games[game_id]['players'][i]['name'] == c.from_user.first_name:
                im = i
                break
        kb = types.InlineKeyboardMarkup()
        btns = []
        for i in games[game_id]['cabinets']:
            if int(str(i)[0]) <= games[game_id]['players'][im]['al']:
                btns.append(types.InlineKeyboardButton(str(i), callback_data='2_go_to_cabinet {} {}'.format(str(i),
                                                                                                            game_id)))
        kb.add(*btns)
        bot.edit_message_text('В какой кабинет вы хотите пойти?', c.message.chat.id, c.message.message_id,
                              reply_markup=kb)
        return
    elif action == '2_go_to_cabinet':
        cab = int(text[1])
        im = 0
        for i in range(len(games[game_id]['users'])):
            if games[game_id]['players'][i]['name'] == c.from_user.first_name:
                im = i
                break
        if cab == games[game_id]['codes']:
            if games[game_id]['players'][im]['spy']:
                tts = 'Шпион {} нашел коды в {} кабинете! Он выиграл!'.format(games[game_id]['players'][im]['name'],
                                                                              str(cab))
                del games[game_id]
                bot.send_message(game_id, tts)
                bot.edit_message_text(tts, c.message.chat.id, c.message.message_id)
            else:
                games[game_id]['acts'].append(
                    'Вы узнали, что {} ходил в {} кабинет!'.format(games[game_id]['players'][im]['name'],
                                                                   str(cab)))
                games[game_id]['players'][im]['memory'] += 'Вы ничего не нашли в {} кабинете.'.format(str(cab))
                ptts = 'Вы собираетесь искать в {} кабинете.'.format(str(cab))
                bot.edit_message_text(ptts, c.message.chat.id, c.message.message_id)
        return
    elif action == 'arrest':
        kb = types.InlineKeyboardMarkup()
        btns = []
        for i in range(len(games[game_id]['users'])):
            if games[game_id]['players'][i]['name'] != c.from_user.first_name:
                btns.append(types.InlineKeyboardButton(games[game_id]['players'][i]['name'],
                                                       callback_data='2_arrest {} {}'.format(str(i), game_id)))
        kb.add(*btns)
        bot.edit_message_text('Кого вы хотите посадить в тюрьму?', c.message.chat.id, c.message.message_id,
                              reply_markup=kb)
        return
    elif action == '2_arrest':
        kb = types.InlineKeyboardMarkup()
        btns = []
        for i in range(len(games[game_id]['users'])):
            if games[game_id]['players'][i]['name'] != c.from_user.first_name:
                btns.append(types.InlineKeyboardButton(games[game_id]['players'][i]['name'],
                                                       callback_data='2_arrest {} {}'.format(str(i), game_id)))
        kb.add(*btns)
        tts = 'Вы аррестовали {}!'
        bot.edit_message_text(tts, c.message.chat.id, c.message.message_id)
        return


def next_turn(game_id):
    game_exists = False
    for i in games.keys():
        if game_id == i:
            game_exists = not game_exists
    if games[game_id]['active'] and game_exists:
        turn = games[game_id]['turn']
        workers = ''
        for i in range(len(games[game_id]['users'])):
            name = games[game_id]['players'][i]['name']
            role = rusificate[games[game_id]['players'][i]['role']]
            workers += '{} {}\n'.format(role, name)
        tts = 'День {}. У вас есть 60 секунд на ход и обсуждение ситуации...\n\n{}\nТекущие работники:\n{}'.format(
            str(turn), games[game_id]['history'], workers)
        bot.send_message(game_id, tts)
        games[game_id]['history'] = ''
        for i in range(len(games[game_id]['users'])):
            kb = types.InlineKeyboardMarkup()
            btns = []
            h = games[game_id]['players'][i]['actions']
            user = games[game_id]['players'][i]['id']
            role = games[game_id]['players'][i]['role']
            for ids in h:
                btns.append(
                    types.InlineKeyboardButton(rusificate[ids],
                                               callback_data='{} {} {}'.format(ids, str(user), str(game_id))))
            kb.add(*btns)
            if games[game_id]['players'][i]['see']:
                if games[game_id]['acts']:
                    bot.send_message(user, random.choice(games[game_id]['acts']))
                else:
                    bot.send_message(user, 'Вам ничего не удалось услышать!')
                    games[game_id]['players'][i]['see'] = False
            if games[game_id]['players'][i]['memory'] != '':
                bot.send_message(user, games[game_id]['players'][i]['memory'])
                games[game_id]['players'][i]['memory'] = ''
            if not games[game_id]['players'][i]['arrested']:
                tts = 'Что вы будете делать сегодня, {}?\n\nВаш уровень доступа: {}.'.format(rusificate[role],
                                                                                             games[game_id]['players'][
                                                                                                 i]['al'])
                bot.send_message(user, tts, reply_markup=kb)
            else:
                bot.send_message(user, 'Сегодня вы играли с бананом в тюрьме.', reply_markup=kb)
        games[game_id]['acts'] = []
        games[game_id]['turn'] = turn + 1
        threading.Timer(60, next_turn, [game_id]).start()
    else:
        return


def creategame():
    return {
        'players': [],
        'cabinets': [100, 101, 102, 103, 104, 105, 200, 201, 202, 203, 204, 205, 300, 301, 302, 303, 304, 305],
        'codes': None,
        'roles': [],
        'users': [],
        'spy': None,
        'turn': 0,
        'history': '',
        'acts': [],
        'active': False,
    }


def createuser(role, user, name, spy='None'):
    return {
        'id': user,
        'name': name,
        'role': role,
        'cabinet': roles[role]['cabinet'],
        'al': roles[role]['al'],
        'actions': roles[role]['actions'],
        'spy': spy,
        'see': False,
        'memory': '',
        'arrested': False
    }


boottext = bot.get_me().username + ' is started!'
print(boottext.capitalize())
bot.polling(none_stop=True, timeout=600)
