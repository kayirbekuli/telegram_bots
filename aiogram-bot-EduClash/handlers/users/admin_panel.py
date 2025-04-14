from aiogram import types
from loader import dp, db, bot
from data.config import ADMINS
from keyboards.default.admins_panel import admin_menu

@dp.message_handler(commands=["admin"])
async def admins(message: types.Message):
    user_id = message.from_user.id
    print(f"Received /admin command from {user_id}")
    if user_id in [int(admin_id) for admin_id in ADMINS]:
        print(f"User {user_id} is an admin")
        await bot.send_message(chat_id=user_id, text="Admin paneline xosh kelipsiz", reply_markup=admin_menu)
    else:
        print(f"User {user_id} is not an admin")
        await message.reply("Bul tek adminler ushin")


@dp.message_handler(text_contains="Statistika")
async def admin_stat(message: types.Message):
    users_stat = db.count_users()
    user_id = message.from_user.id
    print(f"Received /admin command from {user_id}")
    if user_id in [int(admin_id) for admin_id in ADMINS]:
        print(f"User {user_id} is an admin")
        await bot.send_message(chat_id=user_id, text=f"Bottagi barliq paydalaniwshilar sani: {users_stat[0]}", reply_markup=admin_menu)
    else:
        print(f"User {user_id} is not an admin")
        await message.reply("Bul tek adminler ushin")

    # await message.bot.send_message(chat_id=,text=f"Bottagi barliq paydalaniwshilar sani: {users_stat[0]}")