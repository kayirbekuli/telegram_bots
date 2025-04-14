from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admin_menu = ReplyKeyboardMarkup(resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="Statistika"),
            KeyboardButton(text="Reklama jiberiw")
        ],
        [
            KeyboardButton(text="ID arqali tabiw"),
            KeyboardButton(text="Reytingi joqarilar")
        ],
        [
            KeyboardButton(text="Izge qaytiw")
        ]
    ])