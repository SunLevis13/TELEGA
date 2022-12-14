from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

commands_default_keyboard = ReplyKeyboardMarkup(
 keyboard=[
        [
            KeyboardButton(text = 'Начать'),
            KeyboardButton(text = 'Список товаров'), #здесь кнопки клавиатуры в одну строку
            KeyboardButton(text = 'О нас'),
        ],
        [
            KeyboardButton(text = 'Помощь') #здесь создается второй подсписок - вторая строка кнопок
           
        ],
        [
            KeyboardButton(text = 'Регистрация', #здесь создается третий подсписок - третья строка кнопок
            request_contact=True), #запрашиваем номер телефона
            KeyboardButton(text = 'Поделиться локацией',
            request_location=True) #запрашиваем локацию
        ],
        [
            KeyboardButton(text = 'Скрыть меню') #новая кнопка, скрыть клаву
           
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


