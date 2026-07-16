from bd.conexion_mysql import ConexionMySQL
from Modelo.compra import Compra
from Modelo.proveedor import Proveedor

class ControlCompra:

    def getAll(self):
        sql = "SELECT * FROM compra"

        connMySQL = ConexionMySQL()
        conn = connMySQL.abrir()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql)
        compras = []

        for registro in cursor:
            c = self.fillDatos(registro)
            compras.append(c)
        cursor.close()
        connMySQL.cerrar()

        return compras

    def fillDatos(self, registro=None):
        p = Proveedor()
        p.id = registro["idProveedor"]
        c = Compra()
        c.id = registro["idCompra"]
        c.proveedor = p
        c.fecha = str(registro["fechaCompra"])
        return c

    def insert(self, c=None):
        sql = "INSERT INTO compra(idProveedor, fechaCompra) VALUES(%s, %s)"
        valores = (c.proveedor,c.fecha)

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
        sql = "UPDATE compra SET idProveedor=%s, fechaCompra=%s WHERE idCompra=%s"
        valores = (c.proveedor, c.fecha, c.id)
    
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
        sql = "DELETE FROM compra WHERE idCompra=" + str(c.id)
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
        sql = "SELECT * FROM compra WHERE fechaCompra LIKE '%" + str(busqueda) + "%'"
        connMySQL = ConexionMySQL()
        conn = connMySQL.abrir()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql)
        compra = []

        for registro in cursor:
            c = self.fillDatos(registro)
            compra.append(c)

        cursor.close()
        connMySQL.cerrar()

        return compra