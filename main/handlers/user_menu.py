import os
import logging

from aiogram import Router
from aiogram.types import Message, InlineKeyboardMarkup, FSInputFile

from aiogram.filters import Command
from main.keyboards.user_keyboard import create_search_keyboard

logging.basicConfig(filename="log.txt", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
log = logging.getLogger(__name__)

router = Router()
image_path = "test.jpeg"
if os.path.exists(image_path):
    image = FSInputFile(path=image_path, filename=os.path.basename(image_path))
else:
    image = None

@router.message(Command("start"))
async def start_command(message: Message):
    if image:
        await message.answer("Привет! Это бот для поиска и сравнения фотографий. Напиши мне /search и выбери нужные критерии.")
        await message.reply_photo(photo=image)
    else:
        await message.answer("Привет!К сожалению изображение отсутсвует")

@router.message(Command("search"))
async def search_command(message: Message):
     keyboard = InlineKeyboardMarkup(inline_keyboard= await create_search_keyboard())
     await message.answer("Выбери критерии поиска:", reply_markup=keyboard)