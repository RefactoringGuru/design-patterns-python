"""
EN: Memento Design Pattern

Intent: Capture and externalize an object's internal state so that the object
can be restored to this state later, without violating encapsulation.

RU: Паттерн Снимок

Назначение: Фиксирует и восстанавливает внутреннее состояние объекта таким
образом, чтобы  в дальнейшем объект можно было восстановить в этом состоянии
без нарушения инкапсуляции.
"""


from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
from random import sample
from string import ascii_letters, digits


class Originator():
    """
    EN: The Originator holds some important state that may change over time. It
    also defines a method for saving the state inside a memento and another
    method for restoring the state from it.

    RU: Создатель содержит некоторое важное состояние, которое может со временем
    меняться. Он также объявляет метод сохранения состояния внутри снимка и метод
    восстановления состояния из него.
    """

    _state = None
    """
    EN: For the sake of simplicity, the originator's state is
    stored inside a single variable.
    
    RU: Для удобства состояние создателя хранится внутри одной
    переменной.
    """

    def __init__(self, state: str) -> None:
        self._state = state
        print(f"Originator: My initial state is: {self._state}")

    def do_something(self) -> None:
        """
        EN: The Originator's business logic may affect its internal state.
        Therefore, the client should backup the state before launching methods of
        the business logic via the save() method.

        RU: Бизнес-логика Создателя может повлиять на его внутреннее состояние.
        Поэтому клиент должен выполнить резервное копирование состояния с помощью
        метода save перед запуском методов бизнес-логики.
        """

        print("Originator: I'm doing something important.")
        self._state = self._generate_random_string(30)
        print(f"Originator: and my state has changed to: {self._state}")

    def _generate_random_string(self, length: int = 10) -> None:
        return "".join(sample(ascii_letters, length))

    def save(self) -> Memento:
        """
        EN: Saves the current state inside a memento.

        RU: Сохраняет текущее состояние внутри снимка.
        """

        return ConcreteMemento(self._state)

    def restore(self, memento: Memento) -> None:
        """
        EN: Restores the Originator's state from a memento object.

        RU: Восстанавливает состояние Создателя из объекта снимка.
        """

        self._state = memento.get_state()
        print(f"Originator: My state has changed to: {self._state}")


class Memento(ABC):
    """
    EN: The Memento interface provides a way to retrieve the memento's metadata,
    such as creation date or name. However, it doesn't expose the Originator's
    state.

    RU: Интерфейс Снимка предоставляет способ извлечения метаданных снимка, таких
    как дата создания или название. Однако он не раскрывает состояние Создателя.
    """

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_date(self) -> str:
        pass


class ConcreteMemento(Memento):
    def __init__(self, state: str) -> None:
        self._state = state
        self._date = str(datetime.now())[:19]

    def get_state(self) -> str:
        """
        EN: The Originator uses this method when restoring its state.

        RU: Создатель использует этот метод, когда восстанавливает своё
        состояние.
        """
        return self._state

    def get_name(self) -> str:
        """
        EN: The rest of the methods are used by the Caretaker to display
        metadata.

        RU: Остальные методы используются Опекуном для отображения метаданных.
        """

        return f"{self._date} / ({self._state[0:9]}...)"

    def get_date(self) -> str:
        return self._date


class Caretaker():
    """
    EN: The Caretaker doesn't depend on the Concrete Memento class. Therefore, it
    doesn't have access to the originator's state, stored inside the memento. It
    works with all mementos via the base Memento interface.

    RU: Опекун не зависит от класса Конкретного Снимка. Таким образом, он не
    имеет доступа к состоянию создателя, хранящемуся внутри снимка. Он работает
    со всеми снимками через базовый интерфейс Снимка.
    """

    def __init__(self, originator: Originator) -> None:
        self._mementos = []
        self._originator = originator

    def backup(self) -> None:
        print("\nCaretaker: Saving Originator's state...")
        self._mementos.append(self._originator.save())

    def undo(self) -> None:
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        print(f"Caretaker: Restoring state to: {memento.get_name()}")
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()

    def show_history(self) -> None:
        print("Caretaker: Here's the list of mementos:")
        for memento in self._mementos:
            print(memento.get_name())


if __name__ == "__main__":
    originator = Originator("Super-duper-super-puper-super.")
    caretaker = Caretaker(originator)

    caretaker.backup()
    originator.do_something()

    caretaker.backup()
    originator.do_something()

    caretaker.backup()
    originator.do_something()

    print()
    caretaker.show_history()

    print("\nClient: Now, let's rollback!\n")
    caretaker.undo()

    print("\nClient: Once more!\n")
    caretaker.undo()
