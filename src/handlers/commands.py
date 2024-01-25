from aiogram import types, Dispatcher
from src.keyboards.menu_keyboards import start, main_menu
from src.database.database import get_id
from src.database.database import get_time
import time

""" Command start """
async def on_start(message: types.Message) -> None:
    id = message.from_user.id 
    get_id(id=id)
    await message.answer(
        text = f'\t\t Привет {message.from_user.username}! \n \nЯ бот для уведомлений о новых онлайн конференциях! \n \nЧтобы продолжить тыкай на кнопку ниже ⬇️⬇️⬇️',
        reply_markup = start())

""" Command help """
async def help(message: types.Message) -> None:
    await message.answer(text = 'Ну это точно мимо')


""" Command Main menu"""
async def menu(message: types.Message) -> None:
    await message.answer(text="📃ГЛАВНОЕ-МЕНЮ📃",reply_markup=main_menu())


""" Command set the time"""
async def set_the_time(message: types.Message):
    id = message.from_user.id
    try:
        time.strptime(message.text, "%H:%M")
        get_time(id=id, time=message.text)
    except ValueError:
        await message.reply("Время некорректно!")
    else:
        await message.reply(f'Вы назначели время уведомлений на ➡️ "<b>{message.text}</b>" ')



""" Register commands """
def register_user_commands(dp: Dispatcher) -> None:
    dp.register_message_handler(on_start, commands = ['start'])
    dp.register_message_handler(help, commands=['help'])
    dp.register_message_handler(menu, commands=['menu'])
    dp.register_message_handler(set_the_time)
    

