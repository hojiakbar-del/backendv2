from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import WebAppInfo
from aiogram.types import KeyboardButtonRequestUsers
from aiogram.types import KeyboardButtonRequestChat
def tugma():
    b = ReplyKeyboardBuilder()
    b.button(text="Text")
    b.button(text="Phone Number", request_contact=True)
    b.button(text="Location", request_location=True)
    b.button(text="YouTube", web_app=WebAppInfo(url="https://www.youtube.com/"))
    b.button(text="Bot",request_users=KeyboardButtonRequestUsers(request_id=1, user_is_bot=True, max_quantity=1))
    b.button(text="Botlar",request_users=KeyboardButtonRequestUsers(request_id=11, user_is_bot=True, max_quantity=10))
    b.button(text="Foydalanuvchi",request_users=KeyboardButtonRequestUsers(request_id=2, user_is_bot=False, max_quantity=1))
    b.button(text="Foydalanuvchilar",request_users=KeyboardButtonRequestUsers(request_id=12, user_is_bot=False, max_quantity=10))
    b.button(text="Kanal", request_chat=KeyboardButtonRequestChat(request_id=3, chat_is_channel=True, max_quantity=1))
    b.button(text="Kanallar", request_chat=KeyboardButtonRequestChat(request_id=13, chat_is_channel=True, max_quantity=10))
    b.button(text="Guruh", request_chat=KeyboardButtonRequestChat(request_id=4, chat_is_channel=False, max_quantity=1))
    b.button(text="Guruhlar", request_chat=KeyboardButtonRequestChat(request_id=14, chat_is_channel=False, max_quantity=10))

    b.adjust(2)
    return b.as_markup(resize_keyboard=True)













