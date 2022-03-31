import telebot

bot =telebot.TeleBot("1969845722:AAF-18owAfYt8j3rtwqYp6RG_MwysaTM2cU")

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.from_user.id, "Salam)")
    bot.send_message(message.from_user.id, "My name is Akimzhan")
    bot.send_message(message.from_user.id, "I'm 17 years old and I'm from Merke")
    bot.send_message(message.from_user.id, "My hobby is horse riding, fishing and traveling")
bot.polling()