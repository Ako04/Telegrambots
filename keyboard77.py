import telebot
from telebot import types

bot = telebot.TeleBot("2026663788:AAFPcGHaBIm-jwTJ6oovwqks6oEgC0DsUr4")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, "Mr.Qabdushev is the best teacher \n"
                     "in the College")

    keyboard = types.ReplyKeyboardMarkup(True, True, True, True)
    keyboard.row("1", "2", "3")
    keyboard.row("4", "5", "6")
    keyboard.row("7", "8", "9")
    keyboard.row("0")
    bot.send_message(message.chat.id, 'Calling number',
                     reply_markup=keyboard)
bot.polling()