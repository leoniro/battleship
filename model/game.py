import datetime
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
        from model.humanPlayer import HumanPlayer

        game_over = False
        attacker = player_idx
        defender = int(not attacker)
        grid = self.battlespaces[defender].opponent_vision()
        self.game_ctrl.game_view.msg('\n')
        self.game_ctrl.game_view.msg(
            f'Vez do jogador {self.players[attacker].name}. Faça sua jogada:')
        # Humans are shown grid before their move
        if isinstance(self.players[attacker], HumanPlayer):
            self.game_ctrl.game_view.render(grid)
        while True:
            try:
                x, y = self.players[attacker].play_move(grid, self.game_ctrl)
                is_hit, is_sunk = self.battlespaces[defender].check_hit(x, y)
                break
            except Exception:
                self.game_ctrl.game_view.msg("Coordenadas inválidas, tente novamente")
                continue
        self.log_move(attacker, x, y)
        # When Computer plays, grid is shown after, with move already resolved
        if not isinstance(self.players[attacker], HumanPlayer):
            grid = self.battlespaces[defender].opponent_vision()
            self.game_ctrl.game_view.render(grid)
        # Report move result and tally scores
        if is_hit:
            self.game_ctrl.game_view.msg(f"Embarcação atingida em {self.idx2coord(x,y)}")
            self.players[attacker].add_score(1)
            self.scores[attacker] += 1
            if is_sunk:
                self.game_ctrl.game_view.msg("Embarcação afundada")
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
            next_player_idx, game_over = self.turn(player_idx)
            if game_over:
                self.__end_time = datetime.datetime.now()
                return next_player_idx
            player_idx = next_player_idx