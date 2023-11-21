from abc import ABC, abstractmethod


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

    def menu(self):
        """Print full menu, return chosen option"""
        text = self.text
        options = self.options
        print(text)
        for k, v in options.items():
            print(f"{k}: {v}")
        choice, args = self.input_integer_with_args(options.keys())
        return choice, args

    def msg(self, text):
        """Print text"""
        print(text)

    def error(self, text):
        """Print text"""
        print(text)

    def input_integer(self, validator = None, prompt = ''):
        """Get input and tries to cast it to integer in validator"""
        print(prompt)
        while True:
            try:
                data = int(input())
                if (not validator) or (data in validator):
                    return data
                raise ValueError
            except ValueError:
                continue

    def input_integer_with_args(self, validator = None, prompt = ''):
        """Get input, split, cast first element to integer"""
        print(prompt)
        while True:
            data = input().split()
            args = []
            try:
                choice = int(data[0])
                if len(data) > 1:
                    args = data[1:]
                if (not validator) or (choice in validator):
                    return choice, args
            except ValueError:
                continue

    def input(self, prompt = ''):
        """Get arbitrary input"""
        print(prompt)
        return input()
