import telebot
from telebot import types

TOKEN = "2019139517:AAG9AICcMk2gxHN23PYp_ZoD7h_zhEDHcac"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    start_menu = types.ReplyKeyboardMarkup(True, True)
    start_menu.row('🥇 Лучшие студенты', '📃 Документы')
    start_menu.row('⚔ Activity','📖 Study')
    bot.send_message(message.chat.id, "Всем Салам!"
                     "\nЧто я умею: "
                     "\n- Играть в CS;"
                     "\n- Смотреть фильмы с kardesami;"
                     "\n- Делаю студентов образованными и ответственными", reply_markup=start_menu)

def back(message):
    start_menu = types.ReplyKeyboardMarkup(True, True)
    start_menu.row('🥇 Лучшие студенты', '📃 Документы')
    start_menu.row('⚔ Activity', '📖 Study')
    bot.send_message(message.chat.id, "Главное меню", reply_markup=start_menu)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    chat_id = message.chat.id
    photo = 'https://im0-tub-kz.yandex.net/i?id=d4dec800acf8783be774ff645aab76c7-l&n=13'
    photo1 = 'https://im0-tub-kz.yandex.net/i?id=70de5577df60090379bd39cd4ed6ae3a-l&n=13'
    file = photo, photo1

    if message.text == '🥇 Лучшие студенты':
        second_menu = types.ReplyKeyboardMarkup(True, True)
        second_menu.row('3I', '4E')
        second_menu.row('Назад')
        bot.send_message(message.chat.id, "🥇 Лучшие студенты", reply_markup=second_menu)

    elif message.text == '📃 Документы':
        third_menu = types.ReplyKeyboardMarkup(True, True, True, True)
        third_menu.row('1F-1', '1F-2', '1A', '1D')
        third_menu.row('2B-1', '2B-2', '2D', '2E', '2G')
        third_menu.row('3C', '3F', '3G', '3H', '3I')
        third_menu.row('4E')
        third_menu.row('Назад')
        bot.send_message(message.chat.id, "📃 Документы", reply_markup=third_menu)

    elif message.text == '⚔ Activity':
        bot.send_media_group(message.chat.id, [types.InputMediaPhoto(photo)])

    elif message.text == '📖 Study':
        bot.send_media_group(message.chat.id, [types.InputMediaPhoto(photo1)])

    elif message.text == 'Назад':
        back(message)


bot.polling(none_stop=True)
