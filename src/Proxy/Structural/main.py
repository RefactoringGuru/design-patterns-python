"""
EN: Proxy Design Pattern

Intent: Provide a surrogate or placeholder for another object to control
access to the original object or to add other responsibilities.

RU: Паттерн Заместитель

Назначение: Предоставляет заменитель или местозаполнитель для другого
объекта, чтобы контролировать доступ к оригинальному объекту или добавлять
другие обязанности.
"""


from abc import ABC, abstractmethod


class Subject(ABC):
    """
    EN: The Subject interface declares common operations for both RealSubject
    and the Proxy. As long as the client works with RealSubject using this
    interface, you'll be able to pass it a proxy instead of a real subject.

    RU: Интерфейс Субъекта объявляет общие операции как для Реального Субъекта,
    так и для Заместителя. Пока клиент работает с Реальным Субъектом, используя
    этот интерфейс, вы сможете передать ему заместителя вместо реального
    субъекта.
    """

    @abstractmethod
    def request(self) -> None:
        pass


class RealSubject(Subject):
    """
    EN: The RealSubject contains some core business logic. Usually, RealSubjects
    are capable of doing some useful work which may also be very slow or
    sensitive - e.g. correcting input data. A Proxy can solve these issues
    without any changes to the RealSubject's code.

    RU: Реальный Субъект содержит некоторую базовую бизнес-логику. Как правило,
    Реальные Субъекты способны выполнять некоторую полезную работу, которая к
    тому же может быть очень медленной или точной – например, коррекция входных
    данных. Заместитель может решить эти задачи без каких-либо изменений в коде
    Реального Субъекта.
    """

    def request(self) -> None:
        print("RealSubject: Handling request.")


class Proxy(Subject):
    """
    EN: The Proxy has an interface identical to the RealSubject.

    RU: Интерфейс Заместителя идентичен интерфейсу Реального Субъекта.
    """

    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject

    def request(self) -> None:
        """
        EN: The most common applications of the Proxy pattern are lazy loading,
        caching, controlling the access, logging, etc. A Proxy can perform one
        of these things and then, depending on the result, pass the execution to
        the same method in a linked RealSubject object.

        RU: Наиболее распространёнными областями применения паттерна Заместитель
        являются ленивая загрузка, кэширование, контроль доступа, ведение
        журнала и т.д. Заместитель может выполнить одну из этих задач, а затем,
        в зависимости от результата, передать выполнение одноимённому методу в
        связанном объекте класса Реального Субъекта.
        """

        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self) -> bool:
        print("Proxy: Checking access prior to firing a real request.")
        return True

    def log_access(self) -> None:
        print("Proxy: Logging the time of request.", end="")


def client_code(subject: Subject) -> None:
    """
    EN: The client code is supposed to work with all objects (both subjects and
    proxies) via the Subject interface in order to support both real subjects
    and proxies. In real life, however, clients mostly work with their real
    subjects directly. In this case, to implement the pattern more easily, you
    can extend your proxy from the real subject's class.

    RU: Клиентский код должен работать со всеми объектами (как с реальными, так
    и заместителями) через интерфейс Субъекта, чтобы поддерживать как реальные
    субъекты, так и заместителей. В реальной жизни, однако, клиенты в основном
    работают с реальными субъектами напрямую. В этом случае, для более простой
    реализации паттерна, можно расширить заместителя из класса реального
    субъекта.
    """

    # ...

    subject.request()

    # ...


if __name__ == "__main__":
    print("Client: Executing the client code with a real subject:")
    real_subject = RealSubject()
    client_code(real_subject)

    print("")

    print("Client: Executing the same client code with a proxy:")
    proxy = Proxy(real_subject)
    client_code(proxy)
