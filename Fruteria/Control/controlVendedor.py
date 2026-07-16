from bd.conexion_mysql import ConexionMySQL
from Modelo.vendedor import Vendedor

class ControlVendedor:

    def getAll(self):
        sql = "SELECT * FROM vendedor"

        connMySQL = ConexionMySQL()
        conn = connMySQL.abrir()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql)
        vendedores = []

        for registro in cursor:
            v = self.fillDatos(registro)
            vendedores.append(v)

        cursor.close()
        connMySQL.cerrar()

        return vendedores

    def fillDatos(self, registro=None):
        v = Vendedor()
        v.id = registro["idVendedor"]
        v.nombre = registro["nombre"]
        v.fechaNac = str(registro["fechaNac"])
        v.genero = registro["genero"]
        v.calle = registro["calle"]
        v.numeroExt = registro["numExt"]
        v.numeroInt = registro["numInt"]
        v.colonia = registro["colonia"]
        v.cp = registro["cp"]
        v.ciudad = registro["ciudad"]
        v.estado = registro["estado"]
        v.pais = registro["pais"]
        v.telefono = registro["telefono"]
        v.fechaAlta = str(registro["fechaAlta"])
        v.email = registro["email"]
        v.estatus = registro["estatus"]

        return v

    def insert(self, v=None):
        sql = "INSERT INTO vendedor(nombre, fechaNac, genero, calle, numExt, numInt,colonia, cp, ciudad, estado, pais,telefono, fechaAlta, email, estatus) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        valores = (v.nombre,v.fechaNac,v.genero,v.calle,v.numeroExt,v.numeroInt,v.colonia,v.cp,v.ciudad,v.estado,v.pais,v.telefono,v.fechaAlta,v.email,v.estatus)

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
        sql = "UPDATE vendedor SET nombre=%s,fechaNac=%s,genero=%s,calle=%s,numExt=%s,numInt=%s,colonia=%s,cp=%s,ciudad=%s,estado=%s,pais=%s,telefono=%s,fechaAlta=%s,email=%s,estatus=%s WHERE idVendedor=%s"
        valores = (v.nombre,v.fechaNac,v.genero,v.calle,v.numeroExt,v.numeroInt,v.colonia,v.cp,v.ciudad,v.estado,v.pais,v.telefono,v.fechaAlta,v.email,v.estatus,v.id)

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
        sql = "UPDATE vendedor SET estatus=0 WHERE idVendedor=" + str(v.id)

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
        sql = "SELECT * FROM vendedor WHERE SOUNDEX(nombre)=SOUNDEX('" + str(busqueda) + "')"

        connMySQL = ConexionMySQL()
        conn = connMySQL.abrir()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql)
        vendedores = []

        for registro in cursor:
            v = self.fillDatos(registro)
            vendedores.append(v)

        cursor.close()
        connMySQL.cerrar()

        return vendedores