"""
Структуры данных

Стек - Stack
данные записываются в начало (в 1й элемент)
удаляются тоже с начала (сначала 1й элемент)
при этом верхний элемент (топ) - элемент n
"""

stack = [15, 6, 2, 9]        # stack
stack.append(999)            # push
elem = stack.pop()           # pop
top = stack[len(stack) - 1]  # peek
print(elem, top, stack)


class StackItem(object):
    def __init__(self, x, prev=None):
        self.x = x
        self.prev = prev


class Stack(object):
    def __init__(self):
        self.__top = None

    def push(self, x):
        if self.__top is None:
            self.__top = StackItem(x)
        else:
            item = StackItem(x, self.__top)
            self.__top = item

    def pop(self):
        if self.__top is None:
            raise RuntimeError
        item = self.__top
        self.__top = item.prev
        return item.x

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.pop())
print(s.pop())
print(s.pop())

"""
Очередь - Queue
данные записываются в конец
удаляются с начала
collections.deque


Списки, связные списки
"""


class Ingredient(object):
    def __init__(self, name, amount=1):
        self.__name = name
        self.__amount = amount

    def get_name(self):
        return self.__name

    @property  # доступ к закрытому свойству, становится доступным только для чтения
    def name(self):
        return self.__name

    @property
    def amount(self):
        return self.__amount

    @amount.setter  # установщик значения в закрытое свойство
    def amount(self, x):
        if not isinstance(x, int):
            raise TypeError
        self.__amount = x

cherry = Ingredient('Вишня')
print(cherry.get_name(), cherry.name)

# cherry.name = 'Груша'
cherry.amount = 5
print(cherry.amount)
