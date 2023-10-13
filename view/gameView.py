from view.abstractView import AbstractView


class GameView(AbstractView):
    def __init__(self):
        self.__text = "BATALHA NAVAL. Escolha uma opção:"
        self.__options = {1: "Novo jogo",
                   2: "Gerenciar Jogadores",
                   3: "Gerencias Embarcações",
                   4: "Ranking de Jogadores",
                   5: "Histório de Partidas",
                   0: "Sair"}

    @property
    def text(self):
        return self.__text

    @property
    def options(self):
        return self.__options

    def new_game(self):
        pass

    def render(self, grid):
        pass
