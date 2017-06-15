import random
from string import ascii_letters, digits


# Фибоначчи

def fibonacci_generator(n):
    # сначала создаем список-последовательность Фибоначчи
    l = list()
    l.append(1)
    l.append(1)
    for i in range(2, n):
        l.append(l[i-1] + l[i-2])

    for item in l:
        yield item

for i in fibonacci_generator(10):
    print(i)


# Случайные пароли

def password_generator(n):
    pw_list = []
    for i in range(n):
        pw_list.append(random.choice(ascii_letters + digits))

    yield ''.join(pw_list)

for i in password_generator(16):
    print(i)
