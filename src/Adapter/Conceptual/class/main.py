"""
EN: Adapter Design Pattern

Intent: Provides a unified interface that allows objects with incompatible
interfaces to collaborate.

RU: Паттерн Адаптер

Назначение: Позволяет объектам с несовместимыми интерфейсами работать вместе.
"""


class Target:
    """
    EN: The Target defines the domain-specific interface used by the client
    code.

    RU: Целевой класс объявляет интерфейс, с которым может работать клиентский
    код.
    """

    def request(self) -> str:
        return "Target: The default target's behavior."


class Adaptee:
    """
    EN: The Adaptee contains some useful behavior, but its interface is
    incompatible with the existing client code. The Adaptee needs some
    adaptation before the client code can use it.

    RU: Адаптируемый класс содержит некоторое полезное поведение, но его
    интерфейс несовместим с существующим клиентским кодом. Адаптируемый класс
    нуждается в некоторой доработке, прежде чем клиентский код сможет его
    использовать.
    """

    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Target, Adaptee):
    """
    EN: The Adapter makes the Adaptee's interface compatible with the Target's
    interface via multiple inheritance.

    RU: Адаптер делает интерфейс Адаптируемого класса совместимым с целевым
    интерфейсом благодаря множественному наследованию.
    """

    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.specific_request()[::-1]}"


def client_code(target: "Target") -> None:
    """
    EN: The client code supports all classes that follow the Target interface.

    RU: Клиентский код поддерживает все классы, использующие интерфейс Target.
    """

    print(target.request(), end="")


if __name__ == "__main__":
    print("Client: I can work just fine with the Target objects:")
    target = Target()
    client_code(target)
    print("\n")

    adaptee = Adaptee()
    print("Client: The Adaptee class has a weird interface. "
          "See, I don't understand it:")
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

    print("Client: But I can work with it via the Adapter:")
    adapter = Adapter()
    client_code(adapter)
