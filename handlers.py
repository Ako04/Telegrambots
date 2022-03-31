from EchoBot import bot, dp

from aiogram.types import Message
from Config import admin_id

async def send_to_admin(dp):
    await bot.send_message(chat_id=admin_id, text="Hi Akimzhan")

@dp.message_handler()
async def echo(message):
    if message.text == "Кто ты?":
        text = f"Я БОТ Акимжана."
        await bot.send_message(chat_id=message.from_user.id, text=text)
