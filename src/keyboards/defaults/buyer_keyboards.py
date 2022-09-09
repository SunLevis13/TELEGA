from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

commands_default_keyboard = ReplyKeyboardMarkup(
 keyboard=[
        [
            KeyboardButton(text = '/start'),
            KeyboardButton(text = '/items') #здесь кнопки клавиатуры в одну строку
        ],
        [
            KeyboardButton(text = '/help') #здесь создается второй подсписок - вторая строка кнопок
           
        ],
        [
            KeyboardButton(text = 'Поделиться контактом', #здесь создается третий подсписок - третья строка кнопок
            request_contact=True) #запрашиваем номер телефона
            
        ],
        [
            KeyboardButton(text = 'Скрыть клавиатуру') #новая кнопка, скрыть клаву
           
        ],
    ],
    resize_keyboard=True
 
)

see_commands_default_keyboards = ReplyKeyboardMarkup(
 keyboard=[
    [
        KeyboardButton(text = 'Показать')
    ]
 ],
    resize_keyboard=True
)


