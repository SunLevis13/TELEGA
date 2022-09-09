from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from keyboards import commands_default_keyboard
from loader import dp

@dp.message_handler(text=['Hello', 'Начать', 'hello','начать', 'привет'])
@dp.message_handler(commands="start")
async def answer_start_command(message: types.Message):
	# print(message ['from'] ['first_name'])
	print(message.from_user.first_name)
	await message.answer(text = f'Hi, {message.from_user.first_name}!\nGlad to see you!')

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

@dp.message_handler(text=["Помидоры"])
async def answer_start_command(message: types.Message):
		await message.answer(text = f"Помидоры черри")


@dp.message_handler(text=["Редис"])
async def answer_start_command(message: types.Message):
		await message.answer(text = f"Редис сезонный")