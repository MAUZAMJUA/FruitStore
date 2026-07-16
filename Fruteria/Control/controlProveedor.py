from bd.conexion_mysql import ConexionMySQL
from Modelo.proveedor import Proveedor

class ControlProveedor:

    def getAll(self):
        sql = "SELECT * FROM proveedor"

        connMySQL = ConexionMySQL()
        conn = connMySQL.abrir()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql)
        proveedores = []

        for registro in cursor:
            p = self.fillDatos(registro)
            proveedores.append(p)

        cursor.close()
        connMySQL.cerrar()

        return proveedores

    def fillDatos(self, registro=None):
        p = Proveedor()
        p.id = registro["idProveedor"]
        p.nombre = registro["nombre"]
        p.razonSocial = registro["razonSocial"]
        p.RFC = registro["rfc"]
        p.direccion = registro["direccion"]
        p.email = registro["email"]
        p.tel = registro["telefonoFijo"]
        p.cel = registro["telefonoMovil"]
        p.estatus = registro["estatus"]

        return p

    def insert(self, p=None):
        sql = "INSERT INTO proveedor (nombre, razonSocial, rfc, direccion,email, telefonoFijo, telefonoMovil, estatus) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
        valores = (p.nombre,p.razonSocial,p.RFC,p.direccion,p.email,p.tel,p.cel,p.estatus)

        connMySQL = ConexionMySQL()
        conn = connMySQL.abrir()
        cursor = conn.cursor()
        cursor.execute(sql, valores)
        conn.commit()
        id = cursor.lastrowid
        p.id = id
        cursor.close()
        connMySQL.cerrar()

        return id

    def update(self, p=None):
        sql = "UPDATE proveedor SET nombre=%s,razonSocial=%s,rfc=%s,direccion=%s,email=%s,telefonoFijo=%s,telefonoMovil=%s,estatus=%s WHERE idProveedor=%s"
        valores = (p.nombre,p.razonSocial,p.RFC,p.direccion,p.email,p.tel,p.cel,p.estatus,p.id)

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
        sql = "UPDATE proveedor SET estatus=0 WHERE idProveedor=" + str(p.id)

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
        sql = "SELECT * FROM proveedor WHERE SOUNDEX(nombre)=SOUNDEX('" + str(busqueda) + "')"

        connMySQL = ConexionMySQL()
        conn = connMySQL.abrir()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql)
        proveedores = []

        for registro in cursor:
            p = self.fillDatos(registro)
            proveedores.append(p)

        cursor.close()
        connMySQL.cerrar()

        return proveedores