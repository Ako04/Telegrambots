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
    bot.send_message(message.from_user.id, 'What is your name?')

@bot.message_handler(content_types=['text'])
def soz(message):
    if message.text == "Merke":
        bot.send_message(message.chat.id, "You're from best place")
    else:
        user = message.text
        print(user)
        contains = ref.child('Registration').child('name').get()
        cStr = "" + str(contains)

        user_ref = ref.child('Registration').child('name')
        user_ref.set(user)
        bot.reply_to(message, "Thanks")

bot.polling()

