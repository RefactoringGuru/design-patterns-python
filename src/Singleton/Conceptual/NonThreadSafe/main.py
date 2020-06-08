"""
EN: Singleton Design Pattern

Intent: Lets you ensure that a class has only one instance, while providing a
global access point to this instance. One instance per each subclass (if any).

RU: Паттерн Одиночка

Назначение: Гарантирует, что у класса есть только один экземпляр, и
предоставляет к нему глобальную точку доступа. У каждого наследника класса тоже
будет по одному экземпляру.
"""


class SingletonMeta(type):
    """
    EN: The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.

    RU: В Python класс Одиночка можно реализовать по-разному. Возможные
    способы включают себя базовый класс, декоратор, метакласс. Мы воспользуемся
    метаклассом, поскольку он лучше всего подходит для этой цели.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        EN: Possible changes to the value of the `__init__` argument do not
        affect the returned instance.

        RU: Данная реализация не учитывает возможное изменение передаваемых
        аргументов в `__init__`.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
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

    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")
