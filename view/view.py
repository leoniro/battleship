from abc import ABC, abstractmethod


class View(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def menu(self, text, options):
        pass

    @abstractmethod
    def msg(self, text):
        pass

    @abstractmethod
    def get_input(self, validator):
        pass
