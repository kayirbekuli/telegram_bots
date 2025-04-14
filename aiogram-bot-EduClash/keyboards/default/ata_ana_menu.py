from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

basqa_menyu = ReplyKeyboardMarkup(resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="Reytingi"),
            KeyboardButton(text="Qatnasi")
        ],
        [
            KeyboardButton(text="Jetiskenlikleri"),
            KeyboardButton(text="Kemshilikleri")
        ],
        [
            KeyboardButton(text="Oyindi bloklaw"),
            KeyboardButton(text="Menyuga qaytiw")
        ],

    ])