from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

sabaq_menyu = ReplyKeyboardMarkup(resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="Sabaqliqlar"),
            KeyboardButton(text="Videokurslar")
        ],
        [
            KeyboardButton(text="Testler"),
            KeyboardButton(text="Kitaplar")
        ],
        [
            KeyboardButton(text="Menyuga qaytiw")
        ]
    ])