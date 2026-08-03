from mysql.connector import Error
from bd.conexion_mysql import ConexionMySQL
from modelo.vendedor import Vendedor


class ControlVendedor:

    def getAll(self):
        sql = "SELECT * FROM v_vendedor WHERE estatus = 1 ORDER BY idVendedor"
        connMySQL = ConexionMySQL()
        conn = connMySQL.abrir()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql)
        vendedores = []

        for registro in cursor:  # type: ignore
            v = self.fillDatos(registro)
            vendedores.append(v)

        cursor.close()
        connMySQL.cerrar()
        return vendedores

    def fillDatos(self, registro=None):
        v = Vendedor()
        v.id = registro["idVendedor"]  # type: ignore
        v.nombre = registro["nombre"]  # type: ignore
        v.fecha_nacimiento = str(registro["fechaNac"]) if registro.get("fechaNac") is not None else ""  # type: ignore
        v.genero = registro["genero"]  # type: ignore
        v.calle = registro["calle"]  # type: ignore
        v.num_ext = registro["numExt"]  # type: ignore
        v.num_int = registro["numInt"]  # type: ignore
        v.colonia = registro["colonia"]  # type: ignore
        v.CP = registro.get("CP", registro.get("cp", ""))  # type: ignore
        v.ciudad = registro["ciudad"]  # type: ignore
        v.estado = registro["estado"]  # type: ignore
        v.pais = registro["pais"]  # type: ignore
        v.tel = registro["telefono"]  # type: ignore
        v.fecha_ingreso = str(registro["fechaAlta"]) if registro.get("fechaAlta") is not None else ""  # type: ignore
        v.email = registro["email"]  # type: ignore
        v.estatus = registro["estatus"]  # type: ignore
        return v

    def insert(self, v=None):
        sql = """
            INSERT INTO vendedor(nombre, fechaNac, genero, calle, numExt, numInt, colonia, cp,
                                 ciudad, estado, pais, telefono, fechaAlta, email, estatus)
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        valores = (v.nombre, v.fecha_nacimiento, v.genero, v.calle, v.num_ext, v.num_int, v.colonia,
                   v.CP, v.ciudad, v.estado, v.pais, v.tel, v.fecha_ingreso, v.email, v.estatus)  # type: ignore

        connMySQL = ConexionMySQL()
        conn = connMySQL.abrir()
        cursor = conn.cursor()
        cursor.execute(sql, valores)
        conn.commit()
        id = cursor.lastrowid
        v.id = id  # type: ignore

        cursor.close()
        connMySQL.cerrar()
        return id

    def update(self, v=None):
        sql = """
            UPDATE vendedor
            SET nombre=%s, fechaNac=%s, genero=%s, calle=%s, numExt=%s, numInt=%s,
                colonia=%s, cp=%s, ciudad=%s, estado=%s, pais=%s, telefono=%s,
                fechaAlta=%s, email=%s, estatus=%s
            WHERE idVendedor=%s
        """
        valores = (v.nombre, v.fecha_nacimiento, v.genero, v.calle, v.num_ext, v.num_int, v.colonia,
                   v.CP, v.ciudad, v.estado, v.pais, v.tel, v.fecha_ingreso, v.email, v.estatus, v.id)  # type: ignore

        connMySQL = ConexionMySQL()
        conn = connMySQL.abrir()
        cursor = conn.cursor()
        cursor.execute(sql, valores)
        conn.commit()
        i = cursor.rowcount

        cursor.close()
        connMySQL.cerrar()
        return i

    def delete(self, v=None):
        sql = "UPDATE vendedor SET estatus = 0 WHERE idVendedor = %s"
        valores = (v.id,)  # type: ignore

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
            FROM v_vendedor
            WHERE estatus = 1
              AND (
                    nombre LIKE %s
                 OR email LIKE %s
                 OR telefono LIKE %s
                 OR SOUNDEX(nombre) = SOUNDEX(%s)
              )
            ORDER BY idVendedor
        """
        texto = str(busqueda).strip()
        valor = "%" + texto + "%"
        valores = (valor, valor, valor, texto)

        connMySQL = ConexionMySQL()
        conn = connMySQL.abrir()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql, valores)
        vendedores = []

        for registro in cursor:  # type: ignore
            v = self.fillDatos(registro)
            vendedores.append(v)

        cursor.close()
        connMySQL.cerrar()
        return vendedores
