from mysql.connector import Error
from bd.conexion_mysql import ConexionMySQL
from Modelo.producto import Producto
from Modelo.categoria import Categoria
 
 
class ControlProducto:
 
    def getAll(self):
        sql = "SELECT * FROM v_producto"
 
        connMySQL = ConexionMySQL()
        conn = connMySQL.abrir()
 
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql)
 
        productos = []
 
        for registro in cursor:
            p = self.fillDatos(registro)
            productos.append(p)

        cursor.close()
        connMySQL.cerrar()
        return productos
 
    def fillDatos(self, registro=None):
        c = Categoria()
        c.id = registro["idCategoria"]
        c.nombre = registro["nombreCategoria"]
        p = Producto()
        p.categoria = c
        p.id = registro["idProducto"]
        p.nombre = registro["nombre"]      
        p.precioCompra = registro["precioCompra"]
        p.precioVenta = registro["precioVenta"]
        p.existenciaDisponible = registro["existencia"]
        p.estatus = registro["estatus"]
        return p
    
    def insert(self, p = None):
        sql = "INSERT INTO producto (nombre, idCategoria, precioCompra, precioVenta, existencia, estatus) VALUES(%s, %s, %s, %s, %s, %s)"
        valores = (p.nombre, p.categoria.id, p.precioCompra, p.precioVenta, p.existenciaDisponible, p.estatus)
        connMySQL = None
        conn = None
        cursor = None

        connMySQL = ConexionMySQL()
        conn = connMySQL.abrir()
        cursor = conn.cursor()
        cursor.execute(sql,valores)
        conn.commit()
        id = cursor.lastrowid
        p.id = id 
        cursor.close()
        connMySQL.cerrar()
        return id 
    
    def update(self, p = None):
        sql = "UPDATE producto SET nombre=%s, idCategoria=%s, precioCompra=%s, precioVenta=%s, existencia=%s, estatus=%s WHERE idProducto=%s"
        valores = (p.nombre, p.categoria.id, p.precioCompra, p.precioVenta, p.existenciaDisponible, p.estatus, p.id)
        connMySQL = None
        conn = None
        cursor = None

        connMySQL = ConexionMySQL()
        conn = connMySQL.abrir()
        cursor = conn.cursor()
        cursor.execute(sql,valores)
        conn.commit()
        i = cursor.rowcount
        cursor.close()
        connMySQL.cerrar()
        return i
    
    def delete(self, p = None):
        sql = "UPDATE producto SET  estatus=0 WHERE idProducto="+str(p.id)
        connMySQL = None
        conn = None
        cursor = None
        connMySQL = ConexionMySQL()
        conn = connMySQL.abrir()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        i = cursor.rowcount
        cursor.close()
        connMySQL.cerrar()
        return i
    
    def search(self, busqueda = ""):
        sql = "SELECT * FROM v_producto WHERE SOUNDEX(nombre) = SOUNDEX('"+str(busqueda)+"')"
        connMySQL = None
        conn = None
        cursor = None
        productos = []

        connMySQL = ConexionMySQL()
        conn = connMySQL.abrir()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql)
 
        for registro in cursor:
            p = self.fillDatos(registro)
            productos.append(p)

        cursor.close()
        connMySQL.cerrar()

        return productos
    