from dataclasses import dataclass
from modelo.producto import Producto

@dataclass
class DetalleVenta:
    _idVenta : int = 0
    _producto : Producto = None # type: ignore
    _cantidad : float = 0.0
    _precioventa : float = 0.0
    _preciocompra : float = 0.0
    _descuento : float = 0.0

    @property
    def idVenta(self):
        return self._idVenta
    @idVenta.setter
    def idVenta(self, idVenta : int):
        self._idVenta = idVenta
    
    @property
    def producto(self):
        return self._producto
    @producto.setter
    def producto(self, producto : Producto):
        self._producto = producto
    
    @property
    def cantidad(self):
        return self._cantidad
    @cantidad.setter
    def cantidad(self, cantidad : float):
        self._cantidad = cantidad
    
    @property
    def precioventa(self):
        return self._precioventa
    @precioventa.setter
    def precioventa(self, precioventa : float):
        self._precioventa = precioventa

    @property
    def preciocompra(self):
        return self._preciocompra
    @preciocompra.setter
    def preciocompra(self, preciocompra : float):
        self._preciocompra = preciocompra

    @property
    def descuento(self):
        return self._descuento
    @descuento.setter
    def descuento(self, descuento : float):
        self._descuento = descuento
