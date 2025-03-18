"""
    __call__
"""


class A:
    def __call__(self, *args, **kwargs):
        print('call method...')


# a1 = A()
# a1()
################################################################################
"""
    __new__
"""


class B:
    def __init__(self, name):
        self.name = name

    def __new__(cls, name, *args, **kwargs):
        if name == 'reza':
            return None
        else:
            return super().__new__(cls, *args, **kwargs)


# b1 = B('reza')
# print(b1)
################################################################################
"""
    Meta class
"""


class Singleton(type):
    _instance = None

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance


class db(metaclass=Singleton):
    pass


# d1 = db()
# d2 = db()
# print(id(d1))
# print(id(d2))