# Observer (наблюдатель)
# еще есть Mediator (посредник)

from abc import ABCMeta, abstractmethod
from random import randrange


class Subject(metaclass=ABCMeta):
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        if not isinstance(observer, Observer):
            raise TypeError
        self._observers.append(observer)

    def remove_observer(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.handle_event(self)


class Observer(metaclass=ABCMeta):
    @abstractmethod
    def handle_event(self, subject):
        pass


class LoginHandler(Subject):
    def __init__(self):
        super().__init__()
        self.result = None

    def authorize(self):
        self.result = randrange(3)
        self.notify_observers()


class LoggerObserver(Observer):
    def handle_event(self, subject):
        if subject.result == 0:
            print('Пишем в access.log - Вход успешный')


class ErrorObserver(Observer):
    def handle_event(self, subject):
        if subject.result == 1:
            print('Пишем в error.log - Неверный логин/пароль')


class CookieObserver(Observer):
    def handle_event(self, subject):
        if subject.result == 2:
            print('Посылка cookie-файлов')


login_handler = LoginHandler()
login_handler.add_observer(LoggerObserver())
login_handler.add_observer(ErrorObserver())
login_handler.add_observer(CookieObserver())

login_handler.authorize()
