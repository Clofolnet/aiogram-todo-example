from datetime import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from bot import bot, dp
from bot.messages import (create_job_get_date, create_job_message,
                          success_message)
from bot.utils import check_user_exists
from db import session
from db.crud import job_crud, user_crud
from db.schemas import JobCreate


class CreateJobStates(StatesGroup):
    job = State()
    date = State()


@dp.message_handler(commands=['write'])
@check_user_exists
async def write(message: types.Message, db=session.get_db()):
    """
        This handler will be called when user sends `/write` command
    """
    user_id = message.from_user.id
    chat_id = message.chat.id
    state = dp.current_state(chat=chat_id, user=user_id)
    await state.set_state(CreateJobStates.job)
    await CreateJobStates.job.set()
    await bot.send_message(chat_id, create_job_message)


class CreateJobFunctions(object):
    """ Functions for creating a case reminder """

    @dp.message_handler(state=CreateJobStates.job, content_types=types.ContentType.ANY)
    @check_user_exists
    async def get_job(message: types.Message, state: FSMContext):
        """ 
            Obtaining a job and running a date wait
        """
        chat_id = message.chat.id
        user_id = message.from_user.id
        text_data = message.text
        await state.update_data(job=text_data)
        await bot.send_message(chat_id=chat_id, text=create_job_get_date)
        await CreateJobStates.date.set()

    @dp.message_handler(state=CreateJobStates.date, content_types=types.ContentType.ANY)
    @check_user_exists
    async def get_date(message: types.Message, state: FSMContext):
        """ 
            Getting the date and starting to create a job record
        """
        chat_id = message.chat.id
        user_id = message.from_user.id
        text_data = message.text
        await state.update_data(date=text_data)
        data = await state.get_data()
        await state.finish()
        await CreateJobFunctions.create_job(chat_id, data, user_id)

    async def create_job(chat_id, data, user_id, db=session.get_db()):
        job = data['job']
        date = data['date']
        user = user_crud.get_user_by_user_id(db=db, user_id=user_id)
        date_obj = datetime.strptime(date, "%d.%m.%Y").date()
        obj_in = JobCreate(user_id=user.id, title=job, date=date_obj)
        job_crud.create(db=db, obj_in=obj_in)
        await bot.send_message(chat_id, success_message)
