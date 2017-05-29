"""
Модуль "Ежедневник".
"""


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

    if id_action == '1':
        print('Вы выбрали действие "Вывести список задач"\n')
        select_action()
    elif id_action == '2':
        print('Вы выбрали действие "Добавить задачу"\n')
        select_action()
    elif id_action == '3':
        print('Вы выбрали действие "Отредактировать задачу"\n')
        select_action()
    elif id_action == '4':
        print('Вы выбрали действие "Завершить задачу"\n')
        select_action()
    elif id_action == '5':
        print('Вы выбрали действие "Начать задачу сначала"\n')
        select_action()
    elif id_action == '6':
        print('Вы выбрали действие "Выход"\n')
        select_action()
    else:
        print('Вы ввели неверные данные.\n')
        select_action()

select_action()
