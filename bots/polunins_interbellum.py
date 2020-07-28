from flask import Flask, request
from telebot import TeleBot, types
from pymongo import MongoClient
from config import *
import threading
import time

bot = TeleBot(token=token)
bot.remove_webhook()
bot.set_webhook(url=WEBHOOK_URL)

app = Flask(__name__)

client = MongoClient(mongo)
db = client.db
games = db.games
players = db.players
game_types = db.game_types


@bot.message_handler(commands=['newgame'])
def start_game(msg):
    if msg.from_user.id in GLOBALADMINS:
        if msg.chat.type != 'supergroup':
            bot.send_message(msg.chat.id, 'Сделайте группу супергуппой')
            return 0

        if not bot_have_all_rights(bot.get_chat_member(msg.chat.id, BOT)):
            bot.send_message(msg.chat.id, 'Для начала игры необходимо дать боту все права администратора')
            return 0
        games.insert_one(
            {'game_id': msg.chat.id, 'floodilka': msg.chat.id, 'admin': msg.from_user.id, 'players': [], 'type': '1997', 'countries': [], 'status': 'wait_for_players'})
        bot.send_message(msg.chat.id, 'Запущен процесс создания игры. Новые игроки могут присоеденится с помощью следующего сообщения:')
        bot.send_message(msg.chat.id, '/join %s' % (msg.chat.id, ))
        bot.send_message(msg.chat.id, 'Отныне этот чат становится моей собственностью. Я буду делать тут все, что пожелаю нужным.\n'
                                          'Этот чат будет флудилкой для игры. Пожалуйста, создайте еще несколько чатов:\n'
                                          '1. Официальный чат, в котором будет происходить общение\n'
                                          '2. Канал, где будут выкладываться новости игры\n'
                                          '3. Чат для проведения ивентов\n'
                                          'Все чаты необходимо сделать супергруппами. Во всех чатах необходимо дать боту права администратора.\n'
                                          'После создания чата, напишите в них следующее:\n'
                                          '1. /officialchat %s\n'
                                          '2. channel %s (в самом канале)\n'
                                          '3. /eventchat %s\n' % (msg.chat.id, msg.chat.id, msg.chat.id))


@bot.message_handler(commands=['officialchat'])
def set_official_chat(msg):
    if msg.from_user.id in GLOBALADMINS:
        text = msg.text.split()
        if len(text) != 2:
            bot.send_message(msg.chat.id, '/officialchat <id_игры>')
            return 0
        if msg.chat.type != 'supergroup':
            bot.send_message(msg.chat.id, 'Сделайте группу супергуппой')
            return 0

        if not bot_have_all_rights(bot.get_chat_member(msg.chat.id, BOT)):
            bot.send_message(msg.chat.id, 'Необходимо дать боту все права администратора')
            return 0
        games.update_one({'game_id': int(text[1])}, {'$set': {'official_chat': msg.chat.id}})
        bot.send_message(msg.chat.id, 'Теперь это официальный чат')


@bot.channel_post_handler(func=lambda msg: msg.text.split()[0] == 'channel')
def set_channel(msg):
    if not bot_have_all_rights(bot.get_chat_member(msg.chat.id, BOT), is_channel=True):
        return 0
    try:
        game_id = int(msg.text.split()[1])
    except:
        return
    games.update_one({'game_id': game_id}, {'$set': {'channel': msg.chat.id}})


@bot.message_handler(commands=['eventchat'])
def set_event_chat(msg):
    if msg.from_user.id in GLOBALADMINS:
        text = msg.text.split()
        if len(text) != 2:
            bot.send_message(msg.chat.id, '/eventchat <id_игры>')
            return
        if msg.chat.type != 'supergroup':
            bot.send_message(msg.chat.id, 'Сделайте группу супергуппой')
            return

        if not bot_have_all_rights(bot.get_chat_member(msg.chat.id, BOT)):
            bot.send_message(msg.chat.id, 'Необходимо дать боту все права администратора')
            return
        games.update_one({'game_id': int(text[1])}, {'$set': {'event_chat': msg.chat.id}})
        bot.send_message(msg.chat.id, 'Теперь это чат для ивентов')


