from mysql.connector import Error
from bd.conexion_mysql import ConexionMySQL
from modelo.venta import Venta
from modelo.vendedor import Vendedor


class ControlVenta:

    def getAll(self):
        sql = """
            SELECT  VT.idVenta,
                    VT.idVendedor,
                    DATE_FORMAT(VT.fechaVenta, '%Y-%m-%d') AS fechaVenta,
                    DATE_FORMAT(VT.fechaVenta, '%H:%i:%s') AS horaVenta,
                    VD.nombre AS nombreVendedor
            FROM venta VT
            INNER JOIN vendedor VD ON VT.idVendedor = VD.idVendedor
            ORDER BY VT.idVenta DESC
        """
        connMySQL = ConexionMySQL()
        conn = connMySQL.abrir()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql)
        ventas = []

        for registro in cursor:  # type: ignore
            v = self.fillDatos(registro)
            ventas.append(v)

        cursor.close()
        connMySQL.cerrar()
        return ventas

    def fillDatos(self, registro=None):
        vendedor = Vendedor()
        vendedor.id = registro["idVendedor"]  # type: ignore
        vendedor.nombre = registro.get("nombreVendedor", "")  # type: ignore

        v = Venta()
        v.id = registro["idVenta"]  # type: ignore
        v.vendedor = vendedor
        v.fecha = str(registro["fechaVenta"]) if registro.get("fechaVenta") is not None else ""  # type: ignore
        v.hora = str(registro.get("horaVenta", ""))  # type: ignore
        return v

    def insert(self, v=None):
        sql = "INSERT INTO venta(idVendedor, fechaVenta) VALUES(%s, %s)"
        fecha = str(v.fecha).strip()  # type: ignore
        hora = str(v.hora).strip()  # type: ignore
        if hora == "":
            hora = "00:00:00"
        if len(hora) == 5:
            hora = hora + ":00"
        fecha_hora = None if fecha == "" else fecha + " " + hora
        valores = (v.vendedor.id, fecha_hora)  # type: ignore

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

    def delete(self, v=None):
        sql_detalle = "DELETE FROM detalle_venta WHERE idVenta = %s"
        sql_venta = "DELETE FROM venta WHERE idVenta = %s"
        valores = (v.id,)  # type: ignore

        connMySQL = ConexionMySQL()
        conn = connMySQL.abrir()
        cursor = conn.cursor()
        cursor.execute(sql_detalle, valores)
        cursor.execute(sql_venta, valores)
        conn.commit()
        i = cursor.rowcount

        cursor.close()
        connMySQL.cerrar()
        return i

    def search(self, busqueda=" "):
        sql = """
            SELECT  VT.idVenta,
                    VT.idVendedor,
                    DATE_FORMAT(VT.fechaVenta, '%Y-%m-%d') AS fechaVenta,
                    DATE_FORMAT(VT.fechaVenta, '%H:%i:%s') AS horaVenta,
                    VD.nombre AS nombreVendedor
            FROM venta VT
            INNER JOIN vendedor VD ON VT.idVendedor = VD.idVendedor
            WHERE CAST(VT.fechaVenta AS CHAR) LIKE %s
               OR VD.nombre LIKE %s
               OR SOUNDEX(VD.nombre) = SOUNDEX(%s)
            ORDER BY VT.idVenta DESC
        """
        texto = str(busqueda).strip()
        valor = "%" + texto + "%"
        valores = (valor, valor, texto)

        connMySQL = ConexionMySQL()
        conn = connMySQL.abrir()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql, valores)
        ventas = []

        for registro in cursor:  # type: ignore
            v = self.fillDatos(registro)
            ventas.append(v)

        cursor.close()
        connMySQL.cerrar()
        return ventas
