from aiogram import F, Bot, Dispatcher, Router, types
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile, CallbackQuery
from keyboards.startkey import sign

router = Router()

@router.message(Command("start"))
async def start(message: Message):
    photo = FSInputFile("media/start.jpg")
    await message.answer_photo(photo, caption = f'Привет! Я – чат-бот "EngTeachBot", помогу вам с изучением английских слов, с помощью специально разработанных тренажеров.', reply_markup=sign())
