from model.player import Player


class HumanPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def play_move(self, grid, game_ctrl):
        pass
    
    def place_ship(self, game_ctrl):
        pass
