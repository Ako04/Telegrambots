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
def start(message):
    start_menu = types.ReplyKeyboardMarkup(True, True)
    start_menu.row('🚞 Экскурсии', '🕒 Дата')
    start_menu.row('🎟 Бронь', '⚙ Помощь')
    bot.send_message(message.chat.id, "Вас приветствует KazTravel Bot"
                                        "\nОсновные функции: "
                                        "\n- Онлайн консультации насчет Экскурсии и туров;"
                                        "\n- Информация о местах, куда мы проводим туры"
                                        "\n- Можно онлайн бронировать удобные для вас места;"
                                        "\n- Помощь если у вас возникли проблемы с экскурсией и т.д.;"
                                        "\n"
                                        "\nУважаемые экскурсаводы прибывайте на экскурсий в назначенное время и место "
                                        "Работаем без выходных", reply_markup=start_menu)

@bot.message_handler(content_types=['text'])
def soz(message):
    if message == "Merke":
        bot.send_message(message.chat.id, "You're from best place")
    else:
        user = message.text
        print(user)
        contains = ref.child('Registration').child('name').get()
        cStr = "" + str(contains)
        if cStr == "None":
            user_ref = ref.child('Registration').child('name')
            user_ref.set(user)
            bot.reply_to(message, "Thanks")

bot.polling()

