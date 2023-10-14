from model.abstractPlayer import AbstractPlayer
from model.battlespace import Battlespace
from ctrl.gameCtrl import GameCtrl


class ComputerPlayer(AbstractPlayer):
    def __init__(self, name: str):
        
        super().__init__(name)

    def play_move(self, grid: list[list[int]], game_ctrl: GameCtrl):
        pass
    
    def place_ship(self, battlespace: Battlespace, game_ctrl: GameCtrl):
        pass
