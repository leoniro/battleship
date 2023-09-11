from enum import Enum

class GameStatus(Enum):
    WAITING_FOR_PLAYERS = 1
    SETTING_BOARD_SIZE = 2
    PLACING_SHIPS = 3
    PLAYING = 4
    FINISHED = 5