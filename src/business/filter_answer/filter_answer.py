# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
from datetime import datetime

from src.business.filter_answer.date_filter import date_filter
from src.utils.logger._logger import logger_msg

from re import search


async def filter_answer(filter_answer, answer):
    if filter_answer == 'phone':
        regular_ = r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$'

        match = search(regular_, answer)

        return match
    elif filter_answer == 'email':
        regular_ = r'^((([0-9A-Za-z]{1}[-0-9A-z\.]{1,}[0-9A-Za-z]{1})|([0-9А-Яа-я]{1}[-0-9А-я\.]{1,}[0-9А-Яа-я]{1}))' \
                   r'@([-A-Za-z]{1,}\.){1,2}[-A-Za-z]{2,})$'

        match = search(regular_, answer)

        return match
    elif filter_answer == 'sex':

        if 'Мужской' in answer or 'Женский' in answer:
            return True

    elif not filter_answer:
        return True

    elif filter_answer == 'fio':
        split_fio = answer.split()

        if len(split_fio) == 3:
            return True

    elif filter_answer == 'text':
        if str(answer).isdigit():
            return False

        if len(answer) <= 2:
            return False

        return True

    elif filter_answer == 'date':
        res_filter = date_filter(answer)

        date_now = datetime.now()

        if date_now < res_filter:
            return False

        return res_filter

    else:
        error_ = f'Фильтр не задан для "{filter_answer}"'

        logger_msg(error_)

        return False

    return False
