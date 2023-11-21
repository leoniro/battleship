from view.abstractView import AbstractView


class ShipView(AbstractView):
    """View for ship management module"""
    def __init__(self):
        self.__text = "Cadastro de embarcações"
        self.__options = {
            1: "Listar todos as embarcações",
            2: "Adicionar nova embarcação",
            3: "Excluir embarcação",
            0: "Voltar"
        }

    @property
    def text(self):
        return self.__text

    @property
    def options(self):
        return self.__options