# Singleton (одиночка) - переиспользование одного и того же объекта вместо создания новых
# На базе данного шаблона строится шаблон Registry (реестр)


class Singleton(object):
    """Первое решение"""
    __instance = None  # __private

    def __new__(cls, *args, **kwargs):  # настоящий конструктор - выделяет память, создает объект.
                                        # использовать только если нужно вмешаться в процесс создания объекта
        if cls.__instance is None:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance

# print(Singleton.__dict__)
# print(Singleton._Singleton__instance)
#
# obj1 = Singleton()
# obj2 = Singleton()
# print(obj1 == obj2)  # видно, что это один и тот же объект


class SingletonMeta(type):
    """Второе решение"""
    __instances = {}  # для множества классов (БД, например)

    def __call__(cls, *args, **kwargs):  # позволяет использовать объект как функцию. не статический метод
        if cls not in cls.__instances:
            cls.__instances[cls] = super().__call__(*args, **kwargs)
        return cls.__instances[cls]


class DB(metaclass=SingletonMeta):
    pass

db1 = DB()
db2 = DB()
print(db1, db2)


def singleton(cls):
    """Решение третье - декоратор"""
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class Config(object):
    pass

conf1 = Config()
conf2 = Config()
print(conf1 == conf2)
