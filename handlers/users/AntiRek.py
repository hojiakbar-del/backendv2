from aiogram import Router, Bot, F
from aiogram.types import Message

rt = Router()

@rt.message(F.chat.type.in_({"group", "supergroup"}))
async def reklama_ochir(msg: Message, bot: Bot):
    user = await bot.get_chat_member(msg.chat.id, msg.from_user.id)
    if user.status in ["member", "creator", "administrator"]:
        if msg.entities or msg.caption_entities:
            try:
                await msg.delete()
            except:
                pass









