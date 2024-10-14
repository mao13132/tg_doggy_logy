from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from aiogram import Dispatcher

from src.business.start_one.start_one import start_one


async def start(message: Message, state: FSMContext):
    await state.finish()

    result = await start_one(message, state)

    return result


def register_user(dp: Dispatcher):
    dp.register_message_handler(start, text_contains='/start', state='*')

    dp.register_message_handler(start, text_contains='')
