import mysql.connector
from mysql.connector import Error
class ConexionMySQL:
    def __init__(self):
        self.host = "127.0.0.1"
        self.puerto = 3306
        self.usuario = "MAUZAMJUA"
        self.contrasenia = "MAUZAMJUA"
        self.db = "fruit_store"
        self.conexion = None
 
    def abrir(self):
        try:
            if self.conexion is None or not self.conexion.is_connected():
                self.conexion = mysql.connector.connect(host=self.host, port=self.puerto, user=self.usuario, password=self.contrasenia, database=self.db)
            return self.conexion
        except Error as e:
            raise e
       
    def cerrar(self):
        if self.conexion is not None and self.conexion.is_connected():
            self.conexion.close()