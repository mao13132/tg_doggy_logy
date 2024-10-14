# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
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
    else:
        error_ = f'Фильтр не задан для "{filter_answer}"'

        logger_msg(error_)

        return False
