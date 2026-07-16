from dataclasses import dataclass
from Modelo.vendedor import Vendedor

@dataclass
class Venta:
    _id : int = 0
    _fecha : str = ""
    _hora : float = 0
    _vendedor : Vendedor = None   # type: ignore
    _descuento : float = 0
    _total : float = 0

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id:int):
        self._id=id

    @property
    def fecha(self):
        return self._fecha
    
    @fecha.setter
    def fecha(self, fecha: str):
        self._fecha=fecha
            
    @property
    def hora(self):
        return self._hora
    
    @hora.setter
    def hora(self, hora:float):
        self._hora=hora

    @property
    def vendedor(self):
        return self._vendedor
    
    @vendedor.setter
    def vendedor(self, vendedor:Vendedor):
        self._vendedor=vendedor

    @property
    def descuento(self):
        return self._descuento
    
    @descuento.setter
    def descuento(self, descuento:float):
        self._descuento=descuento

    @property
    def total(self):
        return self._total
    
    @total.setter
    def total(self, total:float):
        self._total=total

#Zamudio Juarez Mauricio