from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
def sign():
    menu = [
        [
            InlineKeyboardButton(text="Войти/Зарегистрироваться", callback_data="sign"),
        ]
        [
            InlineKeyboardButton(text="FAQ", callback_data="faq"),
            InlineKeyboardButton(text="Пожертвование", callback_data="donate"),
            InlineKeyboardButton(text="О нас", callback_data="about"),
        ]
    ]
    menu = InlineKeyboardMarkup(inline_keyboard=menu)
    return menu