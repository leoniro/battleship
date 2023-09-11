from match import Match
from userInterface import UserInterface
from gameLog import GameLog

class GameControl:
    def __init__(self):
        self.__players = []
        self.__match = None
        self.__ui = UserInterface()

    def start(self):
        match self.__ui.start_screen():
            case 0:
                new_player = self.__ui.add_new_player()
                self.__players.append(new_player)
            case 1:
                self.__match = Match(self.__players, self.__ui)
                self.__match.main_loop()
                





