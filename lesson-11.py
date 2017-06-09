# Iterators

from urllib.request import urlopen

s = 'Linus Torvalds'
lst = [1, 2, 3, 4, 5]
person = {
    'name': 'Linus Torvalds',
    'age': 47,
    'is_developer': True
}

iterator = iter(lst)
# print(next(iterator))
# print(next(iterator))
while 1:
    try:
        i = next(iterator)
        # print(i)
    except StopIteration:
        break

# for i in s:
#     print(i)
#
# for i in lst:
#     print(i)
#
# for i in person:
#     print(i)


# Generators

def generator():  # уже является итератором
    print('step 1')
    yield 1
    print('step 2')
    yield 2
    print('step 3')

gen = generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))
for i in gen:
    print(i)
    print(i)

# если генератор перебран, он уже ничего не будет возвращать
# нужно его переопределить
for i in generator():
    print(i)

# range is generator
for i in range(5):
    print(i)


def countdown(n):
    print('Generator started')
    while n:
        yield n
        n -= 1
    print('Generator stopped')

for i in countdown(5):
    print(i)


# вместо генератора (показывает результат только после обработки всего списка,
# тогда как генератор выбрасывает результат после каждой итерации)
def get_pages(url_list):
    pages = []
    for url in url_list:
        pages.append(urlopen(url).read())
    return pages

pages = get_pages([
    'http://ya.ru',
    'http://vk.cc',
    'http://lenta.ru'
])

# for code in pages:
#     print(code)


def page_generator(url_list):
    for url in url_list:
        yield urlopen(url).read()

gen = page_generator([
    'http://ya.ru',
    'http://vk.cc',
    'http://lenta.ru'
])

# for code in gen:
#     print(code)


# Генератор это функция, которая воспроизводит последовательность значений и может использоваться при итерациях.

# Генераторы списков, словарей, множеств.

'''
[expression for item1 in iterable1 if condition1
            for item2 in iterable2 if condition2
            ...
            for itemN in iterableN if conditionN
]
'''

# points = []
#
# for x in range(10):
#     for y in range(5):
#         points.append((x, y))

points = [(x, y) for x in range(3) for y in range(2)]
print(type(points), points)

# lists
lst = [1, 1, 2, 2, 3, 4]
squares = [i ** 2 for i in lst]
print(squares)
odd = [i for i in lst if not i % 2]
print(odd)

# s = set(lst) - mnozhestvo
s = {i for i in lst}
print(s)

keys = ['id', 'name']
values = [1, 'margarita']

# создание словаря
# d = zip(keys, values)
# print(list(d))
d = {k: v
     for i, k in enumerate(keys)
     for j, v in enumerate(values)
     if i == j
     }
print(d)


data = [
    {
        'id': 1,
        'name': 'Linus Torvalds',
        'skills': ('C++', 'Linux')
    },
    {
        'id': 2,
        'name': 'Richard Stallman',
        'skills': ('C++', 'C', 'GNU')
    },
    {
        'id': 1,
        'name': 'Linus Torvalds',
        'skills': ('C++', 'Linux')
    }
]

data = {d['id']: d for d in data}
print(data)


# Генераторные выражения

lst = [1, 1, 2, 2, 3, 4]
gen_squares = (i ** 2 for i in lst)
print(gen_squares)

with open('lesson-11.py', encoding='utf-8') as f:
    lines = (line.strip() for line in f)
    comments = (s for s in lines if s.startswith('#'))
    print(comments, list(comments))


# Сопрограммы

def coroutine(func):  # async.io
    def wrapper(*args, **kwargs):
        g = func(*args, **kwargs)
        next(g)
        return g
    return wrapper


@coroutine
def echo():
    print('Generator is ready for messages')
    while 1:
        msg = (yield)
        print(msg)

ge = echo()
ge.send('hello')
ge.send('world')
ge.close()
