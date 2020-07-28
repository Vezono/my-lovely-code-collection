import telebot
bot = telebot.TeleBot('')
@bot.message_handler(content_types=['stickers'], func=lambda m: m.from_user.id == 930671372)
def handler(m): bot.delete_message(m.chat.id, m.messsage_id)
bot.polling(none_stop=True, timeout=600)
