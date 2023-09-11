from grid import Grid

class Match:
    def __init__(self, player_list, ui):
        self.__ui = ui
        self.__player_list = player_list
        self.__players = (None, None)
        self.__grids = (None, None)
        self.__current_player = 0
        self.__game_finished = False
    
    def turn(self):
        # runs one turn of the game (single move + move feedback)
        attacker = self.__current_player
        defender = 1 if attacker == 0 else 0
        coords = self.__players[attacker].get_input(self.__ui)
        hit = self.__grids[defender].check_hit(coords,self.__ui)
        if not hit:
            self.__current_player = defender
        else:
            if self.__grids[defender].check_defeat():
                self.__game_finished = True

    def main_loop(self):
        self.__players = self.__ui.choose_players(self.__player_list)
        h, w = self.__ui.input_grid_size()
        self.__grids = (Grid(h,w), Grid(h,w))
        self.__grids[0].place_ships(self.__ui)
        self.__grids[1].place_ships(self.__ui)
        while not self.__game_finished:
            self.turn()
            