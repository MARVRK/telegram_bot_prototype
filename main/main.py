# import telegram_bot_prototype.main.data.config
#
# from telegram_bot_prototype.main.data.config import *
import asyncio
import logging

from telegram_bot_prototype.main.data.loader import dp, bot

from telegram_bot_prototype.main.handlers import user_menu, admin_menu

logging.basicConfig(filename="log.txt")

async def main():
	dp.include_router(user_menu.router)
	# dp.include_router(admin_menu.router)
	await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())