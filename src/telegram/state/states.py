from aiogram import Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from settings import LOGO
from src.business.filter_answer.filter_answer import filter_answer
from src.business.questions.questions import QUESTIONS
from src.telegram.keyboard.keyboards import Admin_keyb
from src.telegram.sendler.sendler import Sendler_msg

from src.telegram.bot_core import BotDB


class States(StatesGroup):
    add_question = State()


async def add_question(message: Message, state: FSMContext):
    id_user = message.chat.id

    answer = message.text

    quest_number = None

    async with state.proxy() as data:
        quest_number = data['quest_number']

    filter_ = QUESTIONS[quest_number]['filter']

    is_bad = await filter_answer(filter_, answer)

    keyb = Admin_keyb().back_question(quest_number)

    if not is_bad:

        if QUESTIONS[quest_number]['keyboard']:
            keyb = QUESTIONS[quest_number]['keyboard'](quest_number - 1)

        error_ = QUESTIONS[quest_number]['error']

        await Sendler_msg().sendler_photo_message(message, LOGO, error_, keyb)

        return False

    question = QUESTIONS[quest_number]['title']

    res_add = BotDB.add_or_update_question(id_user, quest_number, question, answer)

    next_quest = quest_number + 1

    if QUESTIONS[next_quest]['keyboard']:
        keyb = QUESTIONS[next_quest]['keyboard'](quest_number)

    quest_text = QUESTIONS[next_quest]['text']

    async with state.proxy() as data:
        data['quest_number'] += 1

    await Sendler_msg().sendler_photo_message(message, LOGO, quest_text, keyb)

    return True


def register_state(dp: Dispatcher):
    dp.register_message_handler(add_question, state=States.add_question)
