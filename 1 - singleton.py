"""
    Singleton
        - Ensure a class only has one instance, and provide a global point of access to it.
"""


# # way 1
# class A:
#     _instance = None
#
#     def __init__(self):
#         raise RuntimeError('call get_instance() instead')
#
#     @classmethod
#     def get_instance(cls):
#         if cls._instance is None:
#             cls._instance = cls.__new__(cls)
#         return cls._instance
#
#
# one = A.get_instance()
# two = A.get_instance()
# print(id(one))
# print(id(two))
##################################################################################
# way 2

class Singleton(type):
    _instance = None

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance


class B(metaclass=Singleton):
    pass


b1 = B()
b2 = B()

print(id(b1))
print(id(b2))
