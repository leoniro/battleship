from ctrl.shipCtrl import ShipCtrl
from view.gameView import GameView


class GameCtrl:
    def __init__(self):
        from ctrl.playerCtrl import PlayerCtrl

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
                choice = self.game_view.input_integer(options.keys())
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
        except:
            self.game_view.msg("Tamanho inválido")
        self.game_view.msg("Digite a largura do tabuleiro (10 a 20)")
        try:
            w = self.game_view.input(range(10,21))
        except:
            self.game_view.msg("Tamanho inválido")
        
        game = Game(self, h, w, p1, p2, self.ship_ctrl.ships)
        self.game_history.append(game)
        
        for player_idx in range(2):
            self.game_view.msg(f"\nJogador {game.players[player_idx]}: Posicione seus navios")
            self.game_view.msg(f'Formato: "<linha> <coluna> <orientação>", com orientação 0 para
                               horizontal e 1 para vertical')
            for ship in game.battlespaces[player_idx].ships:
                while True:
                    try:
                        self.game_view.render(game.battlespaces[player_idx].grid)
                        self.game_view.msg(
                            f"Posicione um(a) {ship.type}, de comprimento {ship.length()}:")
                        coord = game.players[player_idx].place_ship(
                            game.battlespaces[player_idx].grid)
                        game.battlespaces[0].place_ship(coord)
                        break
                    except:
                        self.game_view.msg("Posição inválida, tente novamente")
                        continue

        winner = game.turn(0)

        if winner == 0:
            self.game_view.msg(f"{p1.name} venceu")
        else:
            self.game_view.msg(f"{p2.name} venceu")
        
        pass

    def player_ranking(self):
        pass

    def previous_games(self):
        pass