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

    def start(self):
        # main menu
        text = self.game_view.text
        options = self.game_view.options
        while True:
            self.game_view.menu(text, options)
            try:
                choice = self.game_view.get_input(options)
            except:
                self.game_view.msg("Opção inválida. Tente novamente\n")
                continue
            if choice == 0:
                print(choice)
                return
            elif choice == 1:
                self.new_game()
            elif choice == 2:
                self.player_ctrl.start()
            elif choice == 3:
                self.ship_ctrl.start()
            elif choice == 4:
                self.player_ranking()
            elif choice == 5:
                self.previous_games()

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