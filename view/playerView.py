import datetime
from view.abstractView import AbstractView


class PlayerView(AbstractView):
    """View for player management module"""
    def __init__(self):
        self.__text = "Cadastro de Jogadores"
        self.__options = {
            1: 'Listar jogadores ( "1 <termo>" para buscar)',
            2: "Adicionar novo jogador",
            3: "Editar nome de um jogador",
            4: "Excluir jogador",
            0: "Voltar"
        }

    @property
    def text(self):
        return self.__text

    @property
    def options(self):
        return self.__options

    def input_dob(self):
        """get date of birth"""
        while True:
            try:
                y = self.input_integer(None, "Ano de nascimento:")
                m = self.input_integer(None, "Mes de nascimento:")
                d = self.input_integer(None, "Dia de nascimento:")
                dob = datetime.datetime(y, m, d)
                return dob
            except ValueError:
                continue
