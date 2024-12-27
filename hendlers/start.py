from aiogram import Router, types
from aiogram.filters import Command


start_router = Router()

kb = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [
            types.InlineKeyboardButton(text='Оставить жалобу', callback_data='complaint')
        ]
    ])
@start_router.message(Command('start'))
async def start(message: types.Message):
    await message.answer(f'Привет я бот этого теста', reply_markup=kb)
