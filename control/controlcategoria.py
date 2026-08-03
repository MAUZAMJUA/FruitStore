from mysql.connector import Error
from bd.conexion_mysql import ConexionMySQL
from modelo.categoria import Categoria


class ControlCategoria:

    def getAll(self):
        sql = "SELECT * FROM categoria WHERE estatus = 1 ORDER BY idCategoria"
        connMySQL = ConexionMySQL()
        conn = connMySQL.abrir()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql)
        categorias = []

        for registro in cursor:  # type: ignore
            c = self.fillDatos(registro)
            categorias.append(c)

        cursor.close()
        connMySQL.cerrar()
        return categorias

    def fillDatos(self, registro=None):
        c = Categoria()
        c.id = registro["idCategoria"]  # type: ignore
        c.nombre = registro["nombre"]  # type: ignore
        c.estatus = registro["estatus"]  # type: ignore
        return c

    def insert(self, c=None):
        sql = "INSERT INTO categoria(nombre, estatus) VALUES(%s, %s)"
        valores = (c.nombre, c.estatus)  # type: ignore

        connMySQL = ConexionMySQL()
        conn = connMySQL.abrir()
        cursor = conn.cursor()
        cursor.execute(sql, valores)
        conn.commit()
        id = cursor.lastrowid
        c.id = id  # type: ignore

        cursor.close()
        connMySQL.cerrar()
        return id

    def update(self, c=None):
        sql = "UPDATE categoria SET nombre=%s, estatus=%s WHERE idCategoria=%s"
        valores = (c.nombre, c.estatus, c.id)  # type: ignore

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
        sql = "UPDATE categoria SET estatus = 0 WHERE idCategoria = %s"
        valores = (c.id,)  # type: ignore

        connMySQL = ConexionMySQL()
        conn = connMySQL.abrir()
        cursor = conn.cursor()
        cursor.execute(sql, valores)
        conn.commit()
        i = cursor.rowcount

        cursor.close()
        connMySQL.cerrar()
        return i

    def search(self, busqueda=" "):
        sql = """
            SELECT *
            FROM categoria
            WHERE estatus = 1
              AND (nombre LIKE %s OR SOUNDEX(nombre) = SOUNDEX(%s))
            ORDER BY idCategoria
        """
        valor = "%" + str(busqueda).strip() + "%"
        valores = (valor, str(busqueda).strip())

        connMySQL = ConexionMySQL()
        conn = connMySQL.abrir()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql, valores)
        categorias = []

        for registro in cursor:  # type: ignore
            c = self.fillDatos(registro)
            categorias.append(c)

        cursor.close()
        connMySQL.cerrar()
        return categorias
