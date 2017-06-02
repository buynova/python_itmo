from diary import storage


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
    print('Вы выбрали действие "Отредактировать задачу"\n')


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
        elif task['status'] in ['открыта', 'переоткрыта']:
            print('Задача уже открыта.')
            break
        else:
            storage.change_task_status(task_id, 'переоткрыта')
            print('Задача переоткрыта.')
            break


def delete_task():
    print('удаление задачи')
