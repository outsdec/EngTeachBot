from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

@router.message(F.data == "faq")
async def start(message: Message):
    await message.answer(f'В будущем тут будет FAQ.')
