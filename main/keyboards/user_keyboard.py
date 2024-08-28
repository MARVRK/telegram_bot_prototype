from aiogram.types.inline_keyboard_button import InlineKeyboardButton

button_init = InlineKeyboardButton
def create_search_keyboard():
	return [
        [
            button_init(text="Изображения", callback_data="image"),
            button_init(text="Тексты", callback_data="text")
        ],
        [
            button_init(text="Аудиозаписи", callback_data="audio"),
            button_init(text="Видеозаписи", callback_data="video")
        ]
    ]