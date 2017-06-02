from diary import storage

TASK_STATUS_OPEN = 'open'
TASK_STATUS_REOPEN = 'reopen'
TASK_STATUS_CLOSE = 'close'


def show_tasks():
    tasks = storage.show_all_tasks()
    for task in tasks:
        print("""
- Задача №{task[id]}: {task[name]}
Описание: {task[description]}
Статус: {task[status]}
Начало: {task[start_date]}
Конец: {task[end_date]}
_____""".format(task=task))


def add_task():
    while True:
        task_name = input('Введите название задачи: ')
        task_description = input('Введите описание задачи: ')
        if task_name:
            storage.add_task(task_name, task_description)
            break
        else:
            print('Вы не ввели название задачи!')
    print('Задача добавлена.')


def edit_task():
    while True:
        task_id = input('Введите id редактируемой задачи: ')
        if not task_id:
            print('Вы не ввели идентификатор задачи!')
        task = storage.find_task_by_id(task_id)
        if not task:
            print('Задача с таким id не найдена!')

        new_name = input('Введите новое название задачи: ')
        new_desc = input('Введите новое описание задачи: ')
        if new_name:
            storage.edit_task_name(task_id, new_name)
            break
        if new_desc:
            storage.edit_task_description(task_id, new_desc)
            print('Задача отредактирована.')
            break


def close_task():
    while True:
        task_id = input('Введите id завершенной задачи: ')
        if task_id:
            task = storage.find_task_by_id(task_id)
            if not task:
                print('Задача с таким id не найдена!')
            else:
                storage.close_task(task_id)
                break
        else:
            print('Вы не ввели идентификатор задачи!')
    print('Задача закрыта.')


def reopen_task():
    while True:
        task_id = input('Введите id переоткрываемой задачи: ')
        if not task_id:
            print('Вы не ввели идентификатор задачи!')
        task = storage.find_task_by_id(task_id)
        if not task:
            print('Задача с таким id не найдена!')
        elif task['status'] in [TASK_STATUS_OPEN, TASK_STATUS_REOPEN]:
            print('Задача уже открыта.')
            break
        else:
            storage.change_task_status(task_id, TASK_STATUS_REOPEN)
            print('Задача переоткрыта.')
            break


def delete_task():
    print('удаление задачи')
