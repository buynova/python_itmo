import sqlite3

from telegram_bot import queries


class DataBase(object):
    def __init__(self, database):
        """Констурктор класса DataBase"""
        self.conn = sqlite3.connect(database)
        self.cursor = self.conn.cursor()

    def select_all_translates_except(self, word_id):
        """Получение всех записей с переводом, кроме id"""
        with self.conn:
            result = self.cursor.execute(queries.SELECT_TRANSLATES, (word_id,)).fetchall()
            return result

    def select_word(self, word_id):
        """Получение записи по id"""
        with self.conn:
            result = self.cursor.execute(queries.SELECT_WORD, (word_id,)).fetchone()
            return result

    def select_spanish(self, rus):
        """Получение испанского слова по переводу"""
        with self.conn:
            result = self.cursor.execute(queries.SELECT_SPANISH, (rus,)).fetchone()
            return result

    def add_new_word(self, esp, rus):
        """Добавление нового слова в словарь"""
        with self.conn:
            result = self.cursor.execute(queries.INSERT_WORD, (esp, rus))
            return result

    def close(self):
        """Закрываем текущее соединение с БД"""
        self.conn.close()
