from aiogram import types

from bot import bot, dp
from bot.messages import hello_again_message
from db import session
from db.crud import user_crud
from db.schemas import UserCreate


@dp.message_handler(commands=['start'])
async def start(message: types.Message, db=session.get_db()):
    """
        This handler will be called when user sends `/start`command
    """
    user_id = message.from_user.id
    chat_id = message.chat.id
    language_code = message.from_user.language_code
    username = message.from_user.username
    full_name = message.from_user.full_name

    if user_crud.check_unique_by_user_id(db=db, user_id=user_id):
        await bot.send_message(chat_id, hello_again_message)
    else:
        obj_in = UserCreate(user_id=user_id, chat_id=chat_id, language_code=language_code,
                            username=username, full_name=full_name)
        user_crud.create(db=db, obj_in=obj_in)
        await bot.send_message(chat_id, hello_again_message)
