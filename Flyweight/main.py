import sys


class BigChar:
    def __init__(self, charname):
        self.charname = charname
        try:
            with open('data/big{charname}.txt'.format(charname=self.charname), mode='r') as f:
                self.fontdata = f.read()
        except FileNotFoundError:
            self.fontdata = charname + '?'

    def print(self):
        print(self.fontdata)


class BigCharFactory:
    singleton = None

    def __new__(cls):
        if cls.singleton is None:
            cls.singleton = super().__new__(cls)
        return cls.singleton

    def __init__(self):
        self.pool = {}

    def get_big_char(self, charname):
        bc = self.pool.get(charname)
        if not bc:
            bc = BigChar(charname)
            self.pool[charname] = bc
        return bc


class BigString:
    def __init__(self, string):
        self.bigchars = []
        factory = BigCharFactory()
        for char in string:
            self.bigchars.append(factory.get_big_char(char))

    def print(self):
        for char in self.bigchars:
            char.print()


if __name__ == '__main__':
    args = sys.argv
    if len(args) == 1:
        print('Usage: python main.py digits')
        print('Example: python main.py 1212123')
        sys.exit()

    bs = BigString(args[1])
    bs.print()
