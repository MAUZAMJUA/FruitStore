from dataclasses import dataclass

@dataclass
class Vendedor:
    _id : int = 0
    _nombre : str = " "
    _fecha_nacimiento : str = " "
    _genero : str = " "
    _calle : str = " "
    _num_ext : str = " "
    _num_int : str = " "
    _CP : str = " "
    _colonia : str = " "
    _ciudad : str = " "
    _estado : str = " "
    _pais : str = " "
    _tel : str = " "
    _fecha_ingreso : str = " "
    _email : str = " "
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
    def fecha_nacimiento(self):
        return self._fecha_nacimiento
    @fecha_nacimiento.setter
    def fecha_nacimiento(self, fecha_nacimiento : str):
        self._fecha_nacimiento = fecha_nacimiento
    
    @property
    def genero(self):
        return self._genero
    @genero.setter
    def genero(self, genero : str):
        self._genero = genero
    
    @property
    def calle(self):
        return self._calle
    @calle.setter
    def calle(self, calle : str):
        self._calle = calle
    
    @property
    def num_ext(self):
        return self._num_ext
    @num_ext.setter
    def num_ext(self, num_ext : str):
        self._num_ext = num_ext
    
    @property
    def num_int(self):
        return self._num_int
    @num_int.setter
    def num_int(self, num_int : str):
        self._num_int = num_int
    
    @property
    def CP(self):
        return self._CP
    @CP.setter
    def CP(self, CP : str):
        self._CP = CP
    
    @property
    def colonia(self):
        return self._colonia
    @colonia.setter
    def colonia(self, colonia : str):
        self._colonia = colonia
    
    @property
    def ciudad(self):
        return self._ciudad
    @ciudad.setter
    def ciudad(self, ciudad : str):
        self._ciudad = ciudad
    
    @property
    def estado(self):
        return self._estado
    @estado.setter
    def estado(self, estado : str):
        self._estado = estado
    
    @property
    def pais(self):
        return self._pais
    @pais.setter
    def pais(self, pais : str):
        self._pais = pais
    
    @property
    def tel(self):
        return self._tel
    @tel.setter
    def tel(self, tel : str):
        self._tel = tel
    
    @property
    def fecha_ingreso(self):
        return self._fecha_ingreso
    @fecha_ingreso.setter
    def fecha_ingreso(self, fecha_ingreso : str):
        self._fecha_ingreso = fecha_ingreso
    
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, email : str):
        self._email = email
    
    @property
    def estatus(self):
        return self._estatus
    @estatus.setter
    def estatus(self, estatus : int):
        self._estatus = estatus
