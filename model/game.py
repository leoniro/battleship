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
        game_over = False
        attacker = player_idx
        defender = int(not attacker)
        while True:
            try:
                grid = [[
                    '~' if self.battlespaces[defender].fog_of_war[i][j] is True
                    else  self.battlespaces[defender].grid[i][j]
                    for j in range(self.__width)]
                    for i in range(self.__height)]
                self.game_ctrl.game_view.render(grid)
                self.game_ctrl.game_view.msg(
                    f'Vez do jogador {self.players[attacker].name}. Faça sua jogada:')
                x, y = self.players[attacker].play_move(grid, self.game_ctrl)
                is_hit = self.battlespaces[defender].check_hit(x, y)
                break
            except Exception:
                self.game_ctrl.game_view.msg("Coordenadas inválidas, tente novamente")
                continue
        self.log_move(attacker, x, y)
        if is_hit:
            if self.battlespaces[defender].check_defeat():
                game_over = True
            return attacker, game_over
        return defender, game_over

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

    def main_loop(self, player_idx):
        """turn() wrapper because no tail call optimization :("""
        while True:
            next_player_idx, game_over = self.turn(player_idx)
            if game_over:
                return next_player_idx
            player_idx = next_player_idx