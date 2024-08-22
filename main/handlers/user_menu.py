from aiogram import Router
from aiogram.types import Message

from aiogram.filters import Command


router = Router()


@router.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Привет! Это бот для поиска и сравнения фотографий. Напиши мне /search и выбери нужные критерии.")