from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.dizim import dizimm
from loader import dp, db
from keyboards.default.basmenyu import bas_menyu


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    if db.select_user(id=user_id):
        await message.answer(f"Xosh kelipsiz {message.from_user.first_name}", reply_markup=bas_menyu)
    else:
        await message.answer(f"Salem, {message.from_user.full_name}\nBottan toliq paydalaniw ushin dizimnen otin!", reply_markup=dizimm)
