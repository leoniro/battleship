from game import Game
from playerControl import PlayerControl

class GameControl:
    def __init__(self):
        self.__player_control = PlayerControl()
        self.__game_history = None

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
                # new player
                pass
            case 1:
                # start game
                pass
