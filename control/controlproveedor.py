from mysql.connector import Error
from bd.conexion_mysql import ConexionMySQL
from modelo.proveedor import Proveedor


class ControlProveedor:

    def getAll(self):
        sql = "SELECT * FROM proveedor WHERE estatus = 1 ORDER BY idProveedor"
        connMySQL = ConexionMySQL()
        conn = connMySQL.abrir()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql)
        proveedores = []

        for registro in cursor:  # type: ignore
            p = self.fillDatos(registro)
            proveedores.append(p)

        cursor.close()
        connMySQL.cerrar()
        return proveedores

    def fillDatos(self, registro=None):
        p = Proveedor()
        p.id = registro["idProveedor"]  # type: ignore
        p.nombre = registro["nombre"]  # type: ignore
        p.razon_social = registro["razonSocial"]  # type: ignore
        p.RFC = registro["rfc"]  # type: ignore
        p.direccion = registro["direccion"]  # type: ignore
        p.email = registro["email"]  # type: ignore
        p.tel = registro["telefonoFijo"]  # type: ignore
        p.cel = registro["telefonoMovil"]  # type: ignore
        p.estatus = registro["estatus"]  # type: ignore
        return p

    def insert(self, p=None):
        sql = """
            INSERT INTO proveedor(nombre, razonSocial, rfc, direccion, email, telefonoFijo, telefonoMovil, estatus)
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s)
        """
        valores = (p.nombre, p.razon_social, p.RFC, p.direccion, p.email, p.tel, p.cel, p.estatus)  # type: ignore

        connMySQL = ConexionMySQL()
        conn = connMySQL.abrir()
        cursor = conn.cursor()
        cursor.execute(sql, valores)
        conn.commit()
        id = cursor.lastrowid
        p.id = id  # type: ignore

        cursor.close()
        connMySQL.cerrar()
        return id

    def update(self, p=None):
        sql = """
            UPDATE proveedor
            SET nombre=%s, razonSocial=%s, rfc=%s, direccion=%s, email=%s,
                telefonoFijo=%s, telefonoMovil=%s, estatus=%s
            WHERE idProveedor=%s
        """
        valores = (p.nombre, p.razon_social, p.RFC, p.direccion, p.email, p.tel, p.cel, p.estatus, p.id)  # type: ignore

        connMySQL = ConexionMySQL()
        conn = connMySQL.abrir()
        cursor = conn.cursor()
        cursor.execute(sql, valores)
        conn.commit()
        i = cursor.rowcount

        cursor.close()
        connMySQL.cerrar()
        return i

    def delete(self, p=None):
        sql = "UPDATE proveedor SET estatus = 0 WHERE idProveedor = %s"
        valores = (p.id,)  # type: ignore

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
            FROM proveedor
            WHERE estatus = 1
              AND (
                    nombre LIKE %s
                 OR razonSocial LIKE %s
                 OR rfc LIKE %s
                 OR SOUNDEX(nombre) = SOUNDEX(%s)
              )
            ORDER BY idProveedor
        """
        texto = str(busqueda).strip()
        valor = "%" + texto + "%"
        valores = (valor, valor, valor, texto)

        connMySQL = ConexionMySQL()
        conn = connMySQL.abrir()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql, valores)
        proveedores = []

        for registro in cursor:  # type: ignore
            p = self.fillDatos(registro)
            proveedores.append(p)

        cursor.close()
        connMySQL.cerrar()
        return proveedores
