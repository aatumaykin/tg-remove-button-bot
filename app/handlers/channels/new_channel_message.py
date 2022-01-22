from aiogram.types import Message, ContentTypes, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.utils.callback_data import CallbackData

from app.loader import dp, bot

action_callback = CallbackData("action", "id", "action")


@dp.channel_post_handler(content_types=ContentTypes.ANY)
async def new_channel_message(message: Message):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text="🗑️ удалить", callback_data="remove"))

    await message.copy_to(message.chat.id, reply_markup=keyboard)
    await bot.delete_message(message.chat.id, message.message_id)


@dp.callback_query_handler(text="remove")
async def send_random_value(call: CallbackQuery):
    await bot.delete_message(call.message.chat.id, call.message.message_id)
