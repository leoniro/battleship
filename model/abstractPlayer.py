import datetime
from abc import ABC, abstractmethod
from ctrl.gameCtrl import GameCtrl


class AbstractPlayer(ABC):
    """Base abstract class for Player implementation"""
    def __init__(self, name: str, dob: datetime):
        self.__name = name
        self.__score = 0
        self.__date_of_birth = dob

    @property
    def name(self):
        """Get name"""
        return self.__name

    @name.setter
    def name(self, name):
        """Set new name"""
        self.__name = name

    @property
    def score(self):
        """Get score"""
        return self.__score

    @property
    def date_of_birth(self):
        """Get date of birth"""
        return self.__date_of_birth

    def add_score(self, score):
        """Add to current score"""
        self.__score += score

    @abstractmethod
    def play_move(self, grid: list[list[str]], game_ctrl: GameCtrl):
        """Returns coordinates of the move to be played"""

    @abstractmethod
    def place_ship(self, grid: list[list[str]], game_ctrl: GameCtrl):
        """Returns coordinates and orientation of ship to be places"""
