
from aiogram.utils import executor
from handlers import dp


print("server start")


if __name__ == '__main__':
	executor.start_polling(dispatcher = dp)
