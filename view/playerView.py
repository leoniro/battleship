from view.abstractView import AbstractView


class PlayerView(AbstractView):
    def __init__(self):
        self.__text = "Cadastro de Jogadores"
        self.__options = {
            1: 'Listar jogadores ( "1 <termo>" para buscar)',
            2: "Adicionar novo jogador",
            3: "Editar nome um jogador",
            4: "Excluir jogador",
            0: "Voltar"
        }

    @property
    def text(self):
        return self.__text

    @property
    def options(self):
        return self.__options
