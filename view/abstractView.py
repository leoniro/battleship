from abc import ABC, abstractmethod
from exception.invalidInputException import InvalidInputException

class AbstractView(ABC):
    """Base abstract class for View implementation"""
    @abstractmethod
    def __init__(self):
        self.__text = ""
        self.__options = {}

    @property
    def text(self):
        """Top menu description"""
        return self.__text

    @property
    def options(self):
        """Dictionary with menu options"""
        return self.__options

    def menu(self, text: str, options: dict[int, str]):
        """Print full menu"""
        print(text)
        for k in options:
            print(f"{k}: {options[k]}")

    def msg(self, text: str):
        """Print text"""
        print(text)

    def input_integer(self, validator = None):
        """Get input and tries to cast it to integer in validator"""
        try:
            data = input()
            data = int(data)
            if (not validator) or (data in validator):
                return data
            raise InvalidInputException()
        except:
            raise InvalidInputException()

    def input(self):
        """Get arbitrary input"""
        return input()
