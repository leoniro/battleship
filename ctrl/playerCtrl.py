from view.playerView import PlayerView


class PlayerCtrl:
    def __init__(self):
        self.__players = []
        self.__player_view = PlayerView()

    @property
    def players(self):
        return self.__players

    @property
    def player_view(self):
        return self.__player_view

    def add(self):
        pass

    def list(self):
        pass
    
    def modify(self):
        pass

    def remove(self):
        pass