from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes,filters, MessageHandler, CallbackContext
import config
import logging
import asyncio
from datetime import datetime

from aiogram import Bot, Dispatcher, executor, types
from sqlighter import SQLighter

# задаем уровень логов
logging.basicConfig(level=logging.INFO)

# инициализируем бота
# bot = Bot(token=config.API_TOKEN)
# dp = Dispatcher(bot)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hi, {update.effective_user.first_name}! I'm a subscribe bot!")

if __name__ == '__main__':
    bot = ApplicationBuilder().token('5467090782:AAGmpzB3bDp0sbcAItgUMYgxbL4mIKI5O9c').build()
	
    print('server start')
   
    bot.add_handler(CommandHandler('start', start))
       
    bot.run_polling()
    
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)	

dp = Dispatcher(bot)
# инициализируем соединение с БД
db = SQLighter('db.db')

# Команда активации подписки
@dp.message_handler(commands=['subscribe'])
async def subscribe(message: types.Message):
	if(not db.subscriber_exists(message.from_user.id)):
		# если юзера нет в базе, добавляем его
		db.add_subscriber(message.from_user.id)
	else:
		# если он уже есть, то просто обновляем ему статус подписки
		db.update_subscription(message.from_user.id, True)
	
	await message.answer("Вы успешно подписались на рассылку!")

# Команда отписки
@dp.message_handler(commands=['unsubscribe'])
async def unsubscribe(message: types.Message):
	if(not db.subscriber_exists(message.from_user.id)):
		# если юзера нет в базе, добавляем его с неактивной подпиской (запоминаем)
		db.add_subscriber(message.from_user.id, False)
		await message.answer("Вы и так не подписаны.")
	else:
		# если он уже есть, то просто обновляем ему статус подписки
		db.update_subscription(message.from_user.id, False)
		await message.answer("Вы успешно отписаны от рассылки.")

if __name__ == '__main__':
	...
	echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    
	bot.add_handler(CommandHandler('start', start))
	bot.add_handler(echo_handler)

	bot.run_polling()

if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)