from view.playerView import PlayerView
from model.humanPlayer import HumanPlayer
from model.computerPlayer import ComputerPlayer

class PlayerCtrl:
    def __init__(self):
        self.__players = []
        self.__player_view = PlayerView()
        self.__player_types = {
            0: HumanPlayer,
            1: ComputerPlayer
        }

    @property
    def players(self):
        return self.__players

    @property
    def player_view(self):
        return self.__player_view

    @property
    def player_types(self):
        return self.__player_types

    def start(self):
        while True:
            text = self.player_view.text
            options = self.player_view.options
            self.player_view.menu(text, options)
            # get and parse input
            term = ""
            choice = self.player_view.get_input().split()
            if len(choice) == 2:
                try:
                    term = choice[1]
                    choice = int(choice[0])
                except:
                    self.player_view.msg("Opção inválida. Tente novamente\n")
                    continue
            elif len(choice) == 1:
                try:
                    choice = int(choice[0])
                except:
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
                name = self.player_view.get_input()
                if name in [p.name for p in self.players]:
                    self.player_view.msg("Jogador com esse nome já existe")
                    continue
                self.player_types.msg("Tipo de jogador: 0 para humano, 1 para computador")
                try:
                    player_type = self.player_view.get_integer(range(len(self.player_types)))
                except:
                    self.player_view.msg("Opção inválida")
                    continue
                self.add(name, player_type)
                self.player_view.msg("Jogador adicionado com sucesso")
            elif choice == 3:
                # edit
                self.player_view.msg("Digite o nome atual do jogador:")
                old_name = self.player_view.get_input()
                self.player_view.msg("Digite o novo nome do jogador:")
                new_name = self.player_view.get_input()
                try:
                    self.modify(old_name, new_name)
                    self.player_view.msg("Nome alterado com sucesso")
                except:
                    self.player_view.msg("Não foi possível realizar a alteração")
                    continue
            elif choice == 4:
                # remove
                self.player_view.msg("Digite o nome de jogador a ser removido")
                name = self.player_view.get_input()
                try:
                    self.remove(name)
                    self.player_view.msg("Jogador excluído com sucesso")
                except:
                    self.player_view.msg("Não foi possível realizar a exclusão")
                    continue

    def add(self, name, player_type):
        self.players.append(self.player_types[player_type](name))

    def list(self, term):
        self.player_view.msg("Tipo  Pts  Nome")
        for player in [p for p in self.players if (term in p.name)]:
            if isinstance(player, HumanPlayer):
                p_type = "Hum"
            else:
                p_type = "Com"
            self.player_view.msg(
                f"{p_type:<5}{player.score:4d}  {player.name}")
            
    
    def modify(self, old_name, new_name):
            if old_name not in [p.name for p in self.players]:
                #self.player_view.msg("Jogador não encontrado")
                raise Exception
            if new_name in [p.name for p in self.players]:
                #self.player_view.msg("Esse nome de jogador já existe")
                raise Exception
            player = [p for p in self.players if p.name == old_name]
            player = player[0]
            player.name = new_name
            # self.player_view.msg("Nome alterado com sucesso")

    def remove(self, name):
        if name not in [p.name for p in self.players]:
            # self.player_view.msg("Jogador não encontrado")
            raise Exception
        idx = [p.name for p in self.players].index(name)
        self.players.pop(idx)
        # self.player_view.msg("Jogador excluído com sucesso")