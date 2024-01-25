import asyncio
import logging
from aiogram import executor
from src.bot.bot import dp
from src.handlers.checkerTime import on_startup
from src.handlers.register import register_handler

""" Main func for start """
def main() -> None:
    register_handler(dp=dp)    
    try:
        print('Bot is run')
        executor.start_polling(dispatcher=dp, on_startup=on_startup)
    except Exception as _ex:
        print(f'There as an {_ex}')

""" Run bot """
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())