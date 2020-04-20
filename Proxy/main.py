from abc import ABCMeta, abstractmethod
from time import sleep


class Printable:
    @abstractmethod
    def set_printer_name(self, name):
        pass

    @abstractmethod
    def get_printer_name(self):
        pass

    @abstractmethod
    def print(self, string):
        pass


class Printer(Printable):
    def __init__(self, name=None):
        if not name:
            self.heavy_job('Printerのインスタンスを生成中')
        else:
            self.name = name
            self.heavy_job('Printerのインスタンス({name})を生成中'.format(name=name))

    def set_printer_name(self, name):
        self.name = name

    def get_printer_name(self):
        return self.name

    def print(self, string):
        print('==={name}==='.format(name=self.name))
        print(string)

    def heavy_job(self, msg):
        print(msg, end='')
        for _ in range(5):
            print('.', end='')
            sleep(0.5)
        print('完了。')


class PrinterProxy(Printable):
    def __init__(self, name=None):
        if name:
            self.name = name
        self.real = None

    def set_printer_name(self, name):
        if self.real:
            self.real.set_printer_name(name)
        self.name = name

    def get_printer_name(self):
        return self.name

    def print(self, string):
        self.realize()
        self.real.print(string)

    def realize(self):
        if not self.real:
            self.real = Printer(self.name)


if __name__ == '__main__':
    p = PrinterProxy('Alice')
    print('名前は現在{name}です。'.format(name=p.get_printer_name()))
    p.set_printer_name('Bob')
    print('名前は現在{name}です。'.format(name=p.get_printer_name()))
    p.print('Hello, world.')
