from abc import ABC, abstractmethod
from exception.invalidInputException import InvalidInputException

class AbstractView(ABC):
    @abstractmethod
    def __init__(self):
        pass

    def menu(self, text: str, options: dict[int, str]):
        print(text)
        for k in options:
            print(f"{k}: {options[k]}")

    def msg(self, text: str):
        print(text)

    def input_integer(self, validator = None):
        try:
            data = input()
            data = int(data)
            if validator == None:
                return data
            elif data in validator:
                return data
        except:
            return None
        raise InvalidInputException()

    def input(self):
        return input()
