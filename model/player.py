from abc import ABC, abstractmethod


class Player(ABC):
    @abstractmethod
    def __init__(self, name):
        self.__name = name
        self.__score = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        self.__score += score

    @abstractmethod
    def play_move(self, grid, game_view):
        pass

    @abstractmethod
    def place_ship(self, game_view):
        pass
