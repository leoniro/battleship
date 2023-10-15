from model.ship import Ship
from view.shipView import ShipView
from exception.maximumShipsReachedException import MaximumShipsReachedException
from exception.minimumShipsReachedException import MinimumShipsReachedException


class ShipCtrl():
    """Ship Controller class"""
    def __init__(self):
        self.__ships = [Ship(1), Ship(1), Ship(1), Ship(2), Ship(2),
                        Ship(3), Ship(3), Ship(4)]
        self.__ship_view = ShipView()

    @property
    def ships(self):
        """Ships list"""
        return self.__ships

    @property
    def ship_view(self):
        """Ship View"""
        return self.__ship_view

    def start(self):
        """Main menu for ship CRUD"""
        while True:
            text = self.ship_view.text
            options = self.ship_view.options
            self.ship_view.menu(text, options)
            try:
                choice = self.ship_view.input_integer(options.keys())
            except Exception:
                self.ship_view.msg("Opção inválida. Tente novamente\n")
                continue
            if choice == 0:
                return
            elif choice == 1:
                self.list()
            elif choice == 2:
                self.ship_view.msg("Escolha o comprimento da embarcação (1 a 4):")
                try:
                    length = self.ship_view.input_integer(range(1,5))
                    self.add(length)
                except Exception:
                    self.ship_view.msg("Não foi possível adicionar")
            elif choice == 3:
                # remove
                self.list()
                self.ship_view.msg("Digite o Id da embarcação a ser removida")
                try:
                    idx = self.ship_view.input_integer(range(len(self.ships)))
                    self.remove(idx)
                    self.ship_view.msg("Removido com sucesso")
                except Exception:
                    self.ship_view.msg("Não foi possível remover")

    def add(self, length):
        """Add new ship"""
        if len(self.ships) >= 10:
            raise MaximumShipsReachedException("Máximo de 10 embarcações atingido")
        else:
            self.ships.append(Ship(length))

    def list(self):
        """List current ships"""
        self.ship_view.msg("Id  Tam Tipo")
        for idx, ship in enumerate(self.ships):
            self.ship_view.msg(f"{idx: 3d}{ship.length(): 4d} {ship.type}")

    def remove(self, idx):
        """Remove existing ship"""
        if len(self.ships) <= 1:
            raise MinimumShipsReachedException("Mínimo de 1 embarcação atingido")
        self.ships.pop(idx)
