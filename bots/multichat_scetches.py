import telebot
from pymongo import MongoClient

client1 = ''
client = MongoClient(client1)
users = client.multichat.users
bot_token = ''
bot = telebot.TeleBot(bot_token)

global_admins = [930671372]
main_admin_id = 930671372


def medit(message_text, chat_id, message_id, reply_markup=None, parse_mode='Markdown'):
    return bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=message_text, reply_markup=reply_markup,
                                 parse_mode=parse_mode)


@bot.message_handler(commands=['start'])
def start(m):
    if not users.find_one({'id': m.from_user.id}):
        users.insert(createuser(m))
        bot.send_message(m.from_user.id,
                         '[BOT] Добро пожаловать в чат! '
                         'Так как ты новенький, ты попал в основной чат. Жми /nick что-бы изменить имя!.')
        sendm(m, 'newbie', 0)
    elif not users.find_one({'id': m.from_user.id}):
        users.update_one({id: m.from_user.id}, {'currentchatid': 0})
        bot.send_message(m.from_user.id,
                         '[BOT] Так как вы не находились ни в одном чате, мы вас перенаправили в основной.')
        sendm(m, 'join', 0)


@bot.message_handler(commands=['nick'])
def nikk(m):
    if not m.text.lower().count(' '):
        x = users.find_one({'tgid': m.from_user.id})
        nick = m.text.split(' ')[1]
        lastnick = x['lastnick']
        users.update_one({id: m.from_user.id}, {'lastnick': lastnick})
        users.update_one({id: m.from_user.id}, {'nick': nick})
        chat = x['currentchatid']
        sendm(m, 'changenick', chat)


@bot.message_handler()
def appendix(m):
    x = users.find_one({'tgid': m.from_user.id})
    chat = x['currentchatid']
    sendm(m, 'text', chat)
def createuser(m):
    commit = {
        'tgid': m.from_user.id,
        'nick': 'Без имени',
        'status': 'user',
        'currentchatid': 0,
        'lastnick': 'Без имени'
    }
    return commit


def sendm(m, action, chat):
    fromuser = users.find_one({'tgid': m.from_user.id})
    if action == 'newbie':
        x = users.find_all({'currentchatid': chat})
        for ids in x:
            bot.send_message(ids['tgid'], '[BOT] ' + fromuser['nick'] + ' вступил в чат! Он новенький в боте!')
    elif action == 'join':
        x = users.find_all()
        for ids in x:
            bot.send_message(ids['tgid'], '[BOT] ' + fromuser['nick'] + ' вступил в чат!')
    elif action == 'changenick':
        x = users.find_all()
        for ids in x:
            bot.send_message(ids['tgid'], '[BOT] ' + fromuser['nick'] + ' поменял ник! Он был ' + fromuser['lastnick'])
    elif action == 'text':
        x = users.find_all()
        for ids in x:
            bot.send_message(ids['tgid'], fromuser['nick'] + ': ' + m.text)

print('777')
bot.polling(none_stop=True, timeout=600)
