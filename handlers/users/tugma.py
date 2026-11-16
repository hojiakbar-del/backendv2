from aiogram import types, filters, Router, F
from keyboards.reply_keyboard import tugma
rt = Router()
@rt.message(F.text == "tugma")
async def tugma_handler(msg: types.Message):
    await msg.answer("xohlagan tugmangizni tanlang", reply_markup=tugma())
