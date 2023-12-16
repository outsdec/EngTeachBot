from aiogram import F, Bot, Dispatcher, Router, types
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile, CallbackQuery
from base.registration import reg_users
from keyboards.mainkey import menu
router = Router()

@router.callback_query(F.data == "sign")
async def user_sign(callback: types.CallbackQuery):
    await reg_users(callback.from_user.id, callback.from_user.first_name)
    await callback.message.answer(f'Выберите режим обучения.', reply_markup=menu())

