from abc import ABC, abstractmethod
from model.battlespace import Battlespace
from ctrl.gameCtrl import GameCtrl

class AbstractPlayer(ABC):
    @abstractmethod
    def __init__(self, name: str):
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
    def play_move(self, grid: list[list[int]], game_ctrl: GameCtrl):
        pass

    @abstractmethod
    def place_ship(self, battlespace: Battlespace, game_ctrl: GameCtrl):
        pass
