import json
from datetime import datetime

from aiogram import types

from bot import bot, dp
from bot.keybroads import markup_keybroads
from bot.messages import create_job_with_web_app, success_message
from bot.utils import check_user_exists
from db import session
from db.crud import job_crud, user_crud
from db.schemas import JobCreate


@dp.message_handler(commands=['web'])
@check_user_exists
async def web(message: types.Message):
    """
        This handler will be called when user sends `/web`command
    """
    chat_id = message.chat.id

    await bot.send_message(chat_id, text=create_job_with_web_app, reply_markup=markup_keybroads.create_job_markup())


@dp.message_handler(content_types=types.ContentTypes.WEB_APP_DATA)
@check_user_exists
async def handle_webapp_data(message: types.Message, db=session.get_db()):
    """ Data listener with web app """
    chat_id = message.chat.id
    user_id = message.from_user.id

    data = json.loads(message.web_app_data.data)
    user = user_crud.get_user_by_user_id(db=db, user_id=user_id)
    date_obj = datetime.strptime(data['date'], "%d.%m.%Y").date()
    obj_in = JobCreate(user_id=user.id, title=data['job'], date=date_obj)
    job_crud.create(db=db, obj_in=obj_in)
    await bot.send_message(chat_id, success_message)
