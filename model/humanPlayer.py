from model.abstractPlayer import AbstractPlayer
from ctrl.gameCtrl import GameCtrl
from exception.invalidCoordinateException import InvalidCoordinateException

class HumanPlayer(AbstractPlayer):
    """Class representing human player"""
    def play_move(self, grid, game_ctrl):
        coord = game_ctrl.game_view.input().lower()
        try:
            x, y = self.coord2idx(coord)
            if x < 0 or x >= len(grid):
                raise InvalidCoordinateException
            if y < 0 or y >= len(grid[0]):
                raise InvalidCoordinateException
            return x, y
        except Exception as exc:
            raise InvalidCoordinateException from exc

    def place_ship(self, grid, game_ctrl):
        coord = game_ctrl.game_view.input().lower().split()
        try:
            o = int(coord.pop())
            if o != 0 and o != 1:
                raise InvalidCoordinateException
            coord = ' '.join(coord)
            x, y = self.coord2idx(coord)
            if x < 0 or x >= len(grid):
                raise InvalidCoordinateException
            if y < 0 or y >= len(grid[0]):
                raise InvalidCoordinateException
            return x, y, o
        except Exception as exc:
            raise InvalidCoordinateException from exc

    def coord2idx(self, coord):
        """Convert string coordinate to integer pair. No inbounds check"""
        try:
            x, y = coord.lower().split()
            x = int(x) - 1
            y = ord(y) - 97
            return x, y
        except (TypeError, ValueError) as exc:
            raise InvalidCoordinateException from exc
