from dataclasses import dataclass

@dataclass
class Proveedor:
    _id : int = 0
    _nombre : str = ""
    _razonSocial : str = ""
    _RFC : str = ""
    _direccion : str = ""
    _email : str = ""
    _tel : str = ""
    _cel : str = ""
    _estatus : float = 0

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
    def razonSocial(self):
        return self._razonSocial
    
    @razonSocial.setter
    def razonSocial(self, razonSocial:str):
        self._razonSocial=razonSocial

    @property
    def RFC(self):
        return self._RFC
    
    @RFC.setter
    def RFC(self, RFC:str):
        self._RFC=RFC

    @property
    def direccion(self):
        return self._direccion
    
    @direccion.setter
    def direccion(self, direccion:str):
        self._direccion=direccion
        
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email:str):
        self._email=email

    @property
    def tel(self):
        return self._tel
    
    @tel.setter
    def tel(self, tel:str):
        self._tel=tel

    @property
    def cel(self):
        return self._cel
    
    @cel.setter
    def cel(self, cel:str):
        self._cel=cel
  

    @property
    def estatus(self):
        return self._estatus
    
    @estatus.setter
    def estatus(self, estatus:float):
        self._estatus=estatus

#Zamudio Juarez Mauricio