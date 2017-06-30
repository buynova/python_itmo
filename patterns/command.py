# Command (команда)
from abc import ABCMeta, abstractmethod


def command(name):
    def decorator(cls):
        cls.add_command(name, cls)
        return cls
    return decorator


class Command(metaclass=ABCMeta):
    __commands = {}

    @classmethod
    def add_command(cls, name, command):
        if not name:
            raise ValueError

        if not issubclass(command, cls):
            raise TypeError

        cls.__commands[name] = cls

    @classmethod
    def get_instance(cls, name):
        """Factory method - фабричный метод"""
        klass = cls.__commands.get(name)

        if klass is None:
            raise NameError

        return klass()

    @abstractmethod
    def _do_execute(self):
        pass

    def execute(self):
        """Template method - шаблонный метод"""
        print("Действие в начале")
        self._do_execute()
        print("Действие в конце")


@command('hello')
class HelloCommand(Command):
    def _do_execute(self):
        print('Hello')


@command('show')
class ShowCommand(Command):
    def _do_execute(self):
        print('Show task list')

# Command.add_command('show', ShowCommand)

cmd = Command.get_instance('show')
cmd.execute()

cmd = Command.get_instance('hello')
cmd.execute()
