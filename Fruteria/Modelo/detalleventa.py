from dataclasses import dataclass
from Modelo.producto import Producto

@dataclass
class DetalleVenta:
    _id : int = 0
    _producto : Producto = None # type: ignore
    _precioVenta : float = 0
    _cantidad : int = 0
    _precioCompraReg : float = 0

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id:int):
        self._id=id

    @property
    def producto(self):
        return self._producto
    
    @producto.setter
    def producto(self, producto:Producto):
        self._producto=producto

    @property
    def precioVenta(self):
        return self._precioVenta
    
    @precioVenta.setter
    def precioVenta(self, precioVenta:float):
        self._precioVenta=precioVenta
            
    @property
    def cantidad(self):
        return self._cantidad
    
    @cantidad.setter
    def cantidad(self, cantidad:int):
        self._cantidad=cantidad

    @property
    def precioCompraReg(self):
        return self._precioCompraReg
    
    @precioCompraReg.setter
    def precioCompraReg(self, precioCompraReg:float):
        self._precioCompraReg=precioCompraReg

#Zamudio Juarez Mauricio