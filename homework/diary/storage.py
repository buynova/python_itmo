import sqlite3
import os.path as Path


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
SET status = ?
WHERE id = ?
'''

SQL_CLOSE_TASK = '''
UPDATE diary_tasks
SET status = 'closed', end_date = CURRENT_TIMESTAMP
WHERE id = ?
'''


def connect(db_name=None):
    if db_name is None:
        db_name = ':memory:'

    conn = sqlite3.connect(db_name)

    return conn


def initialize(conn):
    with conn:
        script_file_path = Path.join(Path.dirname(__file__), 'schema.sql')

        with open(script_file_path) as f:
            conn.executescript(f.read())


def add_task(conn, task_name, description):
    with conn:
        cursor = conn.execute(SQL_INSERT_NEW_TASK, (task_name, description))
        cursor.commit()


def edit_task(conn, task_id, task_name, task_desc):
    with conn:
        cursor = conn.execute(SQL_EDIT_TASK, (task_name, task_desc, task_id))
        cursor.commit()


def change_task_status(conn, task_id, status):
    with conn:
        cursor = conn.execute(SQL_CHANGE_STATUS, (status, task_id))
        cursor.commit()


def close_task(conn, task_id):
    with conn:
        cursor = conn.execute(SQL_CLOSE_TASK, (task_id,))
        cursor.commit()
