"""
EN: Singleton Design Pattern

Intent: Ensure that a class has a single instance, and provide a global point
of access to it.

RU: Паттерн Одиночка

Назначение: Гарантирует существование единственного экземпляра класса и
предоставляет глобальную точку доступа к нему.
"""


from __future__ import annotations
from typing import Optional


class Singleton:
    """
    EN: The Singleton class defines the `getInstance` method that lets clients
    access the unique singleton instance.

    RU: Класс Одиночка предоставляет метод getInstance, который позволяет
    клиентам получить доступ к уникальному экземпляру одиночки.
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
