import datetime
from model.battlespace import Battlespace
from model.abstractPlayer import AbstractPlayer
from model.humanPlayer import HumanPlayer
from model.ship import Ship
from ctrl.gameCtrl import GameCtrl
from exception.invalidCoordinateException import InvalidCoordinateException
from exception.uiCancelException import UICancelException

class Game:
    """class representing a single game match"""
    def __init__(self,
                 game_ctrl: GameCtrl,
                 h: int,
                 w: int,
                 player1: AbstractPlayer,
                 player2: AbstractPlayer,
                 ships):

        self.__game_ctrl = game_ctrl
        self.__players = (player1, player2)
        self.__battlespaces = (Battlespace(h, w, ships),
                               Battlespace(h, w, ships))
        self.__height = h
        self.__width = w
        self.__move_list = []
        self.__scores = [0, 0]
        self.__start_time = datetime.datetime.now()
        self.__end_time = None

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

    @property
    def scores(self):
        """Scores for this single match"""
        return self.__scores

    @property
    def start_time(self):
        """Time the game started"""
        return self.__start_time

    @property
    def end_time(self):
        """Time the game ended"""
        return self.__end_time

    def turn(self, player_idx):
        """Processes a single turn of gameplay"""
        game_over = False
        attacker = player_idx
        defender = int(not attacker)
        attacker_name = self.players[attacker].name
        grid = self.battlespaces[defender].opponent_vision()
        if isinstance(self.players[attacker], HumanPlayer):
            try:
                x, y = self.game_ctrl.game_view.turn_menu(attacker_name, grid)
                is_hit, is_sunk = self.battlespaces[defender].check_hit(x, y)
            except UICancelException as exc:
                raise UICancelException from exc
        else:
            x, y = self.players[attacker].play_move(grid, self.game_ctrl)
            is_hit, is_sunk = self.battlespaces[defender].check_hit(x, y)
            grid = self.battlespaces[defender].opponent_vision()
            # self.game_ctrl.game_view.turn_feedback_menu(attacker_name, grid)
        self.log_move(attacker, x, y)

        # Report move result and tally scores
        if is_hit:
            self.players[attacker].add_score(1)
            self.scores[attacker] += 1
            if is_sunk:
                self.players[attacker].add_score(3)
                self.scores[attacker] += 3
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
            try:
                next_player_idx, game_over = self.turn(player_idx)
            except UICancelException as exc:
                raise UICancelException from exc
            if game_over:
                self.__end_time = datetime.datetime.now()
                return next_player_idx
            player_idx = next_player_idx
