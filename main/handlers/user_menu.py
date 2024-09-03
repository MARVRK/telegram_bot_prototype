import os
import logging


from aiogram import Router
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, InlineKeyboardMarkup, FSInputFile
from aiogram.types.reply_keyboard_remove import ReplyKeyboardRemove
from os import path

from aiogram.filters import Command

from main.keyboards.user_keyboard import create_search_keyboard

logging.basicConfig(filename="log.txt", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
log = logging.getLogger(__name__)

router = Router()

class Form(StatesGroup):
    name = State()
    age = State()
    male = State()
    phone_number = State()

@router.message(Command("start"))
async def start_command(message: Message, state: FSMContext):
    await message.answer_photo(caption="some_text", photo=FSInputFile(path.join("main/images", "test.jpeg")))
    await state.set_state(Form.name)
    await message.answer("Hi, i am new bot, what is your name?")
    await state.set_state(Form.age)
    await message.answer("Please provide your age")
@router.message()


@router.message(Form.name)
async def proceed_command(message: Message, state: FSMContext):
    await state.update_data(name=message.text, age=message.text)
    data= await state.get_data()
    name=data["name"]
    age=data["age"]
    await message.answer(f"Nice to meet you, {name}!your age is {age}!")

@router.message(Command("search"))
async def search_command(message: Message):
     keyboard = InlineKeyboardMarkup(inline_keyboard = create_search_keyboard())
     await message.answer("Choose criteria:", reply_markup=keyboard)