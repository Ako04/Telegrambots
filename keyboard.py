import telebot
from telebot import types

bot = telebot.TeleBot("1973229800:AAFb3qSDuXD52bS0NhJg4tJHugWfQdqKfRQ")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, "Mr.Qabdushev is the best teacher \n"
                     "in the College")

    keyboard = types.ReplyKeyboardMarkup(True, True, True)
    keyboard.row("1")
    keyboard.row("2")
    keyboard.row("3")
    bot.send_message(message.chat.id, 'Kim sagan unaidy',
                     reply_markup=keyboard)
bot.polling()