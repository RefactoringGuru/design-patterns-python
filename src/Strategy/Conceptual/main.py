"""
EN: Strategy Design Pattern

Intent: Define a family of algorithms, encapsulate each one, and make them
interchangeable. Strategy lets the algorithm vary independently from clients
that use it.

RU: Паттерн Стратегия

Назначение: Определяет семейство алгоритмов, инкапсулирует каждый из них и
делает взаимозаменяемыми. Стратегия позволяет изменять алгоритм независимо от
клиентов, которые его используют.
"""


from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Context():
    """
    EN: The Context defines the interface of interest to clients.

    RU: Контекст определяет интерфейс, представляющий интерес для клиентов.
    """

    def __init__(self, strategy: Strategy) -> None:
        """
        EN: Usually, the Context accepts a strategy through the constructor, but
        also provides a setter to change it at runtime.

        RU: Обычно Контекст принимает стратегию через конструктор, а также
        предоставляет сеттер для её изменения во время выполнения.
        """

        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        """
        EN: The Context maintains a reference to one of the Strategy objects.
        The Context does not know the concrete class of a strategy. It should
        work with all strategies via the Strategy interface.

        RU: Контекст хранит ссылку на один из объектов Стратегии. Контекст не
        знает конкретного класса стратегии. Он должен работать со всеми
        стратегиями через интерфейс Стратегии.
        """

        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        """
        EN: Usually, the Context allows replacing a Strategy object at runtime.

        RU: Обычно Контекст позволяет заменить объект Стратегии во время
        выполнения.
        """

        self._strategy = strategy

    def do_some_business_logic(self) -> None:
        """
        EN: The Context delegates some work to the Strategy object instead of
        implementing multiple versions of the algorithm on its own.

        RU: Вместо того, чтобы самостоятельно реализовывать множественные версии
        алгоритма, Контекст делегирует некоторую работу объекту Стратегии.
        """

        # ...

        print("Context: Sorting data using the strategy (not sure how it'll do it)")
        result = self._strategy.do_algorithm(["a", "b", "c", "d", "e"])
        print(",".join(result))

        # ...


class Strategy(ABC):
    """
    EN: The Strategy interface declares operations common to all supported
    versions of some algorithm.

    The Context uses this interface to call the algorithm defined by Concrete
    Strategies.

    RU: Интерфейс Стратегии объявляет операции, общие для всех поддерживаемых
    версий некоторого алгоритма.

    Контекст использует этот интерфейс для вызова алгоритма, определённого
    Конкретными Стратегиями.
    """

    @abstractmethod
    def do_algorithm(self, data: List):
        pass


"""
EN: Concrete Strategies implement the algorithm while following the base
Strategy interface. The interface makes them interchangeable in the Context.

RU: Конкретные Стратегии реализуют алгоритм, следуя базовому интерфейсу
Стратегии. Этот интерфейс делает их взаимозаменяемыми в Контексте.
"""


class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data: List) -> List:
        return sorted(data)


class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data: List) -> List:
        return reversed(sorted(data))


if __name__ == "__main__":
    # EN: The client code picks a concrete strategy and passes it to the
    # context. The client should be aware of the differences between strategies
    # in order to make the right choice.
    #
    # RU: Клиентский код выбирает конкретную стратегию и передаёт её в контекст.
    # Клиент должен знать о различиях между стратегиями, чтобы сделать
    # правильный выбор.

    context = Context(ConcreteStrategyA())
    print("Client: Strategy is set to normal sorting.")
    context.do_some_business_logic()
    print()

    print("Client: Strategy is set to reverse sorting.")
    context.strategy = ConcreteStrategyB()
    context.do_some_business_logic()
