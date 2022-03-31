import telebot
from telebot import types
bot = telebot.TeleBot("2019139517:AAG9AICcMk2gxHN23PYp_ZoD7h_zhEDHcac")

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    web = types.InlineKeyboardButton(text="4-ter", callback_data="1st")
    design = types.InlineKeyboardButton(text="3-ter", callback_data="2nd")
    mobile = types.InlineKeyboardButton(text="2-ler", callback_data="3rd")
    video = types.InlineKeyboardButton(text="1-ler", callback_data="4th")
    security = types.InlineKeyboardButton(text="Hocamdar", callback_data="5th")
    social = types.InlineKeyboardButton(text="Abiler", callback_data="6th")
    keyboard.add(web, design, mobile, video, security, social)
    bot.send_message(message.chat.id, "Hello my friend! Select your course", reply_markup=keyboard)
def back(message):
    h5 = types.InlineKeyboardButton(text="Back", callback_data="5th")
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    bot.send_message(message.chat.id, 'Please choose', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call:True)
def call_in(call):
    if call.data == "1st":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        f1 = types.InlineKeyboardButton(text="4E", url="https://www.instagram.com/1e_m1k/")
        h5 = types.InlineKeyboardButton(text="Back", callback_data="5th")
        keyboard.add(f1, h5)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Choose your class", reply_markup=keyboard)

    if call.data == "2nd":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        g2 = types.InlineKeyboardButton(text="3I", url="https://www.instagram.com/jihc_ione/")
        d2 = types.InlineKeyboardButton(text="3G", url="https://www.instagram.com/jic_btmns/")
        b1 = types.InlineKeyboardButton(text="3C", url="https://www.instagram.com/29person/")
        h5 = types.InlineKeyboardButton(text="Back", callback_data="5th")
        keyboard.add(g2, d2, b1, h5)
        keyboard.add(g2, d2, b1,)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="replaced text", reply_markup=keyboard)


    if call.data == "3rd":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        g2 = types.InlineKeyboardButton(text="2E", url="https://www.instagram.com/jihc_slytherinn/")
        h5 = types.InlineKeyboardButton(text="Back", callback_data="5th")
        keyboard.add(g2,h5)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="replaced text", reply_markup=keyboard)

    if call.data == "5th":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        web = types.InlineKeyboardButton(text="4-ter", callback_data="1st")
        design = types.InlineKeyboardButton(text="3-ter", callback_data="2nd")
        mobile = types.InlineKeyboardButton(text="2-ler", callback_data="3rd")
        video = types.InlineKeyboardButton(text="1-ler", callback_data="4th")
        security = types.InlineKeyboardButton(text="Hocamdar", callback_data="5th")
        social = types.InlineKeyboardButton(text="Abiler", callback_data="6th")
        keyboard.add(web, design, mobile, video, security, social)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="replaced text", reply_markup=keyboard)



bot.polling()