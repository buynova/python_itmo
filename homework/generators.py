import random
from string import ascii_letters, digits


# Фибоначчи

def fibonacci_generator(n):
    a = b = 1
    i = 0
    while i < n:
        if i in [0, 1]:
            c = a
        else:
            c = a + b
            a = b
            b = c
        i += 1
        yield c

for i in fibonacci_generator(10):
    print(i)


# Случайные пароли

def password_generator(n):
    while True:
        yield ''.join([random.choice(ascii_letters + digits) for i in range(n)])

gen = password_generator(16)
print(next(gen))
print(next(gen))
print(next(gen))
