from view.abstractView import AbstractView
from exception.uiCancelException import UICancelException
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
    
    def draw_ui_grid(self, layout, grid):
        h = len(grid)
        w = len(grid[0])
        for i in range(h):
            line = []
            for j in range(w):
                if grid[i][j] == ' ':
                    line.append(sg.Button(key = (i,j), button_color='light blue', border_width=0.1))
                elif grid[i][j] == 'x':
                    line.append(sg.Button(key = (i,j), button_color='red', border_width=0.1))
                elif grid[i][j] == 'o':
                    line.append(sg.Button(key = (i,j), button_color='yellow', border_width=0.1))
                elif grid[i][j] == '~':
                    line.append(sg.Button(key = (i,j), button_color='gray', border_width=0.1))
                else:
                    line.append(sg.Button(key = (i,j), button_color='black', border_width=0.1))
            layout.append(line)
        return layout

    def place_ship_menu(self, player_name, grid, ship_length):
        layout = [
            [sg.Text(f"Jogador {player_name}: Posicione um navio de comprimento {ship_length}")],
            [sg.Radio(text = "Horizontal", group_id=0, key = 'hor', default = True),
             sg.Radio(text = "Vertical", group_id=0, key = 'ver')]]
        self.draw_ui_grid(layout, grid)
        placement_menu = sg.Window('Posicionar embarcação').Layout(layout)
        button, data = placement_menu.Read()
        placement_menu.close()
        if button is None:
            raise UICancelException
        x, y = button
        if data['hor']:
            o = 0
        elif data['ver']:
            o = 1
        return x, y, o

    def turn_menu(self, player_name, grid):
        layout = [[sg.Text(f"Vez do jogador {player_name}")]]
        self.draw_ui_grid(layout, grid)
        turn_window = sg.Window("Batalha Naval").Layout(layout)
        while True:
            button, _ = turn_window.Read()
            if button is None:
                turn_window.close()
                raise UICancelException
            x, y = button
            if grid[x][y] == '~':
                break
        turn_window.close()
        return x, y

    def turn_feedback_menu(self, player_name, grid):
        layout = [[sg.Text(f'Resultado da vez de {player_name}:')]]
        self.draw_ui_grid(layout, grid)
        layout.append([sg.OK()])
        feedback_window = sg.Window('Batalha Naval').Layout(layout)
        feedback_window.Read()
        feedback_window.close()

    def game_description_menu(self, games_data):
        layout = [[sg.T('Jogos Encontrados:')]]
        for k, v in games_data.items():
            layout.append([sg.T(v)])
        window = sg.Window('Batalha Naval').Layout(layout)
        window.Read()
        window.close()
