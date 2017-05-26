# functions


def say_hello():
    print("hello python")

say_hello()

# arguments


def say_hello_2(name):
    print("hello, " + name)

say_hello_2("kitty")


def summa(a, b):
    print(a + b)
    return  # выход из функции, ничего не возвращает

summa(2, 4)
print(summa(2, 4))
summa('lala', 'land')


# return


def mega_pow(x, p):
    return x ** p

a = mega_pow(3, 2)
print(a)

print(mega_pow(2, 3))


def connect(host, user, password, dbname):
    if not db_connect(host, user, password):
        print("no connection")
        return False  # завершение выполнения функции

    if not db_set(dbname):
        print("no such database")
        return False


# default args


def extra_pow(x=4, p=2, v=None):
    if v is None:
        v = {}
    v = v or {}
    return x ** p

print('extra pow: ', extra_pow(p=3))
print('extra pow: ', extra_pow(3, 3))


# передача значений аргументов по ссылке


def parse(s, output):
    s = s.strip('.')  # удалить символы с конца и начала строки

    for i in s.split():
        # разбивает строку по указанному символу (по умолчанию пробел)
        output.append(i)

s = 'Python is a programming language.'
lst = []

parse(s, lst)
print(s, lst)


# переменное количество аргументов


def multi(initial=1, *args):
    result = initial

    for i in args:
        result *= i

    return result

lst2 = [1, 2, 3, 4, 5]
print(multi(1, 2, 3, 4, 5))
print(multi(100, 2, *lst2))


def join1(separator=' ', lst=None):
    if lst is None:
        lst = []

    return separator.join(lst)

print(
    join1(lst=['a', 'b', 'c'], separator=':')
)


def make_query_string(separator="&", **kwargs):  # две звездочки - именованные арг-ты, одна - позиционные
    l = []

    for name, value in kwargs.items():
        # l.append(name + '=' + value)
        l.append('{}={}'.format(name, value))

    return separator.join(l)

print(
    make_query_string(uid=1, fio='ivan')
)

d = {
    'uid': 1,
    'fio': 'ivan'
}
print(
    make_query_string(**d)
)


# анонимная функция (lambda)

# def sqrt(x):
#     return x ** 0.5

sqrt = lambda x: x ** 0.5

print(sqrt(9))


# замыкание

def wrapper():
    print('___')

    def do_smth():
        pass

    print('___')


# каррирование - частичное применение
def trim(chars=None):
    return lambda s: s.strip(chars)


# def trim(s, chars=None):
#     return s.strip(chars)


spaces_trim = trim(' ')
slashes_trim = trim('/\\')

print(
    spaces_trim('    username       '),
    slashes_trim('/\post//')
)


# рекурсия!!!

def factorial(x):
    print(x)
    return 1 if x == 0 else x * factorial(x - 1)

print('Factorial: {}'.format(factorial(5)))


def A():
    B()


# ^ косвенная рекурсия v
def B():
    A()


# Область видимости и время жизни переменной

"""
1) глобальная область видимости
        - все, кроме функций и классов
        - globals()
            'var' in globals() - проверка существования глобальной переменной
2) локальная область видимости
        - функции и классы
        - locals()
            'var' in locals() - проверка существования локальной переменной
"""

g = 666


def wrapper2():
    external = 777

    def func():
        global g  # сделать глобальную переменную локальной
        nonlocal external  # использовать неглобальную и нелокальную | ONLY PYTHON 3

        g += 1
        external += 1

        print(g, external)

    func()

wrapper2()
print(g)


lst = []
for i, e in enumerate(lst):
    e[i + 1] < e
