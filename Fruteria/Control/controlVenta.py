from bd.conexion_mysql import ConexionMySQL
from Modelo.venta import Venta
from Modelo.vendedor import Vendedor

class ControlVenta:

    def getAll(self):
        sql = "SELECT * FROM venta"

        connMySQL = ConexionMySQL()
        conn = connMySQL.abrir()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql)
        ventas = []

        for registro in cursor:
            v = self.fillDatos(registro)
            ventas.append(v)

        cursor.close()
        connMySQL.cerrar()

        return ventas

    def fillDatos(self, registro=None):
        vendedor = Vendedor()
        vendedor.id = registro["idVendedor"]

        v = Venta()
        v.id = registro["idVenta"]
        v.vendedor = vendedor
        v.fecha = str(registro["fechaVenta"])

        return v

    def insert(self, v=None):
        sql = "INSERT INTO venta(idVendedor, fechaVenta) VALUES(%s, %s)"
        valores = (v.id, v.vendedor.id,v.fecha)

        connMySQL = ConexionMySQL()
        conn = connMySQL.abrir()
        cursor = conn.cursor()
        cursor.execute(sql, valores)
        conn.commit()
        id = cursor.lastrowid
        v.id = id
        cursor.close()
        connMySQL.cerrar()

        return id

    def update(self, v=None):
        sql = "UPDATE venta SET idVendedor=%s, fechaVenta=%s WHERE idVenta=%s"
        valores = (v.vendedor.id,v.fecha,v.id)

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
        sql = "DELETE FROM venta WHERE idVenta=" + str(v.id)

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
        sql = "SELECT * FROM venta WHERE fechaVenta LIKE '%" + str(busqueda) + "%'"

        connMySQL = ConexionMySQL()
        conn = connMySQL.abrir()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql)
        ventas = []

        for registro in cursor:
            v = self.fillDatos(registro)
            ventas.append(v)

        cursor.close()
        connMySQL.cerrar()

        return ventas