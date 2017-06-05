import sys
from collections import OrderedDict, namedtuple

from url_shortener import storage


# def get_connection():
#     return storage.connect('shortener.sqlite')

get_connection = lambda: storage.connect('shortener.sqlite')

Action = namedtuple('Action', ['func', 'name'])  # именованный кортеж
actions = OrderedDict()


def action(cmd, name):
    def decorator(func):
        actions[cmd] = Action(func=func, name=name)
        return func
    return decorator


@action('1', 'Добавить URL-адрес')
def action_add():
    """Обработчик действия 'Добавить URL-адрес'."""
    ok = False

    while not ok:
        url = input('\nВведите URL-адрес: ')

        if not url:
            break

        if url.startswith(('http://', 'https://', 'ftp://', 'ftps://')):
            with get_connection() as conn:
                short_url = storage.add_url(conn, url)

            print('Короткий URL-адрес: {}'.format(short_url))
            ok = True
        else:
            print('Некорректный URL-адрес!')


@action('2', 'Найти оригинальный URL-адрес')
def action_find():
    """Обработчик действия 'Найти оригинальный адрес'."""
    short_url = input('\nВведите короткий URL-адрес: ')

    if short_url:
        with get_connection() as conn:
            url = storage.find_url_by_short(conn, short_url)

        if url:
            url = url.get('original_url')
            print('Оригинальный URL-адрес: {}'.format(url))
        else:
            print('Оригинальный адрес не найден.')


@action('3', 'Вывести все URL-адреса')
def action_find_all():
    """Обработчик действия 'Показать все ссылки'."""
    with get_connection() as conn:
        urls = storage.find_all(conn)

    for url in urls:
        print('{url[short_url]} - {url[original_url]} - {url[created]}'.format(url=url))


@action('m', 'Показать меню')
def action_show_menu():
    """Обработчик действия 'Показать меню'."""
    print('\nURL Shortener v2.0\n')
    for cmd, act in actions.items():
        print('{}. {}'.format(cmd, act.name))


@action('q', 'Выйти')
def action_exit():
    """Обработчик действия 'Выйти'."""
    sys.exit(0)


def main():
    with get_connection() as conn:
        storage.initialize(conn)

    action_show_menu()

    # actions = {
    #     '1': action_add,
    #     '2': action_find,
    #     '3': action_find_all,
    #     'm': action_show_menu,
    #     'q': action_exit
    # }

    while True:
        cmd = input('\nВведите команду: ')
        action = actions.get(cmd)

        if action:
            action.func()
        else:
            print('Неизвестная команда!')
