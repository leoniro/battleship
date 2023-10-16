import datetime
from view.abstractView import AbstractView


class PlayerView(AbstractView):
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
        try:
            self.msg("Ano de nascimento:")
            y = self.input_integer(range(1800, 2024))
            self.msg("Mes de nascimento:")
            m = self.input_integer(range(1, 13))
            self.msg("Dia de nascimento:")
            d = self.input_integer(range(1, 32))
            dob = datetime.datetime(y, m, d)
        except:
            raise Exception
        return dob