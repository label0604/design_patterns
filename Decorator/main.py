from abc import ABCMeta, abstractmethod
from typing import final
from unicodedata import east_asian_width


class Display(metaclass=ABCMeta):
    @abstractmethod
    def get_columns(self):
        pass

    @abstractmethod
    def get_rows(self):
        pass

    @abstractmethod
    def get_row_text(self, row):
        pass

    @final
    def show(self):
        rows = self.get_rows()
        for row in range(rows):
            print(self.get_row_text(row))


class StringDisplay(Display):
    def __init__(self, string):
        self.string = string

    def get_columns(self):
        return self._count_length(self.string)

    def get_rows(self):
        return 1

    def get_row_text(self, row):
        if row == 0:
            return self.string
        else:
            return None

    def _count_length(self, string):
        count = 0
        for c in string:
            if east_asian_width(c) in 'FWA':
                count += 2
            else:
                count += 1
        return count


class Border(Display):
    def __init__(self, display):
        self.display = display


class SideBorder(Border):
    def __init__(self, display, ch):
        super().__init__(display)
        self.border_char = ch

    def get_columns(self):
        return 1 + self.display.get_columns() + 1

    def get_rows(self):
        return self.display.get_rows()

    def get_row_text(self, row):
        return self.border_char + self.display.get_row_text(row) + self.border_char


class FullBorder(Border):
    def __init__(self, display):
        super().__init__(display)

    def get_columns(self):
        return 1 + self.display.get_columns() + 1

    def get_rows(self):
        return 1 + self.display.get_rows() + 1

    def get_row_text(self, row):
        if row == 0:
            return '+{line}+'.format(line=self._make_line('-', self.display.get_columns()))
        elif row == self.display.get_rows() + 1:
            return '+{line}+'.format(line=self._make_line('-', self.display.get_columns()))
        else:
            return '|{line}|'.format(line=self.display.get_row_text(row - 1))

    def _make_line(self, ch, count):
        buf = []
        for _ in range(count):
            buf.append(ch)
        return ''.join(buf)


if __name__ == '__main__':
    b1 = StringDisplay('Hello, world.')
    b2 = SideBorder(b1, '#')
    b3 = FullBorder(b2)
    b1.show()
    b2.show()
    b3.show()

    b4 = SideBorder(
        FullBorder(
            FullBorder(
                SideBorder(
                    FullBorder(
                        StringDisplay('こんにちは。')
                    ), '*'
                )
            )
        ), '/'
    )
    b4.show()
