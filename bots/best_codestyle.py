import threading
from pyrogram import Client
bot = Client("my_account")
chat = -347301545
def zopa():
    bot.send_message(chat, 'kaka')
    bot.send_message(chat, 'kaka')
    t=threading.Timer(60, zopa)
@bot.on_message()
def f(pisos, m):
    print(m)
bot.run()
zopa()
print('7777')
