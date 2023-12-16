from aiogram import F, Router, types
from aiogram.types import Message, FSInputFile, CallbackQuery


router = Router()

@router.callback_query(F.data == "about_dev")
async def about_message(callback: types.CallbackQuery):
    await callback.message.answer(f'В будущем тут буде информация о разработчиках и авторах данного бота')