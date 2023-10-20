import random
from model.abstractPlayer import AbstractPlayer
from ctrl.gameCtrl import GameCtrl


class BetterComputerPlayer(AbstractPlayer):
    """Class represeting computer that plays as well as me"""
    def play_move(self, grid, game_ctrl):
        for i, row in enumerate(grid):
            for j in range(len(row) - 1):
                if row[j] == '~' and row[j+1] == 'o':
                    return (i, j)
                if row[j] == 'o' and row[j+1] == '~':
                    return (i, j+1)
        for j in range(len(grid[0])):
            for i in range(len(grid) -1 ):
                if grid[i][j] == '~' and grid[i+1][j] == 'o':
                    return (i, j)
                if grid[i][j] == 'o' and grid[i+1][j] == '~':
                    return (i+1, j)
        while True:
            x = random.randint(0, len(grid)-1)
            y = random.randint(0, len(grid[0])-1)
            if grid[x][y] == '~':
                return x, y

    def place_ship(self, grid, game_ctrl):
        x = random.randint(0, len(grid)-1)
        y = random.randint(0, len(grid[0])-1)
        o = random.randint(0, 1)
        return x, y, o
