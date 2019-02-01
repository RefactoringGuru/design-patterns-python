"""
EN: Command Design Pattern

Intent: Encapsulate a request as an object, thereby letting you parameterize
clients with different requests (e.g. queue or log requests) and support
undoable operations.

RU: Паттерн Команда

Назначение: Инкапсулирует запрос как объект, позволяя тем
самым параметризовать клиентов с различными запросами (например, запросами
очереди или логирования) и поддерживать отмену операций.
"""


from __future__ import annotations
from abc import ABC, abstractmethod


class Command(ABC):
    """
    EN: The Command interface declares a method for executing a command.

    RU: Интерфейс Команды объявляет метод для выполнения команд.
    """

    @abstractmethod
    def execute(self) -> None:
        pass


class SimpleCommand(Command):
    """
    EN: Some commands can implement simple operations on their own.

    RU: Некоторые команды способны выполнять простые операции самостоятельно.
    """

    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> None:
        print(f"SimpleCommand: See, I can do simple things like printing"
              f"({self._payload})")


class ComplexCommand(Command):
    """
    EN: However, some commands can delegate more complex operations to other
    objects, called "receivers."

    RU: Но есть и команды, которые делегируют более сложные операции другим
    объектам, называемым «получателями».
    """

    def __init__(self, receiver: Receiver, a: str, b: str) -> None:
        """
        EN: Complex commands can accept one or several receiver objects along
        with any context data via the constructor.

        RU: Сложные команды могут принимать один или несколько
        объектов-получателей вместе с любыми данными о контексте через
        конструктор.
        """

        self._receiver = receiver
        self._a = a
        self._b = b

    def execute(self) -> None:
        """
        EN: Commands can delegate to any methods of a receiver.

        RU: Команды могут делегировать выполнение любым методам получателя.
        """

        print("ComplexCommand: Complex stuff should be done by a receiver object", end="")
        self._receiver.do_something(self._a)
        self._receiver.do_something_else(self._b)


class Receiver:
    """
    EN: The Receiver classes contain some important business logic. They know how
    to perform all kinds of operations, associated with carrying out a request.
    In fact, any class may serve as a Receiver.

    RU: Классы Получателей содержат некую важную бизнес-логику. Они умеют
    выполнять все виды операций, связанных с выполнением запроса. Фактически,
    любой класс может выступать Получателем.
    """

    def do_something(self, a: str) -> None:
        print(f"\nReceiver: Working on ({a}.)", end="")

    def do_something_else(self, b: str) -> None:
        print(f"\nReceiver: Also working on ({b}.)", end="")


class Invoker:
    """
    EN: The Invoker is associated with one or several commands. It sends a
    request to the command.

    RU: Отправитель связан с одной или несколькими командами. Он отправляет запрос
    команде.
    """

    _on_start = None
    _on_finish = None

    """
    EN: Initialize commands.
    
    RU: Инициализация команд.
    """

    def set_on_start(self, command: Command):
        self._on_start = command

    def set_on_finish(self, command: Command):
        self._on_finish = command

    def do_something_important(self) -> None:
        """
        EN: The Invoker does not depend on concrete command or receiver classes.
        The Invoker passes a request to a receiver indirectly, by executing a
        command.

        RU: Отправитель не зависит от классов конкретных команд и получателей.
        Отправитель передаёт запрос получателю косвенно, выполняя команду.
        """

        print("Invoker: Does anybody want something done before I begin?")
        if isinstance(self._on_start, Command):
            self._on_start.execute()

        print("Invoker: ...doing something really important...")

        print("Invoker: Does anybody want something done after I finish?")
        if isinstance(self._on_finish, Command):
            self._on_finish.execute()


if __name__ == "__main__":
    """
    EN: The client code can parameterize an invoker with any commands.

    RU: Клиентский код может параметризовать отправителя любыми командами.
    """

    invoker = Invoker()
    invoker.set_on_start(SimpleCommand("Say Hi!"))
    receiver = Receiver()
    invoker.set_on_finish(ComplexCommand(
        receiver, "Send email", "Save report"))

    invoker.do_something_important()
