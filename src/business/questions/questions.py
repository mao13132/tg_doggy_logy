# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
from src.telegram.keyboard.keyboards import Admin_keyb

QUESTIONS = {
    1: {
        'text': '🍀Пришлите следующим сообщением <b>свой номер телефона.</b>\n\nПример: +79113152214',
        'title': 'Телефон',
        'error': 'Вы прислали не корректный номер. Пожалуйста, пришлите следующим сообщением Ваш номер телефона.'
                 '\n\nПример: +79113152214',
        'filter': 'phone',
        'keyboard': '',
    },
    2: {
        'text': '🍀Пришлите следующим сообщением <b>Электронный адрес</b> (Email) \n\nПример dog@gmail.com',
        'title': 'Email',
        'error': 'Вы прислали не корректный электронный адрес, попробуйте ещё. \n\nПример dog@gmail.com',
        'filter': 'email',
        'keyboard': '',
    },
    3: {
        'text': '🍀Выберите <b>Пол собаки</b>',
        'title': 'Пол собаки',
        'error': 'Некорректный пол собаки! Выберите <b>Пол собаки</b>',
        'filter': 'sex',
        'keyboard': Admin_keyb.sex,
    },
    4: {
        'text': '',
        'title': '',
        'error': '',
        'filter': '',
        'keyboard': '',
    },
    5: {
        'text': '',
        'title': '',
        'error': '',
        'filter': '',
        'keyboard': '',
    },
    6: {
        'text': '',
        'title': '',
        'error': '',
        'filter': '',
        'keyboard': '',
    },
}
