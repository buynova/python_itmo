# Объектно-ориентированное программирование

# Наследование всегда расширяет функционал класса-родителя
# Множественное наследование лучше не использовать (наследование от нескольких родителей)


class Person(object):  # наследуемся от object всегда; object - тип данных
    # статические свойства (общие данные для всех объектов)
    last_id = 1

    # специальный метод
    # self - ссылка на текущий объект
    def __init__(self, firstname, lastname, phone):
        """Конструктор."""
        self.sex = None
        self.firstname = firstname
        self.lastname = lastname
        self.phone = phone

    def get_info(self):
        return '{} {}: {}'.format(
            self.firstname,
            self.lastname,
            self.phone
        )

    # статический метод.
    # использовать только когда не собираемся работать с самим классом (например, helper)
    # @staticmethod
    @classmethod  # тоже статический метод, но передает ссылку на класс
    def get_instance(cls):  # получить экземпляр
        print(cls.last_id)

person1 = Person('Johnny', 'Depp', '+71234567890')
# person1.last_id = 2  # создано другое свойство last_id, привязанное к текущему объекту (в приоритете)
Person.last_id = 2  # изменение статического свойства для всех - через ссылку на класс

person2 = Person('', '', '')
# print(person1.last_id, person2.last_id)

Person.get_instance()


class Developer(Person):  # Person - базовый (родительский) класс
    def __init__(self, firstname, lastname, phone, skills=None):
        super().__init__(firstname, lastname, phone)  # вызов родительского метода __init__
        # self.skills = [] if skills is None else skills
        self.skills = skills or []  # сделать переменную списком, если она пуста


# при создании объекта вызывается инит
# person2 = Developer('Ryan', 'Gosling', '+71234567890')
# print(person2.get_info())

# запись данных, переопределение свойств
person1.firstname = 'Johnny'
person1.lastname = 'Depp'

# чтение данных (свойств)
# print(person1.firstname, person1.lastname)


class Product(object):

    instances = {}

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def get_instance(cls, name, price):
        key = (name, price)

        if key in cls.instances:
            # print('instance already exists')
            return cls.instances.get(key)

        obj = cls(name, price)
        cls.instances[key] = obj
        # print('instance added')
        return obj


class OrderException(BaseException):
    pass


class Order(object):

    def __init__(self, person, products=None):
        self.person = person
        self.products = []

        if products is not None:
            for p in products:
                self.add_product(p)

    def add_product(self, product):
        if not isinstance(product, Product):  # проверка, является ли объект наследником указанного класса
            raise OrderException('Это не продукт магазина!')

        self.products.append(product)


person3 = Person('Brad', 'Pitt', '+78121234567')

book1 = Product.get_instance('Harry Potter', 999)
book2 = Product.get_instance('Harry Potter', 999)
book3 = Product.get_instance('The Lord of the Rings', 1200)

order = Order(person3, [book1, book3])
order.add_product(book2)
# order.add_product(666)

print(book1, book2)
