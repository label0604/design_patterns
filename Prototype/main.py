from copy import copy
from unicodedata import east_asian_width

from framework import Manager, Product


class MessageBox(Product):
    def __init__(self, decochar):
        self.decochar = decochar

    def use(self, string):
        length = self._count_length(string)
        decoline = self.decochar * (length + 4)
        print(decoline)
        print('{deco} {string} {deco}'.format(
            deco=self.decochar, string=string))
        print(decoline)

    def create_clone(self):
        return copy(self)

    def _count_length(self, string):
        count = 0
        for c in string:
            if east_asian_width(c) in 'FWA':
                count += 2
            else:
                count += 1
        return count


class UnderlinePen(Product):
    def __init__(self, ulchar):
        self.ulchar = ulchar

    def use(self, string):
        length = self._count_length(string)
        ul = self.ulchar * length
        print('\"{string}\"'.format(string=string))
        print(' {ul} '.format(ul=ul))

    def create_clone(self):
        return copy(self)

    def _count_length(self, string):
        count = 0
        for c in string:
            if east_asian_width(c) in 'FWA':
                count += 2
            else:
                count += 1
        return count


if __name__ == "__main__":
    # initialize
    manager = Manager()
    upen = UnderlinePen('~')
    mbox = MessageBox('*')
    sbox = MessageBox('/')
    manager.register('strong message', upen)
    manager.register('warning box', mbox)
    manager.register('slash box', sbox)

    # clone
    p1 = manager.create('strong message')
    p1.use('Hello, World')
    p2 = manager.create('warning box')
    p2.use('Hello, World')
    p3 = manager.create('slash box')
    p3.use('Hello, World')
