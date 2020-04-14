import sys
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

    def construct(self):
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


class HTMLBuilder(Builder):
    def __init__(self, filename):
        self.filename = filename

    def make_title(self, title):
        with open(self.filename, mode='w') as f:
            f.writelines(
                '<html><head><title>{title}</title></head><body>'.format(title=title))
            f.writelines('<h1>{title}</h1>'.format(title=title))

    def make_string(self, string):
        with open(self.filename, mode='a') as f:
            f.writelines('<p>{string}</p>'.format(string=string))

    def make_items(self, items):
        with open(self.filename, mode='a') as f:
            f.writelines('<ul>')
            for item in items:
                f.writelines('<li>{item}</li>'.format(item=item))
            f.writelines('</ul>')

    def close(self):
        with open(self.filename, mode='a') as f:
            f.writelines('</body><html>')

    def get_result(self):
        return self.filename


def usage():
    print('Usage: python main.py plain -> プレーンテキスト')
    print('Usage: python main.py html  -> HTMLファイル')


if __name__ == '__main__':
    args = sys.argv
    if len(args) != 2:
        usage()
        sys.exit()
    if args[1] == 'plain':
        builder = TextBuilder()
        director = Director(builder)
        director.construct()
        result = builder.get_result()
        print(result, end='')
    elif args[1] == 'html':
        builder = HTMLBuilder('output.html')
        director = Director(builder)
        director.construct()
        filename = builder.get_result()
        print('{filename} を生成しました'.format(filename=filename))
