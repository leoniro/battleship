from enum import Enum


class Ship:
    def __init__(self, length):
        self.__type = ShipType(length)
        self.__orientation = None
        self.__position = (None, None)
        self.__sunk = False
        self.__hits = [False for _ in range(length)]

    @property
    def type(self):
        return self.__type

    @property
    def sunk(self):
        return self.__sunk

    @property
    def hits(self):
        return self.__hits
    
    def length(self):
        return self.__type.value

    def check_hit(self, x, y):
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
        for h in self.hits:
            if h == False:
                return False
        self.__sunk = True
        return True

class ShipType(Enum):
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
