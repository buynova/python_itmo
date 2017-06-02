from diary import storage


def show_tasks():
    tasks = storage.show_all_tasks()
    for task in tasks:
        print("""Задача №{task[id]}: {task[name]}
Описание: {task[description]}
Статус: {task[status]}
Начало: {task[start_date]}
Конец: {task[end_date]}
""".format(task=task))


def add_task():
    while True:
        task_name = input('Введите название задачи: ')
        task_description = input('Введите описание задачи: ')
        if task_name:
            storage.add_task(task_name, task_description)
            break
        else:
            print('Вы не ввели название задачи!')
    print('Задача добавлена!')


def edit_task():
    print('Вы выбрали действие "Отредактировать задачу"\n')


def close_task():
    print('Вы выбрали действие "Завершить задачу"\n')


def reopen_task():
    print('Вы выбрали действие "Начать задачу сначала"\n')


def delete_task():
    print('удаление задачи')
