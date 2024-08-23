from aiogram import Bot, Dispatcher

from main.data.config import token

bot = Bot(token=token)
dp = Dispatcher(bot=bot)

