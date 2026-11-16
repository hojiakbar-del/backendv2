from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import WebAppInfo
from aiogram.types import KeyboardButtonRequestUsers
from aiogram.types import KeyboardButtonRequestChat
def tugma():
    b = ReplyKeyboardBuilder()
    b.button(text="Jo'rabek")
    # b.button(text="telefon", request_contact=True)
    b.button(text="lokatsiya", request_location=True)
    b.button(text="youtube", web_app=WebAppInfo(
    url="https://www.youtube.com/",
    ))
    b.button(text="sinov123",
             request_users=KeyboardButtonRequestUsers(request_id=1, user_is_bot=False, max_quantity=2))
    b.button(text="sinov456", request_chat=KeyboardButtonRequestChat(request_id=2, chat_is_channel=False))

    b.adjust(2)
    return b.as_markup(resize_keyboard=True)


# text
# request_users
# request_chat
# request_contact
# request_location
# web_app











