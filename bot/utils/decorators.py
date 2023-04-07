
from functools import wraps

from aiogram import types

from bot.messages import only_registration
from db import session
from db.crud import user_crud


def check_user_exists(func):
    @wraps(func)
    async def wrapper(message: types.Message, *args, **kwargs):
        user_id = message.from_user.id
        db = session.get_db()
        if not user_crud.check_unique_by_user_id(db=db, user_id=user_id):
            await message.answer(only_registration)
            return
        return await func(message, db=db, *args, **kwargs)
    return wrapper
