from exception.invalidCoordinateException import InvalidCoordinateException
from model.battlespace import Battlespace
from model.abstractPlayer import AbstractPlayer
from model.ship import Ship
from ctrl.gameCtrl import GameCtrl

class Game:
    """class representing a single game match"""
    def __init__(self,
                 game_ctrl: GameCtrl,
                 h: int,
                 w: int,
                 player1: AbstractPlayer,
                 player2: AbstractPlayer,
                 ships: list[Ship]):
        
        self.__game_ctrl = game_ctrl
        self.__players = (player1, player2)
        self.__battlespaces = (Battlespace(h, w, ships),
                               Battlespace(h, w, ships))
        self.__height = h
        self.__width = w
        self.__move_list = []

    @property
    def game_ctrl(self):
        """Game controller (to allow I/O)"""
        return self.__game_ctrl

    @property
    def players(self):
        """Pair of players"""
        return self.__players

    @property
    def battlespaces(self):
        """Pair of battlespaces"""
        return self.__battlespaces

    @property
    def height(self):
        """Grid height"""
        return self.__height

    @property
    def width(self):
        """Grid width"""
        return self.__width

    @property
    def move_list(self):
        """History of all moves played"""
        return self.__move_list

    def turn(self, player_idx):
        """Processes a single turn of gameplay"""
        attacker = player_idx
        defender = int(not attacker)
        is_valid = False
        while not is_valid:
            try:
                x, y = self.players[attacker].play_move()
                is_hit, is_valid = self.battlespaces[defender].check_hit(x, y)
            except Exception:
                pass
            if not is_valid:
                self.game_ctrl.game_view.msg("Coordenadas inválidas, tente novamente")
        self.log_move(attacker, x, y)
        if is_hit:
            if self.battlespaces[defender].check_defeat():
                return attacker
            return self.turn(attacker)
        return self.turn(defender)

    def log_move(self, player_idx, x, y):
        """Add valid move do move history"""
        coord = self.idx2coord(x,y)
        self.move_list.append( (player_idx, coord) )

    def idx2coord(self, x, y):
        """Convert string coordinate to integer pair"""
        x = x + 1
        y = chr(y + 97)
        coord = str(x) + ' ' + str(y)
        return coord
