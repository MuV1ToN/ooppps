from aiogram import Dispatcher
from aiogram.types import CallbackQuery
from src.keyboards.menu_keyboards import *
from src.bot.bot import bot
from src.database.database import get_conf_info
from src.handlers.commands import set_the_time


""" Events """
async def on_callback(callback: CallbackQuery):
    """
     Handler 
    for start
    """
    if callback.data == 'start':
        await bot.edit_message_text( text='📃ГЛАВНОЕ-МЕНЮ📃',
                                    chat_id=callback.message.chat.id,
                                    message_id=callback.message.message_id,
                                    reply_markup=main_menu())
        

    """
    Main menu
     handler
    """
    if callback.data == 'main_menu_btn1':
        await bot.edit_message_text( text='📃МЕНЮ-КОНФЕРЕНЦИЙ📃',
                                    chat_id=callback.message.chat.id,
                                    message_id=callback.message.message_id,
                                    reply_markup=conferences_menu())
        
    if callback.data == 'main_menu_btn2':
        await bot.edit_message_text( text='📃МЕНЮ-УВЕДОМЛЕНИЙ📃',
                                    chat_id=callback.message.chat.id,
                                    message_id=callback.message.message_id,
                                    reply_markup=notification_menu())
    

    """
    Conferences
       menu
      Handler
    """
    if callback.data == 'conf_menu_btn1':
        text = get_conf_info()
        for value in text.items():
            await bot.send_message( chat_id=callback.message.chat.id,
                                    text=f'<b><u>{value[0]}</u></b> \n\n{value[1]}')
            
        await bot.edit_message_text( text='Список конференций',
                                    chat_id=callback.message.chat.id,
                                    message_id=callback.message.message_id)
            
    if callback.data == 'back1':
        await bot.edit_message_text( text='📃ГЛАВНОЕ-МЕНЮ📃',
                                    chat_id=callback.message.chat.id,
                                    message_id=callback.message.message_id,
                                    reply_markup=main_menu())
        

    """
    Notification
       menu
      handler
    """
    if callback.data == 'notification_menu_btn1':
        await bot.edit_message_text(text=f'Введит время для уведомлений \nПример ввода времени в ковычках \n\n\t\t"06:00"',
                                    chat_id=callback.message.chat.id,
                                    message_id=callback.message.message_id)
        set_the_time(callback.message)
        



""" Register events """
def register_user_events(dp: Dispatcher) -> None:
    dp.register_callback_query_handler(on_callback)