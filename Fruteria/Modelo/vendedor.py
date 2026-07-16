from dataclasses import dataclass

@dataclass
class Vendedor:
    _id : int = 0
    _nombre : str = ""
    _fechaNac : str = ""
    _genero : str = ""
    _calle : str = ""
    _numeroExt : str = ""
    _numeroInt : str = ""
    _colonia : str = ""
    _cp : str = ""
    _ciudad : str = ""
    _estado : str = ""
    _pais : str = ""
    _telefono : str = ""
    _fechaAlta : str = ""
    _email : str = ""
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
    def fechaNac(self):
        return self._fechaNac
    
    @fechaNac.setter
    def fechaNac(self, fechaNac:str):
        self._fechaNac=fechaNac

    @property
    def genero(self):
        return self._genero
    
    @genero.setter
    def genero(self, genero:str):
        self._genero=genero

    @property
    def calle(self):
        return self._calle
    
    @calle.setter
    def calle(self, calle:str):
        self._calle=calle
        
    @property
    def numeroExt(self):
        return self._numeroExt
    
    @numeroExt.setter
    def numeroExt(self, numeroExt:str):
        self._numeroExt=numeroExt

    @property
    def numeroInt(self):
        return self._numeroInt
    
    @numeroInt.setter
    def numeroInt(self, numeroInt:str):
        self._numeroInt=numeroInt

    @property
    def colonia(self):
        return self._colonia
    
    @colonia.setter
    def colonia(self, colonia:str):
        self._colonia=colonia

    @property
    def cp(self):
        return self._cp
    
    @cp.setter
    def cp(self, cp:str):
        self._cp=cp

    @property
    def ciudad(self):
        return self._ciudad
    
    @ciudad.setter
    def ciudad(self, ciudad:str):
        self._ciudad=ciudad

    @property
    def estado(self):
        return self._estado
    
    @estado.setter
    def estado(self, estado:str):
        self._estado=estado

    @property
    def pais(self):
        return self._pais
    
    @pais.setter
    def pais(self, pais:str):
        self._pais=pais

    @property
    def telefono(self):
        return self._telefono
    
    @telefono.setter
    def telefono(self, telefono:str):
        self._telefono=telefono

    @property
    def fechaAlta(self):
        return self._fechaAlta
    
    @fechaAlta.setter
    def fechaAlta(self, fechaAlta:str):
        self._fechaAlta=fechaAlta

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email:str):
        self._email=email
  

    @property
    def estatus(self):
        return self._estatus
    
    @estatus.setter
    def estatus(self, estatus:float):
        self._estatus=estatus

#Zamudio Juarez Mauricio