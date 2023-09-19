from grid import Grid

class Match:
    def __init__(self, player1, player2, h, w, ui):
        self.__ui = ui
        self.__players = (player1, player2)
        self.__grids = (Grid(h,w), Grid(h,w))
        self.__current_player = 0
        self.__game_finished = False

    @property
    def players(self):
        return self.__players
    
    @property
    def grids(self):
        return self.__grids
    
    def turn(self):
        # runs one turn of the game (single move + move feedback)
        attacker = self.__current_player
        defender = 1 if attacker == 0 else 0
        self.__ui.render_grid()
        coords = self.players[attacker].get_input(self.__ui)
        hit, valid = self.grids[defender].check_hit(coords,self.__ui)
        if not valid:
            self.__ui.invalid_move()
            return
        if not hit:
            self.__ui.miss()
            self.__current_player = defender
            return
        elif self.grids[defender].check_defeat():
            self.__ui.game_ended(self.players[attacker])
            self.__game_finished = True
            return
        self.__ui.hit()
        return
        
        

    def game_loop(self):
        while not self.__game_finished:
            self.turn()