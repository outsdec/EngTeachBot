from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
def menu_lvl_repetition():
    main = [
        [
            InlineKeyboardButton(text = "Начинающий (A1)", callback_data = "rep_A1"),
            InlineKeyboardButton(text = "Начальный (A2)", callback_data = "rep_A2")
        ],
        [
            InlineKeyboardButton(text = "Средний (B1)", callback_data = "rep_B1"),
            InlineKeyboardButton(text = "Выше среднего (B1)", callback_data = "rep_B2")
        ],
        [
            InlineKeyboardButton(text = "◀ Назад", callback_data = "sign"),
        ]
    ]
    main = InlineKeyboardMarkup(inline_keyboard=main)
    return main

def repetition_A1_theme():
    main = [
        [
            InlineKeyboardButton(text = "Еда/Напитки", callback_data = "rep_A1_eat")
        ],
        [
            InlineKeyboardButton(text = "Семья/Друзья/Родственники", callback_data = "rep_A1_family")
        ],
        [
            InlineKeyboardButton(text = "Школа/Образование", callback_data = "rep_A1_school")
        ],
        [
            InlineKeyboardButton(text = "Путешествия/Отдых", callback_data = "rep_A1_relax")
        ],
        [
            InlineKeyboardButton(text = "◀ Назад", callback_data = "learning"),
        ]
    ]
    main = InlineKeyboardMarkup(inline_keyboard=main)
    return main

def repetition_A2_theme():
    main = [
        [
            InlineKeyboardButton(text = "Здоровье и тело", callback_data = "rep_A1_eat")
        ],
        [
            InlineKeyboardButton(text = "Жилье и обстановка", callback_data = "rep_A1_family")
        ],
        [
            InlineKeyboardButton(text = "Покупки и магазины", callback_data = "rep_A1_school")
        ],
        [
            InlineKeyboardButton(text = "Отношения и дружба", callback_data = "rep_A1_relax")
        ],
        [
            InlineKeyboardButton(text = "◀ Назад", callback_data = "learning"),
        ]
    ]
    main = InlineKeyboardMarkup(inline_keyboard=main)
    return main

def repetition_B1_theme():
    main = [
        [
            InlineKeyboardButton(text = "Технологии и интернет", callback_data = "rep_A1_eat")
        ],
        [
            InlineKeyboardButton(text = "Хобби и досуг", callback_data = "rep_A1_family")
        ],
        [
            InlineKeyboardButton(text = "Искусство и культура", callback_data = "rep_A1_school")
        ],
        [
            InlineKeyboardButton(text = "Работа и карьера", callback_data = "rep_A1_relax")
        ],
        [
            InlineKeyboardButton(text = "◀ Назад", callback_data = "learning"),
        ]
    ]
    main = InlineKeyboardMarkup(inline_keyboard=main)
    return main

def repetition_B2_theme():
    main = [
        [
            InlineKeyboardButton(text = "Политика и общество", callback_data = "rep_A1_eat")
        ],
        [
            InlineKeyboardButton(text = "Экономика и финансы", callback_data = "rep_A1_family")
        ],
        [
            InlineKeyboardButton(text = "Личностный рост и развитие", callback_data = "rep_A1_school")
        ],
        [
            InlineKeyboardButton(text = "Этика и мораль", callback_data = "rep_A1_relax")
        ],
        [
            InlineKeyboardButton(text = "◀ Назад", callback_data = "learning"),
        ]
    ]
    main = InlineKeyboardMarkup(inline_keyboard=main)
    return main