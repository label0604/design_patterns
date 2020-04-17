from abc import ABCMeta, abstractmethod
from typing import final


class Trouble:
    def __init__(self, number):
        self.number = number

    def get_number(self):
        return self.number

    def __str__(self):
        return '[Trouble {number}]'.format(number=self.number)


class Support(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name
        self.next = None

    def set_next(self, next_support):
        self.next = next_support
        return self.next

    @final
    def support(self, trouble):
        if self.resolve(trouble):
            self.done(trouble)
        elif self.next:
            self.next.support(trouble)
        else:
            self.fail(trouble)

    def __str__(self):
        return '[{name}]'.format(name=self.name)

    @abstractmethod
    def resolve(self, trouble):
        pass

    def done(self, trouble):
        print('{trouble} is resolved by {support}.'.format(
            trouble=trouble, support=self))

    def fail(self, trouble):
        print('{trouble} cannot be resolved'.format(trouble=trouble))


class NoSupport(Support):
    def __init__(self, name):
        super().__init__(name)

    def resolve(self, trouble):
        return False


class LimitSupport(Support):
    def __init__(self, name, limit):
        super().__init__(name)
        self.limit = limit

    def resolve(self, trouble):
        if trouble.get_number() < self.limit:
            return True
        else:
            return False


class OddSupport(Support):
    def __init__(self, name):
        super().__init__(name)

    def resolve(self, trouble):
        if trouble.get_number() % 2 == 1:
            return True
        else:
            return False


class SpecialSupport(Support):
    def __init__(self, name, number):
        super().__init__(name)
        self.number = number

    def resolve(self, trouble):
        if trouble.get_number() == self.number:
            return True
        else:
            return False


if __name__ == '__main__':
    alice = NoSupport('Alice')
    bob = LimitSupport('Bob', 100)
    charlie = SpecialSupport('Charlie', 429)
    diana = LimitSupport('Diana', 200)
    elmo = OddSupport('Elmo')
    fred = LimitSupport('Fred', 300)

    alice.set_next(bob).set_next(charlie).set_next(
        diana).set_next(elmo).set_next(fred)

    for i in range(0, 500, 33):
        alice.support(Trouble(i))
