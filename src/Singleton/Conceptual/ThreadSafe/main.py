"""
EN: Singleton Design Pattern

Intent: Lets you ensure that a class has only one instance, while providing a
global access point to this instance. One instance per each subclass (if any).

RU: Паттерн Одиночка

Назначение: Гарантирует, что у класса есть только один экземпляр, и
предоставляет к нему глобальную точку доступа. У каждого наследника класса тоже
будет по одному экземпляру.
"""

from threading import Lock, Thread


class SingletonMeta(type):
    """
    EN: This is a thread-safe implementation of Singleton.

    RU: Это потокобезопасная реализация класса Singleton.
    """

    _instances = {}

    _lock: Lock = Lock()
    """
    We now have a lock object that will be used to synchronize
    threads during first access to the Singleton.
    
    RU: У нас теперь есть объект-блокировка для синхронизации потоков во
    время первого доступа к Одиночке.
    """

    def __call__(cls, *args, **kwargs):
        """
        EN: Possible changes to the value of the `__init__` argument do not
        affect the returned instance.

        RU: Данная реализация не учитывает возможное изменение передаваемых
        аргументов в `__init__`.
        """
        # EN: Now, imagine that the program has just been launched.
        # Since there's no Singleton instance yet, multiple threads can
        # simultaneously pass the previous conditional and reach this
        # point almost at the same time. The first of them will acquire
        # lock and will proceed further, while the rest will wait here.
        #
        # RU: Теперь представьте, что программа была только-только
        # запущена. Объекта-одиночки ещё никто не создавал, поэтому
        # несколько потоков вполне могли одновременно пройти через
        # предыдущее условие и достигнуть блокировки. Самый быстрый
        # поток поставит блокировку и двинется внутрь секции, пока
        # другие будут здесь его ожидать.
        with cls._lock:
            # EN: The first thread to acquire the lock, reaches this
            # conditional, goes inside and creates the Singleton
            # instance. Once it leaves the lock block, a thread that
            # might have been waiting for the lock release may then
            # enter this section. But since the Singleton field is
            # already initialized, the thread won't create a new
            # object.
            #
            # RU: Первый поток достигает этого условия и проходит внутрь,
            # создавая объект-одиночку. Как только этот поток покинет
            # секцию и освободит блокировку, следующий поток может
            # снова установить блокировку и зайти внутрь. Однако теперь
            # экземпляр одиночки уже будет создан и поток не сможет
            # пройти через это условие, а значит новый объект не будет
            # создан.
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    value: str = None
    """
    EN: We'll use this property to prove that our Singleton really works.
    
    RU: Мы используем это поле, чтобы доказать, что наш Одиночка
    действительно работает.
    """

    def __init__(self, value: str) -> None:
        self.value = value

    def some_business_logic(self):
        """
        EN: Finally, any singleton should define some business logic, which can
        be executed on its instance.

        RU: Наконец, любой одиночка должен содержать некоторую бизнес-логику,
        которая может быть выполнена на его экземпляре.
        """


def test_singleton(value: str) -> None:
    singleton = Singleton(value)
    print(singleton.value)


if __name__ == "__main__":
    # EN: The client code.
    #
    # RU: Клиентский код.

    print("If you see the same value, then singleton was reused (yay!)\n"
          "If you see different values, "
          "then 2 singletons were created (booo!!)\n\n"
          "RESULT:\n")

    process1 = Thread(target=test_singleton, args=("FOO",))
    process2 = Thread(target=test_singleton, args=("BAR",))
    process1.start()
    process2.start()
