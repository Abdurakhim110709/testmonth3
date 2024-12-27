from database import Database
from aiogram import Bot, Dispatcher
from dotenv import dotenv_values



token = dotenv_values(".env").get("TOKEN")
bot = Bot(token=token)
dp = Dispatcher()
db = Database("database/db.sqlite3")
