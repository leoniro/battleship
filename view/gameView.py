from view.abstractView import AbstractView
import PySimpleGUI as sg


class GameView(AbstractView):
    """View for main game logic"""
    def __init__(self):
        self.__text = "BATALHA NAVAL. Escolha uma opção:"
        self.__options = {
            1: "Novo jogo",
            2: "Gerenciar Jogadores",
            3: "Gerenciar Embarcações",
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
        """Prints grid in a user-friendly format"""
        letters = 'abcdefghijklmnopqrst'
        print('  ', end = '')
        for i in range(len(grid[0])):
            print(f'{letters[i]:>2}', end = '')
        print('')
        for line_num, line in enumerate(grid):
            print(f'{line_num + 1:>2}', end = '')
            for c in line:
                print(f'{c:>2}', end = '')
            print('')
            
    def place_ship_menu(self, player_name, grid, ship_length):
        layout = [
            [sg.Text(f"Jogador {player_name}: Posicione um navio de comprimento {ship_length}")],
            [sg.Radio(text = "Horizontal", group_id=0, key = 'hor', default = True),
             sg.Radio(text = "Vertical", group_id=0, key = 'ver')]]
        h = len(grid)
        w = len(grid[0])
        for i in range(h):
            line = []
            for j in range(w):
                if grid[i][j] == ' ':
                    line.append(sg.Button(key = (i,j), button_color='blue'))
                else:
                    line.append(sg.Button(key = (i,j), button_color='black'))
            layout.append(line)
        placement_menu = sg.Window('Posicionar embarcação').Layout(layout)
        button, data = placement_menu.Read()
        placement_menu.close()
        try:
            x, y = button
            if data['hor']:
                o = 0
            elif data['ver']:
                o = 1
            return x, y, o
        except:
            pass
