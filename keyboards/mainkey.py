from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
def menu():
    main = [
        [
            InlineKeyboardButton(text="Обучение", callback_data="learning"),
        ],
        [
            InlineKeyboardButton(text="Закрепление", callback_data="training")
        ]
    ]
    main = InlineKeyboardMarkup(inline_keyboard=main)
    return main