@bot.message_handler(commands=['join'])
def join_to_game(msg):
    text = msg.text.split()
    if len(text) != 2:
        bot.send_message(msg.chat.id, '/join <id игры>')
        return
    if players.find_one({'user_id': msg.from_user.id}):
        bot.send_message(msg.chat.id, 'Вы уже учавствуете в игре')
        return
    game_id = int(text[1])
    game = games.find_one({'game_id': game_id})
    if not game:
        bot.send_message(msg.chat.id, 'Такой игры нет. Проверьте правильность id')
        return
    if game['status'] != 'wait_for_players':
        bot.send_message(msg.chat.id, 'Игра уже начата!')
        return
    games.update_one({'game_id': game_id}, {'$push': {'players': msg.from_user.id}})
    players.insert_one({
        'game_id': game_id,
        'user_id': msg.from_user.id,
        'country': '',
        'res': {
            'oil': 0,
            'money': 0,
            'food': 0,
            'army': 0,
            'defence': 0
        },
        'growth': {
            'oil': 0,
            'money': 0,
            'food': 0,
        },
        'pop_loyal': 0,
        'OI': 0,
        'contracts': {},
        'actions': [],
        'relations': {}
    })
    bot.send_message(msg.chat.id, 'Теперь вы должны выбрать свою страну. Введите: \n'
                                  '/country <TAG>\n'
                                  'Доступные страны:\n'
                                  'UKR - Украина\n'
                                  'BRI - Британия\n'
                                  'FRA - Франция\n'
                                  'USA - США\n'
                                  'RUS - Россия\n'
                                  'CHI - Китай\n'
                                  'BRA - Бразилия\n'
                                  'GER - Германия\n'
                                  'JAP - Япония\n'
                                  'POL - Польша\n'
                                  'SPA - Испания\n'
                                  'ITA - Италия')


@bot.message_handler(commands=['country'])
def set_country(msg):
    text = msg.text.split()
    if len(text) != 2:
        bot.send_message(msg.chat.id, '/country <TAG>')
        return
    tag = text[1]
    player = players.find_one({'user_id': msg.from_user.id})
    if not player:
        bot.send_message(msg.chat.id, 'Вы не в игре!')
        return
    if player['country']:
        bot.send_message(msg.chat.id, 'Вы уже выбрали страну')
        return
    game = games.find_one({'game_id': player['game_id']})
    if not game_types.find_one({'table': 'config', 'name': game['type'], 'countries': tag}):
        bot.send_message(msg.chat.id, 'Такой страны в данной игре нет')
        return
    if players.find_one({'game_id': player['game_id'], 'tag': tag}):
        bot.send_message(msg.chat.id, 'Данная страна уже занята!')
        return
    country = game_types.find_one({'table': 'countries'}, {tag: 1})[tag]
    players.update_one({'user_id': msg.from_user.id},
                       {
                           '$set': {
                               'country': tag,
                               'res.oil': country['start_res']['oil'],
                               'res.money': country['start_res']['money'],
                               'res.food': country['start_res']['food'],
                               'res.army': country['start_res']['army'],
                               'res.defence': country['start_res']['defence'],
                               'growth.oil': country['start_growth']['oil'],
                               'growth.money': country['start_growth']['money'],
                               'growth.food': country['start_growth']['food'],
                               'pop_loyal': country['pop_loyal'],
                               'OI': 3
                           }
                       })
    games.update_one({'game_id': player['game_id']}, {'$push': {'countries': tag}})
    bot.send_message(msg.chat.id, 'Вы окончательно зарегистрированы! Ждите начала игры!')


@bot.message_handler(commands=['startgame'])
def start_game(msg):
    player = players.find_one({'user_id': msg.from_user.id}, {'game_id': 1, '_id': 0})
    if not player:
        bot.send_message(msg.chat.id, 'Вы не зарегистрированы ни в одной игре')
        return
    game = games.find_one({'game_id': player['game_id']})
    if game['admin'] != msg.from_user.id:
        bot.send_message(msg.chat.id, 'Вы не администратор игры.')
        return
    games.update_one({'game_id': game['game_id']},
                     {
                         '$set': {
                             'status': 'playing',
                             'turn': 1,
                             'now_date': {
                                 'year': 1997,
                                 'month': 3
                             }
                         }
                     })
    for pl in game['players']:
        # for country in game['countries']:
        #     if country != pl['country']:
        bot.send_message(pl, 'Игра началась! Чтобы посмотреть список доступных действий, нажмите /turn')
    threading.Timer(86400, next_turn).start()


@bot.message_handler(commands=['nextturn'])
def nextturn(msg):
    if msg.from_user.id in GLOBALADMINS:
        next_turn()


