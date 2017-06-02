"""
1.1. Установка соединения
1.2. Выбор БД, с которой хотим работать
Для SQLite:
1. Выбор файла, с которым хотим работать

2. Создание объекта-курсора
3. Выполнение SQL-запросов
    - на изменение состояния БД
    - выборка данных из БД
4. Закрытие соединения
"""

import sqlite3
import os.path as Path

from url_shortener.converter import convert, inverse

SQL_SELECT_ALL = '''
    SELECT id, original_url, short_url, created
    FROM shortener
'''
SQL_SELECT_URL_BY_PK = SQL_SELECT_ALL + ' WHERE id = ?'
SQL_SELECT_URL_BY_ORIGINAL = SQL_SELECT_ALL + ' WHERE original_url = ?'
SQL_INSERT_URL = '''
    INSERT INTO shortener (original_url)
    VALUES (?)
'''
SQL_UPDATE_SHORT_URL = '''
    UPDATE shortener
    SET short_url = ?
    WHERE id = ?
'''


def dict_factory(cursor, row):
    d = {}
    # print('row:', row)
    # print('col:', cursor.description)
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def connect(db_name=None):
    if db_name is None:
        db_name = ':memory:'

    conn = sqlite3.connect(db_name)
    conn.row_factory = dict_factory  # подключили 'фабрику'

    return conn


def initialize(conn):
    with conn:
        script_file_path = Path.join(Path.dirname(__file__), 'schema.sql')

        with open(script_file_path) as f:
            conn.executescript(f.read())


def add_url(conn, url, domain=''):
    url = url.strip('/')
    if not url:
        # here must be error
        return

    with conn:
        found = find_url_by_origin(conn, url)
        if found:
            return found.get('short_url')

        cursor = conn.execute(SQL_INSERT_URL, (url,))

        pk = cursor.lastrowid
        short_url = '{}/{}'.format(domain.strip('/'), convert(pk))

        conn.execute(SQL_UPDATE_SHORT_URL, (short_url, pk))
        return short_url


def find_all(conn):
    with conn:
        cursor = conn.execute(SQL_SELECT_ALL)
        return cursor.fetchall()


def find_url_by_pk(conn, pk):
    with conn:
        cursor = conn.execute(SQL_SELECT_URL_BY_PK, (pk,))
        return cursor.fetchone()


def find_url_by_short(conn, short_url):
    short_url = short_url.rsplit('/', 1).pop()
    pk = inverse(short_url)
    return find_url_by_pk(conn, pk)


def find_url_by_origin(conn, original_url):
    original_url = original_url.strip('/')
    with conn:
        cursor = conn.execute(SQL_SELECT_URL_BY_ORIGINAL, (original_url,))
        return cursor.fetchone()
