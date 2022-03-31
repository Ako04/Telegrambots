import telebot
from telebot import types

TOKEN = "2022745357:AAHk9ZHJF7ixt_xDmLCSJPzljpd0OBWMexY"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    h1 = types.InlineKeyboardButton(text="1st course", callback_data="1st")
    h2 = types.InlineKeyboardButton(text="2nd course", callback_data="2nd")
    h3 = types.InlineKeyboardButton(text="3rd course", callback_data="3rd")
    h4 = types.InlineKeyboardButton(text="4th course", callback_data="4th")
    h5 = types.InlineKeyboardButton(text="5th course", callback_data="5th")
    h6 = types.InlineKeyboardButton(text="6th course", callback_data="6th")
    keyboard.add(h1, h2, h3, h4, h5, h6)
    bot.send_message(message.chat.id, 'Please choose your course', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call:True)
def call_in(call):
    if call.data == "1st":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        f1 = types.InlineKeyboardButton(text="1F-1", callback_data="f1")
        f2 = types.InlineKeyboardButton(text="1F-2", callback_data="f2")
        a1 = types.InlineKeyboardButton(text="1A", callback_data="fa")
        d1 = types.InlineKeyboardButton(text="1D", callback_data="d1")
        keyboard.add(f1, f2, a1, d1)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Choose your class", reply_markup=keyboard)

    if call.data == "2nd":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        g2 = types.InlineKeyboardButton(text="2G", callback_data="g2")
        d2 = types.InlineKeyboardButton(text="2D", callback_data="d2")
        b1 = types.InlineKeyboardButton(text="2B-1", callback_data="b1")
        b2 = types.InlineKeyboardButton(text="2B-2", callback_data="b2")
        keyboard.add(g2, d2, b1, b2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="replaced text", reply_markup=keyboard)


bot.polling()