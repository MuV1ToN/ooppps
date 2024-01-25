from aiogram import Dispatcher
from src.handlers.commands import register_user_commands
from src.handlers.events import register_user_events

""" Register handlers(commands and events)"""
def register_handler(dp: Dispatcher) -> None:
    register_user_commands(dp=dp)
    register_user_events(dp=dp)
    
