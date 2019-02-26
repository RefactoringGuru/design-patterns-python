"""
EN: Observer Design Pattern

Intent: Define a one-to-many dependency between objects so that when one
object changes state, all of its dependents are notified and updated
automatically.

Note that there's a lot of different terms with similar meaning associated
with this pattern. Just remember that the Subject is also called the
Publisher and the Observer is often called the Subscriber and vice versa.
Also the verbs "observe", "listen" or "track" usually mean the same thing.

RU: Паттерн Наблюдатель

Назначение: Устанавливает между объектами зависимость «один ко многим» таким
образом,  что когда изменяется состояние одного объекта, все зависимые от
него объекты оповещаются и обновляются автоматически.

Обратите внимание, что существует множество различных терминов с похожими
значениями, связанных с этим паттерном. Просто помните, что Субъекта также
называют Издателем,  а Наблюдателя часто называют Подписчиком и наоборот.
Также глаголы «наблюдать», «слушать» или «отслеживать» обычно означают одно
и то же.
"""


from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List

class Subject(ABC):
    """
    EN: The Subject interface declares a set of methods for managing subscribers.

    RU: Интферфейс издателя объявляет набор методов для управлениями подпискичами.
    """

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        EN: Attach an observer to the subject.

        RU: Присоединяет наблюдателя к издателю.
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        EN: Detach an observer from the subject.

        RU: Отсоединяет наблюдателя от издателя.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        EN: Notify all observers about an event.

        RU: Уведомляет всех наблюдателей о событии.
        """
        pass


class ConcreteSubject(Subject):
    """
    EN: The Subject owns some important state and notifies observers when the
    state changes.

    RU: Издатель владеет некоторым важным состоянием и оповещает наблюдателей о
    его изменениях.
    """

    _state: int = None
    """
     EN: For the sake of simplicity, the Subject's state, essential
     to all subscribers, is stored in this variable.
     
     RU: Для удобства в этой переменной хранится состояние Издателя,
     необходимое всем подписчикам.
    """

    _observers: List[Observer] = []
    """
    EN: List of subscribers. In real life, the list of subscribers
    can be stored more comprehensively (categorized by event type, etc.).

    RU: Список подписчиков. В реальной жизни список подписчиков
    может храниться в более подробном виде (классифицируется по типу события
    и т.д.)
    """

    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    """
    EN: The subscription management methods.

    RU: Методы управления подпиской.
    """

    def notify(self) -> None:
        """
        EN: Trigger an update in each subscriber.

        RU: Запуск обновления в каждом подписчике.
        """

        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:
        """
        EN: Usually, the subscription logic is only a fraction of what a Subject
        can really do. Subjects commonly hold some important business logic,
        that triggers a notification method whenever something important is
        about to happen (or after it).

        RU: Обычно логика подписки – только часть того, что делает Издатель.
        Издатели часто содержат некоторую важную бизнес-логику, которая
        запускает метод уведомления всякий раз, когда должно произойти что-то
        важное (или после этого).
        """

        print("\nSubject: I'm doing something important.")
        self._state = randrange(0, 10)

        print(f"Subject: My state has just changed to: {self._state}")
        self.notify()


class Observer(ABC):
    """
    EN: The Observer interface declares the update method, used by subjects.

    RU: Интерфейс Наблюдателя объявляет метод уведомления, который издатели
    используют для оповещения своих подписчиков.
    """

    @abstractmethod
    def update(self, subject: Subject) -> None:
        """
        EN: Receive update from subject.

        RU: Получить обновление от субъекта.
        """
        pass



"""
EN: Concrete Observers react to the updates issued by the Subject they had
been attached to.

RU: Конкретные Наблюдатели реагируют на обновления, выпущенные Издателем, к
которому они прикреплены.
"""


class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state < 3:
            print("ConcreteObserverA: Reacted to the event")


class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 0 or subject._state >= 2:
            print("ConcreteObserverB: Reacted to the event")


if __name__ == "__main__":
    # EN: The client code.
    #
    # RU: Клиентский код.

    subject = ConcreteSubject()

    observer_a = ConcreteObserverA()
    subject.attach(observer_a)

    observer_b = ConcreteObserverB()
    subject.attach(observer_b)

    subject.some_business_logic()
    subject.some_business_logic()

    subject.detach(observer_a)

    subject.some_business_logic()
