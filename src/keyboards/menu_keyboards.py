from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

""" Start """
def start() -> InlineKeyboardMarkup:
    btn1 = InlineKeyboardButton(text = 'Продолжить', callback_data='start')
    markup = InlineKeyboardMarkup(inline_keyboard=[[btn1]])
    return markup

""" Main menu """
def main_menu() -> InlineKeyboardMarkup:
    btn1 = InlineKeyboardButton(text='Конференции', callback_data='main_menu_btn1')
    btn2 = InlineKeyboardMarkup(text='Уведомления', callback_data='main_menu_btn2')
    markup = InlineKeyboardMarkup(inline_keyboard=[[btn1], [btn2]])
    return markup

""" Conferences menu """
def conferences_menu() -> InlineKeyboardMarkup:
    btn1 = InlineKeyboardButton(text='Информация о конференциях', callback_data='conf_menu_btn1')
    btn2 = InlineKeyboardButton(text='Назад', callback_data='back1')
    markup = InlineKeyboardMarkup(inline_keyboard=([[btn1], [btn2]]))
    return markup

""" Notification menu """
def notification_menu() -> InlineKeyboardMarkup:
    btn1 = InlineKeyboardButton(text='Собственные Уведомления', callback_data='notification_menu_btn1')
    btn2 = InlineKeyboardButton(text='Назад', callback_data='back1')
    markup = InlineKeyboardMarkup(inline_keyboard=([[btn1], [btn2]]))
    return markup
