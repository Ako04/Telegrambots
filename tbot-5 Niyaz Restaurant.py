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
    start_menu.row('🍗 Chicken', '🕒 Доставка')
    start_menu.row('🍱 Меню', '🍟 Сеты')
    bot.send_message(message.chat.id, "Вас приветствует Adal Chicken Bot"
                                        "\nТаразкие Чикены 🍖🔥😎 : "
                                        "\n- 🍗 Вкус который ты искал;"
                                        "\n- 🕌 Халал Продукт;"
                                        "\n- 🕒 11:00-00:00 (без выходных);"
                                        "\n- 📲 +77071887071;"
                                        "\n"
                                        "\nДоставка/Самовызов; "
                                        "\nРаботаем без выходных", reply_markup=start_menu)

def back(message):
    start_menu = types.ReplyKeyboardMarkup(True, True)
    start_menu.row('🍗 Chicken', '🕒 Доставка')
    start_menu.row('🍱 Меню', '🍟 Сеты')
    bot.send_message(message.chat.id, "Главное меню", reply_markup=start_menu)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    chat_id = message.chat.id
    photo = 'https://b.zmtcdn.com/data/menus/182/6113182/67df8122e19d5af412863528bf81cddc.jpg'
    photo1 = 'https://cdn.website.dish.co/media/86/11/2588832/Chicken-Spot-neue-karte-2-neu.jpg'
    file = photo, photo1

    if message.text == '🍗 Chicken':
        second_menu = types.ReplyKeyboardMarkup(True, True)
        second_menu.row('Голень', 'Крылашки')
        second_menu.row('Назад')
        bot.send_message(message.chat.id, "Chicken", reply_markup=second_menu)

    elif message.text == '🕒 Доставка':
        third_menu = types.ReplyKeyboardMarkup(True, True, True, True)
        third_menu.row('1.00', '2.00', '3.00', '4.00')
        third_menu.row('5.00', '6.00', '7.00', '8.00', '9.00')
        third_menu.row('10.00', '11.00', '12.00', '13.00', '14.00')
        third_menu.row('15.00')
        third_menu.row('Назад')
        bot.send_message(message.chat.id, "Доставка", reply_markup=third_menu)

    elif message.text == '🍱 Меню':
        bot.send_media_group(message.chat.id, [types.InputMediaPhoto(photo)])

    elif message.text == '🍟 Сеты':
        bot.send_media_group(message.chat.id, [types.InputMediaPhoto(photo1)])



    elif message.text == 'Назад':
        back(message)

#Города
    if message.text == 'Голень':
        bot.send_message(message.from_user.id, 'Ваша доставка будет доставлено через 45 минут. Ожидайте! Приятного вам аппетита!😋')
        user = message.text
        print(user)
        contains = ref.child('Регистрация заказов').child('name').get()
        cStr = "" + str(contains)

        user_ref = ref.child('Регистрация заказов').child('name')
        user_ref.set(user)
        bot.reply_to(message, "Thanks")


    elif message.text == 'Крылашки':
        bot.send_message(message.from_user.id, 'Ваша доставка будет доставлено через 45 минут. Ожидайте! Приятного вам аппетита!😋')
        user = message.text
        print(user)
        contains = ref.child('Регистрация заказов').child('name').get()
        cStr = "" + str(contains)

        user_ref = ref.child('Регистрация заказов').child('name')
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
            contains = ref.child('Registration').child('meal').get()
            cStr = "" + str(contains)

            user_ref = ref.child('Registration').child('meal')
            user_ref.set(user)
            bot.reply_to(message, "Thanks")







bot.polling(none_stop=True)