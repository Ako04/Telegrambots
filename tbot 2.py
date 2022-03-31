import telebot
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('akim.json')
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://telegrambot1-16294-default-rtdb.firebaseio.com/"
})
ref = db.reference()

bot = telebot.TeleBot("2019139517:AAG9AICcMk2gxHN23PYp_ZoD7h_zhEDHcac")

@bot.message_handler(commands=['start'])
def handle_start(message):
    time =  ref.child('zapis').get()
    #dict1 = time.val()
    for key, value in time.items():
        #print(key, value['name'])
        if key == "10:00":
            bot.send_message(message.from_user.id, "10:00 "+ value['name'])
        if key == "11:00":
            bot.send_message(message.from_user.id, "11:00 "+ value['name'])
        if key == "12:00":
            bot.send_message(message.from_user.id, "12:00 "+ value['name'])
        if key == "13:00":
            bot.send_message(message.from_user.id, "13:00 "+ value['name'])
        if key == "14:00":
            bot.send_message(message.from_user.id, "14:00 "+ value['name'])
        if key == "15:00":
            bot.send_message(message.from_user.id, "15:00 "+ value['name'])
        if key == "16:00":
            bot.send_message(message.from_user.id, "16:00 "+ value['name'])
        if key == "17:00":
            bot.send_message(message.from_user.id, "17:00 "+ value['name'])
        if key == "18:00":
            bot.send_message(message.from_user.id, "18:00 "+ value['name'])
        if key == "19:00":
            bot.send_message(message.from_user.id, "19:00 "+ value['name'])
        else:
            bot.send_message(message.from_user.id, "No one signed up for this time.\nYOU CAN TAKE A REST")

bot.polling()