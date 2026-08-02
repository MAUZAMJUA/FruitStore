from dataclasses import dataclass

@dataclass
class Proveedor:
    _id : int = 0
    _nombre : str = " "
    _razon_social : str = " "
    _RFC : str = " "
    _direccion : str = " "
    _email : str = " "
    _tel : str = " "
    _cel : str = " "
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
    def razon_social(self):
        return self._razon_social

    @razon_social.setter
    def razon_social(self, razon_social : str):
        self._razon_social = razon_social

    @property
    def RFC(self):
        return self._RFC

    @RFC.setter
    def RFC(self, RFC : str):
        self._RFC = RFC

    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, direccion : str):
        self._direccion = direccion

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email : str):
        self._email = email

    @property
    def tel(self):
        return self._tel

    @tel.setter
    def tel(self, tel : str):
        self._tel = tel

    @property
    def cel(self):
        return self._cel

    @cel.setter
    def cel(self, cel : str):
        self._cel = cel

    @property
    def estatus(self):
        return self._estatus

    @estatus.setter
    def estatus(self, estatus : int):
        self._estatus = estatus