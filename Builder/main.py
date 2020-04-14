from abc import ABCMeta, abstractmethod


class Builder(metaclass=ABCMeta):
    @abstractmethod
    def make_title(self, title):
        pass

    @abstractmethod
    def make_string(self, string):
        pass

    @abstractmethod
    def make_items(self, items):
        pass

    @abstractmethod
    def close(self):
        pass


class Director:
    def __init__(self, builder):
        self.builder = builder

    def contruct(self):
        self.builder.make_title('Greeding')
        self.builder.make_string('朝から昼にかけて')
        self.builder.make_items(['おはようございます。',
                                 'こんにちは。'])
        self.builder.make_string('夜に')
        self.builder.make_items(['こんばんは。',
                                 'おやすみなさい。',
                                 'さようなら。'])
        self.builder.close()


class TextBuilder(Builder):
    def __init__(self):
        self.buffer = []
        self.line = '========================\n'

    def make_title(self, title):
        self.buffer.append(self.line)
        self.buffer.append('「{title}」\n'.format(title=title))
        self.buffer.append('\n')

    def make_string(self, string):
        self.buffer.append('■ {string}\n'.format(string=string))
        self.buffer.append('\n')

    def make_items(self, items):
        for item in items:
            self.buffer.append(' ・{item}\n'.format(item=item))
        self.buffer.append('\n')

    def close(self):
        self.buffer.append(self.line)

    def get_result(self):
        return "".join(self.buffer)


if __name__ == '__main__':
    builder = TextBuilder()
    director = Director(builder)
    director.contruct()
    result = builder.get_result()
    print(result, end='')
