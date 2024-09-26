from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_main_keyboard():
    buttons = [
        [KeyboardButton(text="Поиск в базе знаний")],
        [KeyboardButton(text="История запросов")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
