from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

bellesiw_menyu = ReplyKeyboardMarkup(resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="Reyting"),
            KeyboardButton(text="Oyinlar")
        ],
        [
            KeyboardButton(text="Testler"),
            KeyboardButton(text="Bellesiw")
        ],
        [
            KeyboardButton(text="Menyuga qaytiw")
        ]
    ])