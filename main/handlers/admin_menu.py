import re
import logging

from aiogram import Router
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, InlineKeyboardMarkup, FSInputFile
from aiogram.types.reply_keyboard_remove import ReplyKeyboardRemove
from os import path

from aiogram.filters import Command
from main.api_sql.dp import Database

# from main.keyboards.admin_keyboard import create_search_keyboard

router = Router()
db = Database()

logging.basicConfig(filename="log.txt", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
log = logging.getLogger(__name__)


class Registration(StatesGroup):
    name = State()
    age = State()
    gender = State()
    email = State()
    phone_number = State()


@router.message(Command("registration"))
async def registration(message: Message, state: FSMContext):
    await message.answer("Введите ваше имя")
    await state.set_state(Registration.name)


@router.message(Registration.name)
async def registration_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите ваш возраст")
    await state.set_state(Registration.age)


@router.message(Registration.age)
async def registration_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("Введите ваш пол")
    await state.set_state(Registration.gender)


@router.message(Registration.gender)
async def registration_gender(message: Message, state: FSMContext):
    await state.update_data(gender=message.text)
    await message.answer("Введите вашу электронную почту")
    await state.set_state(Registration.email)


@router.message(Registration.email)
async def registration_email(message: Message, state: FSMContext):
    while True:
        if re.match(r'[^@]+@[^@]+\.[^@]+', message.text):
            await state.update_data(email=message.text)
            await message.answer("Введите ваш номер телефона")
            await state.set_state(Registration.phone_number)
            break
        else:
            await message.answer("Неверный формат, убедитесь что имейл имеет символ @")
            return

@router.message(Registration.phone_number)
async def registration_phone_number(message: Message, state: FSMContext):
    while True:
        if message.text.isdigit():
            await state.update_data(phone_number=message.text)
            await message.answer("Регистрация прошла успешно")
            data = await state.get_data()
            db.insert_database(name=data['name'],
                               age=data['age'],
                               gender=data['gender'],
                               email=data['email'],
                               phone_number=data['phone_number']
                               )
            await message.answer(
                f"Ваше имя: {data['name']}\nВаш возраст: {data['age']}\nВаш пол: {data['gender']}\nВаш имейл: {data['email']}\nВаш номер телефона: {data['phone_number']}")
            await state.clear()
            break
        else:
            await message.answer("Неверный формат номера, убедитесь что номер состоит из цифр")
            return