def send_actions(user_id):
    kb = types.ReplyKeyboardMarkup()
    pl = players.find_one({'user_id': user_id}, {'game_id': 1, 'country': 1, '_id': 0})
    type_game = games.find_one({'game_id': pl['game_id']}, {'type': 1, '_id': 0})['type']
    for name_action in game_types.find_one({'name': type_game, 'table': 'config'}, {'actions': 1, '_id': 0})['actions'].keys():
        kb.add(types.KeyboardButton('{}'.format(name_action)))
    for name_action in game_types.find_one({'name': type_game, 'table': 'countries'}, {'{}.actions'.format(pl['country']): 1, '_id': 0})[
        pl['country']]['actions'].keys():
        kb.add(types.KeyboardButton('{}'.format(name_action)))
    bot.send_message(user_id, 'Ход', reply_markup=kb)
    return type_game, pl['country']


def send_info_about_action(msg, *args):
    action_name = msg.text
    type_game, country = args

    action = game_types.find_one({'name': type_game, 'table': 'config', 'actions.{}'.format(action_name): {'$exists': True}},
                                 {'actions.{}'.format(action_name): 1, '_id': 0})
    if not action:
        action = game_types.find_one({'name': type_game, 'table': 'countries', '{}.actions.{}'.format(country, action_name): {'$exists': True}},
                                     {'{}.actions.{}'.format(country, action_name): 1, '_id': 0})
    if not action:
        bot.send_message(msg.from_user.id, 'Нет такого действия')
        bot.register_next_step_handler_by_chat_id(msg.chat.id, send_info_about_action, type_game, country)
        return
    cost_text = ''
    try:
        action = action['actions'][action_name]
    except KeyError as e:
        print(action)
        action = action[country]['actions'][action_name]
    for key in action['cost']:
        if key == 'growth':
            cost_text += '└Прирост\n'
        if key == 'res':
            cost_text += '└Ресурсы\n'
        for key1 in action['cost'][key]:
            cost_text += '└-{}: {}\n'.format(key1, action['cost'][key][key1])

    award_text = ''
    for key in action['award']:
        if key == 'growth':
            award_text += '└Прирост\n'
        if key == 'res':
            award_text += '└Ресурсы\n'
        for key1 in action['award'][key]:
            award_text += '└-{}: {}\n'.format(key1, action['award'][key][key1])

    text = 'Имя: {}\n' \
           'Стоимость: \n{}\n' \
           'Выручка: \n{}\n'.format(action_name, cost_text, award_text)
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton('Выполнить', callback_data='run_action {}'.format(action_name)))
    bot.send_message(msg.chat.id, text, reply_markup=kb)


@bot.callback_query_handler(func=lambda c: c.data.startswith('run_action'))
def run_action_handler(call):
    action = call.data.split()[1]

    players.update_one({'user_id': call.from_user.id}, {'$push': {'actions': action}})

    player = players.find_one({'user_id': call.from_user.id})
    type_game = games.find_one({'game_id': player['game_id']}, {'type': 1})['type']
    act = find_act(type_game, player['country'], action)

    query = {'$inc': {}}
    for key in act['cost']:
        for res in act['cost'][key]:
            query['$inc']['{}.{}'.format(key, res)] = -act['cost'][key][res]
            player[key][res] -= act['cost'][key][res]
    for key in act['award']:
        for res in act['award'][key]:
            query['$inc']['{}.{}'.format(key, res)] = act['award'][key][res]
            player[key][res] -= act['award'][key][res]
    for res in player['res']:
        if player['res'][res] < 0:
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.send_message(call.message.chat.id, 'Невозможно действие, так как количество {} станет {}'.format(res, player['res'][res]), reply_markup=types.ReplyKeyboardRemove())
            return
    players.update_one({'user_id': call.from_user.id}, query)

    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.send_message(call.message.chat.id, 'Ваше действие "{}" выполнено!'.format(action), reply_markup=types.ReplyKeyboardRemove())


@bot.message_handler(commands=['turn'])
def turn(msg):
    type_game, country = send_actions(msg.from_user.id)
    bot.register_next_step_handler_by_chat_id(msg.chat.id, send_info_about_action, type_game, country)


@bot.message_handler(commands=['me'])
def about_me(msg):
    player = players.find_one({'user_id': msg.from_user.id})
    res_text = ''
    for res in player['res']:
        res_text += '{}: {}\n'.format(res, player['res'][res])
    growth_text = ''
    for growth in player['growth']:
        growth_text += '{}: {}\n'.format(growth, player['growth'][growth])
    text = 'Страна: {}\n' \
           'Ресурсы: \n{}\n' \
           'Прирост: \n{}\n' \
           'ОЛ: {}/100\n' \
           'ОИ: {}/3\n' \
           'id: `{}`'.format(player['country'], res_text, growth_text, player['pop_loyal'], player['OI'], player['user_id'])
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton('Контракты', callback_data='show_contracts {}'.format(player['user_id'])))
    kb.add(types.InlineKeyboardButton('Действия', callback_data='show_actions {}'.format(player['user_id'])))
    #kb.add(types.InlineKeyboardButton('Дипломатия', callback_data='show_diplomacy {}'.format(player['user_id'])))
    bot.send_message(msg.chat.id, text, reply_markup=kb, parse_mode='Markdown')


