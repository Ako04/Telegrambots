import telebot
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
    start_menu.row('🚞 Geizi', '🕒 Дата')
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
    start_menu.row('🚞 Geizi', '🕒 Дата')
    start_menu.row('🎟 Бронь', '⚙ Помощь')
    bot.send_message(message.chat.id, "Главное меню", reply_markup=start_menu)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    chat_id = message.chat.id
    photo = 'https://i.отзывы-ру.рф/review/966/2644966/1.jpg'
    photo1 = 'https://krasunia.ru/wp-content/uploads/7/c/1/7c16ce0b65b950a2cd6e5f681622cf6f.jpeg'
    file = photo, photo1

    if message.text == '🚞 Geizi':
        second_menu = types.ReplyKeyboardMarkup(True, True)
        second_menu.row('Алматы', 'Тараз')
        second_menu.row('Назад')
        bot.send_message(message.chat.id, "Geizi", reply_markup=second_menu)

    elif message.text == '🕒 Дата':
        time = ref.child('zapis').get()
        # dict1 = time.val()
        for key, value in time.items():
            # print(key, value['name'])
            if key == "10:00":
                bot.send_message(message.from_user.id, "10:00 " + value['name'])
            if key == "11:00":
                bot.send_message(message.from_user.id, "11:00 " + value['name'])
            if key == "12:00":
                bot.send_message(message.from_user.id, "12:00 " + value['name'])
            if key == "13:00":
                bot.send_message(message.from_user.id, "13:00 " + value['name'])
            if key == "14:00":
                bot.send_message(message.from_user.id, "14:00 " + value['name'])
            if key == "15:00":
                bot.send_message(message.from_user.id, "15:00 " + value['name'])
            if key == "16:00":
                bot.send_message(message.from_user.id, "16:00 " + value['name'])
            if key == "17:00":
                bot.send_message(message.from_user.id, "17:00 " + value['name'])
            if key == "18:00":
                bot.send_message(message.from_user.id, "18:00 " + value['name'])
            if key == "19:00":
                bot.send_message(message.from_user.id, "19:00 " + value['name'])
            else:
                bot.send_message(message.from_user.id, "No one signed up for this time.\nYOU CAN TAKE A REST")

    elif message.text == '🎟 Бронь':
        bot.send_media_group(message.chat.id, [types.InputMediaPhoto(photo)])

    elif message.text == '⚙ Помощь':
        bot.send_media_group(message.chat.id, [types.InputMediaPhoto(photo1)])



    elif message.text == 'Назад':
        back(message)

#Города
    if message.text == 'Алматы':
        bot.send_message(message.from_user.id, 'Вы зарегестрировались. Удачного вам пути!')
        user = message.text
        print(user)
        contains = ref.child('Registration Geizi for 3I').child('name').get()
        cStr = "" + str(contains)

        user_ref = ref.child('Registration Geizi for 3I').child('name')
        user_ref.set(user)
        bot.reply_to(message, "Thanks")


    elif message.text == 'Тараз':
        bot.send_message(message.from_user.id, 'Вы зарегестрировались. Удачного вам пути!')
        user = message.text
        print(user)
        contains = ref.child('Registration Geizi for 3I').child('name').get()
        cStr = "" + str(contains)

        user_ref = ref.child('Registration Geizi for 3I').child('name')
        user_ref.set(user)
        bot.reply_to(message, "Thanks")



    @bot.message_handler(commands=['text'])
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






bot.polling(none_stop=True)