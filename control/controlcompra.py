from mysql.connector import Error
from bd.conexion_mysql import ConexionMySQL
from modelo.compra import Compra
from modelo.proveedor import Proveedor


class ControlCompra:

    def getAll(self):
        sql = """
            SELECT C.idCompra, C.idProveedor, C.fechaCompra, P.nombre AS nombreProveedor
            FROM compra C
            INNER JOIN proveedor P ON C.idProveedor = P.idProveedor
            ORDER BY C.idCompra DESC
        """
        connMySQL = ConexionMySQL()
        conn = connMySQL.abrir()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql)
        compras = []

        for registro in cursor:  # type: ignore
            c = self.fillDatos(registro)
            compras.append(c)

        cursor.close()
        connMySQL.cerrar()
        return compras

    def fillDatos(self, registro=None):
        p = Proveedor()
        p.id = registro["idProveedor"]  # type: ignore
        p.nombre = registro.get("nombreProveedor", "")  # type: ignore

        c = Compra()
        c.id = registro["idCompra"]  # type: ignore
        c.proveedor = p
        c.fecha = str(registro["fechaCompra"]) if registro.get("fechaCompra") is not None else ""  # type: ignore
        c.hora = registro.get("horaCompra", "")  # type: ignore
        return c

    def insert(self, c=None):
        sql = "INSERT INTO compra(idProveedor, fechaCompra) VALUES(%s, %s)"
        valores = (c.proveedor.id, c.fecha)  # type: ignore

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

    def delete(self, c=None):
        sql_detalle = "DELETE FROM detalle_compra WHERE idCompra = %s"
        sql_compra = "DELETE FROM compra WHERE idCompra = %s"
        valores = (c.id,)  # type: ignore

        connMySQL = ConexionMySQL()
        conn = connMySQL.abrir()
        cursor = conn.cursor()
        cursor.execute(sql_detalle, valores)
        cursor.execute(sql_compra, valores)
        conn.commit()
        i = cursor.rowcount

        cursor.close()
        connMySQL.cerrar()
        return i

    def search(self, busqueda=" "):
        sql = """
            SELECT C.idCompra, C.idProveedor, C.fechaCompra, P.nombre AS nombreProveedor
            FROM compra C
            INNER JOIN proveedor P ON C.idProveedor = P.idProveedor
            WHERE CAST(C.fechaCompra AS CHAR) LIKE %s
               OR P.nombre LIKE %s
               OR SOUNDEX(P.nombre) = SOUNDEX(%s)
            ORDER BY C.idCompra DESC
        """
        texto = str(busqueda).strip()
        valor = "%" + texto + "%"
        valores = (valor, valor, texto)

        connMySQL = ConexionMySQL()
        conn = connMySQL.abrir()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql, valores)
        compras = []

        for registro in cursor:  # type: ignore
            c = self.fillDatos(registro)
            compras.append(c)

        cursor.close()
        connMySQL.cerrar()
        return compras
