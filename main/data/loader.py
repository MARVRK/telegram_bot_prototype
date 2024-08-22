from aiogram import Bot, Dispatcher

from telegram_bot_prototype.main.data.config import token

bot = Bot(token=token)
dp = Dispatcher(bot=bot)

