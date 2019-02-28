"""
EN: Chain of Responsibility Design Pattern

Intent: Lets you pass requests along a chain of handlers. Upon receiving a
request, each handler decides either to process the request or to pass it to the
next handler in the chain.

RU: Паттерн Цепочка обязанностей

Назначение: Позволяет передавать запросы последовательно по цепочке
обработчиков. Каждый последующий обработчик решает, может ли он обработать
запрос сам и стоит ли передавать запрос дальше по цепи.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):
    """
    EN: The Handler interface declares a method for building the chain of
    handlers. It also declares a method for executing a request.

    RU: Интерфейс Обработчика объявляет метод построения цепочки обработчиков.
    Он также объявляет метод для выполнения запроса.
    """

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    """
    EN: The default chaining behavior can be implemented inside a base handler
    class.

    RU: Поведение цепочки по умолчанию может быть реализовано внутри базового
    класса обработчика.
    """

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        # EN: Returning a handler from here will let us link handlers in a
        # convenient way like this:
        # monkey.set_next(squirrel).set_next(dog)
        #
        # RU: Возврат обработчика отсюда позволит связать обработчики простым
        # способом, вот так:
        # monkey.set_next(squirrel).set_next(dog)
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None


"""
EN: All Concrete Handlers either handle a request or pass it to the next handler
in the chain.

RU: Все Конкретные Обработчики либо обрабатывают запрос, либо передают его
следующему обработчику в цепочке.
"""


class MonkeyHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Banana":
            return f"Monkey: I'll eat the {request}"
        else:
            return super().handle(request)


class SquirrelHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Nut":
            return f"Squirrel: I'll eat the {request}"
        else:
            return super().handle(request)


class DogHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "MeatBall":
            return f"Dog: I'll eat the {request}"
        else:
            return super().handle(request)


def client_code(handler: Handler) -> None:
    """
    EN: The client code is usually suited to work with a single handler. In most
    cases, it is not even aware that the handler is part of a chain.

    RU: Обычно клиентский код приспособлен для работы с единственным
    обработчиком. В большинстве случаев клиенту даже неизвестно, что этот
    обработчик является частью цепочки.
    """

    for food in ["Nut", "Banana", "Cup of coffee"]:
        print(f"\nClient: Who wants a {food}?")
        result = handler.handle(food)
        if result:
            print(f"  {result}", end="")
        else:
            print(f"  {food} was left untouched.", end="")


if __name__ == "__main__":
    monkey = MonkeyHandler()
    squirrel = SquirrelHandler()
    dog = DogHandler()

    monkey.set_next(squirrel).set_next(dog)

    # EN: The client should be able to send a request to any handler, not just
    # the first one in the chain.
    #
    # RU: Клиент должен иметь возможность отправлять запрос любому обработчику,
    # а не только первому в цепочке.
    print("Chain: Monkey > Squirrel > Dog")
    client_code(monkey)
    print("\n")

    print("Subchain: Squirrel > Dog")
    client_code(squirrel)
