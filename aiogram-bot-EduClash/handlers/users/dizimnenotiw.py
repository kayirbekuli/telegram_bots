from aiogram import types
from aiogram.dispatcher import FSMContext  # magliwmatlardi, qaerde ekenin saqlap qaliw
from aiogram.dispatcher.filters import Command
from keyboards.default.kontakt import kontaktt
from loader import dp, db
from states.personaldata import PersonalData
from aiogram.types import ContentType
from utils.db_api.sqlitebaza import Database
from aiogram.types import ReplyKeyboardRemove
from keyboards.default.basmenyu import bas_menyu



@dp.message_handler(text="Dizimnen o'tiw")
async def enter_test(message: types.Message):
    await message.answer("Toliq atin'izdi jazin:", reply_markup=ReplyKeyboardRemove())

    await PersonalData.fullname.set()


@dp.message_handler(state=PersonalData.fullname)
async def answer_fullname(message: types.Message,state: FSMContext):
    fullname = message.text
    # await state.update_data(name=fullname)
    await state.update_data(
        {"name": fullname}
    )
    await message.answer("Neshenshi klassiz?:")
    # await PersonalData.email.set()
    await PersonalData.next()


@dp.message_handler(state=PersonalData.klass)
async def answer_email(message: types.Message, state: FSMContext):
    klass = message.text
    await state.update_data(
        {"klass": klass}
    )
    await message.answer("Telefon nomer kiritin:", reply_markup=kontaktt)
    await PersonalData.next()


@dp.message_handler(state=PersonalData.phonenum, content_types=ContentType.CONTACT)
async def answer_phone(message: types.Message, state: FSMContext):
    num = message.contact.phone_number  # Shu yer o‘zgardi
    await state.update_data(
        {"phone": num}
    )

    # Ma'lumotlarni olish
    data = await state.get_data()
    name = data.get('name')
    klass = data.get('klass')
    phone = data.get('phone')

    # msg = "Tomendegi mag'liwmatlar alindi:\n"
    # msg += f"Ati: {name.title()}\n"
    # msg += f"Klasi: {email}\n"
    # msg += f"Telefon: {phone}"

    async def on_startup():
        db.create_table_users()  # Bu faqat dastlabki ishga tushirishda kerak
    id = message.from_user.id

    db.add_user(id, name, klass, phone)
    await message.answer("Magliwmatlar qabil qilindi", reply_markup=ReplyKeyboardRemove())
    await message.answer(f"Botimizga xosh kelipsiz {name}", reply_markup=bas_menyu)
    try:
        await state.finish()
    except KeyError:
        print(f"❗️State already removed for chat: {message.chat.id}")

