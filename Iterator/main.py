from interface import Aggregate, Iterator


class BookShelf(Aggregate):
    def __init__(self):
        self.__books = []
        self.__last = 0

    def __iter__(self):
        return BookShelfIterator(self)

    def get_book_at(self, index):
        return self.__books[index]

    def append_books(self, name):
        self.__books.append(Book(name))
        self.__last += 1

    def get_length(self):
        return self.__last


class Book:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


class BookShelfIterator(Iterator):
    def __init__(self, book_shelf):
        self.book_shelf = book_shelf
        self.index = 0

    def _has_next(self):
        if self.index < self.book_shelf.get_length():
            return True
        else:
            return False

    def __next__(self):
        if self._has_next():
            book = self.book_shelf.get_book_at(self.index)
            self.index += 1
            return book
        else:
            raise StopIteration()


if __name__ == "__main__":

    # Initialize
    book_shelf = BookShelf()
    books = [
        'Around the World in 80 Days',
        'Bible',
        'Cinderella',
        'Daddy-Long-Legs',
    ]
    for book in books:
        book_shelf.append_books(book)

    # Use Iterator
    for book in book_shelf:
        print(book.get_name())
