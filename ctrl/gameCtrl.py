from ctrl.shipCtrl import ShipCtrl
from view.gameView import GameView
from exception.invalidCoordinateException import InvalidCoordinateException
from exception.uiCancelException import UICancelException


class GameCtrl:
    """Game controller class"""
    def __init__(self):
        from ctrl.playerCtrl import PlayerCtrl

        self.__player_ctrl = PlayerCtrl()
        self.__ship_ctrl = ShipCtrl()
        self.__game_view = GameView()
        self.__game_history = []

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
            choice = self.game_view.menu()
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
        self.game_history.append(game)

        # place ships:
        for player_idx in range(2):
            player_name = game.players[player_idx].name
            for ship in game.battlespaces[player_idx].ships:
                grid = game.battlespaces[player_idx].grid
                if isinstance(game.players[player_idx], HumanPlayer):
                    x, y, o = self.game_view.place_ship_menu(
                        player_name, grid, ship.length())
                    game.battlespaces[player_idx].place_ship(ship, x, y, o)
                else:
                    while True:
                        try:
                            x, y, o = game.players[player_idx].place_ship(grid, self)
                            game.battlespaces[player_idx].place_ship(ship, x, y, o)
                            break
                        except InvalidCoordinateException:
                            continue

        winner = game.main_loop(0)

        if winner == 0:
            self.game_view.msg(f"{p1.name} venceu")
        else:
            self.game_view.msg(f"{p2.name} venceu")

    def player_ranking(self):
        """List all registered players according to their score"""
        self.player_ctrl.list("", ranked = True)

    def previous_games(self):
        """List previously played games"""
        from model.game import Game

        name = self.game_view.input("Digite o nome do jogador de interesse:")
        if name not in [p.name for p in self.player_ctrl.players]:
            self.game_view.msg("Jogador não encontrado")
            return
        player = [p for p in self.player_ctrl.players if p.name == name]
        player = player[0]
        self.game_view.msg(f"Histórico de jogos de {player.name}:")
        for idx, game in enumerate(self.game_history):
            if player not in game.players:
                continue
            self.game_view.msg(f'JOGO {idx+1}:')
            self.game_view.msg(f'Início: {game.start_time}')
            self.game_view.msg(f'Fim: {game.end_time}')
            self.game_view.msg(f'Jogador 1: {game.players[0].name}')
            self.game_view.msg(f'Jogador 2: {game.players[1].name}')
            self.game_view.msg(f'Pontuação do jogador 1: {game.scores[0]}')
            self.game_view.msg(f'Pontuação do jogador 2: {game.scores[1]}')
            self.game_view.msg('Tabuleiro do Jogador 1:')
            self.game_view.render(game.battlespaces[0].grid)
            self.game_view.msg('Tabuleiro do Jogador 2:')
            self.game_view.render(game.battlespaces[1].grid)
            self.game_view.msg(f'Movimentos jogados: {game.move_list}')
            self.game_view.msg('\n')
