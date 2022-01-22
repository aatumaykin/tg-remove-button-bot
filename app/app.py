import app.handlers
from aiogram import executor

from app.loader import dp
from app.utils.notify_startup import on_startup_notify
from app.utils.set_bot_commands import set_default_commands
from aiogram.dispatcher import Dispatcher


async def on_startup(dispatcher: Dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

    # Уведомляет про запуск
    await on_startup_notify(dispatcher)


async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


def run():
    executor.start_polling(dispatcher=dp, on_startup=on_startup, on_shutdown=shutdown)
