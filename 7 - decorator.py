"""
    Decorator
    - a structural pattern that allows adding new behaviors to objects dynamically by placing
        them inside special wrapper objects,called decorators.
"""

from abc import ABC, abstractmethod


class Page(ABC):  # Abstract Component
    @abstractmethod
    def show(self):
        pass


class AuthPage(Page):  # Concrete Component 1
    def show(self):
        print('Welcome to authenticated page')


class AnonPage(Page):  # Concrete Component 2
    def show(self):
        print('Welcome to anonymous page')

###########################################################################


class PageDecorator(Page, ABC):  # Abstract Decorator
    def __init__(self, component):
        self._component: AuthPage = component


class PageAuthDecorator(PageDecorator):
    def show(self):
        username = input('Enter username:')
        password = input('Enter password:')
        if username == 'admin' and password == 'secret':
            self._component.show()
        else:
            print('you are not authenticated!')


def auth_client_decorator():
    page = AuthPage()
    authenticated = PageAuthDecorator(page)
    authenticated.show()


auth_client_decorator()



