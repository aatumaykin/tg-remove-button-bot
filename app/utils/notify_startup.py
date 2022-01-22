import logging

from aiogram import Dispatcher
from app.utils import config

logger = logging.getLogger(__name__)


async def on_startup_notify(dp: Dispatcher):
    try:
        await dp.bot.send_message(config.ADMIN_USER, "Бот Запущен")
    except Exception as err:
        logger.exception(err)
