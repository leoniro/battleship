from model.player import Player


class ComputerPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def play_move(self, grid, game_view):
        pass
    
    def place_ship(self, game_view):
        pass
