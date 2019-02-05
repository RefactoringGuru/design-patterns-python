"""
EN: Iterator Design Pattern

Intent: Provide a way to traverse the elements of an aggregate object without
exposing its underlying representation.

RU: Паттерн Итератор

Назначение: Предоставляет возможность обходить элементы составного объекта,
не раскрывая его внутреннего представления.
"""


from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, List


"""
EN: To create an iterator in Python, there are two abstract classes from the
built-in `collections` module - Iterable,Iterator. We need to implement the
`__iter__()` method in the iterated object (collection), and the `__next__ ()`
method in theiterator.

RU: Для создания итератора в Python есть два абстрактных класса из встроенного
модуля collections - Iterable, Iterator. Нужно реализовать метод __iter__() в
итерируемом объекте (списке), а метод __next__() в итераторе.
"""


class AlphabeticalOrderIterator(Iterator):
    """
    EN: Concrete Iterators implement various traversal algorithms. These classes
    store the current traversal position at all times.

    RU: Конкретные Итераторы реализуют различные алгоритмы обхода. Эти классы
    постоянно хранят текущее положение обхода.
    """

    """
    EN: `_position` attribute stores the current traversal position. An iterator
    may have a lot of other fields for storing iteration state, especially when
    it is supposed to work with a particular kind of collection.

    RU: Атрибут _position хранит текущее положение обхода. У итератора может
    быть множество других полей для хранения состояния итерации, особенно когда
    он должен работать с определённым типом коллекции.
    """
    _position: int = None

    """
    EN: This attribute indicates the traversal direction.
    
    RU: Этот атрибут указывает направление обхода.
    """
    _reverse: bool = False

    def __init__(self, collection: WordsCollection, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        """
        EN: The __next__() method must return the next item in the sequence. On
        reaching the end, and in subsequent calls, it must raise StopIteration.

        RU: Метод __next __() должен вернуть следующий элемент в
        последовательности. При достижении конца коллекции и в последующих
        вызовах должно вызываться исключение StopIteration.
        """
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value


class WordsCollection(Iterable):
    """
    EN: Concrete Collections provide one or several methods for retrieving fresh
    iterator instances, compatible with the collection class.

    RU: Конкретные Коллекции предоставляют один или несколько методов для
    получения новых экземпляров итератора, совместимых с классом коллекции.
    """

    def __init__(self, collection: List[Any] = []) -> None:
        self._collection = collection

    def __iter__(self) -> AlphabeticalOrderIterator:
        """
        EN: The __iter__() method returns the iterator object itself, by default
        we return the iterator in ascending order.

        RU: Метод __iter__() возвращает объект итератора, по умолчанию мы
        возвращаем итератор с сортировкой по возрастанию.
        """
        return AlphabeticalOrderIterator(self._collection)

    def get_reverse_iterator(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self._collection, True)

    def add_item(self, item: Any):
        self._collection.append(item)


if __name__ == "__main__":
    # EN: The client code may or may not know about the Concrete Iterator or
    # Collection classes, depending on the level of indirection you want to keep
    # in your program.
    #
    # RU: Клиентский код может знать или не знать о Конкретном Итераторе или
    # классах Коллекций, в зависимости от уровня косвенности, который вы хотите
    # сохранить в своей программе.
    collection = WordsCollection()
    collection.add_item("First")
    collection.add_item("Second")
    collection.add_item("Third")

    print("Straight traversal:")
    print("\n".join(collection))
    print("")

    print("Reverse traversal:")
    print("\n".join(collection.get_reverse_iterator()), end="")
