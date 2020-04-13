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
class PrintBanner(Print):
    def __init__(self, string):
        self.banner = Banner(string)
    
    def print_weak(self):
        self.banner.show_with_paren()
    
    def print_strong(self):
        self.banner.show_with_aster()


if __name__ == "__main__":
    p = PrintBanner('Hello')
    p.print_weak()
    p.print_strong()
