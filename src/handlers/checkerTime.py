from datetime import datetime 
from aiogram import Dispatcher
from src.bot.bot import bot
import asyncio
from src.database.database import get_conf_info, get_time_info


""" Check time for send info """
async def check_time():
    while True:
        info = get_conf_info()
        time = get_time_info()
        await asyncio.sleep(40)
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        for time_info in time.items():
                if current_time == time_info[1]:
                         for value in info.items():
                            await bot.send_message(chat_id=time_info[0],text=f'<b><u>{value[0]}</u></b> \n\n{value[1]}')


""" Create new procees for check time"""
async def on_startup(dp: Dispatcher):
    asyncio.create_task(check_time())