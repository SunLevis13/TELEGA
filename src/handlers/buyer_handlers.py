from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from keyboards import commands_default_keyboard, see_commands_default_keyboards
from loader import dp

@dp.message_handler(text=['Hello', 'Начать', 'hello','начать', 'привет'])
@dp.message_handler(commands="start")
async def answer_start_command(message: types.Message):
	# print(message ['from'] ['first_name'])
	print(message.from_user.first_name)
	await message.answer(text = f'Hi, {message.from_user.first_name}!\nGlad to see you!',
    reply_markup=ReplyKeyboardRemove()) #убираем клавиатуру с экрана, чтобы только на команде help она была)

@dp.message_handler(text=['Показать'])
@dp.message_handler(commands=['help'])
async def answer_help_command(message: types.Message):
		await message.answer(text = f"Список команд представлен на клавиатуре", reply_markup=commands_default_keyboard)

@dp.message_handler(commands=["items"])
async def answer_items_command(message: types.Message):
		await message.answer(text = f'У нас в наличии:'
                                    '\n-Огурцы Луховицкие'
                                    '\n-Помидоры черри'
                                    '\n-Редис сезонный',
                                    reply_markup=ReplyKeyboardRemove()) #убираем клавиатуру с экрана, чтобы только на команде help она была

@dp.message_handler(text=["Скрыть клавиатуру"])
async def answer_start_command(message: types.Message):
		await message.answer(text = f"Мы её спрятали.",
                            reply_markup=see_commands_default_keyboards) # ЗДЕСЬ МЫ ЗАМЕНЯЕМ НАШУ 1ую клаву на клаву С КНОПКОЙ ПОКАЗАТЬ!!!!!!!!!!!!!!!!!!!!

@dp.message_handler() # хэндлер, который отвечает на любую ерунду
async def answer_trash_command(message: types.Message):
		await message.answer(text = f'Я пока такого не знаю..',
                             reply_markup=ReplyKeyboardRemove()) #убираем клавиатуру с экрана, чтобы только на команде help она была

@dp.message_handler(content_types=['contact']) # хэндлер, который отлавливает определенный тип данных. Через запятую можно перечислить в списке что ловить. Сейчас contact
async def answer_contact_command(message: types.Message):
        print(message)
        if message.from_user.id == message.contact.user_id: # проверяем, что полученный контакт принадлежит пользователю (сверяем user_id)
            await message.answer(text = f'Это твой контакт',
                             reply_markup=ReplyKeyboardRemove()) #убираем клавиатуру с экрана, чтобы только на команде help она была
        else: 
            await message.answer(text = f'А это кто?',
                             reply_markup=ReplyKeyboardRemove())

@dp.message_handler(content_types=['location']) # хэндлер, который отлавливает определенный тип данных. Через запятую можно перечислить в списке что ловить. Сейчас локация
async def answer_contact_command(message: types.Message):
        print(message)
        if message.from_user.id == message.contact.user_id: # проверяем, что полученная локация принадлежит пользователю (сверяем user_id)
            await message.answer(text = f'Ты здесь',
                             reply_markup=ReplyKeyboardRemove()) #убираем клавиатуру с экрана, чтобы только на команде help она была
        else: 
            await message.answer(text = f'Кто здесь?',
                             reply_markup=ReplyKeyboardRemove())




# @dp.message_handler(text=["Помидоры"])
# async def answer_start_command(message: types.Message):
# 		await message.answer(text = f"Помидоры черри")


# @dp.message_handler(text=["Редис"])
# async def answer_start_command(message: types.Message):
# 		await message.answer(text = f"Редис сезонный")