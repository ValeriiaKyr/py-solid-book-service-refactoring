class DisplayConsole:
    @staticmethod
    def display_type(book):
        print(book.content)


class DisplayReverse:
    @staticmethod
    def display_type(book):
        print(book.content[::-1])


class Display:
    @staticmethod
    def display_type(book, display_type: str) -> None:
        if display_type == "console":
            return DisplayConsole.display_type(book)
        elif display_type == "reverse":
            return DisplayReverse.display_type(book)
        else:
            raise ValueError(f"Unknown display type: {display_type}")
