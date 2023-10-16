import random
from model.abstractPlayer import AbstractPlayer
from ctrl.gameCtrl import GameCtrl


class ComputerPlayer(AbstractPlayer):
    """Class represeting computer player"""
    def play_move(self, grid: list[list[str]], game_ctrl):
        x = random.randint(0, len(grid)-1)
        y = random.randint(0, len(grid[0])-1)
        return x, y

    def place_ship(self, grid: list[list[str]], game_ctrl):
        x = random.randint(0, len(grid)-1)
        y = random.randint(0, len(grid[0])-1)
        o = random.randint(0, 1)
        return x, y, o
