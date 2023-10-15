from view.playerView import PlayerView
from model.humanPlayer import HumanPlayer
from model.computerPlayer import ComputerPlayer

class PlayerCtrl:
    """Player controller class"""
    def __init__(self):
        self.__players = [ComputerPlayer("Computador"), HumanPlayer("Humano")]
        self.__player_view = PlayerView()
        self.__player_types = {
            0: HumanPlayer,
            1: ComputerPlayer
        }

    @property
    def players(self):
        """List of all players"""
        return self.__players

    @property
    def player_view(self):
        """Player view"""
        return self.__player_view

    @property
    def player_types(self):
        """Dictionary of types of Players classes constructors"""
        return self.__player_types

    def start(self):
        """Main menu of Player Control"""
        while True:
            text = self.player_view.text
            options = self.player_view.options
            self.player_view.menu(text, options)
            # get and parse input
            term = ""
            choice = self.player_view.input().split()
            if len(choice) == 2:
                try:
                    term = choice[1]
                    choice = int(choice[0])
                except Exception:
                    self.player_view.msg("Opção inválida. Tente novamente\n")
                    continue
            elif len(choice) == 1:
                try:
                    choice = int(choice[0])
                except Exception:
                    self.player_view.msg("Opção inválida. Tente novamente\n")
                    continue
            else:
                self.player_view.msg("Opção inválida. Tente novamente\n")
                continue
            # case switching
            if choice == 0:
                return
            elif choice == 1:
                # list
                self.list(term)
            elif choice == 2:
                # add
                self.player_view.msg("Digite o nome do jogador:")
                name = self.player_view.input()
                if name in [p.name for p in self.players]:
                    self.player_view.msg("Jogador com esse nome já existe")
                    continue
                self.player_view.msg("Tipo de jogador: 0 para humano, 1 para computador")
                try:
                    player_type = self.player_view.input_integer(range(len(self.player_types)))
                except Exception:
                    self.player_view.msg("Opção inválida")
                    continue
                self.add(name, player_type)
                self.player_view.msg("Jogador adicionado com sucesso")
            elif choice == 3:
                # edit
                self.player_view.msg("Digite o nome atual do jogador:")
                old_name = self.player_view.input()
                self.player_view.msg("Digite o novo nome do jogador:")
                new_name = self.player_view.input()
                try:
                    self.modify(old_name, new_name)
                    self.player_view.msg("Nome alterado com sucesso")
                except Exception:
                    self.player_view.msg("Não foi possível realizar a alteração")
                    continue
            elif choice == 4:
                # remove
                self.player_view.msg("Digite o nome de jogador a ser removido")
                name = self.player_view.input()
                try:
                    self.remove(name)
                    self.player_view.msg("Jogador excluído com sucesso")
                except Exception:
                    self.player_view.msg("Não foi possível realizar a exclusão")
                    continue

    def add(self, name, player_type):
        """Add new player"""
        self.players.append(self.player_types[player_type](name))

    def list(self, term=""):
        """List or search for players"""
        self.player_view.msg("Tipo  Pts  Nome")
        for player in [p for p in self.players if term in p.name]:
            if isinstance(player, HumanPlayer):
                p_type = "Hum"
            else:
                p_type = "Com"
            self.player_view.msg(
                f"{p_type:<5}{player.score:4d}  {player.name}")

    def modify(self, old_name, new_name):
        """Change player name"""
        if old_name not in [p.name for p in self.players]:
            raise Exception
        if new_name in [p.name for p in self.players]:
            raise Exception
        player = [p for p in self.players if p.name == old_name]
        player = player[0]
        player.name = new_name

    def remove(self, name):
        """Remove existing player"""
        if name not in [p.name for p in self.players]:
            raise Exception
        idx = [p.name for p in self.players].index(name)
        self.players.pop(idx)
