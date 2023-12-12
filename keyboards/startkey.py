from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
def sign():
    menu = [
        [
            InlineKeyboardButton(text="Войти/Зарегистрироваться", callback_data="sign"),
        ]
    ]
    menu = InlineKeyboardMarkup(inline_keyboard=menu)
    return menu