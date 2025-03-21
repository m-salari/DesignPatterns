"""
    Prototype
    - Prototype is a creational design pattern that lets you copy existing objects without
        making your code dependent on their classes.

"""
from copy import deepcopy


class Prototype:
    def __init__(self):
        self._objects = {}

    def register(self, name, obj):
        self._objects[name] = obj

    def unregister(self, name):
        del self._objects[name]

    def clone(self, name, **kwargs):
        cloned_obj = deepcopy(self._objects.get(name))
        cloned_obj.__dict__.update(kwargs)
        return cloned_obj


def client_prototype(name, obj, **kwargs):
    prototype = Prototype()
    prototype.register(name, obj)
    return prototype.clone(name, **kwargs)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person_reza = Person('reza', 20)
person_cloned_ali = client_prototype('ali', person_reza, age=100)
person_cloned_ali.name = 'ali'


print(person_reza.__dict__)
print(person_cloned_ali.__dict__)
