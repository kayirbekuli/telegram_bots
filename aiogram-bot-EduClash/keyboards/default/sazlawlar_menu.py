from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

sazlaw_menu = ReplyKeyboardMarkup(resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="Atimdi ozgertiw"),
            KeyboardButton(text="Klasti ozgertiw")
        ],
        [
            KeyboardButton(text="Kontaktti ozgertiw"),
            KeyboardButton(text="Magliwmatlarim")
        ],
        [
            KeyboardButton(text="Menyuga qaytiw")
        ]
    ])