from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, WebAppData

from bot.messages import create_job_button_message
from config import settings


def create_job_markup():
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(
                text=create_job_button_message, web_app=WebAppData(
                    url=f"{settings.SITE_URL}/create-job")
            )
            ]
        ]
    )
    return reply_markup
