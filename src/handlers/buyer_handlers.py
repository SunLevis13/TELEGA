from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from keyboards import commands_default_keyboard, see_commands_default_keyboards
from loader import dp
from loader import db

from keyboards import start_inline_keyboard, get_item_inline_keyboard
from keyboards.inlines.callback_data import start_callback, navigation_callback
from loader import bot, data_manager


@dp.message_handler(text=['Hello', 'Начать', 'hello','начать', 'Привет', 'привет'])
@dp.message_handler(commands="start")
async def answer_start_command(message: types.Message):
	# print(message ['from'] ['first_name'])
	print(message.from_user.first_name)
	await message.answer(text = f'Hi, {message.from_user.first_name}!\nGlad to see you!',
   # reply_markup=ReplyKeyboardRemove(),  #убираем стандартную клавиатуру с экрана, чтобы только на команде help она была
    reply_markup=start_inline_keyboard) #прикрепляем inline клавиатуру ответом на приветствие

@dp.callback_query_handler(start_callback.filter()) # прикрепляем хэндлер с нашей стандартной клавиатурой к inline клавиатуре-кнопке Главное меню
async def answer_help_command(call: types.CallbackQuery):
    print(call)
    await call.message.answer(text='Список команд представлен на клавиатуре',
                                reply_markup=commands_default_keyboard)
    await bot.delete_message(chat_id=call.message.chat.id,
                                message_id=call.message.message_id)

# Делаем хэндлер, чтобы при нажатии на items выпадала клавиатура.
@dp.message_handler(text=['Список товаров'])
@dp.message_handler(commands=["items"])
async def answer_items_command(message: types.Message):
    status, item_info = data_manager.get_item(0)
    item_text = f'Название товара {item_info['name']}:'\ # формируем текст сообщения item_text
                f'\nКоличество товара: {item_info['count']}:'\
                f'\nОписание товара: {item_info['description']}'
	await message.answer(text = item_text, # прикрепляем здесь item_text
                        reply_markup=get_item_inline_keyboard()) # прикрепляем нужную inline клавиатуру ответом

# __________________________________________________________________________________________________________________________________
# НИЖЕ ХЭНДЛЕРЫ ДЛЯ СТАНДАРТНОЙ КЛАВИАТУРЫ

# @dp.message_handler(text=['Показать'])
# @dp.message_handler(text=['Помощь'])
# @dp.message_handler(commands=['help'])
# async def answer_help_command(message: types.Message):
# 		await message.answer(text = f"Список команд представлен на клавиатуре", reply_markup=commands_default_keyboard)

# @dp.message_handler(text=['О нас'])
# @dp.message_handler(commands=['info'])
# async def answer_info_command(message: types.Message):
# 		await message.answer(text = f"Мы - интернет магазин!", reply_markup=commands_default_keyboard)

# @dp.message_handler(text=['Список товаров'])
# @dp.message_handler(commands=["items"])
# async def answer_items_command(message: types.Message):
# 		await message.answer(text = f'У нас в наличии:'
#                                     '\n-Огурцы Луховицкие'
#                                     '\n-Помидоры черри'
#                                     '\n-Редис сезонный',
#                                     reply_markup=ReplyKeyboardRemove()) # убираем клавиатуру с экрана, чтобы только на команде help она была

# @dp.message_handler(text=["Скрыть меню"])
# async def answer_hide_command(message: types.Message):
# 		await message.answer(text = f"Мы его спрятали.",
#                             reply_markup=see_commands_default_keyboards) # ЗДЕСЬ МЫ ЗАМЕНЯЕМ НАШУ 1ую клаву на клаву С КНОПКОЙ ПОКАЗАТЬ!!!!!!!!!!!!!!!!!!!!

# @dp.message_handler() # хэндлер, который отвечает на любую ерунду
# async def answer_trash_command(message: types.Message):
# 		await message.answer(text = f'Я пока такого не знаю..',
#                              reply_markup=ReplyKeyboardRemove()) #убираем клавиатуру с экрана, чтобы только на команде help она была

# @dp.message_handler(content_types=['contact']) # хэндлер, который отлавливает определенный тип данных. Через запятую можно перечислить в списке что ловить. Сейчас contact
# async def answer_contact_command(message: types.Message):
#         print(message) # вывод инфы о пользователе, можно взять его имя, тел, id
#         if message.from_user.id == message.contact.user_id: # проверяем, что полученный контакт принадлежит пользователю (сверяем user_id)
#             await message.answer(text = f'Регистрация прошла успешно',
#                              reply_markup=ReplyKeyboardRemove()) #убираем клавиатуру с экрана, чтобы только на команде help она была
#             db.add_user(int(message.from_user.id), str(message.contact.phone_number)) # записываем контакт в базу данных  
#         else: 
#             await message.answer(text = f'А это кто?',
#                              reply_markup=ReplyKeyboardRemove())

# @dp.message_handler(content_types=['location']) # хэндлер, который отлавливает определенный тип данных. Через запятую можно перечислить в списке что ловить. Сейчас локация
# async def answer_location_command(message: types.Message):
#         print(message)
#         if message.from_user.id == message.contact.user_id: # проверяем, что полученная локация принадлежит пользователю (сверяем user_id)
#             await message.answer(text = f'Ты здесь',
#                              reply_markup=ReplyKeyboardRemove()) #убираем клавиатуру с экрана, чтобы только на команде help она была
#         else: 
#             await message.answer(text = f'Кто здесь?',
#                              reply_markup=ReplyKeyboardRemove())


