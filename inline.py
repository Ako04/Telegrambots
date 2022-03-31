import telebot
from telebot import types

TOKEN = "2019139517:AAG9AICcMk2gxHN23PYp_ZoD7h_zhEDHcac"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    h1 = types.InlineKeyboardButton(text="Figma", callback_data="1st")
    h2 = types.InlineKeyboardButton(text="Design", callback_data="2nd")
    h3 = types.InlineKeyboardButton(text="Flutter", callback_data="3rd")
    h4 = types.InlineKeyboardButton(text="SMM", callback_data="4th")
    h5 = types.InlineKeyboardButton(text="WEB", callback_data="5th")
    h6 = types.InlineKeyboardButton(text="HTML", callback_data="6th")
    keyboard.add(h1, h2, h3, h4, h5, h6)
    bot.send_message(message.chat.id, 'Please choose your course', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call:True)
def call_in(call):
    if call.data == "1st":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        f1 = types.InlineKeyboardButton(text="online", callback_data="f1")
        f2 = types.InlineKeyboardButton(text="beginner", callback_data="f2")
        a1 = types.InlineKeyboardButton(text="next level", callback_data="fa")
        d1 = types.InlineKeyboardButton(text="developer", callback_data="d1")
        keyboard.add(f1, f2, a1, d1)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Choose your class", reply_markup=keyboard)

    if call.data == "2nd":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        g2 = types.InlineKeyboardButton(text="1-course", callback_data="g2")
        d2 = types.InlineKeyboardButton(text="2-course", callback_data="d2")
        b1 = types.InlineKeyboardButton(text="3-course", callback_data="b1")
        b2 = types.InlineKeyboardButton(text="4-course", callback_data="b2")
        keyboard.add(g2, d2, b1, b2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="replaced text", reply_markup=keyboard)

    if call.data == "3rd":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        g2 = types.InlineKeyboardButton(text="Frilance", callback_data="g2")
        d2 = types.InlineKeyboardButton(text="Animation", callback_data="d2")
        b1 = types.InlineKeyboardButton(text="Mobile", callback_data="b1")
        b2 = types.InlineKeyboardButton(text="Promo", callback_data="b2")
        keyboard.add(g2, d2, b1, b2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="replaced text", reply_markup=keyboard)

    if call.data == "4th":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        g2 = types.InlineKeyboardButton(text="4GH", callback_data="g2")
        d2 = types.InlineKeyboardButton(text="2HI", callback_data="d2")
        b1 = types.InlineKeyboardButton(text="2GH-1", callback_data="b1")
        b2 = types.InlineKeyboardButton(text="2HI-2", callback_data="b2")
        keyboard.add(g2, d2, b1, b2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="replaced text", reply_markup=keyboard)

    if call.data == "5th":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        g2 = types.InlineKeyboardButton(text="2GH", callback_data="g2")
        d2 = types.InlineKeyboardButton(text="2HI", callback_data="d2")
        b1 = types.InlineKeyboardButton(text="2GH-1", callback_data="b1")
        b2 = types.InlineKeyboardButton(text="2HI-2", callback_data="b2")
        keyboard.add(g2, d2, b1, b2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="replaced text", reply_markup=keyboard)

    if call.data == "6th":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        g2 = types.InlineKeyboardButton(text="Java", callback_data="g2")
        d2 = types.InlineKeyboardButton(text="CSS", callback_data="d2")
        b1 = types.InlineKeyboardButton(text="html/css", callback_data="b1")
        b2 = types.InlineKeyboardButton(text="design", callback_data="b2")
        keyboard.add(g2, d2, b1, b2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="replaced text", reply_markup=keyboard)


bot.polling()