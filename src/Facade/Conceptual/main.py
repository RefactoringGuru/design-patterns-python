"""
EN: Facade Design Pattern

Intent: Provide a unified interface to a number of classes/interfaces of a
complex subsystem. The Facade pattern defines a higher-level interface that
makes the subsystem easier to use.

RU: Паттерн Фасад

Назначение: Предоставляет единый интерфейс к ряду классов/интерфейсов сложной
подсистемы. Паттерн Фасад определяет интерфейс более высокого уровня, который
упрощает использование подсистемы.
"""


from __future__ import annotations


class Facade:
    """
    EN: The Facade class provides a simple interface to the complex logic of one
    or several subsystems. The Facade delegates the client requests to the
    appropriate objects within the subsystem. The Facade is also responsible for
    managing their lifecycle. All of this shields the client from the undesired
    complexity of the subsystem.

    RU: Класс Фасада предоставляет простой интерфейс для сложной логики одной
    или нескольких подсистем. Фасад делегирует запросы клиентов соответствующим
    объектам внутри подсистемы. Фасад также отвечает за управление их жизненным
    циклом. Все это защищает клиента от нежелательной сложности подсистемы.
    """

    def __init__(self, subsystem1: Subsystem1, subsystem2: Subsystem2) -> None:
        """
        EN: Depending on your application's needs, you can provide the Facade
        with existing subsystem objects or force the Facade to create them on
        its own.

        RU: В зависимости от потребностей вашего приложения вы можете
        предоставить Фасаду существующие объекты подсистемы или заставить Фасад
        создать их самостоятельно.
        """

        self._subsystem1 = subsystem1 or Subsystem1()
        self._subsystem2 = subsystem2 or Subsystem2()

    def operation(self) -> str:
        """
        EN: The Facade's methods are convenient shortcuts to the sophisticated
        functionality of the subsystems. However, clients get only to a fraction
        of a subsystem's capabilities.

        RU: Методы Фасада удобны для быстрого доступа к сложной функциональности
        подсистем. Однако клиенты получают только часть возможностей подсистемы.
        """

        results = []
        results.append("Facade initializes subsystems:")
        results.append(self._subsystem1.operation1())
        results.append(self._subsystem2.operation1())
        results.append("Facade orders subsystems to perform the action:")
        results.append(self._subsystem1.operation_n())
        results.append(self._subsystem2.operation_z())
        return "\n".join(results)


class Subsystem1:
    """
    EN: The Subsystem can accept requests either from the facade or client
    directly. In any case, to the Subsystem, the Facade is yet another client,
    and it's not a part of the Subsystem.

    RU: Подсистема может принимать запросы либо от фасада, либо от клиента
    напрямую. В любом случае, для Подсистемы Фасад – это ещё один клиент, и он
    не является частью Подсистемы.
    """

    def operation1(self) -> str:
        return "Subsystem1: Ready!"

    # ...

    def operation_n(self) -> str:
        return "Subsystem1: Go!"


class Subsystem2:
    """
    EN: Some facades can work with multiple subsystems at the same time.

    RU: Некоторые фасады могут работать с разными подсистемами одновременно.
    """

    def operation1(self) -> str:
        return "Subsystem2: Get ready!"

    # ...

    def operation_z(self) -> str:
        return "Subsystem2: Fire!"


def client_code(facade: Facade) -> None:
    """
    EN: The client code works with complex subsystems through a simple interface
    provided by the Facade. When a facade manages the lifecycle of the
    subsystem, the client might not even know about the existence of the
    subsystem. This approach lets you keep the complexity under control.

    RU: Клиентский код работает со сложными подсистемами через простой
    интерфейс, предоставляемый Фасадом. Когда фасад управляет жизненным циклом
    подсистемы, клиент может даже не знать о существовании подсистемы. Такой
    подход позволяет держать сложность под контролем.
    """

    print(facade.operation(), end="")


if __name__ == "__main__":
    # EN: The client code may have some of the subsystem's objects already created.
    # In this case, it might be worthwhile to initialize the Facade with these
    # objects instead of letting the Facade create new instances.
    # 
    # RU: В клиентском коде могут быть уже созданы некоторые объекты подсистемы. В
    # этом случае может оказаться целесообразным инициализировать Фасад с этими
    # объектами вместо того, чтобы позволить Фасаду создавать новые экземпляры.
    subsystem1 = Subsystem1()
    subsystem2 = Subsystem2()
    facade = Facade(subsystem1, subsystem2)
    client_code(facade)
