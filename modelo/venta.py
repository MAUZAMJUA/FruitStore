from dataclasses import dataclass
from modelo.vendedor import Vendedor

@dataclass
class Venta:
    _id : int = 0
    _vendedor : Vendedor = None  # type: ignore
    _fecha : str = " "
    _hora : str = " "

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, id : int):
        self._id = id

    @property
    def vendedor(self):
        return self._vendedor
    @vendedor.setter
    def vendedor(self, vendedor : Vendedor):
        self._vendedor = vendedor

    @property
    def fecha(self):
        return self._fecha
    @fecha.setter
    def fecha(self, fecha : str):
        self._fecha = fecha

    @property
    def hora(self):
        return self._hora
    @hora.setter
    def hora(self, hora : str):
        self._hora = hora
