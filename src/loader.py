import sqlite3
from pathlib import Path

from aiogram import Bot, Dispatcher
from config import TOKEN

from db_api import Database

bot = Bot(token = TOKEN)
dp = Dispatcher(bot)

db_path = Path('db_api', 'database', 'shop_database.db')
#db_path = Path("C:/Users/wwolf/YandexDisk/Zueva/GB/Telegrambot/src/db_api/database/shop_database.db")
db = Database(db_path=db_path)
try: 
    db.create_table_users() # создать табличку в базе данных тк она сначала пустая
except sqlite3.OperationalError as e:
    print(e)
except Exception as e:
    print(e)
