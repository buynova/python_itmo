# Метаклассы


class NameMeta(type):  # метакласс, на основе которого будут создаваться другие классы (шаблон)
    def __new__(mcs, *args, **kwargs):
        return super().__new__(mcs, *args, **kwargs)


class Person(metaclass=NameMeta):  # python 3
    # __metaclass__ = NameMeta  #python 2

    def __init__(self, username):
        self.username = username

p1 = Person('вася')
p2 = Person('петя')

# print(type(p1), type(Person))
# print(p1.username, p2.username)


Product = type('Product', (object,), {
    'name': None,
    'price': 0.0
})


def __init__(self, name, price):
    self.name = name
    self.price = price

setattr(Product, '__init__', __init__)

# getattr(obj, name) - вернуть значение атрибута объекта
# setattr(obj, name, value) - установить значение атрибута объекта
# hasattr(obj, name) - проверить существование атрибута у объекта
# delattr(obj, name) - удалить атрибут у объекта

book = Product('Python', 500)
print(book.name, book.price)

# print(Person, Product)
# print(type(Person), type(Product))


# == Специальные свойства и методы объектов и классов ==

class Car(object):
    """
    Документация к классу
    """
    stat_prop = 123

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        """Вызывается функцией repr() для получения строки формального представления объекта."""
        return 'Машина марки {} стоит {}'.format(self.name, self.price)

    def __str__(self):
        """Вызывается в случаях преобразования объекта к типу str"""
        return self.name

    def __float__(self):
        """Вызывается в случаях преобразования объекта к типу float"""
        return self.price

print(Car.__doc__)  # __doc__ - документация объекта
print(Car.__name__)  # __name__ - имя объекта
print(Car.__module__)  # имя модуля, в котором располагается объект
print(Car.__bases__)  # все базовые классы, от которых наследуется класс
print(Car.__dict__)  # словарь атрибутов класса

taz = Car('Lada', 20000.01)
zaz = Car('Jopik', 250000.0)

print(taz.__dict__)
print(zaz.__dict__)

print(repr(taz))

print(taz, float(taz) + float(zaz))
