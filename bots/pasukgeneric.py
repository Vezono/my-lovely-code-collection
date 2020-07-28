import telebot
import time
import random
import threading
from pymongo import MongoClient
import pyrogram
from pyrogram import Filters, Client
bot_id = bot.get_me().id
mainchat = -1001167374930
admin = 0
# noinspection SpellCheckingInspection
bot = telebot.TeleBot('')

lophrase = []
pasukid = 441399484

client1=''
client=MongoClient(client1)
db=client.loshadkin
phrases=db.phrases
lophrase = []
x = phrases.find_one({})
for ids in x:
    lophrase.append(x[ids])
lophrase.remove(lophrase[0])
print(len(lophrase))

# noinspection SpellCheckingInspection
def medit(message_text, chat_id, message_id, reply_markup=None, parse_mode='Markdown'):
    return bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=message_text, reply_markup=reply_markup,
                                 parse_mode=parse_mode)

api_id = 0
api_hash = ''
app = Client("my_account", api_id, api_hash)
@app.on_message()
def hello(client, message):
    app.send_message(-1001167374930, 'Скиньте мне мой номер телефона, я не могу залогинится')
    print(app.get_me())
    print(m.text + ' ' + m.from_user.first_name)
    print('done')


@bot.message_handler(commands=['count_of_phrases'])
def start(m):
    global lophrase
    lophrase = []
    x = phrases.find_one({})
    for ids in x:
        lophrase.append(x[ids])
    lophrase.remove(lophrase[0])
    bot.reply_to(m, str(len(lophrase)))

# noinspection SpellCheckingInspection
@bot.message_handler(commands=['getm'])
def start(m):
    bot.reply_to(m, str(m))

@bot.message_handler(commands=["talk"])
def gandoni(m):
    try:
        bot.delete_message(m.chat.id, m.message_id)
        text = m.text.split(' ', 1)[1]  
        if text == 'laguh':
            bot.send_sticker(m.chat.id, 'CAADAgADAwAD-ZeEHnikVOwYHk14Ag', reply_to_message_id = m.reply_to_message.message_id)
            trace = m.from_user.first_name + ' ' + text
            bot.send_message(admin, trace)
        elif text == 'cat':
            bot.send_sticker(m.chat.id, 'CAADAgADCwAD-ZeEHn8PdFdXHqZJAg', reply_to_message_id = m.reply_to_message.message_id)  
            trace = m.from_user.first_name + ' ' + text
            bot.send_message(admin, trace)
        else:
            bot.send_message(m.chat.id, text, reply_to_message_id = m.reply_to_message.message_id)
            trace = m.from_user.first_name + ' ' + text
            bot.send_message(admin, trace)
    except:
        try:
            text = m.text.split(' ', 1)[1]
            if text == 'laguh':
                bot.send_sticker(m.chat.id, 'CAADAgADAwAD-ZeEHnikVOwYHk14Ag')
                trace = m.from_user.first_name + ' ' + text
                bot.send_message(admin, trace)
            elif text == 'cat':
                bot.send_sticker(m.chat.id, 'CAADAgADCwAD-ZeEHn8PdFdXHqZJAg')
                trace = m.from_user.first_name + ' ' + text
                bot.send_message(admin, trace)
            else:
                bot.send_message(m.chat.id, text)
                trace = m.from_user.first_name + ' ' + text
                bot.send_message(admin, trace)
        except:
            bot.send_message(admin, traceback.format_exc())
@bot.message_handler(commands=["google"])
def cgoogle(m):
    google(m)
@bot.message_handler(content_types=['new_chat_members'])
def handler(m):
    if m.new_chat_members[0].id == bot_id:
        bot.reply_to(m, 'Ебло? Нахуя меня в рандомные чаты добавлять')
    elif m.new_chat_members[0].is_bot:
        bot.reply_to(m, 'Тут уже 1000000 твоих ботов')
    else:
        bot.reply_to(m, 'Добро пожаловать к нашему шалашу')

@bot.message_handler()
def texthandler(m):
    if pinloshadkin(m) or random.randint(1, 50) == 1:
        try:
            bot.reply_to(m, random.choice(lophrase))
        except:
            bot.reply_to(m, random.choice(lophrase))
    if m.forward_from is not None:
        if m.from_user.id == pasukid or m.forward_from.id == pasukid:
            phrases.update_one({}, {'$set': {str(random.randint(1, 1000000000000000000)):m.text}})
    else:
        if m.from_user.id == pasukid:
            phrases.update_one({}, {'$set': {str(random.randint(1, 1000000000000000000)):m.text}})
def pinloshadkin(m):
    loshadks = ['пасюк', 'loshadkin', 'лошадкин']
    for i in loshadks:
        if i in m.text.lower():
            yes = True
            break
        else:
            yes = False
    return yes
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
print('The message above is count of pasuk frases.')
#app.run()
bot.polling(none_stop=True, timeout=600)
