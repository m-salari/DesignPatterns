"""
    Composite
    - a structural design pattern that lets  you compose objects into tree structures and
        then work with these structures as if they were individual objects.

    3 parts of composite:   1.Component     2.Composite     3.Leaf
        1. Component: it is its object and its can divide to leafs and composite.
        2. Composite: a part of code(classes) that has subclasses.
            --hint: in method 'execute', we do works of the composite and call subclasses.
        3. Leaf: a part of code (classes) that doesn't have subclasses.
            --hint: in method 'execute', we just do works of the leaf.
"""

from abc import ABC, abstractmethod


class Being(ABC):  # Abstract Component

    def add(self, child):
        pass

    def remove(self, child):
        pass

    def is_composite(self):
        return False

    @abstractmethod
    def execute(self):
        pass


#############################################################################
class Animal(Being):  # leaf of component up
    def __init__(self, name):
        self.name = name

    def execute(self):
        print(f'Animal {self.name}')


###############################################################################
class Human(Being):  # Concrete Composite
    def __init__(self):
        self._children = []

    def add(self, child):
        self._children.append(child)

    def remove(self, child):
        self._children.remove(child)

    def is_composite(self):
        return True

    def execute(self):
        print('processing of Human...')
        for child in self._children:
            child: Being
            child.execute()


###############################################################################
class Male(Human):  # leaf of Composite up
    def __init__(self, name):
        self.name = name

    def is_composite(self):
        return False

    def execute(self):
        print(f'\tMale {self.name}')


class Female(Human):  # Leaf of Composite up
    def __init__(self, name):
        self.name = name

    def is_composite(self):
        return False

    def execute(self):
        print(f'\tFemale {self.name}')


#################################################################################
def client_composite():
    f1 = Female('jane')
    f2 = Female('Katty')
    m1 = Male('Brad')

    human = Human()

    human.add(f1)
    human.add(f2)
    human.add(m1)
    human.execute()


client_composite()