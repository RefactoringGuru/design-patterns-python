"""
EN: Singleton Design Pattern

Intent: Lets you ensure that a class has only one instance, while providing a
global access point to this instance.

RU: Паттерн Одиночка

Назначение: Гарантирует, что у класса есть только один экземпляр, и
предоставляет к нему глобальную точку доступа.
"""


from __future__ import annotations
from typing import Optional


class Singleton:
    """
    EN: The Singleton class defines the `get_instance` method that serves as
    an alternative to constructor and lets clients access the same instance
    of this class over and over.

    RU: Класс Одиночка предоставляет метод `get_instance`, который ведёт себя
    как альтернативный конструктор и позволяет клиентам получать один и тот
    же экземпляр класса при каждом вызове.
    """

    _instance: Optional[Singleton] = None

    def __init__(self) -> None:
        if Singleton._instance is not None:
            raise ReferenceError("Cannot instantiate a singleton class.")
        else:
            Singleton._instance = self

    @staticmethod
    def get_instance() -> Singleton:
        """
        EN: The static method that controls the access to the singleton
        instance.

        This implementation let you subclass the Singleton class while keeping
        just one instance of each subclass around.

        RU: Статический метод, управляющий доступом к экземпляру одиночки.

        Эта реализация позволяет вам расширять класс Одиночки, сохраняя повсюду
        только один экземпляр каждого подкласса.
        """

        if not Singleton._instance:
            Singleton()
        return Singleton._instance

    def some_business_logic(self):
        """
        EN: Finally, any singleton should define some business logic, which can
        be executed on its instance.

        RU: Наконец, любой одиночка должен содержать некоторую бизнес-логику,
        которая может быть выполнена на его экземпляре.
        """

        # ...


if __name__ == "__main__":
    # EN: The client code.
    #
    # RU: Клиентский код.

    s1 = Singleton.get_instance()
    s2 = Singleton.get_instance()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")
