from model.ship import Ship
from view.shipView import ShipView
from exception.maximumShipsReachedException import MaximumShipsReachedException
from exception.minimumShipsReachedException import MinimumShipsReachedException
from exception.uiCancelException import UICancelException
from dao.dao import DAO


class ShipCtrl(DAO):
    """Ship Controller class"""
    def __init__(self):
        super().__init__('ship.pkl')
        self.__ships = super().get()
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
            choice = self.ship_view.menu()
            if choice == 0:
                return
            if choice == 1:
                self.list()
            elif choice == 2:
                try:
                    length = self.ship_view.spinbox('Escolha o tamanho da embarcação', range(1,5))
                    self.add_ship(length)
                except MaximumShipsReachedException:
                    self.ship_view.error("Quantidade máxima de embarcações atingida")
                except ValueError:
                    self.ship_view.error("Tamanho inválido de embarcação")
                except UICancelException:
                    continue
            elif choice == 3:
                try:
                    idx = self.ship_view.multiple_choices(
                        'Escolha a embarcação a ser removida', range(len(self.ships)))
                    self.remove_ship(idx)
                    self.ship_view.msg("Removido com sucesso")
                except MinimumShipsReachedException:
                    self.ship_view.error("Mínimo de embarcações atingido")
                except IndexError:
                    self.ship_view.error("Id inválido")

    def add_ship(self, length):
        """Add new ship"""
        if len(self.ships) >= 10:
            raise MaximumShipsReachedException("Máximo de 10 embarcações atingido")
        else:
            super().add(Ship(length))

    def list(self):
        """List current ships"""
        cols = ['Id', 'Tipo', 'Tamanho']
        data = []
        for idx, ship in enumerate(self.ships):
            data.append([idx, str(ship.type), ship.length()])
        self.ship_view.info_menu(cols, data)

    def remove_ship(self, idx):
        """Remove existing ship"""
        if len(self.ships) <= 1:
            raise MinimumShipsReachedException("Mínimo de 1 embarcação atingido")
        super().remove(idx)
