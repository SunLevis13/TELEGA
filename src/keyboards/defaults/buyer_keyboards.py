from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

commands_default_keyboard = ReplyKeyboardMarkup(
 keyboard=[
        [
            KeyboardButton(text = 'start')
        ]
    ]
 
)








# access_btn = ReplyKeyboardMarkup(
#     keyboard=[
#         [
#             KeyboardButton(text = 'Подтвердить номер телефона', request_contact=True)
#         ]
#     ],
#     resize_keyboard=True
# )