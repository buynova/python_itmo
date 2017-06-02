import sqlite3
import os.path as Path

# здесь использую символ "*", потому что смысл запроса - "Показать всё", а "всё" == "*"
SQL_SHOW_ALL = '''
SELECT id, name, description, status, start_date, end_date
FROM diary_tasks
'''

SQL_SELECT_TASK_BY_ID = '''
SELECT name, description, status, start_date, end_date
FROM diary_tasks
WHERE id = ?
'''

SQL_INSERT_NEW_TASK = '''
INSERT INTO diary_tasks (name, description)
VALUES (?, ?)
'''

SQL_EDIT_TASK = '''
UPDATE diary_tasks
SET name = ?, description = ?
WHERE id = ?
'''

SQL_CHANGE_STATUS = '''
UPDATE diary_tasks
SET status = ?, start_date = CURRENT_TIMESTAMP, end_date = ''
WHERE id = ?
'''

SQL_CLOSE_TASK = '''
UPDATE diary_tasks
SET status = 'close', end_date = CURRENT_TIMESTAMP
WHERE id = ?
'''


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def connect(db_name=None):
    if db_name is None:
        db_name = ':memory:'

    conn = sqlite3.connect(db_name)
    conn.row_factory = dict_factory
    return conn


def initialize(conn):
    with conn:
        script_file_path = Path.join(Path.dirname(__file__), 'schema.sql')

        with open(script_file_path) as f:
            conn.executescript(f.read())


def show_all_tasks():
    with connect('diary.sqlite') as conn:
        initialize(conn)
        cursor = conn.execute(SQL_SHOW_ALL)
        return cursor.fetchall()


def find_task_by_id(task_id):
    with connect('diary.sqlite') as conn:
        initialize(conn)
        cursor = conn.execute(SQL_SELECT_TASK_BY_ID, (task_id,))
        return cursor.fetchone()


def add_task(task_name, description):
    with connect('diary.sqlite') as conn:
        initialize(conn)
        conn.execute(SQL_INSERT_NEW_TASK, (task_name, description))
        return


def edit_task(task_id, task_name, task_desc):
    with connect('diary.sqlite') as conn:
        initialize(conn)
        cursor = conn.execute(SQL_EDIT_TASK, (task_name, task_desc, task_id))


def change_task_status(task_id, status):
    with connect('diary.sqlite') as conn:
        initialize(conn)
        conn.execute(SQL_CHANGE_STATUS, (status, task_id))
        return


def close_task(task_id):
    with connect('diary.sqlite') as conn:
        initialize(conn)
        conn.execute(SQL_CLOSE_TASK, (task_id,))
        return
