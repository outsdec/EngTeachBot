from aiogram import F, Bot, Dispatcher, Router, types
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile, CallbackQuery
from keyboards.level_education import menu_lvl_education, education_A1_theme, education_A2_theme, education_B1_theme, education_B2_theme
from base.registration import find_user
import random
import requests
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
router = Router()

@router.callback_query(F.data == "learning")
async def learn(callback: types.CallbackQuery):
    await callback.message.answer(f"Выберите уровень владения языком", reply_markup=menu_lvl_education())


@router.callback_query(F.data == "edu_A1")
async def eduсA1(callback: types.CallbackQuery):
    await callback.message.answer(f"Выберите тему", reply_markup=education_A1_theme())
    
@router.callback_query(F.data == "edu_A2")
async def eduсA2(callback: types.CallbackQuery):
    await callback.message.answer(f"Выберите тему", reply_markup=education_A2_theme())

@router.callback_query(F.data == "edu_B1")
async def eduсB1(callback: types.CallbackQuery):
    await callback.message.answer(f"Выберите тему", reply_markup=education_B1_theme())
    
@router.callback_query(F.data == "edu_B2")
async def eduсB2(callback: types.CallbackQuery):
    await callback.message.answer(f"Выберите тему", reply_markup=education_B2_theme())
    
    
eduA1eatWords = ["cake", "rice", "soup", "cucumber", "butter", "cheese", "milk", "meat", "fish", "apple"]
eduA1familyWords = ["mother", "father", "sister", "brother", "grandpa", "granny", "family", "uncle", "parents", "child"]
eduA1schoolWords = ["backpack", "blackboard", "classroom", "desk", "school", "pen", "pencil", "ruler", "notebook", "paper"]
eduA1restWords = ["trip", "place", "travel", "journey", "destination", "ship", "bus station", "torch", "plane", "airport"]


@router.callback_query(F.data == "edu_A1_eat")
async def eduсB1(callback: types.CallbackQuery):
    user = await find_user(callback.from_user.id)
    user_words = user["studied"]
    word = random.choice(eduA1eatWords)
    info = skyeng_word(word)
    word_rus = info[0]['translation']['text']
    random_number = random(0,1)
    # Open the file in read mode 
    with open("russian.txt", "r") as file: 
        allText = file.read() 
        words = list(map(str, allText.split())) 
        incorrectword = random.choice(words) 
        main = [
        [
            InlineKeyboardButton(text = f"{word_rus if random_number > 0 else incorrectword}", callback_data = "edu_A1"),
            InlineKeyboardButton(text = f"{word_rus if random_number < 1 else incorrectword}", callback_data = "edu_A2")
        ],
    ]
    main = InlineKeyboardMarkup(inline_keyboard=main)

    await callback.message.answer("Выбери верный вариант")
    print(info[0])
    print(info[0]['translation']['text'])
    await callback.message.answer_photo(photo = f"https:{info[0]['imageUrl']}", caption = f"{word}", reply_markup = main)


def skyeng_word(word):
    url = "http://dictionary.skyeng.ru/api/public/v1/words/search?_format=json&search={}".format(word)
    response = requests.get(url)
    try:
        ids = response.json()[0]['meanings']
        return ids
    except:
        return None
    
def skyeng_meaning(ids):
    url = "http://dictionary.skyeng.ru/api/public/v1/meanings?_format=json&ids={}".format(ids)
    response = requests.get(url)
    return response.json()[0]['examples'][0]['text']