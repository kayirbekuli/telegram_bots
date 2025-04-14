from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

bas_menyu = ReplyKeyboardMarkup(resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="📚 Sabaqlar"),
            KeyboardButton(text="🤖 AI Chat")
        ],
        [
            KeyboardButton(text="🧠 Bellesiw"),
            KeyboardButton(text="⚙️ Sazlawlar")
        ],
        [
            KeyboardButton(text="👨‍👩‍👧 Ata-analar"),
            KeyboardButton(text="💬 Pikir ham usinislar")
        ],
    ])