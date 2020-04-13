from abc import ABCMeta, abstractmethod
from typing import final
from unicodedata import east_asian_width


class AbstractDisplay(metaclass=ABCMeta):
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def close(self):
        pass

    @final
    def display(self):
        self.open()
        for _ in range(5):
            self.print()
        self.close()


class CharDisplay(AbstractDisplay):
    def __init__(self, ch):
        self.ch = ch

    def open(self):
        print('<<', end='')

    def print(self):
        print(self.ch, end='')

    def close(self):
        print('>>')


class StringDisplay(AbstractDisplay):
    def __init__(self, string):
        self.string = string
        self.width = self._count_length(string)

    def open(self):
        self._print_line()

    def print(self):
        print('|{string}|'.format(string=self.string))

    def close(self):
        self._print_line()

    def _count_length(self, string):
        count = 0
        for c in string:
            if east_asian_width(c) in 'FWA':
                count += 2
            else:
                count += 1
        return count

    def _print_line(self):
        line = '-' * self.width
        print('+{line}+'.format(line=line))


if __name__ == '__main__':
    d1 = CharDisplay('H')
    d2 = StringDisplay('Hello, World.')
    d3 = StringDisplay('こんにちは')

    d1.display()
    d2.display()
    d3.display()
