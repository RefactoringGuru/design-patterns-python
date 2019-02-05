"""
EN: State Design Pattern

Intent: Allow an object to alter its behavior when its internal state
changes. The object will appear to change its class.

RU: Паттерн Состояние

Назначение: Позволяет объекту менять поведение при изменении его внутреннего
состояния. Со стороны может казаться, что объект меняет свой класс.
"""


from __future__ import annotations
from abc import ABC, abstractmethod


class Context(ABC):
    """
    EN: The Context defines the interface of interest to clients. It also
    maintains a reference to an instance of a State subclass, which represents
    the current state of the Context.

    RU: Контекст определяет интерфейс, представляющий интерес для клиентов. Он
    также хранит ссылку на экземпляр подкласса Состояния, который отображает
    текущее состояние Контекста.
    """

    _state = None
    """
    EN: A reference to the current state of the Context.
    
    RU: Ссылка на текущее состояние Контекста.
    """

    def __init__(self, state: State) -> None:
        self.transition_to(state)

    def transition_to(self, state: State):
        """
        EN: The Context allows changing the State object at runtime.

        RU: Контекст позволяет изменять объект Состояния во время выполнения.
        """

        print(f"Context: Transition to {type(state).__name__}")
        self._state = state
        self._state.context = self

    """
    EN: The Context delegates part of its behavior to the current State
    object.
    
    RU: Контекст делегирует часть своего поведения текущему объекту
    Состояния.
    """

    def request1(self):
        self._state.handle1()

    def request2(self):
        self._state.handle2()


class State(ABC):
    """
    EN: The base State class declares methods that all Concrete State should
    implement and also provides a backreference to the Context object,
    associated with the State. This backreference can be used by States to
    transition the Context to another State.

    RU: Базовый класс Состояния объявляет методы, которые должны реализовать все
    Конкретные Состояния, а также предоставляет обратную ссылку на объект
    Контекст, связанный с Состоянием. Эта обратная ссылка может использоваться
    Состояниями для передачи Контекста другому Состоянию.
    """

    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context) -> None:
        self._context = context

    @abstractmethod
    def handle1(self) -> None:
        pass

    @abstractmethod
    def handle2(self) -> None:
        pass


"""
EN: Concrete States implement various behaviors, associated with a state of
the Context.

RU: Конкретные Состояния реализуют различные модели поведения, связанные с
состоянием Контекста.
"""


class ConcreteStateA(State):
    def handle1(self) -> None:
        print("ConcreteStateA handles request1.")
        print("ConcreteStateA wants to change the state of the context.")
        self.context.transition_to(ConcreteStateB())

    def handle2(self) -> None:
        print("ConcreteStateA handles request2.")


class ConcreteStateB(State):
    def handle1(self) -> None:
        print("ConcreteStateB handles request1.")

    def handle2(self) -> None:
        print("ConcreteStateB handles request2.")
        print("ConcreteStateB wants to change the state of the context.")
        self.context.transition_to(ConcreteStateA())


if __name__ == "__main__":
    # EN: The client code.
    # 
    # RU: Клиентский код.
    
    context = Context(ConcreteStateA())
    context.request1()
    context.request2()
