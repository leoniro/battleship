import datetime
from view.playerView import PlayerView
from model.humanPlayer import HumanPlayer
from model.computerPlayer import ComputerPlayer
from model.betterComputerPlayer import BetterComputerPlayer
from exception.playerAlreadyExistsException import PlayerAlreadyExistsException
from exception.playerNotFoundException import PlayerNotFoundException


class PlayerCtrl:
    """Player controller class"""
    def __init__(self):
        self.__players = [
            ComputerPlayer("Computador", datetime.datetime(1970, 1, 1)),
            HumanPlayer("Humano", datetime.datetime(1970, 1, 2))]
        self.__player_view = PlayerView()
        self.__player_types = {
            0: HumanPlayer,
            1: ComputerPlayer,
            2: BetterComputerPlayer
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
            choice = self.player_view.menu()
            # get and parse input
            # case switching
            if choice == 0:
                return
            elif choice == 1:
                # list
                self.list()
            elif choice == 2:
                # add
                name = self.player_view.input("Digite o nome do jogador:")
                if name in [p.name for p in self.players]:
                    self.player_view.msg("Jogador com esse nome já existe")
                    continue
                player_type = self.player_view.input_integer(
                    self.player_types.keys(),
                    "Tipo de jogador: 0 para humano, 1 para computador, 2 para computador melhor")
                dob = datetime.datetime(1970, 1, 1)
                if player_type == 0:
                    dob = self.player_view.input_dob()
                self.add(name, player_type, dob)
                self.player_view.msg("Jogador adicionado com sucesso")
            elif choice == 3:
                # edit
                old_name = self.player_view.input("Digite o nome atual do jogador:")
                new_name = self.player_view.input("Digite o novo nome do jogador:")
                try:
                    self.modify(old_name, new_name)
                    self.player_view.msg("Nome alterado com sucesso")
                except PlayerNotFoundException:
                    self.player_view.error("Jogador não existe")
                    continue
                except PlayerAlreadyExistsException:
                    self.player_view.error("Já existe jogador com esse nome")
                    continue
            elif choice == 4:
                # remove
                name = self.player_view.input("Digite o nome de jogador a ser removido")
                try:
                    self.remove(name)
                    self.player_view.msg("Jogador excluído com sucesso")
                except PlayerNotFoundException:
                    self.player_view.error("Jogador não existe")
                    continue

    def add(self, name, player_type, dob):
        """Add new player"""
        self.players.append(self.player_types[player_type](name, dob))

    def list(self, query = "", ranked = False):
        """List or search for players"""
        self.player_view.msg("   Tipo  Pts  Nascimento  Nome")
        player_list = [p for p in self.players if query in p.name]
        if ranked:
            player_list = sorted(player_list, key = lambda p: -p.score)
        for idx, player in enumerate(player_list):
            if isinstance(player, HumanPlayer):
                p_type = "Hum"
            else:
                p_type = "Com"
            self.player_view.msg(
                f"{idx+1:2d} " +
                f"{p_type:<5}" + 
                f"{player.score:4d}  " +
                f"{player.date_of_birth:%Y-%m-%d}  " +
                f"{player.name}")

    def modify(self, old_name, new_name):
        """Change player name"""
        if old_name not in [p.name for p in self.players]:
            raise PlayerNotFoundException
        if new_name in [p.name for p in self.players]:
            raise PlayerAlreadyExistsException
        player = [p for p in self.players if p.name == old_name]
        player = player[0]
        player.name = new_name

    def remove(self, name):
        """Remove existing player"""
        if name not in [p.name for p in self.players]:
            raise PlayerNotFoundException
        idx = [p.name for p in self.players].index(name)
        self.players.pop(idx)
