import copy
from exception.invalidCoordinateException import InvalidCoordinateException
from battlespace import Battlespace
from ctrl.gameCtrl import gameControl
from view.gameView import GameView
from model.player import Player
from model.ship import Ship

class Game:
    def __init__(self,
                 game_ctrl: gameControl,
                 h: int,
                 w: int,
                 player1: Player,
                 player2: Player,
                 ships: list(Ship)):
        self.__game_ctrl = game_ctrl
        self.__players = (player1, player2)
        self.__battlespaces = (Battlespace(h, w, ships),
                               Battlespace(h, w, ships))
        self.__height = h
        self.__width = w
        self.__move_list = []

    @property
    def game_ctrl(self):
        return self.__game_ctrl

    @property
    def players(self):
        return self.__players

    @property
    def battlespaces(self):
        return self.__battlespaces

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @property
    def move_list(self):
        return self.__move_list

    def turn(self, player_idx):
        attacker = player_idx
        defender = 1 if player_idx == 0 else 0
        is_valid = False
        while not is_valid:
            coord = self.players(attacker).play_move()
            try:
                x, y = self.coord2idx(coord)
                is_hit, is_valid = self.battlespaces[defender].check_hit(x, y)
            finally:
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
        self.move_list.append( (player_idx, coord) )

    def coord2idx(self, coord):
        try:
            x, y = coord.lower().split()
            x = int(x) - 1
            y = ord(y) - 97
            if 0 <= x < len(self.grid) and 0 <= y < len(self.grid[0]):
                return x,y
            raise InvalidCoordinateException("Coordenadas fora do tabuleiro")
        except:
            raise InvalidCoordinateException("Coordenadas inválidas")