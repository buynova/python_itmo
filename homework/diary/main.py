"""
Модуль "Ежедневник".
"""

import Tasks


def select_action():
    diary_message = """Ежедневник. Выберите действие:

    1. Вывести список задач.
    2. Добавить задачу.
    3. Отредактировать задачу.
    4. Завершить задачу.
    5. Начать задачу сначала.
    6. Выход.
    """
    print(diary_message)
    id_action = input('Введите номер действия: ')
    if id_action not in ['1', '2', '3', '4', '5', '6']:
        print('Вы ввели неверные данные.\n')
        select_action()
    else:
        id_action = int(id_action)

    if id_action == 1:
        Tasks.show_tasks()
        select_action()
    elif id_action == 2:
        Tasks.add_task()
        select_action()
    elif id_action == 3:
        Tasks.edit_task()
        select_action()
    elif id_action == 4:
        Tasks.close_task()
        select_action()
    elif id_action == 5:
        Tasks.reopen_task()
        select_action()
    elif id_action == 6:
        Tasks.exit_from_diary()

select_action()
