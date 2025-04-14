from aiogram import types
from loader import dp
from aiogram.types import ReplyKeyboardRemove
from keyboards.default.basmenyu import bas_menyu
from keyboards.default.sabaqlar_menu import sabaq_menyu
from keyboards.default.ata_ana_menu import basqa_menyu
from keyboards.default.bellesiw_menu import bellesiw_menyu
from keyboards.default.ai_chat_menu import ai_chat_menyu

@dp.message_handler(text_contains="Sabaqlar")
async def sabaqlar(message: types.Message):
    await message.answer("Sabaqlar menyusi", reply_markup=sabaq_menyu)

@dp.message_handler(text_contains="Bellesiw")
async def sabaqlar(message: types.Message):
    await message.answer("Bellesiw menyusi", reply_markup=bellesiw_menyu)

@dp.message_handler(text_contains="Ata-analar")
async def sabaqlar(message: types.Message):
    await message.answer("Ata-analar menyusi", reply_markup=basqa_menyu)

@dp.message_handler(text_contains="AI Chat")
async def sabaqlar(message: types.Message):
    await message.answer("AI Chat menyusi", reply_markup=ai_chat_menyu)

@dp.message_handler(text_contains="Menyuga qaytiw")
async def sabaqlar(message: types.Message):
    await message.answer("Bas menyu", reply_markup=bas_menyu)




