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

bot = telebot.TeleBot("5005944975:AAFCT1V4cUiHihh6cwU8p3hJ4_I-krPcbTk")

@bot.message_handler(commands=['start'])
def start(message):
    start_menu = types.ReplyKeyboardMarkup(True, True)
    start_menu.row('🍗 Chicken', '🕒 Доставка')
    start_menu.row('🍱 Меню', '🍔Бургер и 🌯Донеры')
    bot.send_message(message.chat.id, "Вас приветствует CHEESY Bot"
                                        "\n😋 Fast Food <<CHEESY>> "
                                        "\n- 🍔 Мощные Бургеры;"
                                        "\n- 🥙 Сытные Донеры;"
                                        "\n- 🍗 Сочные Чикены;"
                                        "\n- ☎ +7 707 400 77 66;"
                                        "\n"
                                        "\n🏠 Pixel Cinema (Food Court); "
                                        "\n📲 Следите за новостями в ленте‼️", reply_markup=start_menu)

def back(message):
    start_menu = types.ReplyKeyboardMarkup(True, True)
    start_menu.row('🍗 Chicken', '🕒 Доставка')
    start_menu.row('🍱 Меню', '🍔Бургер и 🌯Донеры')
    bot.send_message(message.chat.id, "Главное меню", reply_markup=start_menu)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    chat_id = message.chat.id
    photo = 'https://karusel.in.ua/wp-content/uploads/2020/05/fast-food-menu-2020-min.jpg'
    photo1 = 'https://i.ytimg.com/vi/_Lj9UXF5my4/maxresdefault.jpg'
    photo2 = 'https://www.restoclub.ru/uploads/menufile/e/2/4/6/e246dce6d4cec23a3f077c7361d7fd6f.png'
    file = photo, photo1, photo2

    if message.text == '🍗 Chicken':
        second_menu = types.ReplyKeyboardMarkup(True, True)
        second_menu.row('Нагетсы', 'Крылашки')
        second_menu.row('Назад')
        bot.send_message(message.chat.id, "Chicken", reply_markup=second_menu)

    elif message.text == '🕒 Доставка':
        third_menu = types.ReplyKeyboardMarkup(True, True, True, True)
        third_menu.row('09.00', '10.00', '11.00', '12.00')
        third_menu.row('13.00', '14.00', '15.00', '16.00', '17.00')
        third_menu.row('18.00', '19.00', '20.00', '21.00', '22.00')
        third_menu.row('23.00', '24.00')
        third_menu.row('Назад')
        bot.send_message(message.chat.id, "Доставка", reply_markup=third_menu)

    elif message.text == '🍱 Меню':
        bot.send_media_group(message.chat.id, [types.InputMediaPhoto(photo)])

    elif message.text == '🍔Бургер и 🌯Донеры':
        bot.send_media_group(message.chat.id, [types.InputMediaPhoto(photo1)])
        bot.send_media_group(message.chat.id, [types.InputMediaPhoto(photo2)])



    elif message.text == 'Назад':
        back(message)

#Виды
    if message.text == 'Голень':



        bot.send_message(message.from_user.id, 'Ваша доставка будет доставлено через 45 минут. Ожидайте! Приятного вам аппетита!😋')
        user = message.text
        print(user)
        contains = ref.child('Регистрация заказов').child('name').get()
        cStr = "" + str(contains)

        user_ref = ref.child('Регистрация заказов').child('name')
        user_ref.set(user)
        bot.reply_to(message, "Thanks")


    elif message.text == 'Нагетсы':
        bot.send_message(message.from_user.id, 'Ваша доставка принято. Ожидайте! Приятного вам аппетита!😋')
        user = message.text
        print(user)
        contains = ref.child('Регистрация заказов').child('name').get()
        cStr = "" + str(contains)

        user_ref = ref.child('Регистрация заказов').child('name')
        user_ref.set(user)
        bot.reply_to(message, "Thanks")









bot.polling(none_stop=True)