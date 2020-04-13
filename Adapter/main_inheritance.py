from abc import ABCMeta, abstractmethod

from banner import Banner


# interface
class Print(metaclass=ABCMeta):
    @abstractmethod
    def print_weak(self):
        pass

    @abstractmethod
    def print_strong(self):
        pass


# Adapter
class PrintBanner(Banner, Print):
    def __init__(self, string):
        Banner.__init__(self, string)

    def print_weak(self):
        self.show_with_paren()

    def print_strong(self):
        self.show_with_aster()


if __name__ == "__main__":
    p = PrintBanner('Hello')
    p.print_weak()
    p.print_strong()
