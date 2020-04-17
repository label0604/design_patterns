from abc import ABCMeta, abstractmethod


class Visitor(metaclass=ABCMeta):
    @abstractmethod
    def visit(self, element):
        pass


class Element(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class Entry(Element):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_size(self):
        pass

    def add(self):
        raise FileTreatmentError

    def __iter__(self):
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

    def accept(self, visitor):
        visitor.visit(self)


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

    def accept(self, visitor):
        visitor.visit(self)

    def __iter__(self):
        return self.directory.__iter__()


class ListVisitor(Visitor):
    def __init__(self):
        self.currentdir = ''

    def visit(self, element):
        if isinstance(element, File):
            print('{dir}/{element}'.format(dir=self.currentdir, element=element))
        elif isinstance(element, Directory):
            print('{dir}/{element}'.format(dir=self.currentdir, element=element))
            savedir = self.currentdir
            self.currentdir = '{dir}/{element}'.format(
                dir=self.currentdir, element=element.get_name())
            for entry in element:
                entry.accept(self)
            self.currentdir = savedir


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
        # Visit
        rootdir.accept(ListVisitor())

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
        # Visit
        rootdir.accept(ListVisitor())
    except FileTreatmentError as e:
        print(e)
