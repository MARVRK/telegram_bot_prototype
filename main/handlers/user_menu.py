import os
import logging
import types
import os

from aiogram import Router
from aiogram.types import Message, InlineKeyboardMarkup, FSInputFile
from os import path

from aiogram.filters import Command
from main.keyboards.user_keyboard import create_search_keyboard

logging.basicConfig(filename="log.txt", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
log = logging.getLogger(__name__)

router = Router()


@router.message(Command("start"))
async def start_command(message: Message):
    await message.answer_photo(caption="some_text", photo=FSInputFile(path.join("images", "test.jpeg")))



@router.message(Command("search"))
async def search_command(message: Message):
     keyboard = InlineKeyboardMarkup(inline_keyboard= await create_search_keyboard())
     await message.answer("Выбери критерии поиска:", reply_markup=keyboard)