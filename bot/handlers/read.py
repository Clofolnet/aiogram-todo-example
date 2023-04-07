from aiogram import types

from bot import bot, dp
from bot.utils import check_user_exists
from db import session
from db.crud import job_crud


@dp.message_handler(commands=['read'])
@check_user_exists
async def read(message: types.Message, db=session.get_db()):
    """
        This handler will be called when user sends `/read` command
    """
    chat_id = message.chat.id
    message = ""
    for job in job_crud.get_multi(db=db):
        job_date = job.date.strftime("%d.%m.%Y")
        message += f"Job: {job.title}, Date: {job_date}\n\n"

    await bot.send_message(chat_id, message)
