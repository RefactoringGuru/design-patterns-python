"""
EN: Flyweight Design Pattern

Intent: Lets you fit more objects into the available amount of RAM by sharing
common parts of state between multiple objects, instead of keeping all of the
data in each object.

RU: Паттерн Легковес

Назначение: Позволяет вместить бóльшее количество объектов в отведённую
оперативную память. Легковес экономит память, разделяя общее состояние объектов
между собой, вместо хранения одинаковых данных в каждом объекте.
"""


import json
from typing import Dict


class Flyweight():
    """
    EN: The Flyweight stores a common portion of the state (also called
    intrinsic state) that belongs to multiple real business entities. The
    Flyweight accepts the rest of the state (extrinsic state, unique for each
    entity) via its method parameters.

    RU: Легковес хранит общую часть состояния (также называемую внутренним
    состоянием), которая принадлежит нескольким реальным бизнес-объектам.
    Легковес принимает оставшуюся часть состояния (внешнее состояние, уникальное
    для каждого объекта) через его параметры метода.
    """

    def __init__(self, shared_state: str) -> None:
        self._shared_state = shared_state

    def operation(self, unique_state: str) -> None:
        s = json.dumps(self._shared_state)
        u = json.dumps(unique_state)
        print(f"Flyweight: Displaying shared ({s}) and unique ({u}) state.", end="")


class FlyweightFactory():
    """
    EN: The Flyweight Factory creates and manages the Flyweight objects. It
    ensures that flyweights are shared correctly. When the client requests a
    flyweight, the factory either returns an existing instance or creates a new
    one, if it doesn't exist yet.

    RU: Фабрика Легковесов создает объекты-Легковесы и управляет ими. Она
    обеспечивает правильное разделение легковесов. Когда клиент запрашивает
    легковес, фабрика либо возвращает существующий экземпляр, либо создает
    новый, если он ещё не существует.
    """

    _flyweights: Dict[str, Flyweight] = {}

    def __init__(self, initial_flyweights: Dict) -> None:
        for state in initial_flyweights:
            self._flyweights[self.get_key(state)] = Flyweight(state)

    def get_key(self, state: Dict) -> str:
        """
        EN: Returns a Flyweight's string hash for a given state.

        RU: Возвращает хеш строки Легковеса для данного состояния.
        """

        return "_".join(sorted(state))

    def get_flyweight(self, shared_state: Dict) -> Flyweight:
        """
        EN: Returns an existing Flyweight with a given state or creates a new
        one.

        RU: Возвращает существующий Легковес с заданным состоянием или создает
        новый.
        """

        key = self.get_key(shared_state)

        if not self._flyweights.get(key):
            print("FlyweightFactory: Can't find a flyweight, creating new one.")
            self._flyweights[key] = Flyweight(shared_state)
        else:
            print("FlyweightFactory: Reusing existing flyweight.")

        return self._flyweights[key]

    def list_flyweights(self) -> None:
        count = len(self._flyweights)
        print(f"FlyweightFactory: I have {count} flyweights:")
        print("\n".join(map(str, self._flyweights.keys())), end="")


def add_car_to_police_database(
    factory: FlyweightFactory, plates: str, owner: str,
    brand: str, model: str, color: str
) -> None:
    print("\n\nClient: Adding a car to database.")
    flyweight = factory.get_flyweight([brand, model, color])
    # EN: The client code either stores or calculates extrinsic state and passes
    # it to the flyweight's methods.
    #
    # RU: Клиентский код либо сохраняет, либо вычисляет внешнее состояние и
    # передает его методам легковеса.
    flyweight.operation([plates, owner])


if __name__ == "__main__":
    """
    EN: The client code usually creates a bunch of pre-populated flyweights in
    the initialization stage of the application.

    RU: Клиентский код обычно создает кучу предварительно заполненных легковесов
    на этапе инициализации приложения.
    """

    factory = FlyweightFactory([
        ["Chevrolet", "Camaro2018", "pink"],
        ["Mercedes Benz", "C300", "black"],
        ["Mercedes Benz", "C500", "red"],
        ["BMW", "M5", "red"],
        ["BMW", "X6", "white"],
    ])

    factory.list_flyweights()

    add_car_to_police_database(
        factory, "CL234IR", "James Doe", "BMW", "M5", "red")

    add_car_to_police_database(
        factory, "CL234IR", "James Doe", "BMW", "X1", "red")

    print("\n")

    factory.list_flyweights()
