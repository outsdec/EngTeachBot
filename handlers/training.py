from aiogram import F, Bot, Dispatcher, Router, types
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile, CallbackQuery
from keyboards.level_repetition import menu_lvl_repetition, repetition_A1_theme, repetition_A2_theme, repetition_B1_theme, repetition_B2_theme

router = Router()

@router.callback_query(F.data == "training")
async def train(callback: types.CallbackQuery):
    await callback.message.answer(f"Выберите уровень владения языком", reply_markup= menu_lvl_repetition())

@router.callback_query(F.data == "rep_A1")
async def repA1(callback: types.CallbackQuery):
    await callback.message.answer(f"Выберите тему", reply_markup=repetition_A1_theme())
    
@router.callback_query(F.data == "rep_A2")
async def repA2(callback: types.CallbackQuery):
    await callback.message.answer(f"Выберите тему", reply_markup=repetition_A2_theme())

@router.callback_query(F.data == "rep_B1")
async def repB1(callback: types.CallbackQuery):
    await callback.message.answer(f"Выберите тему", reply_markup=repetition_B1_theme())
    
@router.callback_query(F.data == "rep_B2")
async def repB2(callback: types.CallbackQuery):
    await callback.message.answer(f"Выберите тему", reply_markup=repetition_B2_theme())
