from dataclasses import dataclass
from modelo.categoria import Categoria

@dataclass
class Producto:
    _id : int = 0
    _nombre : str = " "
    _preciocompra : float = 0.0
    _precioventa : float = 0.0
    _existencia : int = 0
    _categoria : Categoria = None # type: ignore
    _estatus : int = 0

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id : int):
        self._id = id

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre : str):
        self._nombre = nombre
    
    @property
    def preciocompra(self):
        return self._preciocompra

    @preciocompra.setter
    def preciocompra(self, preciocompra : float):
        self._preciocompra = preciocompra
    
    @property
    def precioventa(self):
        return self._precioventa
    @precioventa.setter
    def precioventa(self, precioventa : float):
        self._precioventa = precioventa
    
    @property
    def existencia(self):
        return self._existencia
    @existencia.setter
    def existencia(self, existencia : int):
        self._existencia = existencia

    @property
    def categoria(self):
        return self._categoria
    @categoria.setter
    def categoria(self, categoria : Categoria):
        self._categoria = categoria
    
    @property
    def estatus(self):
        return self._estatus
    @estatus.setter
    def estatus(self, estatus : int):
        self._estatus = estatus