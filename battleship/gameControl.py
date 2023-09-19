from match import Match
from userInterface import UserInterface
from gameLog import GameLog
from player import Player

class GameControl:
    def __init__(self):
        self.__player_list = []
        self.__match = None
        self.__ui = UserInterface()

    @property
    def match(self):
        return self.__match
    
    @match.setter
    def match(self, match):
        self.__match = match

    @property
    def ui(self):
        return self.__ui

    @property
    def player_list(self):
        return self.__player_list

    def start(self):
        match self.ui.start_screen():
            case 0:
                new_player = self.ui.add_new_player()
                self.player_list.append(Player(new_player))
            case 1:
                player1, player2 = self.ui.choose_players(self.__player_list)
                h, w = self.ui.input_grid_size()
                self.match = Match(player1, player2, h, w, self.ui)
                self.match.players[0].place_ships(self.match.grids[0])
                self.match.players[1].place_ships(self.match.grids[1])
                self.match.game_loop()
    
    
            
                





