from abc import ABCMeta, abstractmethod


class Entry(metaclass=ABCMeta):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_size(self):
        pass

    def print_list(self):
        self._print_list()

    @abstractmethod
    def _print_list(self, prefix=''):
        pass

    def add(self, entry):
        raise FileTreatmentError

    def __str__(self):
        return '{name} ({size})'.format(name=self.get_name(), size=self.get_size())


class File(Entry):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_name(self):
        return self.name

    def get_size(self):
        return self.size

    def _print_list(self, prefix=""):
        print('{prefix}/{name}'.format(prefix=prefix, name=self))


class Directory(Entry):
    def __init__(self, name):
        self.name = name
        self.directory = []

    def get_name(self):
        return self.name

    def get_size(self):
        size = 0
        for entry in self.directory:
            size += entry.get_size()
        return size

    def add(self, entry):
        self.directory.append(entry)
        return self

    def _print_list(self, prefix=''):
        print('{prefix}/{name}'.format(prefix=prefix, name=self))
        for entry in self.directory:
            entry._print_list(
                '{prefix}/{name}'.format(prefix=prefix, name=self.name))


class FileTreatmentError(Exception):
    pass


if __name__ == '__main__':
    try:
        print('Making root entries...')
        rootdir = Directory('root')
        bindir = Directory('bin')
        tmpdir = Directory('tmp')
        usrdir = Directory('usr')
        rootdir.add(bindir)
        rootdir.add(tmpdir)
        rootdir.add(usrdir)
        bindir.add(File('vi', 10000))
        bindir.add(File('latex', 20000))
        rootdir.print_list()

        print()
        print('Making user entries')
        yuki = Directory('yuki')
        hanako = Directory('hanako')
        tomura = Directory('tomura')
        usrdir.add(yuki)
        usrdir.add(hanako)
        usrdir.add(tomura)
        yuki.add(File('diary.html', 100))
        yuki.add(File('Composite.java', 200))
        hanako.add(File('memo.tex', 300))
        tomura.add(File('game.doc', 400))
        tomura.add(File('junk.mail', 500))
        rootdir.print_list()
    except FileTreatmentError as e:
        print(e)
