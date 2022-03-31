import telebot
from telebot import types
bot = telebot.TeleBot("2019139517:AAG9AICcMk2gxHN23PYp_ZoD7h_zhEDHcac")

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    web = types.InlineKeyboardButton(text="Экскурсии", callback_data="1st")
    design = types.InlineKeyboardButton(text="Дата", callback_data="2nd")
    mobile = types.InlineKeyboardButton(text="Бронь", callback_data="3rd")
    video = types.InlineKeyboardButton(text="Помощь", callback_data="4th")
    security = types.InlineKeyboardButton(text="Гиды", callback_data="5th")
    social = types.InlineKeyboardButton(text="Сообщество", callback_data="6th")
    keyboard.add(web, design, mobile, video, security, social)
    bot.send_message(message.chat.id, "Hello my friend! ", reply_markup=keyboard)
def back(message):
    h5 = types.InlineKeyboardButton(text="Back", callback_data="5th")
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    bot.send_message(message.chat.id, 'Please choose', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call:True)
def call_in(call):
    if call.data == "1st":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        f1 = types.InlineKeyboardButton(text="Алматы", callback_data="4th")
        h5 = types.InlineKeyboardButton(text="Back", callback_data="5th")
        keyboard.add(f1, h5)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Chose", reply_markup=keyboard)

    if call.data == "2nd":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        g2 = types.InlineKeyboardButton(text="1.04", callback_data="2nd")
        d2 = types.InlineKeyboardButton(text="2.04", callback_data="3rd")
        b1 = types.InlineKeyboardButton(text="3.04", callback_data="4th")
        h5 = types.InlineKeyboardButton(text="Back", callback_data="5th")
        keyboard.add(g2, d2, b1, h5)
        keyboard.add(g2, d2, b1,)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="replaced text", reply_markup=keyboard)


    if call.data == "3rd":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        g2 = types.InlineKeyboardButton(text="Bilet", url="https://i.отзывы-ру.рф/review/966/2644966/1.jpg")
        h5 = types.InlineKeyboardButton(text="Back", callback_data="5th")
        keyboard.add(g2,h5)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="replaced text", reply_markup=keyboard)

    if call.data == "5th":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        web = types.InlineKeyboardButton(text="Экскурсии", callback_data="1st")
        design = types.InlineKeyboardButton(text="Дата", callback_data="2nd")
        mobile = types.InlineKeyboardButton(text="Бронь", callback_data="3rd")
        video = types.InlineKeyboardButton(text="Помощь", callback_data="4th")
        security = types.InlineKeyboardButton(text="Гиды", callback_data="5th")
        social = types.InlineKeyboardButton(text="Сообщества", callback_data="6th")
        keyboard.add(web, design, mobile, video, security, social)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="replaced text", reply_markup=keyboard)




bot.polling()