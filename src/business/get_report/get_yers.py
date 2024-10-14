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

    if full_years == 0:
        count_month = (date_now - date_birthday).days // 30

        full_years = f"{count_month} месяца(ев)"

    return str(full_years)
