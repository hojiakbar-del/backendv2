from aiogram import Router, types
from filterlar.group import GroupFilter

rt=Router()
@rt.message(GroupFilter())
async def ChatPhoto(msg: types.Message,):
    if msg.new_chat_photo:
        await msg.reply("Yangi rasm!")
    elif msg.delete_chat_photo:
        await msg.reply("Rasm o'chirildi!")
    if msg.new_chat_title:
        await msg.reply(f"Yangi nom {msg.new_chat_title}!")
    else:
        pass
    if msg.caption != None :
        await msg.reply(f"hmmmm \"{msg.caption}\" degin...")
    elif msg.caption_entities != None :
        await msg.reply(f"\"{msg.caption_entities}\" lar")









