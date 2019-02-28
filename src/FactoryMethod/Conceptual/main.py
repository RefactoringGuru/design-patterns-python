"""
EN: Factory Method Design Pattern

Intent: Define an interface for creating an object, but let subclasses decide
which class to instantiate. Factory Method lets a class defer instantiation to
subclasses.

RU: Паттерн Фабричный Метод

Назначение: Определяет интерфейс для создания объекта, но позволяет подклассам
решать, какого класса создавать экземпляр. Фабричный Метод позволяет классу
делегировать создание экземпляра подклассам.
"""


from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):
    """
    EN: The Creator class declares the factory method that is supposed to return
    an object of a Product class. The Creator's subclasses usually provide the
    implementation of this method.

    RU: Класс Создатель объявляет фабричный метод, который должен возвращать
    объект класса Продукт. Подклассы Создателя обычно предоставляют реализацию
    этого метода.
    """

    @abstractmethod
    def factory_method(self):
        """
        EN: Note that the Creator may also provide some default implementation
        of the factory method.

        RU: Обратите внимание, что Создатель может также обеспечить реализацию
        фабричного метода по умолчанию.
        """
        pass

    def some_operation(self) -> str:
        """
        EN: Also note that, despite its name, the Creator's primary
        responsibility is not creating products. Usually, it contains some core
        business logic that relies on Product objects, returned by the factory
        method. Subclasses can indirectly change that business logic by
        overriding the factory method and returning a different type of product
        from it.

        RU: Также заметьте, что, несмотря на название, основная обязанность
        Создателя не заключается в создании продуктов. Обычно он содержит
        некоторую базовую бизнес-логику, которая основана на объектах Продуктов,
        возвращаемых фабричным методом. Подклассы могут косвенно изменять эту
        бизнес-логику, переопределяя фабричный метод и возвращая из него другой
        тип продукта.
        """

        # EN: Call the factory method to create a Product object.
        #
        # RU: Вызываем фабричный метод, чтобы получить объект-продукт.
        product = self.factory_method()

        # EN: Now, use the product.
        #
        # RU: Далее, работаем с этим продуктом.
        result = f"Creator: The same creator's code has just worked with {product.operation()}"

        return result


"""
EN: Concrete Creators override the factory method in order to change the
resulting product's type.

RU: Конкретные Создатели переопределяют фабричный метод для того, чтобы изменить
тип результирующего продукта.
"""


class ConcreteCreator1(Creator):
    """
    EN: Note that the signature of the method still uses the abstract product
    type, even though the concrete product is actually returned from the method.
    This way the Creator can stay independent of concrete product classes.

    RU: Обратите внимание, что сигнатура метода по-прежнему использует тип
    абстрактного продукта, хотя фактически из метода возвращается конкретный
    продукт. Таким образом, Создатель может оставаться независимым от конкретных
    классов продуктов.
    """

    def factory_method(self) -> ConcreteProduct1:
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    def factory_method(self) -> ConcreteProduct2:
        return ConcreteProduct2()


class Product(ABC):
    """
    EN: The Product interface declares the operations that all concrete products
    must implement.

    RU: Интерфейс Продукта объявляет операции, которые должны выполнять все
    конкретные продукты.
    """

    @abstractmethod
    def operation(self) -> str:
        pass


"""
EN: Concrete Products provide various implementations of the Product interface.

RU: Конкретные Продукты предоставляют различные реализации интерфейса Продукта.
"""


class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"


class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"


def client_code(creator: Creator) -> None:
    """
    EN: The client code works with an instance of a concrete creator, albeit
    through its base interface. As long as the client keeps working with the
    creator via the base interface, you can pass it any creator's subclass.

    RU: Клиентский код работает с экземпляром конкретного создателя, хотя и
    через его базовый интерфейс. Пока клиент продолжает работать с создателем
    через базовый интерфейс, вы можете передать ему любой подкласс создателя.
    """

    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Launched with the ConcreteCreator2.")
    client_code(ConcreteCreator2())
