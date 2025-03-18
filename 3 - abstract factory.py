"""
    Abstract Factory
    - Abstract Factory pattern serves to provide an interface for creation related/dependent
     objects without need to specify their actual class

    - 3 components of Abstract Factory : 1.(Abstract, Concrete )Product
            2.(Abstract, Concrete )Factory      3.Client

        1. Abstract Product: a section of code that it does main-work (main process) but it is
            Abstract so, it doesn't implement main-process and implement only structure of product.

        2. Abstract Factory: it is a Factory but doesn't implement and is only of Factory structure
        --hint: Factory is told to a (class, func, method) that returns another object

        3. Concrete Factory: it's opposite of abstract. We in abstract don't any work(process) but
            Concretes do really work (process) and implement methods.

        4. Client: a section of code that the last-user (client) works with its.
        --hint: User (Client) doesn't have access to Products. Client can just call Factory and
            Factory returns objects related.

    - example:
        car => Benz, Bmw  => Suv, Coupe

        Benz suv = gla
        Bmw suv = x1
        benz coupe = cls
        bmw coupe = m2

"""

from abc import ABC, abstractmethod


# Abstract Product suv
class Suv(ABC):
    @abstractmethod
    def create_suv(self):
        pass


# Abstract Product coupe
class Coupe(ABC):
    @abstractmethod
    def create_coupe(self):
        pass


###################################################################################
# Concrete Products suv
class Gla(Suv):
    def create_suv(self):
        print('This is your suv benz gla...')


class X1(Suv):
    def create_suv(self):
        print('This is your suv bmw x1...')


# Concrete Products coupe
class Cls(Coupe):
    def create_coupe(self):
        print('This is your coupe benz cls...')


class M2(Coupe):
    def create_coupe(self):
        print('This is your coupe bmw m2...')


#######################################################################################
# Abstract Factory
class Car(ABC):
    @abstractmethod
    def call_suv(self):
        pass

    @abstractmethod
    def call_coupe(self):
        pass


##########################################################################################
# Concrete Factory benz
class Benz(Car):
    def call_suv(self):
        return Gla()

    def call_coupe(self):
        return Cls()


# Concrete Factory bmw
class Bmw(Car):
    def call_suv(self):
        return X1()

    def call_coupe(self):
        return M2()


############################################################################################
# Client
def client_suv(order):
    brands = {
        'benz': Benz,
        'bmw': Bmw
    }
    suv = brands[order]().call_suv()
    suv.create_suv()


def client_coupe(order):
    brands = {
        'benz': Benz,
        'bmw': Bmw
    }
    suv = brands[order]().call_coupe()
    suv.create_coupe()


client_coupe('bmw')