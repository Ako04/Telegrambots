import telebot
from telebot import types

bot = telebot.TeleBot("2022745357:AAHk9ZHJF7ixt_xDmLCSJPzljpd0OBWMexY")

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    web = types.InlineKeyboardButton(text="html course", callback_data="1st")
    design = types.InlineKeyboardButton(text="figma course", callback_data="2nd")
    mobile = types.InlineKeyboardButton(text="android course", callback_data="3rd")
    video = types.InlineKeyboardButton(text="mobilograph course", callback_data="4th")
    security = types.InlineKeyboardButton(text="system admin course", callback_data="5th")
    social = types.InlineKeyboardButton(text="smm course", callback_data="6th")
    keyboard.add(web, design, mobile, video, security, social)
    bot.send_message(message.chat.id, "Hello my friend! Select your course", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call:True)
def call_in(call):
    if call.data =="1st":
        keyboard = types.ReplyKeyboardMarkup(row_width=2)
        f1 = types.InlineKeyboardButton(text="3I", callback_data="f1")
        f2 = types.InlineKeyboardButton(text="3G", callback_data="f2")
        f3 = types.InlineKeyboardButton(text="3C", callback_data="f3")
        f4 = types.InlineKeyboardButton(text="3F", callback_data="f4")
        f5 = types.InlineKeyboardButton(text="3H", callback_data="f5")
        f6 = types.InlineKeyboardButton(text="4E", callback_data="f6")
        keyboard.add(f1, f2, f3, f4, f5, f6)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="replaced text", reply_markup=keyboard)


    if call.data =="2nd":
        keyboard = types.ReplyKeyboardMarkup(row_width=2)
        d1 = types.InlineKeyboardButton(text="3I", callback_data="d1")
        d2 = types.InlineKeyboardButton(text="3G", callback_data="d2")
        d3 = types.InlineKeyboardButton(text="3C", callback_data="d3")
        d4 = types.InlineKeyboardButton(text="3F", callback_data="d4")
        d5 = types.InlineKeyboardButton(text="3H", callback_data="d5")
        d6 = types.InlineKeyboardButton(text="4E", callback_data="d6")
        keyboard.add(d1, d2, d3, d4, d5, d6)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="replaced text", reply_markup=keyboard)

bot.polling()