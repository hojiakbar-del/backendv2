from aiogram import Router, types, filters
from aiogram.fsm.context import FSMContext
from states.anketa_state import AnketaState
from config.settings import ADMINS
rt = Router()
@rt.message(filters.Command("anketa"))
async def anketa(msg: types.Message, state: FSMContext):
    await msg.answer("ismingizni kiriting: ")
    await state.set_state(AnketaState.ism)

@rt.message(AnketaState.ism)
async def ism(msg: types.Message, state: FSMContext):
    global ism
    ism = msg.text
    await msg.answer(f"{ism} familyangizni kiriting: ")
    await state.set_state(AnketaState.familya)
    await state.update_data(ism=msg.text)

@rt.message(AnketaState.familya)
async def familya(msg: types.Message, state: FSMContext):
    await msg.answer(f"{ism} yoshngizni kiriting: ")
    familya = msg.text
    await state.set_state(AnketaState.yosh)
    await state.update_data(familya=msg.text)

@rt.message(AnketaState.yosh)
async def yosh(msg: types.Message, state: FSMContext):
    if msg.text.isdigit():
        yosh = int(msg.text)
        await msg.answer("barcha ma'lumotlaringizni qabul qildik, e'tiboringzi uchun rahmat!")
        await state.update_data(yosh=msg.text)
        await state.clear()
    else:
        await msg.answer("yoshngizni qayta kiriting!")
        await state.set_state(AnketaState.yosh)

    # global ism
    # global familya
    # global yosh
    if str(familya).endswith("a"):
        gender = "woman" #kodga ta'siri yo'q adashmaslik uchun qo'yganman
        if yosh > 20:
            age = "opa"
        elif yosh < 20:
            age = "singil"
        else:
            age = "\'dugona\'?"
    else:
        gender = "man" #kodga ta'siri yo'q adashmaslik uchun qo'yganman
        if yosh > 20:
            age = "aka"
        elif yosh < 20:
            age = "uka"
        else:
            age = "dost"
    n = f"yaxshimisz {age}? \n"
    n += "registratsiyadan o'tganingzi uchun rahmat.\n"
    n += f"ma'lumotlarni qaytadan kiritish uchun:\n"
    n+= "/anketa"
    await msg.answer(n)
