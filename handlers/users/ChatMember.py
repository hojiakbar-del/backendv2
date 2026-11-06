from aiogram import types, Router
from filterlar.group import GroupFilter

rt= Router()

@rt.message(GroupFilter)
async def chat(msg: types.Message,):
    if msg.new_chat_members[0] == msg.from_user.id:
        print("Foydalanuvchi o'zini o'zi qo'shdi")
    elif msg.new_chat_members[0] != msg.from_user.id:
        print(f"Bu foydalanuvchi {msg.from_user.id} tomonidan qoshildi")









