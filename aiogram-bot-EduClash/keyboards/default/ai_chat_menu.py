from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

ai_chat_menyu = ReplyKeyboardMarkup(resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="Chat GPT"),
            KeyboardButton(text="Claude AI")
        ],
        [
            KeyboardButton(text="Menyuga qaytiw")
        ],
    ])