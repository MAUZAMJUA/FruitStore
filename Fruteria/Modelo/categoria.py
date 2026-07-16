from dataclasses import dataclass

@dataclass
class Categoria:
    _id : int = 0
    _nombre : str = ""
    _estatus : int = 1

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
    def estatus(self):
        return self._estatus
    
    @estatus.setter
    def estatus(self, estatus:int):
        self._estatus=estatus
            
#Zamudio Juarez Mauricio