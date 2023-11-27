from ctrl.shipCtrl import ShipCtrl
from view.gameView import GameView
from exception.invalidCoordinateException import InvalidCoordinateException
from exception.uiCancelException import UICancelException
from dao.dao import DAO

class GameCtrl(DAO):
    """Game controller class"""
    def __init__(self):
        from ctrl.playerCtrl import PlayerCtrl

        super().__init__('game.pkl')

        self.__player_ctrl = PlayerCtrl()
        self.__ship_ctrl = ShipCtrl()
        self.__game_view = GameView()
        self.__game_history = super().get()

    @property
    def player_ctrl(self):
        """Returns player controller"""
        return self.__player_ctrl

    @property
    def ship_ctrl(self):
        """Returns ship controller"""
        return self.__ship_ctrl

    @property
    def game_view(self):
        """Returns game view"""
        return self.__game_view

    @property
    def game_history(self):
        """Returns list of played games"""
        return self.__game_history

    def start(self):
        """Prints main menu and dispatches accordingly"""
        while True:
            try:
                choice = self.game_view.menu()
            except UICancelException:
                return
            if choice == 0:
                return
            if choice == 1:
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
        """Set up a new game and start it"""
        from model.game import Game
        from model.humanPlayer import HumanPlayer

        # create new game
        player_list = [ p.name for p in self.player_ctrl.players ]
        try:
            p1 = self.game_view.multiple_choices("Escolha o primeiro jogador:", player_list)
            player_list.remove(p1)
            p2 = self.game_view.multiple_choices("Escolha o segundo jogador:", player_list)
            p1 = [p for p in self.player_ctrl.players if p.name == p1][0]
            p2 = [p for p in self.player_ctrl.players if p.name == p2][0]
            h = self.game_view.spinbox("Altura do tabuleiro:", range(10,21))
            w = self.game_view.spinbox("Largura do tabuleiro:", range(10,21))
        except UICancelException:
            return
        game = Game(self, h, w, p1, p2, self.ship_ctrl.ships)

        # place ships:
        for player_idx in range(2):
            player_name = game.players[player_idx].name
            for ship in game.battlespaces[player_idx].ships:
                grid = game.battlespaces[player_idx].grid
                if isinstance(game.players[player_idx], HumanPlayer):
                    while True:
                        try:
                            x, y, o = self.game_view.place_ship_menu(
                                player_name, grid, ship.length())
                            game.battlespaces[player_idx].place_ship(ship, x, y, o)
                            break
                        except InvalidCoordinateException:
                            self.game_view.error("Posição inválida. Tente novamente")
                            continue
                        except UICancelException:
                            return
                else:
                    while True:
                        try:
                            x, y, o = game.players[player_idx].place_ship(grid, self)
                            game.battlespaces[player_idx].place_ship(ship, x, y, o)
                            break
                        except InvalidCoordinateException:
                            continue
        try:
            winner = game.main_loop(0)
        except UICancelException:
            return

        if winner == 0:
            self.game_view.msg(f"{p1.name} venceu")
        else:
            self.game_view.msg(f"{p2.name} venceu")

        self.add_game(game)

    def add_game(self, game):
        super().add(game)

    def player_ranking(self):
        """List all registered players according to their score"""
        self.player_ctrl.list("", ranked = True)

    def previous_games(self):
        """List previously played games"""
        from model.game import Game

        player_names = [p.name for p in self.player_ctrl.players]
        try:
            name = self.game_view.multiple_choices("Selecione o jogador de interesse:", player_names)
        except UICancelException:
            name = None
        games_description = {}
        for idx, game in enumerate(self.game_history):
            if (name is not None) and name not in [p.name for p in game.players]:
                continue
            current_game = (f"Jogo {idx}:\n"
                            f"Início: {game.start_time.strftime('%d/%m/%Y %H:%M:%S')}\n"
                            f"Fim: {game.end_time.strftime('%d/%m/%Y %H:%M:%S')}\n\n"
                            f"Jogador 1: {game.players[0].name}\n"
                            f"Pontuação: {game.scores[0]}\n\n"
                            f"Jogador 2: {game.players[1].name}\n"
                            f"Pontuação: {game.scores[1]}\n\n")
            games_description[idx] = current_game
        self.game_view.game_description_menu(games_description)
