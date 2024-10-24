from abc import ABC, abstractmethod


class PrintBook(ABC):
    @abstractmethod
    def print_type(self, book): ...


class PrintConsole(PrintBook):
    def print_type(self, book):
        print(f"Printing the book: {book.title}...")
        print(book.content)


class PrintReverse(PrintBook):
    def print_type(self, book):
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
