from dataclasses import dataclass
from Modelo.categoria import Categoria

@dataclass
class Producto:
    _id : int = 0
    _nombre : str = ""
    _precioCompra : float = 0
    _precioVenta : float = 0
    _existenciaDisponible : int = 0
    _estatus : float = 0
    _categoria : Categoria = None # type: ignore

    @property
    def categoria(self):
        return self._categoria
    
    @categoria.setter
    def categoria(self, categoria:Categoria):
        self._categoria=categoria

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id:int):
        self._id=id

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre:str):
        self._nombre=nombre

    @property
    def precioCompra(self):
        return self._precioCompra
    
    @precioCompra.setter
    def precioCompra(self, precioCompra:float):
        self._precioCompra=precioCompra

    @property
    def precioVenta(self):
        return self._precioVenta
    
    @precioVenta.setter
    def precioVenta(self, precioVenta:float):
        self._precioVenta=precioVenta
            
    @property
    def existenciaDisponible(self):
        return self._existenciaDisponible
    
    @existenciaDisponible.setter
    def existenciaDisponible(self, existenciaDisponible:int):
        self._existenciaDisponible=existenciaDisponible

    @property
    def estatus(self):
        return self._estatus
    
    @estatus.setter
    def estatus(self, estatus:float):
        self._estatus=estatus

#Zamudio Juarez Mauricio