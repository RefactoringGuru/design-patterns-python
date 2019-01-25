from abc import ABCMeta, abstractmethod, abstractproperty


class Builder(metaclass=ABCMeta):
    @abstractproperty
    def product(self):
        pass

    @abstractmethod
    def produce_part_a(self):
        pass

    @abstractmethod
    def produce_part_b(self):
        pass

    @abstractmethod
    def produce_part_c(self):
        pass


class ConcreteBuilder1(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._product = Product1()

    @property
    def product(self):
        product = self._product
        self.reset()
        return product

    def produce_part_a(self):
        self._product.add("PartA1")

    def produce_part_b(self):
        self._product.add("PartB1")

    def produce_part_c(self):
        self._product.add("PartC1")


class Product1(object):
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def list_parts(self):
        print(f"Product parts: {', '.join(self.parts)}", end="")


class Director:
    def __init__(self):
        self._builder = None

    @property
    def builder(self):
        return self._builder

    @builder.setter
    def builder(self, builder):
        self._builder = builder

    def build_minimal_viable_product(self):
        self.builder.produce_part_a()

    def build_full_featured_product(self):
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()


if __name__ == '__main__':
    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder

    print("Standard basic product: ")
    director.build_minimal_viable_product()
    builder.product.list_parts()

    print("\n")

    print("Standard full featured product: ")
    director.build_full_featured_product()
    builder.product.list_parts()

    print("\n")

    print("Custom product: ")
    builder.produce_part_a()
    builder.produce_part_b()
    builder.product.list_parts()
