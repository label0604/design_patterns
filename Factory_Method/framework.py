from abc import ABCMeta, abstractmethod
from typing import final


class Product(metaclass=ABCMeta):
    @abstractmethod
    def use(self):
        pass


class Factory(metaclass=ABCMeta):
    @final
    def create(self, owner):
        p = self.create_product(owner)
        self.register_product(p)
        return p

    @abstractmethod
    def create_product(self, owner):
        pass

    @abstractmethod
    def register_product(self, product):
        pass
