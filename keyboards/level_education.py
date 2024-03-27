from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
def menu_lvl_education():
    main = [
        [
            InlineKeyboardButton(text = "Начинающий (A1)", callback_data = "edu_A1"),
            InlineKeyboardButton(text = "Начальный (A2)", callback_data = "edu_A2")
        ],
        [
            InlineKeyboardButton(text = "Средний (B1)", callback_data = "edu_B1"),
            InlineKeyboardButton(text = "Выше среднего (B1)", callback_data = "edu_B2")
        ]
    ]
    main = InlineKeyboardMarkup(inline_keyboard=main)
    return main