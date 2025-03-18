from abc import ABC, abstractmethod

'''
    Abstract Class, Abstract Method
    force subclasses to override method its parent. if we don't override, it will give error.
'''


class A(ABC):
    @abstractmethod
    def show(self):
        print('A...')


class B(A):
    def show(self):
        # super().show()
        print('show method B...')


b = B()
b.show()