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
        self.__grid = [[ ' ' for i in range(0, w) ] for j in range(0, h)]
        self.__fog_of_war = [[ True for i in range(0, w) ] for j in range(0, h)]

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
        if self.fog_of_war[x][y] is False:
            # the move has already been played
            raise Exception
        self.fog_of_war[x][y] = False
        for ship in self.ships:
            if ship.check_hit(x, y):
                return True
        return False

    def check_defeat(self):
        """Check if all ships have been sunk"""
        for ship in self.ships:
            if not ship.sunk:
                return False
        return True

    def place_ship(self, ship: Ship, x: int, y: int, o: int):
        """Try to place a ship at coord"""
        grid = self.grid
        if o == 0:
            #horizontal
            for i in range(ship.length()):
                if y + i > len(grid[0]):
                    raise Exception
                if grid[x][y + i] != ' ':
                    raise Exception
            ship.position = (x, y)
            ship.orientation = 0
            for i in range(ship.length()):
                grid[x][y + i] = 'o'
        elif o == 1:
            #vertical
            for i in range(ship.length()):
                if x + i > len(grid):
                    raise Exception
                if grid[x + i][y] != ' ':
                    raise Exception
            ship.position = (x, y)
            ship.orientation = 1
            for i in range(ship.length()):
                grid[x + i][y] = 'o'
