from mysql.connector import Error
from bd.conexion_mysql import ConexionMySQL
from Modelo.categoria import Categoria 

class ControlCategoria:
    def getAll(self):
        sql = "SELECT * FROM categoria WHERE estatus=1"
        conn_MySQL = None
        conn = None
        cursor = None
        categorias = []
        conn_MySQL = ConexionMySQL()
        conn = conn_MySQL.abrir()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql)

        for registro in cursor:
            c = self.fillDatos(registro)
            categorias.append(c)

        cursor.close()
        conn_MySQL.cerrar()
        return categorias
    
    def fillDatos(self, registro = None):
        c = Categoria()
        c.id = registro["idCategoria"]
        c.nombre = registro["nombre"]
        c.estatus = registro["estatus"]
        return c
    
    def insert(self, c=None):
        sql = "INSERT INTO categoria(nombre, estatus) VALUES(%s, %s)"
        valores = (c.nombre, c.estatus)

        connMySQL = ConexionMySQL()
        conn = connMySQL.abrir()
        cursor = conn.cursor()

        cursor.execute(sql, valores)
        conn.commit()

        id = cursor.lastrowid
        c.id = id

        cursor.close()
        connMySQL.cerrar()

        return id

    def update(self, c=None):
        sql = "UPDATE categoria SET nombre=%s, estatus=%s WHERE idCategoria=%s"
        valores = (c.nombre, c.estatus, c.id)

        connMySQL = ConexionMySQL()
        conn = connMySQL.abrir()
        cursor = conn.cursor()

        cursor.execute(sql, valores)
        conn.commit()

        i = cursor.rowcount

        cursor.close()
        connMySQL.cerrar()

        return i

    def delete(self, c=None):
        sql = "UPDATE categoria SET estatus=0 WHERE idCategoria=" + str(c.id)

        connMySQL = ConexionMySQL()
        conn = connMySQL.abrir()
        cursor = conn.cursor()

        cursor.execute(sql)
        conn.commit()

        i = cursor.rowcount

        cursor.close()
        connMySQL.cerrar()

        return i

    def search(self, busqueda=""):
        sql = "SELECT * FROM categoria WHERE SOUNDEX(nombre)=SOUNDEX('" + str(busqueda) + "')"

        connMySQL = ConexionMySQL()
        conn = connMySQL.abrir()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(sql)

        categoria = []

        for registro in cursor:
            c = self.fillDatos(registro)
            categoria.append(c)

        cursor.close()
        connMySQL.cerrar()

        return categoria
