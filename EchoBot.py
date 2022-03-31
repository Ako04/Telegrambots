import asyncio

from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message

BOT_TOKEN = "5256014366:AAHachAr6NCGY_Ktm0-6nZkuFxrPJXWSM3Q"
admin_id = 1120772010

loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, loop=loop)
async def send_to_admin(dp):
    await bot.send_message(chat_id=id, text="Salem, Demalaiyqsh")

@dp.message_handler()
async def echo(message: Message):
    if message.text == "Как тебя зовут?":
        text = f"Я БОТ ECHO."
        await message.reply(text=text)
    elif message.text == "Кто ты?":
        text = f"Я БОТ."
        await message.reply(text=text)
    elif message.text == "Привет":
        text = f"Салам)"
        await message.reply(text=text)
    elif message.text == "Че там?":
        text = f"Тишина, сам как?"
        await message.reply(text=text)
    elif message.text == "Че делаешь?":
        text = f"Валяю дурака"
        await message.reply(text=text)
    elif message.text == "Ау":
        text = f"Сиыр сау"
        await message.reply(text=text)
    else:
        text = f"Вы написали ошибку при наборе команды."
        await message.reply(text=text)


if __name__ == "__main__":

    executor.start_polling(dp, on_startup=send_to_admin)
