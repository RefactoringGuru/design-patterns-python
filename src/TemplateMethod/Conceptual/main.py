"""
EN: Template Method Design Pattern

Intent: Define the skeleton of an algorithm, deferring implementation of some
steps to subclasses. Template Method lets subclasses redefine specific steps
of an algorithm without changing the algorithm's structure.

RU: Паттерн Шаблонный метод

Назначение: Определяет общую схему алгоритма, перекладывая реализацию
некоторых шагов на подклассы. Шаблонный метод позволяет подклассам
переопределять отдельные шаги алгоритма без изменения структуры алгоритма.
"""


from abc import ABC, abstractmethod


class AbstractClass(ABC):
    """
    EN: The Abstract Class defines a template method that contains a skeleton of
    some algorithm, composed of calls to (usually) abstract primitive operations.

    Concrete subclasses should implement these operations, but leave the template
    method itself intact.

    RU: Абстрактный Класс определяет шаблонный метод, содержащий скелет
    некоторого алгоритма, состоящего из вызовов (обычно) абстрактных примитивных
    операций.

    Конкретные подклассы должны реализовать эти операции, но оставить сам
    шаблонный метод без изменений.
    """

    def template_method(self) -> None:
        """
        EN: The template method defines the skeleton of an algorithm.

        RU: Шаблонный метод определяет скелет алгоритма.
        """

        self.base_operation1()
        self.required_operations1()
        self.base_operation2()
        self.hook1()
        self.required_operations2()
        self.base_operation3()
        self.hook2()

    # EN: These operations already have implementations.
    #
    # RU: Эти операции уже имеют реализации.

    def base_operation1(self) -> None:
        print("AbstractClass says: I am doing the bulk of the work")

    def base_operation2(self) -> None:
        print("AbstractClass says: But I let subclasses override some operations")

    def base_operation3(self) -> None:
        print("AbstractClass says: But I am doing the bulk of the work anyway")

    # EN: These operations have to be implemented in subclasses.
    #
    # RU: А эти операции должны быть реализованы в подклассах.

    @abstractmethod
    def required_operations1(self) -> None:
        pass

    @abstractmethod
    def required_operations2(self) -> None:
        pass

    # EN: These are "hooks." Subclasses may override them, but it's not
    # mandatory since the hooks already have default (but empty)
    # implementation. Hooks provide additional extension points in some crucial
    # places of the algorithm.
    #
    # RU: Это «хуки». Подклассы могут переопределять их, но это не обязательно,
    # поскольку у хуков уже есть стандартная (но пустая) реализация. Хуки
    # предоставляют дополнительные точки расширения в некоторых критических
    # местах алгоритма.

    def hook1(self) -> None:
        pass

    def hook2(self) -> None:
        pass


class ConcreteClass1(AbstractClass):
    """
    EN: Concrete classes have to implement all abstract operations of the base
    class. They can also override some operations with a default implementation.

    RU: Конкретные классы должны реализовать все абстрактные операции базового
    класса. Они также могут переопределить некоторые операции с реализацией по
    умолчанию.
    """

    def required_operations1(self) -> None:
        print("ConcreteClass1 says: Implemented Operation1")

    def required_operations2(self) -> None:
        print("ConcreteClass1 says: Implemented Operation2")


class ConcreteClass2(AbstractClass):
    """
    EN: Usually, concrete classes override only a fraction of base class'
    operations.

    RU: Обычно конкретные классы переопределяют только часть операций базового
    класса.
    """

    def required_operations1(self) -> None:
        print("ConcreteClass2 says: Implemented Operation1")

    def required_operations2(self) -> None:
        print("ConcreteClass2 says: Implemented Operation2")

    def hook1(self) -> None:
        print("ConcreteClass2 says: Overridden Hook1")


def client_code(abstract_class: AbstractClass) -> None:
    """
    EN: The client code calls the template method to execute the algorithm.
    Client code does not have to know the concrete class of an object it works
    with, as long as it works with objects through the interface of their base
    class.

    RU: Клиентский код вызывает шаблонный метод для выполнения алгоритма.
    Клиентский код не должен знать конкретный класс объекта, с которым работает,
    при условии, что он работает с объектами через интерфейс их базового класса.
    """

    # ...
    abstract_class.template_method()
    # ...


if __name__ == "__main__":
    print("Same client code can work with different subclasses:")
    client_code(ConcreteClass1())
    print("")

    print("Same client code can work with different subclasses:")
    client_code(ConcreteClass2())
