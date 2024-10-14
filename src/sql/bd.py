import datetime
import sqlite3
from datetime import datetime

from src.utils.logger._logger import logger_msg


class BotDB:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self, db_file):
        try:

            self.conn = sqlite3.connect(db_file, timeout=30)

            print('Подключился к SQL DB:', db_file)

            self.cursor = self.conn.cursor()

            self.check_table()

        except Exception as es:
            print(f'Ошибка при работе с SQL {es}')

    def check_table(self):

        try:
            self.cursor.execute(f"CREATE TABLE IF NOT EXISTS "
                                f"users (id_pk INTEGER PRIMARY KEY AUTOINCREMENT, "
                                f"id_user TEXT, "
                                f"username TEXT, "
                                f"first_name TEXT, "
                                f"last_name TEXT, "
                                f"premium TEXT, "
                                f"join_date DATETIME, "
                                f"last_time DATETIME DEFAULT 0, "
                                f"push1 BOOLEAN DEFAULT 0, "
                                f"push2 BOOLEAN DEFAULT 0, "
                                f"push_time DATETIME DEFAULT 0, "
                                f"date_buy DATETIME DEFAULT 0, "
                                f"other TEXT)")

        except Exception as es:
            print(f'SQL исключение check_table users {es}')

        try:
            self.cursor.execute(f"CREATE TABLE IF NOT EXISTS "
                                f"questions (id_pk INTEGER PRIMARY KEY AUTOINCREMENT, "
                                f"id_user TEXT, "
                                f"count_quest NUMBER, "
                                f"question TEXT, "
                                f"answer TEXT, "
                                f"other TEXT)")

        except Exception as es:
            print(f'SQL исключение check_table questions {es}')

        return True

    def check_or_add_user(self, id_user, data_user):

        result = self.cursor.execute(f"SELECT * FROM users WHERE id_user='{id_user}'")

        response = result.fetchall()

        if not response:
            now_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            self.cursor.execute("INSERT OR IGNORE INTO users ('id_user', 'username', 'first_name', 'last_name', "
                                "'premium', 'join_date') VALUES (?,?,?,?,?,?)",
                                (id_user, data_user['username'], data_user['first_name'], data_user['last_name'],
                                 data_user['premium'], now_date,))

            self.conn.commit()

            return True

        return False

    def edit_user(self, key, value, id_user):

        try:

            result = self.cursor.execute(f"SELECT {key} FROM users "
                                         f"WHERE id_user = '{id_user}'")

            response = result.fetchall()

            if not response:
                logger_msg(f'SQL Не могу отредактировать пользователя "{id_user}" поле: "{key}" значение: "{value}"')
                return False

            self.cursor.execute(f"UPDATE users SET {key} = '{value}' WHERE id_user = '{id_user}'")

            self.conn.commit()

            print(f'SQL: Отредактировал пользователя "{id_user}" поле: "{key}" значение: "{value}"')

            return True

        except Exception as es:
            logger_msg(f'SQL ERROR: Не смог изменить пользователя"{id_user}" поле: "{key}" значение: "{value}" "{es}"')

            return False

    def add_or_update_question(self, id_user, count_quest, question, answer):

        result = self.cursor.execute(f"SELECT * FROM questions WHERE id_user='{id_user}' AND "
                                     f"count_quest='{count_quest}'")

        response = result.fetchall()

        if not response:
            self.cursor.execute("INSERT OR IGNORE INTO questions ('id_user', 'count_quest', 'question', "
                                "'answer') VALUES (?,?,?,?)",
                                (id_user, count_quest, question, answer))

            self.conn.commit()

            return True

        else:

            self.cursor.execute(f"UPDATE questions SET question='{question}', answer='{answer}' "
                                f"WHERE id_user = '{id_user}' AND count_quest='{count_quest}'")

            self.conn.commit()

            return True

    def close(self):
        self.conn.close()
        print('Отключился от SQL BD')
