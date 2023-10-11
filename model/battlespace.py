import copy


class Battlespace:
    def __init__(self, h, w, ships):
        self.__ships = copy.deepcopy(ships)
        self.__grid = [[ 0 for i in range(0, w) ] for j in range(0, h)]
        self.__fog_of_war = [[ 0 for i in range(0, w) ] for j in range(0, h)]

    @property
    def ships(self):
        return self.__ships

    @property
    def grid(self):
        return self.__grid

    @property
    def fog_of_war(self):
        return self.__fog_of_war

    def check_hit(self, coord):
        is_hit = False
        is_valid = True
        for ship in self.ships:
            is_hit, is_valid = ship.check_hit(coord)


    def check_defeat(self):
        pass