from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kontaktt = ReplyKeyboardMarkup(resize_keyboard=True,
                             keyboard=[
                                 [
                                     KeyboardButton(text="Kontakt jiberiw", request_contact=True)
                                 ]
                             ])