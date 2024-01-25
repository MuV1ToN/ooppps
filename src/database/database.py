import sqlite3
from src.parsing.parsing import parsing_info
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# Creaet db
def database() -> None:
    """ Create db"""

    db = sqlite3.connect('conferences.db')
    command = db.cursor()
    """
    Table with 
    conferences
       info
    """
    command.execute("""
                    CREATE TABLE IF NOT EXISTS ConfInfo
                    (id int auto_increment primary key,
                    Title varchar UNIQUE,
                    Discription varchar UNIQUE)
                    """)
    

    """
    Table with users 
    id and their time
    """
    command.execute("""
                    CREATE TABLE IF NOT EXISTS UserTime
                    (id int auto_increment primary key,
                    UserID varchar UNIQUE,
                    Time varchar)
                    """)
    db.commit()
    command.close()
    db.close()


# Register id Users
def get_id(id) -> str:
    """ Register id users """

    database()
    db = sqlite3.connect('conferences.db')
    command = db.cursor()
    try:
        command.execute(f"INSERT INTO UserTime(UserID) VALUES ('%s')" % id)
    except:
        command.execute(f"INSERT OR REPLACE INTO UserTime(UserID) VALUES ('%s')" % id)
    db.commit()
    command.close()
    db.close()


# Add user time in db
def get_time(id, time):
    db = sqlite3.connect('conferences.db')
    command = db.cursor()
    try:
        command.execute(f"INSERT INTO UserTime(UserID, Time) VALUES ('%s', '%s')" % (id, time))
    except:
        command.execute(f"INSERT OR REPLACE INTO UserTime(UserID, Time) VALUES ('%s', '%s')" % (id, time))
    db.commit()
    command.close()
    db.close()


# Get info from parsing
def get_info() -> None:
    """ Get info from parsing"""

    database()
    info = parsing_info()
    for value in info:
        title = value[0]
        discription = value[1]
        db = sqlite3.connect('conferences.db')
        command = db.cursor()
        try:
            command.execute(f"INSERT INTO ConfInfo(Title, Discription) VALUES ('%s','%s')" % (title, discription))
        except:
            command.execute(f"INSERT OR REPLACE INTO ConfInfo(Title, Discription) VALUES ('%s','%s')" % (title, discription))
        db.commit()
        command.close()
        db.close()


# Get time from db 
def get_time_info() -> None:
    """ Get time from db """

    db = sqlite3.connect('conferences.db')
    command = db.cursor()
    command.execute('SELECT * FROM UserTime')
    info = command.fetchall()
    time_info = dict()
    for value in info:
        time_info[value[1]] = value[2]
    command.close()
    db.close()
    return time_info

# Get info from db 
def get_conf_info() -> None:
    """ Get info from db """ 

    get_info()
    db = sqlite3.connect('conferences.db')
    command = db.cursor()
    command.execute('SELECT * FROM ConfInfo')
    info = command.fetchall()
    text = dict()
    for value in info:
        text[value[1]] = value[2]
    command.close()
    db.close()
    return text


if __name__ == "__main__":
    database()