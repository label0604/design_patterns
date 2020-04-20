from abc import ABCMeta, abstractmethod
from random import randint
from time import sleep


class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, generator):
        pass


class NumberGenerator(metaclass=ABCMeta):
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def delete_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self)

    @abstractmethod
    def get_number(self):
        pass

    @abstractmethod
    def execute(self):
        pass


class RandomNumberGenerator(NumberGenerator):
    def __init__(self):
        super().__init__()
        self.number = 0

    def get_number(self):
        return self.number

    def execute(self):
        for _ in range(20):
            self.number = randint(0, 50)
            self.notify_observers()


class DigitObserver(Observer):
    def update(self, generator):
        print('DigitObserver:' + str(generator.get_number()))
        sleep(0.5)


class GraphObserver(Observer):
    def update(self, generator):
        print('GraphObserver:', end='')
        count = generator.get_number()
        for _ in range(count):
            print('*', end='')
        print('')
        sleep(0.5)


if __name__ == '__main__':
    generator = RandomNumberGenerator()
    observer1 = DigitObserver()
    observer2 = GraphObserver()
    generator.add_observer(observer1)
    generator.add_observer(observer2)
    generator.execute()
