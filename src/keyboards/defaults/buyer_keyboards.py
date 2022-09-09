from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

commands_default_keyboard = ReplyKeyboardMarkup(
 keyboard=[
        [
            KeyboardButton(text = '/start'),
            KeyboardButton(text = '/items') #здесь кнопки клавиатуры в одну строку
        ],
        [
            KeyboardButton(text = '/help') #здесь создается второй подсписок - вторая строка кнопок
           
        ]
    ],
    resize_keyboard=True
 
)








# access_btn = ReplyKeyboardMarkup(
#     keyboard=[
#         [
#             KeyboardButton(text = 'Подтвердить номер телефона', request_contact=True)
#         ]
#     ],
#     resize_keyboard=True
# )