@bot.callback_query_handler(func=lambda c: c.data.startswith('show_diplomacy'))
def show_diplomacy(call):
    text = call.data.split()
    if call.from_user.id != int(text[1]):
        bot.answer_callback_query(call.id, 'Не ваше меню :(')
        return
    player = players.find_one({call.from_user.id}, {'relations': 1, 'game_id': 1})
    relations = player['relations']
    game_id = player['game_id']
    text = 'Отношения:\n'
    for key in relations:
        text += '*{}*: `{}`\n'.format(key, relations[key])
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton('Объявить войну', callback_data='call_war {} {}'.format(call.from_user.id, game_id)))
    kb.add(types.InlineKeyboardButton('Заключить союз', callback_data='create_union {} {}'.format(call.from_user.id, game_id)))


@bot.callback_query_handler(func=lambda c: c.data.split()[1] in ['call_war', 'create_union'])
def diplomacy(call):
    action, user_id, game_id = call.data.split()
    user_id = int(user_id)
    if user_id != call.from_user.id:
        bot.answer_callback_query(call.id, 'Не ваше меню!')
        return
    tags = games.find_one({'game_id'})
    text = 'Введите тег страны.\n' \
           'Доступные: {}'


@bot.inline_handler(func=lambda q: True)
def inline_query_handler(query):
    pass


@bot.message_handler(commands=['set'])
def set_data(msg):
    try:
        player = players.find_one({'user_id': msg.reply_to_message.from_user.id}, {'user_id': 1, 'game_id': 1})
    except:
        return
    if not player:
        bot.send_message(msg.chat.id, 'Этот человек не играет')
        return
    admin = games.find_one({'game_id': player['game_id']}, {'admin': 1, '_id': 0})['admin']
    if admin != msg.from_user.id:
        bot.send_message(msg.chat.id, 'Вы не администратор игры')
        return
    # /set <res|gro> <type> <count>
    data = msg.text.split()
    if len(data) == 4:
        temp, target, type_res, count = msg.text.split()
        target = 'res' if target == 'res' else 'growth'
        players.update_one({'user_id': player['user_id']}, {
            '$inc': {
                '{}.{}'.format(target, type_res): int(count)
            }
        })
    elif len(data) == 3:
        temp, type_res, count = msg.text.split()
        players.update_one({'user_id': player['user_id']}, {
            '$inc': {
                '{}'.format(type_res): int(count)
            }
        })
    else:
        bot.send_message(msg.chat.id, '/set <res|gro> <type> <count>')
        return
    bot.send_message(msg.chat.id, '{} было добавлено {} {}'.format(msg.reply_to_message.from_user.first_name, count, type_res))


@bot.message_handler(commands=['id'])
def get_user_id(msg):
    try:
        bot.send_message(msg.chat.id, msg.reply_to_message.from_user.id)
    except:
        pass


def find_act(game_type, country, action):
    act = game_types.find_one(
        {'name': game_type, 'table': 'config', 'actions.{}'.format(action): {'$exists': True}},
        {'actions.{}'.format(action): 1, '_id': 0})
    if not act:
        act = game_types.find_one({'name': game_type, 'table': 'countries',
                                   '{}.actions.{}'.format(country, action): {'$exists': True}},
                                  {'{}.actions.{}'.format(country, action): 1, '_id': 0})[country]['actions'][action]
    else:
        act = act['actions'][action]
    return act


def next_turn():
    gms = games.find()
    for game in gms:
        for player_id in game['players']:
            player = players.find_one({'user_id': player_id})
            query = {'$inc': {}}
            for res in player['growth']:
                query['$inc']['res.{}'.format(res)] = player['growth'][res]
            players.update_one({'user_id': player_id}, query)
            bot.send_message(player_id, 'Начался новый ход!')
        games.update_one({'game_id': game['game_id']}, {'$inc': {'turn': 1}})
    threading.Timer(86400, next_turn).start()


def bot_have_all_rights(member, is_channel=False):
    if is_channel:
        return member.can_post_messages
    else:
        return member.can_delete_messages and member.can_invite_users and member.can_promote_members and member.can_restrict_members


@app.route('/%s' % token, methods=['POST'])
def get_message():
    bot.process_new_updates([types.Update.de_json(request.stream.read().decode('UTF-8'))])
    return 'ok', 200


app.run(host='0.0.0.0', port=port)
bot.remove_webhook()
