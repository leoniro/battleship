from view.abstractView import AbstractView


class PlayerView(AbstractView):
    def __init__(self):
        self.__text = ""
        self.__options = {}

    @property
    def text(self):
        return self.__text

    @property
    def options(self):
        return self.__options
