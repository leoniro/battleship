from enum import Enum


class Ship:
    """Class representing a single ship"""
    def __init__(self, length):
        self.__type = ShipType(length)
        self.__orientation = None
        self.__position = (None, None)
        self.__sunk = False
        self.__hits = [False for _ in range(length)]

    @property
    def type(self):
        """Type of ship"""
        return self.__type

    @property
    def sunk(self):
        """True if ship has been sunk"""
        return self.__sunk

    @property
    def hits(self):
        """Vector tracking ship damage"""
        return self.__hits

    @property
    def position(self):
        """Ship position in grid (top left)"""
        return self.__position

    @position.setter
    def position(self, pos):
        self.__position = pos

    @property
    def orientation(self):
        """Ship orientation in grid (0: horizontal, 1: vertical)"""
        return self.__orientation

    @orientation.setter
    def orientation(self, o):
        self.__orientation = o

    def length(self):
        """Ship length in grid"""
        return self.__type.value

    def check_hit(self, x, y):
        """Checks if a move has hit the ship and modifies it accordingly"""
        for i in range(self.length()):
            if self.__orientation == 0:
                if (x, y) == (self.__position[0], self.__position[1] + i):
                    self.hits[i] = True
                    self.check_sunk()
                    return True
            else:
                if (x, y) == (self.__position[0] + i, self.__position[1]):
                    self.hits[i] = True
                    self.check_sunk()
                    return True
        return False

    def check_sunk(self):
        """check if all squares this ship is on have been hit"""
        for h in self.hits:
            if h is False:
                return False
        self.__sunk = True
        return True

class ShipType(Enum):
    """Class representing types of ships"""
    BOAT = 1
    SUBMARINE = 2
    FRIGATE = 3
    CARRIER = 4

    def __str__(self):
        if self.value == 1:
            return "Bote"
        if self.value == 2:
            return "Submarino"
        if self.value == 3:
            return "Fragata"
        if self.value == 4:
            return "Porta-aviões"
        return "Desconhecido"
