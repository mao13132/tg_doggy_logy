# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
import threading

from src.business.get_report.start_get_report import StartGetReport
from src.telegram.bot_core import BotDB


async def get_report_call(bot, id_user, loop):
    user_list = BotDB.get_all_users()

    if not user_list:
        try:
            await bot.send_message(id_user, '❌ Отчет пуст! В базе данных нет пользователей')
        except:
            pass

        return False

    question_list = BotDB.get_all_questions()

    settings_report = {
        'bot': bot,
        'id_user': id_user,
        'user_list': user_list,
        'question_list': question_list,
        'loop': loop,
    }

    trh = threading.Thread(target=StartGetReport(settings_report).start_get_report, name=(f'thr-1'))

    trh.setDaemon(True)

    trh.start()

    return True
