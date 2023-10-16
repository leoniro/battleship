from ctrl.shipCtrl import ShipCtrl
from view.gameView import GameView


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
        text = self.game_view.text
        options = self.game_view.options
        while True:
            self.game_view.menu(text, options)
            try:
                choice = self.game_view.input_integer(options.keys())
            except Exception:
                self.game_view.msg("Opção inválida. Tente novamente\n")
                continue
            if choice == 0:
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
        """Set up a new game and start it"""
        from model.game import Game

        self.player_ctrl.list()
        self.game_view.msg("Digite o nome do primeiro jogador:")
        p1 = self.game_view.input()
        self.game_view.msg("Digite o nome do segundo jogador:")
        p2 = self.game_view.input()
        if p1 not in [p.name for p in self.player_ctrl.players]:
            self.game_view.msg("Jogador 1 não existe")
            return
        if p2 not in [p.name for p in self.player_ctrl.players]:
            self.game_view.msg("Jogador 2 não existe")
            return
        p1 = [p for p in self.player_ctrl.players if p.name == p1]
        p2 = [p for p in self.player_ctrl.players if p.name == p2]
        p1 = p1[0]
        p2 = p2[0]
        self.game_view.msg("Digite a altura do tabuleiro (10 a 20)")
        try:
            h = self.game_view.input_integer(range(10,21))
        except Exception:
            self.game_view.msg("Tamanho inválido")
            return
        self.game_view.msg("Digite a largura do tabuleiro (10 a 20)")
        try:
            w = self.game_view.input_integer(range(10,21))
        except Exception:
            self.game_view.msg("Tamanho inválido")
            return

        game = Game(self, h, w, p1, p2, self.ship_ctrl.ships)
        self.game_history.append(game)

        for player_idx in range(2):
            self.game_view.msg(
                f"\nJogador {game.players[player_idx].name}: Posicione seus navios")
            self.game_view.msg(
                'Formato: "<linha> <coluna> <orientação>", '
                'com orientação 0 para horizontal e 1 para vertical')
            for ship in game.battlespaces[player_idx].ships:
                while True:
                    try:
                        self.game_view.render(game.battlespaces[player_idx].grid)
                        self.game_view.msg(
                            f"Posicione um(a) {ship.type}, de comprimento {ship.length()}:")
                        x, y, o = game.players[player_idx].place_ship(
                            game.battlespaces[player_idx].grid, self)
                        game.battlespaces[player_idx].place_ship(ship, x, y, o)
                        break
                    except Exception:
                        self.game_view.msg("Posição inválida, tente novamente")
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

        self.game_view.msg("Digite o nome do jogador de interesse:")
        name = self.game_view.input()
        if name not in [p.name for p in self.player_ctrl.players]:
            self.game_view.msg("Jogador não encontrado")
            return
        player = [p for p in self.player_ctrl.players if p.name == name]
        player = player[0]
        self.game_view.msg("Histório de jogos de {player.name}:")
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
