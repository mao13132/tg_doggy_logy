from aiogram import Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from settings import LOGO
from src.business.filter_answer.filter_answer import filter_answer
from src.business.questions.questions import QUESTIONS
from src.telegram.sendler.sendler import Sendler_msg


class States(StatesGroup):
    add_question = State()


async def add_question(message: Message, state: FSMContext):
    answer = message.text

    quest_number = None

    async with state.proxy() as data:
        quest_number = data['quest_number']

    filter_ = QUESTIONS[quest_number]['filter']

    is_bad = await filter_answer(filter_, answer)

    if not is_bad:

        keyb = None

        error_ = QUESTIONS[quest_number]['error']

        await Sendler_msg().sendler_photo_message(message, LOGO, error_, keyb)

    next_quest = quest_number + 1

    print()


def register_state(dp: Dispatcher):
    dp.register_message_handler(add_question, state=States.add_question)
