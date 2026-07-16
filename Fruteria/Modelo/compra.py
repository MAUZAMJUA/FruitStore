from dataclasses import dataclass
from Modelo.proveedor import Proveedor

@dataclass
class Compra:
    _id : int = 0
    _proveedor : Proveedor = None # type: ignore
    _fecha : str = " "
    _hora : str = " "

    @property
    def id(self):
        return self._id 
    
    @id.setter
    def id(self, id : int):
        self._id = id

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

    @property
    def proveedor(self):
        return self._proveedor

    @proveedor.setter
    def proveedor(self, proveedor: Proveedor):
        self._proveedor = proveedor

#Zamudio Juarez Mauricio