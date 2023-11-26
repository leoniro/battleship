from abc import ABC, abstractmethod
from exception.invalidInputException import InvalidInputException
from exception.uiCancelException import UICancelException
import PySimpleGUI as sg


class AbstractView(ABC):
    """Base abstract class for View implementation"""
    @abstractmethod
    def __init__(self):
        self.__text = ""
        self.__options = {}

    @property
    def text(self):
        """Top menu description"""
        return self.__text

    @property
    def options(self):
        """Dictionary with menu options"""
        return self.__options

    def menu(self, text = None, options = None):
        """Print full menu, return chosen option"""
        if text is None:
            text = self.text
        if options is None:
            options = self.options
        layout = [[ sg.Text(text) ]]
        for k, v in options.items():
            layout.append([sg.Button( button_text = v, key = k)])
        main_menu = sg.Window('Batalha Naval').Layout(layout)
        choice, _ = main_menu.Read()
        main_menu.close()
        if choice is None:
            raise UICancelException
        return choice
    
    def multiple_choices(self, text, options):
        """One-time window with multiple options"""
        layout = [[sg.Text(text)],
                  [sg.Listbox(values = options, key = 'choice', size = (30,3))],
                  [sg.Submit(), sg.Cancel()]]
        listbox_window = sg.Window(text).Layout(layout)
        button, data = listbox_window.Read()
        listbox_window.close()
        if button == 'Cancel' or button is None:
            raise UICancelException
        if button == 'Submit':
            data = data['choice']
            return data[0]

    def spinbox(self, text, options):
        layout = [
            [sg.Text(text)],
            [sg.Spin(values = list(options), initial_value = options[0], key = 'spin')],
            [sg.Submit(), sg.Cancel()]]
        spin_window = sg.Window(text).Layout(layout)
        button, data = spin_window.Read()
        spin_window.close()
        if button == 'Cancel' or button is None:
            raise UICancelException
        if button == 'Submit':
            data = data['spin']
        return data


    def msg(self, text):
        """Info Box"""
        layout = [[sg.Text(text)], [sg.Submit()]]
        window = sg.Window("Info").Layout(layout)
        window.Read()
        window.close()

    def error(self, text):
        """Error box"""
        layout = [[sg.Text(text)], [sg.Submit()]]
        window = sg.Window("Erro").Layout(layout)
        window.Read()
        window.close()

    def input_integer(self, validator = None, prompt = ''):
        """Get input and tries to cast it to integer in validator"""
        layout = [[sg.Text(prompt)], [sg.Input(key = 'input')], [sg.Submit(), sg.Cancel()]]
        input_window = sg.Window(prompt).Layout(layout)
        button, data = input_window.Read()
        print(button, input)
        input_window.close()
        if button == 'Cancel' or button is None:
            raise UICancelException
        if button == 'Submit':
            data = data['input']
        try:
            data = int(input())
            if (not validator) or (data in validator):
                return data
            raise InvalidInputException
        except ValueError as exc:
            raise InvalidInputException from exc

    def input(self, prompt = ''):
        """Get arbitrary input"""
        layout = [[sg.Text(prompt)], [sg.Input(key = 'input')], [sg.Submit(), sg.Cancel()]]
        input_window = sg.Window(prompt).Layout(layout)
        button, data = input_window.Read()
        print(button, input)
        input_window.close()
        if button == 'Cancel' or button is None:
            raise UICancelException
        if button == 'Submit':
            data = data['input']
            return data