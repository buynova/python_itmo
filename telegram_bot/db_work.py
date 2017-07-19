import sqlite3

SELECT_TRANSLATES = '''
SELECT trans_w FROM words WHERE _id_w != ?
'''

SELECT_WORD = '''
SELECT * FROM words WHERE _id_w = ?
'''

SELECT_SPANISH = '''
SELECT word, sound FROM words WHERE UPPER(trans_w) like UPPER(?)
'''

INSERT_WORD = '''
INSERT INTO words (word, trans_w) VALUES (?, ?)
'''


class DataBase(object):
    def __init__(self, database):
        self.conn = sqlite3.connect(database)
        self.cursor = self.conn.cursor()

    def select_all_except(self, rownum):
        with self.conn:
            return self.cursor.execute(SELECT_TRANSLATES, (rownum,)).fetchall()

    def select_word(self, rownum):
        with self.conn:
            return self.cursor.execute(SELECT_WORD, (rownum,)).fetchone()

    def select_spanish(self, rus):
        with self.conn:
            return self.cursor.execute(SELECT_SPANISH, (rus,)).fetchone()

    def add_new_word(self, esp, rus):
        with self.conn:
            return self.cursor.execute(INSERT_WORD, (esp, rus))

    def close(self):
        """ Закрываем текущее соединение с БД """
        self.conn.close()
