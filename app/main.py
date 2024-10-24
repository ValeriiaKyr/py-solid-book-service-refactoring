from app.display import Display
from app.print import PrintConsole, PrintReverse
from app.serialize import Serialize


class Book:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            Display.display_type(book, method_type)
        elif cmd == "print":
            if method_type == "console":
                printer = PrintConsole()
                printer.print_type(book)
            elif method_type == "reverse":
                printer = PrintReverse()
                printer.print_type(book)
            else:
                raise ValueError(f"Unknown print type: {method_type}")
        elif cmd == "serialize":
            return Serialize.serialize(book, method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
