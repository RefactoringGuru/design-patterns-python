"""
EN: Mediator Design Pattern

Intent: Lets you reduce chaotic dependencies between objects. The pattern
restricts direct communications between the objects and forces them to
collaborate only via a mediator object.

RU: Паттерн Посредник

Назначение: Позволяет уменьшить связанность множества классов между собой,
благодаря перемещению этих связей в один класс-посредник.
"""


from __future__ import annotations
from abc import ABC


class Mediator(ABC):
    """
    EN: The Mediator interface declares a method used by components to notify
    the mediator about various events. The Mediator may react to these events
    and pass the execution to other components.

    RU: Интерфейс Посредника предоставляет метод, используемый компонентами для
    уведомления посредника о различных событиях. Посредник может реагировать на
    эти события и передавать исполнение другим компонентам.
    """

    def notify(self, sender: object, event: str) -> None:
        pass


class ConcreteMediator(Mediator):
    def __init__(self, component1: Component1, component2: Component2) -> None:
        self._component1 = component1
        self._component1.mediator = self
        self._component2 = component2
        self._component2.mediator = self

    def notify(self, sender: object, event: str) -> None:
        if event == "A":
            print("Mediator reacts on A and triggers following operations:")
            self._component2.do_c()
        elif event == "D":
            print("Mediator reacts on D and triggers following operations:")
            self._component1.do_b()
            self._component2.do_c()


class BaseComponent:
    """
    EN: The Base Component provides the basic functionality of storing a
    mediator's instance inside component objects.

    RU: Базовый Компонент обеспечивает базовую функциональность хранения
    экземпляра посредника внутри объектов компонентов.
    """

    def __init__(self, mediator: Mediator = None) -> None:
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator


"""
EN: Concrete Components implement various functionality. They don't depend on
other components. They also don't depend on any concrete mediator classes.

RU: Конкретные Компоненты реализуют различную функциональность. Они не зависят
от других компонентов. Они также не зависят от каких-либо конкретных классов
посредников.
"""


class Component1(BaseComponent):
    def do_a(self) -> None:
        print("Component 1 does A.")
        self.mediator.notify(self, "A")

    def do_b(self) -> None:
        print("Component 1 does B.")
        self.mediator.notify(self, "B")


class Component2(BaseComponent):
    def do_c(self) -> None:
        print("Component 2 does C.")
        self.mediator.notify(self, "C")

    def do_d(self) -> None:
        print("Component 2 does D.")
        self.mediator.notify(self, "D")


if __name__ == "__main__":
    # EN: The client code.
    #
    # RU: Клиентский код.
    c1 = Component1()
    c2 = Component2()
    mediator = ConcreteMediator(c1, c2)

    print("Client triggers operation A.")
    c1.do_a()

    print("\n", end="")

    print("Client triggers operation D.")
    c2.do_d()
