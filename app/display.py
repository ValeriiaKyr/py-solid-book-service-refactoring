from typing import Any


class DisplayConsole:
    @staticmethod
    def display_type(book: Any) -> None:
        print(book.content)


class DisplayReverse:
    @staticmethod
    def display_type(book: Any) -> None:
        print(book.content[::-1])


class Display:
    @staticmethod
    def display_type(book: Any, display_type: str) -> None:
        if display_type == "console":
            DisplayConsole.display_type(book)
        elif display_type == "reverse":
            DisplayReverse.display_type(book)
        else:
            raise ValueError(f"Unknown display type: {display_type}")
