from ctrl.playerCtrl import PlayerCtrl
from ctrl.shipCtrl import ShipCtrl
from view.gameView import GameView


class GameCtrl:
    def __init__(self):
        self.__player_ctrl = PlayerCtrl()
        self.__ship_ctrl = ShipCtrl()
        self.__game_view = GameView()
        self.__game_history = []

    @property
    def player_ctrl(self):
        return self.__player_ctrl

    @property
    def ship_ctrl(self):
        return self.__ship_ctrl

    @property
    def game_view(self):
        return self.__game_view

    @property
    def game_history(self):
        return self.__game_history

    def new_game(self):
        # get players
        # get board size
        # create game
        # place ships
        # call turn
        pass

    def manage_player(self):
        pass

    def manage_ships(self):
        pass

    def player_ranking(self):
        pass

    def previous_games(self):
        pass