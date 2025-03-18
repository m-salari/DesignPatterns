"""
    Factory
        - Factory is a creational design pattern that provides an interface for creating objects
        in a subclass, but allows subclasses to alter the type of objects that will be created.

        --hint: Factory is told to a (class, func, method) that returns another object

        - 3 components of Factory: 1. creator   2. product  3. client

            1. creator: creators define what type of objects must be created.
            2. product: a section of code that it does main-work (main process)
            3. client: a section of code that the last-user (client) works with its.
"""

from abc import ABC, abstractmethod


# section CREATOR
class File(ABC):
    def __init__(self, file):
        self.file = file

    @abstractmethod
    def make(self):
        pass

    def call_edit(self):
        product = self.make()
        return product.edit(self.file)


class JsonFile(File):
    def make(self):
        return Json()


class XmlFile(File):
    def make(self):
        return Xml()


#################################################################################
# section PRODUCT

class Json:
    def edit(self, file):
        return f'Working in {file}.json...'


class Xml:
    def edit(self, file):
        return f'Working in {file}.xml...'


#################################################################################
# section CLIENT

def client(file, format_file):
    formats = {
        'json': JsonFile,
        'xml': Xml,
    }

    result = formats[format_file](file)
    return result.call_edit()


print(client('student', 'json'))