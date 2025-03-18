"""
    Proxy
    - q structural design pattern that lets you provide a substitute or placeholder for another
        object. A proxy controls access to the original object, allowing you to perform something
        either before or after the request gets through to the original object.

    - 3 components of Proxy:    1. Client   2.Proxy     3.Service
    --hint: we sometimes don't have access to service
    --hint: we can have multy service and proxy. So in class proxy we must choose what server we
        need and in def client we must choose what proxy we need.
"""
from abc import ABC, abstractmethod
import time
import datetime


class AbstractServer(ABC):  # ServiceInterface
    @abstractmethod
    def receive(self):
        pass


class Server(AbstractServer):  # Service
    def receive(self):
        print('Processing your request...')
        time.sleep(1)
        print('Done.!')

###########################################################################################


class LogProxy(AbstractServer):  # Proxy
    def __init__(self, server):
        self._server: Server = server

    def logging(self):
        with open('log.log', 'a') as log:
            log.write(f'Request {datetime.datetime.now()}\n')

    def receive(self):
        self.logging()
        # ... another method
        self._server.receive()


def client_server(server: Server, proxy: LogProxy):
    s = server()
    p = proxy(s)
    p.receive()


client_server(Server, LogProxy)











