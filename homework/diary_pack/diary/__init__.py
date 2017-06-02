import sys

from diary import tasks, storage


DIARY_MESSAGE = """==============================
Ежедневник. Выберите действие:

1. Вывести список задач.
2. Добавить задачу.
3. Отредактировать задачу.
4. Завершить задачу.
5. Начать задачу сначала.
6. Удалить задачу.
7. Выход.
==============================
"""


def show_menu():
    print(DIARY_MESSAGE)


def action_exit():
    sys.exit(0)


def main():
    show_menu()

    actions = {
        '1': tasks.show_tasks,
        '2': tasks.add_task,
        '3': tasks.edit_task,
        '4': tasks.close_task,
        '5': tasks.reopen_task,
        '6': tasks.delete_task,
        '7': action_exit
    }

    while True:
        id_action = input('Введите номер действия: ')
        action = actions.get(id_action)

        if action:
            action()
        else:
            print('Вы ввели неверные данные')
