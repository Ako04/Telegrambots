import telebot
import time
from telebot import types
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

def back(message):
    start_menu = types.ReplyKeyboardMarkup(True, True)
    start_menu.row('🚞 Экскурсии', '🕒 Дата')
    start_menu.row('🎟 Бронь', '⚙ Помощь')
    bot.send_message(message.chat.id, "Главное меню", reply_markup=start_menu)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    chat_id = message.chat.id
    photo = 'https://i.отзывы-ру.рф/review/966/2644966/1.jpg'
    photo1 = 'https://krasunia.ru/wp-content/uploads/7/c/1/7c16ce0b65b950a2cd6e5f681622cf6f.jpeg'
    file = photo, photo1

    if message.text == '🚞 Экскурсия в Туркистан':
        second_menu = types.ReplyKeyboardMarkup(True, True)
        second_menu.row('3I - Akimzhan', '3I - Amirbek', '3I - Nurshat')
        second_menu.row('Назад')
        bot.send_message(message.chat.id, "Экскурсия в Туркистан", reply_markup=second_menu)

    elif message.text == '🕒 Дата':
        third_menu = types.ReplyKeyboardMarkup(True, True, True, True)
        third_menu.row('1.04', '2.04', '3.04', '4.04')
        third_menu.row('5.04', '6.04', '7.04', '8.04', '9.04')
        third_menu.row('10.04', '11.04', '12.04', '13.04', '14.04')
        third_menu.row('15.04')
        third_menu.row('Назад')
        bot.send_message(message.chat.id, "Дата", reply_markup=third_menu)

    elif message.text == '🎟 Бронь':
        bot.send_media_group(message.chat.id, [types.InputMediaPhoto(photo)])

    elif message.text == '⚙ Помощь':
        bot.send_media_group(message.chat.id, [types.InputMediaPhoto(photo1)])



    elif message.text == 'Назад':
        back(message)

#Города
    if message.text == '3I - Akimzhan':
        bot.send_message(message.from_user.id, 'Thanks')
        user = message.text
        print(user)
        contains = ref.child('Registration').child('name').get()
        cStr = "" + str(contains)

        user_ref = ref.child('Registration').child('name')
        user_ref.set(user)
        bot.reply_to(message, "Thanks")


    elif message.text == '3I - Amirbek':
        bot.send_message(message.from_user.id, 'Thanks')
        user = message.text
        print(user)
        contains = ref.child('Registration').child('name').get()
        cStr = "" + str(contains)

        user_ref = ref.child('Registration').child('name')
        user_ref.set(user)
        bot.reply_to(message, "Thanks")





bot.polling(none_stop=True)