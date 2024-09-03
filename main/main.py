# import telegram_bot_prototype.main.data.config
#
# from telegram_bot_prototype.main.data.config import *
import asyncio
import logging
from datetime import time

from main.data.loader import bot, dp
from main.handlers import user_menu, admin_menu

logging.basicConfig(filename="log.txt", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

async def main():
    logger.info("Starting")
    #dp.include_router(user_menu.router)
    dp.include_router(admin_menu.router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logger.info ("Run_Main")
    asyncio.run(main())
