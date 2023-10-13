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

    def get_input(self, validator: dict[int, str] = None):
        if validator == None:
            return input()
        else:
            try:
                data = input()
                data = int(data)
                if data in validator.keys():
                    return data
            except:
                return None
            raise InvalidInputException()
                
