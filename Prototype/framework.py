from abc import ABCMeta, abstractmethod


class Product(metaclass=ABCMeta):
    @abstractmethod
    def use(self, str):
        pass

    @abstractmethod
    def create_clone(self):
        pass


class Manager:
    def __init__(self):
        self._showcase = {}

    def register(self, name, product):
        self._showcase[name] = product

    def create(self, name):
        p = self._showcase[name]
        return p.create_clone()
