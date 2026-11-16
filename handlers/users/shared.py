from aiogram import Router, F
from aiogram.types import Message

rt = Router()
@rt.message(F.users_shared)
async def user_handler(message: Message):
    users = message.users_shared.users
    for user in users:
        await message.answer(f"User ID: {user.user_id}")

@rt.message(F.chat_shared)
async def chat_handler(message: Message):
    chat_id = message.chat_shared.chat_id
    await message.answer(f"Chat ID: {chat_id}")