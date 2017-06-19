from abc import ABCMeta, abstractmethod
from os import path


class ParamHandler(metaclass=ABCMeta):
    types = {}

    def __init__(self, source):
        self.source = source
        self.params = {}

    def add_param(self, key, value):
        self.params[key] = value

    def get_all_params(self):
        return self.params

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass

    @classmethod
    def add_type(cls, name, klass):
        if not name:
            raise ParamHandlerException('Type must have name!')

        if not issubclass(klass, ParamHandler):
            raise ParamHandlerException('Class {} is not ParamHandler!'.format(klass))

        cls.types[name] = klass

    @classmethod
    def get_instance(cls, source, *args, **kwargs):
        _, ext = path.splitext(source.lower())
        ext = ext.lstrip('.')
        klass = cls.types.get(ext)

        if klass is None:
            raise ParamHandlerException('Type {} not found!'.format(ext))

        return klass(source, *args, **kwargs)
