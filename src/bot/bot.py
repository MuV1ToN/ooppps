import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

""" Load token"""
load_dotenv('.env')
TOKEN = os.getenv('TOKEN')

""" Create bot """
bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher(bot=bot)

