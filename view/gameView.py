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

    def render(self, grid):
        letters = 'abcdefghijklmnopqrst'
        print('  ', end = '')
        for i in range(len(grid[0])):
            print(f'{letters[i]:>2}', end = '')
        print('')
        for line_num, line in enumerate(grid):
            print(f'{line_num:>2}', end = '')
            for c in line:
                print(f'{c:>2}', end = '')
            print('')
            
