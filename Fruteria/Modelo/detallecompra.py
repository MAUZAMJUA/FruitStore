from dataclasses import dataclass
from Modelo.producto import Producto

@dataclass
class DetalleCompra:
    _id : int = 0
    _producto : Producto = None # type: ignore
    _cantidad : float = 0
    _precio : float = 0

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
    def cantidad(self):
        return self._cantidad
    
    @cantidad.setter
    def cantidad(self, cantidad:float):
        self._cantidad=cantidad

    @property
    def precio(self):
        return self._precio
    
    @precio.setter
    def precio(self, precio:float):
        self._precio=precio

#Zamudio Juarez Mauricio