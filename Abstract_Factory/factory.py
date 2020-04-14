from abc import ABCMeta, abstractmethod


class Item(metaclass=ABCMeta):
    def __init__(self, caption):
        self.caption = caption

    @abstractmethod
    def make_html(self):
        pass


class Link(Item):
    def __init__(self, caption, url):
        super().__init__(caption)
        self.url = url


class Tray(Item):
    def __init__(self, caption):
        super().__init__(caption)
        self.tray = []

    def add(self, item):
        self.tray.append(item)


class Page(metaclass=ABCMeta):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.content = []

    def add(self, item):
        self.content.append(item)

    def output(self):
        filename = '{title}.html'.format(title=self.title)
        with open(filename, mode='w', encoding='utf-8') as f:
            f.write(self.make_html())
        print('{filename} を生成しました'.format(filename=filename))

    @abstractmethod
    def make_html(self):
        pass


class Factory(metaclass=ABCMeta):
    @classmethod
    def get_factory(cls, classname):
        import listfactory
        return eval(classname)()

    @abstractmethod
    def create_link(self, caption, url):
        pass

    @abstractmethod
    def create_tray(self, caption):
        pass

    @abstractmethod
    def create_page(self, title, author):
        pass
