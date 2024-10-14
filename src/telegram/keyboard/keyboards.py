from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, \
    InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData


class Admin_keyb:
    def start_keyb(self):
        self._start_key = InlineKeyboardMarkup(row_width=1)

        self._start_key.add(InlineKeyboardButton(text=f'🐼 Начать опрос', callback_data='start_question'))

        return self._start_key

    def back_start_menu(self):
        self._start_key = InlineKeyboardMarkup(row_width=1)

        self._start_key.add(InlineKeyboardButton(text=f'⬅️ Назад', callback_data='over_state'))

        return self._start_key

    def back_question(self, quest_number):
        self._start_key = InlineKeyboardMarkup(row_width=1)

        self._start_key.add(InlineKeyboardButton(text=f'⬅️ Назад', callback_data=f'back-quest_{quest_number}'))

        return self._start_key

    @staticmethod
    def sex(quest_number):
        _start_key = InlineKeyboardMarkup(row_width=2)

        _start_key.add(InlineKeyboardButton(text=f'Мужской', callback_data=f'sex_Мужской'))

        _start_key.insert(InlineKeyboardButton(text=f'Женский', callback_data=f'sex_Женский'))

        _start_key.add(InlineKeyboardButton(text=f'⬅️ Назад', callback_data=f'back-quest_{quest_number}'))

        return _start_key
