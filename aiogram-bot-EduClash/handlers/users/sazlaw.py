from aiogram import types
from loader import dp, db
import re
from keyboards.default.sazlawlar_menu import sazlaw_menu

@dp.message_handler(text_contains="Sazlawlar")
async def sazlawlar(message: types.Message):
    await message.answer("Sazlawlar menyusi", reply_markup=sazlaw_menu)

@dp.message_handler(text_contains="Magliwmatlarim")
async def magliwmatlar(message: types.Message):
    user_id=message.from_user.id
    user = db.select_user(id=user_id)

    msg = "Magliwmatlariniz: \n"
    msg += f"Atiniz: {user[1]}\n"
    msg += f"Klasiniz: {user[2]}\n"
    msg += f"Telefon nomer: +{user[3]}\n"
    msg += f"Telegram ID: <code>{user_id}</code>"

    await message.answer(msg)



@dp.message_handler(text_contains="Atimdi ozgertiw")
async def change_name(message: types.Message):
    user_id = message.from_user.id

    await message.answer("Jana atinizdi kiritin:")

    @dp.message_handler(lambda message: message.from_user.id == user_id)
    async def set_new_name(message: types.Message):
        new_name = message.text.strip()

        if not new_name:
            await message.answer("Iltimas, Atinizdi kiritin.")
            return

        if not re.match("^[A-Za-zА-Яа-яЁё ]+$", new_name):
            await message.answer("Atiniz tek gana hariplerden boliwi kerek")
            return

        db.update_user_name(new_name, user_id)
        await message.answer(f"Atiniz ozgertildi! Jana atiniz: {new_name}")


@dp.message_handler(text_contains="Kontaktti ozgertiw")
async def update_phone(message: types.Message):
    user_id = message.from_user.id

    await message.reply("Taza telefon nomerinizdi kiritin, misali: 9989xxxxxxx")
    new_phone = message.text.strip()

    if new_phone.isdigit() and len(new_phone) == 12:
        db.update_user_phone(new_phone, user_id)
        await message.reply(f"Sizdin telefon nomeriniz janalandi: {new_phone}")
    else:
        await message.reply("Iltimas, telefon nomerinizdi duris kiritin(+ belgisin qoymay kiritin): 9989xxxxxxx")









#         from aiogram import types
#         from loader import dp, db, bot
#
#         # Foydalanuvchiga telefon raqamini yangilash
#         @dp.message_handler(commands=["update_phone"])
#         async def update_phone(message: types.Message):
#             user_id = message.from_user.id
#
#             # Foydalanuvchining ma'lumotlarini bazadan olish
#             user = db.select_user(id=user_id)
#             if not user:
#                 await message.reply("Sizning profilingiz topilmadi. Iltimos, avval ro'yxatdan o'ting.")
#                 return
#
#             # Foydalanuvchiga yangi telefon raqamini kiritish uchun so'rov yuborish
#             await message.reply("Yangi telefon raqamingizni kiriting, masalan: 9989xxxxxxx")
#
#         # Foydalanuvchi yangi telefon raqamini yuborganda
#         @dp.message_handler(lambda message: message.text)
#         async def process_phone(message: types.Message):
#             user_id = message.from_user.id
#
#             # Foydalanuvchining ma'lumotlarini bazadan olish
#             user = db.select_user(id=user_id)
#             if not user:
#                 await message.reply("Sizning profilingiz topilmadi. Iltimos, avval ro'yxatdan o'ting.")
#                 return
#
#             # Telefon raqamini yangilash
#             new_phone = message.text.strip()
#
#             # Telefon raqami formatini tekshirish
#             if new_phone.isdigit() and len(new_phone) == 13:  # 9989xxxxxxx formatida bo'lishi kerak
#                 db.update_user_phone(new_phone, user_id)
#                 await message.reply(f"Sizning telefon raqamingiz yangilandi: {new_phone}")
#             else:
#                 await message.reply("Iltimos, telefon raqamingizni to'g'ri formatda kiriting: 9989xxxxxxx")
#
# from aiogram import types
# from loader import dp, db, bot
#
# # Foydalanuvchiga sinfini yangilash
# @dp.message_handler(commands=["update_class"])
# async def update_class(message: types.Message):
#     user_id = message.from_user.id
#
#     # Foydalanuvchining ma'lumotlarini bazadan olish
#     user = db.select_user(id=user_id)
#     if not user:
#         await message.reply("Sizning profilingiz topilmadi. Iltimos, avval ro'yxatdan o'ting.")
#         return
#
#     # Foydalanuvchiga yangi sinfini kiritish uchun so'rov yuborish
#     await message.reply("Yangi sinfingizni kiriting, masalan: 10B")
#
# # Foydalanuvchi yangi sinfini yuborganda
# @dp.message_handler(lambda message: message.text)
# async def process_class(message: types.Message):
#     user_id = message.from_user.id
#
#     # Foydalanuvchining ma'lumotlarini bazadan olish
#     user = db.select_user(id=user_id)
#     if not user:
#         await message.reply("Sizning profilingiz topilmadi. Iltimos, avval ro'yxatdan o'ting.")
#         return
#
#     # Sinfini yangilash
#     new_class = message.text.strip()
#
#     # Sinf nomini yangilash
#     db.update_user_klass(new_class, user_id)
#     await message.reply(f"Sizning sinfingiz yangilandi: {new_class}")
