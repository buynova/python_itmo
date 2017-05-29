# Ввод и вывод. Форматы данных

"""
Стандартные потоки:
    - stdin - стандартный поток ввода
        input()
        sys.stdin
    - stdout - стандартные потом вывода
        print()
        sys.stdout
    - stderr - стандартный поток ошибок
        все ошибки, которые кидает интерпретатор
        sys.stderr


Файлы
open(<путь к файлу> [, <режим>])

Режимы:
    w - запись в файл
        - если не существует - создается
        - если существует - перезаписывается
    a - добавление в файл
        - если не существует - создается
        - если существует - запись добавляется в конец
    x -
        - если не существует - создается
        - если существует - выбрасывается исключение
    r - чтение файла
    w+ - запись + чтение
    a+
    x+
"""

f = open('out.txt', 'w')  # I/O object (input/output)
f.write('привет\n')
f.write('hello\n')
f.write('world\n')

f.writelines(['D', 'C'])
f.close()

f = open('out.txt')
# f.read()
# print(f.read())

# переместиться в начало файла (задать позицию "курсора")
# смещение относительно начала файла в байтах
f.seek(5)
# как получить текущую позицию курсора
print(f.tell())

# прочитать файл построчно
# print(f.readline())
for line in f:
    print(line)

f.seek(0)

# print(f.readlines())

# как прочитать указанное количество байтов
print(f.read(4))
f.close()


# Менеджеры контекста или контекстные менеджеры

with open('out.txt') as f:
    print(f.readlines())


""" Форматы данных """

# Pickle

import pickle

data = {
    'users': [
        {
            'id': 1,
            'name': 'Linus Torvalds',
            'skills': ('C++', 'Linux')
        },
        {
            'id': 2,
            'name': 'Richard Stallman',
            'skills': ('C++', 'C', 'GNU')
        }
    ]
}

with open('users.pickle', 'wb') as f:
    pickle.dump(data, f)

with open('users.pickle', 'rb') as f:
    print(pickle.load(f))


# JSON - JavaScript Object Notation

import json

with open('users.json', 'w') as f:
    json.dump(data, f)

with open('users.json', 'r') as f:
    print(json.load(f))


# CSV

import csv

'''
id;name;skills
1;Linus Torvalds;C
1;Linus Torvalds;C
1;Linus Torvalds;C
'''

with open('users.csv', 'w') as f:
    users = data.get('users', {})
    fieldnames = users[0].keys()
    writer = csv.DictWriter(f, fieldnames)
    writer.writeheader()
    for user in users:
        writer.writerow(user)

with open('users.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)

# ini - config files
'''
db.host = localhost
db.user = root

[db]
host = localhost
user = root

'''


# XML
'''
<users>
    <user>
        <id>1</id>
        <name>Linus Torvalds</name>
    </user>
</users>
'''


# SQLite3 - DB SQL
