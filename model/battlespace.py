import copy
from model.ship import Ship
#from exception.invalidCoordinateException import InvalidCoordinateException


class Battlespace:
    """Class modelling state of a players grid"""
    def __init__(self,
                 h: int,
                 w: int,
                 ships: list[Ship]):
        self.__ships = copy.deepcopy(ships)
        self.__grid = [[ 0 for i in range(0, w) ] for j in range(0, h)]
        self.__fog_of_war = [[ 0 for i in range(0, w) ] for j in range(0, h)]

    @property
    def ships(self):
        """List of all ships used in game"""
        return self.__ships

    @property
    def grid(self):
        """Grid with ship positions"""
        return self.__grid

    @property
    def fog_of_war(self):
        """Mask of played moves"""
        return self.__fog_of_war

    def check_hit(self, x: int, y: int):
        """Try to play a move and modify state of game accordingly"""
        is_hit = False
        is_valid = True
        if self.fog_of_war[x][y] == 1:
            # the move has already been played
            is_valid = False
            return is_hit, is_valid
        for ship in self.ships:
            if ship.check_hit(x, y):
                is_hit = True
                return is_hit, is_valid
        return is_hit, is_valid

    def check_defeat(self):
        """Check if all ships have been sunk"""
        for ship in self.ships:
            if not ship.is_sunk():
                return False
        return True

    def place_ship(self, x, y, o):
        """Try to place a ship at coord"""
