from aiogram import Router, types, F
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from bot_config import db


review_router = Router()

class Review(StatesGroup):
    name = State()
    inst = State()
    review = State()
    confirm = State()

@review_router.callback_query(F.data == 'complaint')
async def start_review(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer('Как вас зовут?')
    await call.message.edit_reply_markup(reply_markup=None)
    await state.set_state(Review.name)

@review_router.message(Review.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer('Ваш инстаграм или номер')
    await state.set_state(Review.inst)


@review_router.message(Review.inst)
async def process_inst_number(message: types.Message, state: FSMContext):
    await message.answer('Оставте жалобу')
    await state.update_data(inst=message.text)
    await state.set_state(Review.review)

@review_router.message(Review.review)
async def process_review(message: types.Message, state: FSMContext):
    await message.answer('Сохранить?, y/n')
    await state.update_data(review=message.text)
    await state.set_state(Review.confirm)

@review_router.message(Review.confirm)
async def process_confirm(message: types.Message, state: FSMContext):
    if message.text == 'y':
        data = await state.get_data()
        await message.answer('Спосибо за жолобу')
        db.execute(
            """INSERT INTO reviews VALUES (?, ?, ?)""",
            (None, data['name'], data['inst'], data['review'])
        )

        await state.clear()

    elif message.text == 'n':
        await message.answer('Без проблем')
        await state.clear()
    else:
        await message.answer('"y" = "ДА", "n" = "НЕТ"')




