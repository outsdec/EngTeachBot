from aiogram import F, Bot, Router, types
from aiogram.types import Message, FSInputFile, CallbackQuery
from aiogram.filters import Command
import json
from aiogram.types import URLInputFile

router = Router()

@router.callback_query(F.data == "faq")
async def faq_message(callback: types.CallbackQuery):
    await callback.message.answer(f'В будущем тут буде FAQ по боту.')

@router.message(Command("test"))
async def start_newsletter(message: types.Message, bot: Bot):
        text = message.text[6:]
        info = skyeng_word(text)
        print(info[0])
        await message.answer_photo(info[0]['imageUrl'])
        await message.answer_audio(info[0]['soundUrl'])

import requests

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