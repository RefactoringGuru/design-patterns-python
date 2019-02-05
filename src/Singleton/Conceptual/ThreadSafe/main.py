"""
EN: Singleton Design Pattern

Intent: Ensure that a class has a single instance, and provide a global point
of access to it.

RU: Паттерн Одиночка

Назначение: Гарантирует существование единственного экземпляра класса и
предоставляет глобальную точку доступа к нему.
"""


from __future__ import annotations
from threading import Lock, Thread
from typing import Optional


class Singleton:
    """
    EN: The Singleton class defines the `getInstance` method that lets clients
    access the unique singleton instance.

    RU: Класс Одиночка предоставляет метод getInstance, который позволяет
    клиентам получить доступ к уникальному экземпляру одиночки.
    """

    _instance: Optional[Singleton] = None

    _lock: Lock = Lock()

    value: str

    def __init__(self, value: str) -> None:
        self.value = value

    @staticmethod
    def get_instance(value: str) -> Singleton:
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
            with Singleton._lock:
                if not Singleton._instance:
                    Singleton._instance = Singleton(value)
        return Singleton._instance

    def some_business_logic(self):
        """
        EN: Finally, any singleton should define some business logic, which can
        be executed on its instance.

        RU: Наконец, любой одиночка должен содержать некоторую бизнес-логику,
        которая может быть выполнена на его экземпляре.
        """

        # ...


def test_singleton(value: str) -> None:
    singleton = Singleton.get_instance(value)
    print(singleton.value)


if __name__ == "__main__":
    """
    EN: The client code.

    RU: Клиентский код.
    """

    print("If you see the same value, then singleton was reused (yay!)\n"
          "If you see different values, then 2 singletons were created (booo!!)\n\n"
          "RESULT:\n")

    process1 = Thread(target=test_singleton, args=("FOO",))
    process2 = Thread(target=test_singleton, args=("BAR",))
    process1.start()
    process2.start()
