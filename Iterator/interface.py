from abc import ABCMeta, abstractmethod


class Aggregate(metaclass=ABCMeta):

    @abstractmethod
    def __iter__(self):
        pass


class Iterator(metaclass=ABCMeta):

    @abstractmethod
    def __next__(self):
        pass
