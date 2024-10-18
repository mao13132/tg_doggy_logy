# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
from aiogram.types import Message

from settings import ADMIN, COUNT_QUEST_DATE
from src.business.filter_answer.date_filter import date_filter
from src.business.get_report.get_yers import _get_years
from src.telegram.bot_core import BotDB
from src.telegram.sendler.sendler import Sendler_msg


async def finish_send_admin(message: Message):
    id_user = message.chat.id

    user_data = BotDB.get_users_by_id(id_user)

    questions = BotDB.get_questions_by_id(id_user)

    questions = sorted(questions, key=lambda x: int(x[0]))

    questions_text = ''

    for quest_row in questions:
        count_quest = int(quest_row[2])

        question_sql = quest_row[3]

        answer_sql = quest_row[4]

        questions_text += f"\n<b>{question_sql}</b>\n<code>{answer_sql}</code>\n"

        if count_quest == COUNT_QUEST_DATE:
            date_birthday = date_filter(answer_sql)

            full_years = _get_years(date_birthday)

            questions_text += f"\n<b>Лет</b>\n<code>{full_years}</code>\n"

    msg = f'⭐️ <b>Новая анкета</b>\n\n' \
          f'Юзернейм: <code>@{user_data[2]}</code>\n' \
          f'Имя: {user_data[3]}\n' \
          f'Фамилия: {user_data[4]}\n' \
          f'Премиум: {user_data[5]}\n' \
          f'Дата первого касания: {user_data[6]}\n' \
          f'Последняя активность: {user_data[7]}\n\n' \
          f'➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n' \
          f'{questions_text}'

    for admin_ in ADMIN:
        try:
            msg_id = await message.bot.send_message(admin_, msg, disable_web_page_preview=True)
        except:
            pass

        try:
            await message.bot.pin_chat_message(chat_id=admin_,
                                               message_id=msg_id['message_id'])
        except:
            pass
