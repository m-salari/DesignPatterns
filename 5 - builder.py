"""
    Builder
    - Builder is a creational design pattern that lets you construct complex objects step by step.
    the pattern allows you to produce different types and representations of an object using the same
    construction code.

    - 4 components of Builder: 1.Product  2.Builder   3.Director  4.client

        2. Builder: Builders define how to create a product.
        3. Director: Director decides which builder must be chosen for create our product.
        --hint: In director, we define steps of use method on builder.
        4. Client use only director.
"""
from abc import ABC, abstractmethod


# out of design pattern
class Wheel: size = None


class Body: shape = None


class Engine: hp = None


class Car:  # product
    def __init__(self):
        self._wheel = None
        self._engine = None
        self._body = None

    def set_wheel(self, wheel):
        self._wheel = wheel

    def set_body(self, body):
        self._body = body

    def set_engine(self, engine):
        self._engine = engine

    def detail(self):
        print(f'Body: {self._body.shape}')
        print(f'Engine: {self._engine.hp}')
        print(f'Wheel: {self._wheel.size}')


###################################################################################

class AbstractBuilder(ABC):  # Abstract Builder

    @abstractmethod
    def get_engine(self): pass

    @abstractmethod
    def get_wheel(self): pass

    @abstractmethod
    def get_body(self): pass


class Benz(AbstractBuilder):  # Concrete builder Benz
    def get_body(self):
        body = Body()
        body.shape = 'suv'
        return body

    def get_engine(self):
        engine = Engine()
        engine.hp = 500
        return engine

    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 22
        return wheel


class Bmw(AbstractBuilder):  # Concrete Builder Bmw
    def get_body(self):
        body = Body()
        body.shape = 'sedan'
        return body

    def get_engine(self):
        engine = Engine()
        engine.hp = 340
        return engine

    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 20
        return wheel


##################################################################################
class Director:  # Director
    _builder: AbstractBuilder = None

    def set_builder(self, builder):
        self._builder = builder

    def construct(self):
        car = Car()

        body = self._builder.get_body()
        car.set_body(body)

        wheel = self._builder.get_wheel()
        car.set_wheel(wheel)

        engine = self._builder.get_engine()
        car.set_engine(engine)

        return car


##################################################################################
def client_builder(builder):
    builders = {
        'benz': Benz,
        'bmw': Bmw
    }
    builder = builders[builder]()

    director = Director()
    director.set_builder(builder)

    result = director.construct()
    result.detail()


client_builder('bmw')