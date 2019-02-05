"""
EN: Decorator Design Pattern

Intent: Attach additional responsibilities to an object dynamically.
Decorators provide a flexible alternative to subclassing for extending
functionality.

RU: Паттерн Декоратор

Назначение: Динамически подключает к объекту дополнительную функциональность.
Декораторы предоставляют гибкую альтернативу практике создания подклассов для
расширения функциональности.
"""


class Component():
    """
    EN: The base Component interface defines operations that can be altered by
    decorators.

    RU: Базовый интерфейс Компонента определяет поведение, которое изменяется
    декораторами.
    """

    def operation(self) -> str:
        pass


class ConcreteComponent(Component):
    """
    EN: Concrete Components provide default implementations of the operations.
    There might be several variations of these classes.

    RU: Конкретные Компоненты предоставляют реализации поведения по умолчанию.
    Может быть несколько вариаций этих классов.
    """

    def operation(self) -> str:
        return "ConcreteComponent"


class Decorator(Component):
    """
    EN: The base Decorator class follows the same interface as the other
    components. The primary purpose of this class is to define the wrapping
    interface for all concrete decorators. The default implementation of the
    wrapping code might include a field for storing a wrapped component and the
    means to initialize it.

    RU: Базовый класс Декоратора следует тому же интерфейсу, что и другие
    компоненты. Основная цель этого класса - определить интерфейс обёртки для
    всех конкретных декораторов. Реализация кода обёртки по умолчанию может
    включать в себя поле для хранения завёрнутого компонента и средства его
    инициализации.
    """

    _component: Component = None

    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> str:
        """
        EN: The Decorator delegates all work to the wrapped component.

        RU: Декоратор делегирует всю работу обёрнутому компоненту.
        """

        return self._component

    def operation(self) -> str:
        self._component.operation()


class ConcreteDecoratorA(Decorator):
    """
    EN: Concrete Decorators call the wrapped object and alter its result in some
    way.

    RU: Конкретные Декораторы вызывают обёрнутый объект и изменяют его результат
    некоторым образом.
    """

    def operation(self) -> str:
        """
        EN: Decorators may call parent implementation of the operation, instead
        of calling the wrapped object directly. This approach simplifies
        extension of decorator classes.

        RU: Декораторы могут вызывать родительскую реализацию операции, вместо
        того, чтобы вызвать обёрнутый объект напрямую. Такой подход упрощает
        расширение классов декораторов.
        """
        return f"ConcreteDecoratorA({self.component.operation()})"


class ConcreteDecoratorB(Decorator):
    """
    EN: Decorators can execute their behavior either before or after the call to
    a wrapped object.

    RU: Декораторы могут выполнять своё поведение до или после вызова обёрнутого
    объекта.
    """

    def operation(self) -> str:
        return f"ConcreteDecoratorB({self.component.operation()})"


def client_code(component: Component) -> None:
    """
    EN: The client code works with all objects using the Component interface.
    This way it can stay independent of the concrete classes of components it
    works with.

    RU: Клиентский код работает со всеми объектами, используя интерфейс
    Компонента. Таким образом, он остаётся независимым от конкретных классов
    компонентов, с которыми работает.
    """

    # ...

    print(f"RESULT: {component.operation()}", end="")

    # ...


if __name__ == "__main__":
    # EN: This way the client code can support both simple components...
    # 
    # RU: Таким образом, клиентский код может поддерживать как простые
    # компоненты...
    simple = ConcreteComponent()
    print("Client: I've got a simple component:")
    client_code(simple)
    print("\n")

    # EN: ...as well as decorated ones.
    # 
    # Note how decorators can wrap not only simple components but the other
    # decorators as well.
    # 
    # RU: ...так и декорированные.
    # 
    # Обратите внимание, что декораторы могут обёртывать не только простые
    # компоненты, но и другие декораторы.
    decorator1 = ConcreteDecoratorA(simple)
    decorator2 = ConcreteDecoratorB(decorator1)
    print("Client: Now I've got a decorated component:")
    client_code(decorator2)
