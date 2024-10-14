# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
from datetime import datetime

from settings import COUNT_QUEST_DATE
from src.business.filter_answer.date_filter import date_filter


def get_years(questions_user):
    try:
        date_birthday = questions_user[COUNT_QUEST_DATE]['answer']

        date_birthday = date_filter(date_birthday)
    except:
        return 'Неизвестно'

    date_now = datetime.now()

    full_years = (date_now - date_birthday).days // 365

    return str(full_years)
