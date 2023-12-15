from aiogram import F, Router, types
from aiogram.types import Message, FSInputFile, CallbackQuery


router = Router()

@router.callback_query(F.data == "faq")
async def faq_message(callback: types.CallbackQuery):
    await callback.message.answer(f'В будущем тут буде FAQ по боту.')