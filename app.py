from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils import executor

TOKEN = r"5742356636:AAHBvQOAV5Y7LDG8dmyIlmTVDEyUPRdoWCs"

bot = Bot(token = TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(text=['Hello', 'Начать'])
@dp.message_handler(commands="start")
async def answer_start_command(message: types.Message):
		await message.answer(text = f"Hi!\nGlad to see you!")


if __name__ == '__main__':
	executor.start_polling(dispatcher = dp)