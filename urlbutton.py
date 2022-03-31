import telebot
from telebot import types
bot = telebot.TeleBot("2029002229:AAHQpll81DLntRszb_ZIVvw3P1OkntVQ_lY")

@bot.message_handler(commands=['start'])
def start(message):
    start = types.InlineKeyboardMarkup(row_width=2)
    a1 = types.InlineKeyboardButton(text="Akimzhan", url="https://www.instagram.com/ak1mzhan_08/")
    a2 = types.InlineKeyboardButton(text="Jihc Site", url="https://jihc.edupage.org/?")
    a3 = types.InlineKeyboardButton(text="Tutor Davronbek Insta", url="https://www.instagram.com/davronbek.abdurashidov/")
    start.add(a1,a2,a3)
    bot.send_message(message.chat.id, "Select the link", reply_markup=start)

bot.polling(none_stop=True)