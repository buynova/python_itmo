# Декораторы

# Замыкания

from urllib.request import urlopen
import time


def page(url):

    # Замкнутая область

    def get():
        return urlopen(url).read()
    return get

python = page('http://python.org')
# print(python)
# print(python())


def benchmark(func):
    # замкнутая область. будет жить пока живет ссылка на внутреннюю область
    def wrapper(*args, **kwargs):
        started = time.time()
        result = func(*args, **kwargs)
        worked = time.time() - started
        print('Функция "{}" выполнилась за {:f} микросекунд'.format(func.__name__, worked * 1e6))
        return result
    return wrapper


def counter(func):
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print('Функция {} вызвана {} раз.'.format(func.__name__, count))
        return func(*args, **kwargs)
    return wrapper


@counter
@benchmark  # декоратор - это обертка
def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

# print(factorial(4))
# print(factorial(20))


# Декораторы с параметрами

def sugar(n, sugar_price):
    def decorator(func):
        def wrapper(price, *args, **kwargs):
            print("Добавка: сахар {}".format(n))
            price += n * sugar_price
            return func(price, *args, **kwargs)
        return wrapper
    return decorator

v = 10


@sugar(2, 5)
@sugar(1, v)
def cup_of_tea(price, name='Черный чай'):
    print("Вы заказали: {}".format(name))
    print("Стоимость заказа: {}".format(price))
    return price


cup_of_tea(60)
