from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
def sign():
    menu = [
        [
            InlineKeyboardButton(text="Войти/Зарегистрироваться", callback_data="sign"),
        ],
        [
            InlineKeyboardButton(text="FAQ", callback_data="faq"),
            InlineKeyboardButton(text="О нас", callback_data="about_dev"),
        ]
    ]
    menu = InlineKeyboardMarkup(inline_keyboard=menu)
    return menu