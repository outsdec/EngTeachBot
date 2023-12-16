from aiogram import F, Bot, Dispatcher, Router, types
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile, CallbackQuery

router = Router()

@router.callback_query(F.data == "training")
async def train(callback: types.CallbackQuery):
    await callback.message.answer(f"Выберите уровень словарного запаса")