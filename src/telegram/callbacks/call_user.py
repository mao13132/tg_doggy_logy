from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

from settings import LOGO
from src.business.questions.questions import QUESTIONS
from src.business.start_one.start_one import start_one
from src.telegram.sendler.sendler import *

from src.telegram.keyboard.keyboards import *
from src.telegram.state.states import States


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

    await Sendler_msg().new_sendler_photo_call(call, LOGO, _msg, keyb)

    await States.add_question.set()

    async with state.proxy() as data:
        data['quest_number'] = quest_number

    return True


async def back_quest(call: types.CallbackQuery, state: FSMContext):
    await Sendler_msg.log_client_call(call)

    # TODO выбор клавиатуры на 1 вопрос и если есть клавиатура

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

    _msg = QUESTIONS[quest_number]['text']

    await Sendler_msg().new_sendler_photo_call(call, LOGO, _msg, keyb)

    await States.add_question.set()

    return True


def register_callbacks(dp: Dispatcher):
    dp.register_callback_query_handler(start_question, text_contains='start_question')

    dp.register_callback_query_handler(over_state, text='over_state', state='*')

    dp.register_callback_query_handler(back_quest, text_contains='back-quest_', state='*')
