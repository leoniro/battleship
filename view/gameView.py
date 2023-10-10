from view.view import View


class GameView(View):
    def __init__(self):
        super().__init__()

    def menu(self, text, options):
        return super().menu(text, options)

    def msg(self, text):
        return super().msg(text)

    def get_input(self, validator):
        return super().get_input(validator)

    def new_game(self):
        pass

    def render(grid):
        pass
