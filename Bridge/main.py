from abc import ABCMeta, abstractmethod
from typing import final
from unicodedata import east_asian_width


class Display:
    def __init__(self, impl):
        self.impl = impl

    def open(self):
        self.impl.raw_open()

    def print(self):
        self.impl.raw_print()

    def close(self):
        self.impl.raw_close()

    @final
    def display(self):
        self.open()
        self.print()
        self.close()


class CountDisplay(Display):
    def multiDisplay(self, times):
        self.open()
        for _ in range(times):
            self.print()
        self.close()


class DisplayImpl:
    @abstractmethod
    def raw_open(self):
        pass

    @abstractmethod
    def raw_print(self):
        pass

    @abstractmethod
    def raw_close(self):
        pass


class StringDisplayImpl(DisplayImpl):
    def __init__(self, string):
        self.string = string
        self.width = self._count_width(string)

    def raw_open(self):
        self._printLine()

    def raw_print(self):
        print('|{string}|'.format(string=self.string))

    def raw_close(self):
        self._printLine()

    def _printLine(self):
        line = '-' * self.width
        print('+{line}+'.format(line=line))

    def _count_width(self, string):
        count = 0
        for c in string:
            if east_asian_width(c) in 'FWA':
                count += 2
            else:
                count += 1
        return count


if __name__ == '__main__':
    d1 = Display(StringDisplayImpl('Hello, Japan.'))
    d2 = CountDisplay(StringDisplayImpl('Hello, World.'))
    d3 = CountDisplay(StringDisplayImpl('Hello, Universe.'))

    d1.display()
    d2.display()
    d3.display()
    d3.multiDisplay(5)
