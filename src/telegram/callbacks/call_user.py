from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

from settings import LOGO
from src.business.get_report.get_report_call import get_report_call
from src.business.questions.questions import QUESTIONS
from src.business.start_one.start_one import start_one
from src.telegram.sendler.sendler import *

from src.telegram.keyboard.keyboards import *
from src.telegram.state.states import States, add_question


async def over_state(call: types.CallbackQuery, state: FSMContext):
    await state.finish()

    await Sendler_msg.log_client_call(call)

    await start_one(call.message, state)

    return True


async def start_question(call: types.CallbackQuery, state: FSMContext):
    await Sendler_msg.log_client_call(call)

    keyb = Admin_keyb().back_start_menu()

    quest_number = 1

    _msg = QUESTIONS[quest_number]['text']

    img = QUESTIONS[quest_number]['img']

    await Sendler_msg().sendler_photo_call(call, img, _msg, keyb)

    await States.add_question.set()

    async with state.proxy() as data:
        data['quest_number'] = quest_number

    return True


async def sex_(call: types.CallbackQuery, state: FSMContext):
    await Sendler_msg.log_client_call(call)

    try:
        _, sex = str(call.data).split('_')

    except Exception as es:
        print(f'Ошибка при разборе sex_ {es}')

        return False

    call.message.text = sex

    await add_question(call.message, state)

    return True


async def back_quest(call: types.CallbackQuery, state: FSMContext):
    await Sendler_msg.log_client_call(call)

    try:
        _, quest_number = str(call.data).split('_')

        quest_number = int(quest_number)

    except Exception as es:
        print(f'Ошибка при разборе back_quest {es}')

        return False

    async with state.proxy() as data:
        data['quest_number'] = quest_number

    if quest_number == 1:
        keyb = Admin_keyb().back_start_menu()
    else:
        keyb = Admin_keyb().back_question(quest_number - 1)

    if QUESTIONS[quest_number]['keyboard']:
        keyb = QUESTIONS[quest_number]['keyboard'](quest_number - 1)

    _msg = QUESTIONS[quest_number]['text']

    img = QUESTIONS[quest_number]['img']

    await Sendler_msg().sendler_photo_call(call, img, _msg, keyb)

    await States.add_question.set()

    return True


async def get_report(call: types.CallbackQuery, state: FSMContext):
    await Sendler_msg.log_client_call(call)

    await state.finish()

    id_user = call.message.chat.id

    msg_ = f'⚠️ Формирование отчета запущено, я пришлю его как он будет готов, ожидайте...'

    keyb = Admin_keyb().back_admin()

    await Sendler_msg().sendler_photo_call(call, LOGO, msg_, keyb)

    import asyncio

    loop = asyncio.get_event_loop()

    await get_report_call(call.bot, id_user, loop)

    return True


def register_callbacks(dp: Dispatcher):
    dp.register_callback_query_handler(start_question, text_contains='start_question')

    dp.register_callback_query_handler(over_state, text='over_state', state='*')

    dp.register_callback_query_handler(back_quest, text_contains='back-quest_', state='*')

    dp.register_callback_query_handler(sex_, text_contains='sex_', state='*')

    dp.register_callback_query_handler(get_report, text_contains='get_report', state='*')
