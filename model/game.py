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
            coord = self.players[attacker].play_move()
            try:
                x, y = self.coord2idx(coord)
                is_hit, is_valid = self.battlespaces[defender].check_hit(x, y)
            except Exception:
                pass
            if not is_valid:
                self.game_ctrl.game_view.msg("Coordenadas inválidas, tente novamente")
        self.log_move(attacker, coord)
        if is_hit:
            if self.battlespaces[defender].check_defeat():
                return attacker
            return self.turn(attacker)
        else:
            return self.turn(defender)

    def log_move(self, player_idx, coord):
        """Add valid move do move history"""
        self.move_list.append( (player_idx, coord) )

    def coord2idx(self, coord):
        """Convert string coordinate to integer pair"""
        try:
            x, y = coord.lower().split()
            x = int(x) - 1
            y = ord(y) - 97
            if 0 <= x < len(self.width) and 0 <= y < len(self.height):
                return x,y
            raise InvalidCoordinateException("Coordenadas fora do tabuleiro")
        except:
            raise InvalidCoordinateException("Coordenadas inválidas")