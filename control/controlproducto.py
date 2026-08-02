from mysql.connector import Error
from bd.conexion_mysql import ConexionMySQL
from modelo.producto import Producto
from modelo.categoria import Categoria


class ControlProducto:

    def getAll(self):
        sql = "SELECT * FROM v_producto WHERE estatus = 1 ORDER BY idProducto"
        connMySQL = ConexionMySQL()
        conn = connMySQL.abrir()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql)
        productos = []

        for registro in cursor:  # type: ignore
            p = self.fillDatos(registro)
            productos.append(p)

        cursor.close()
        connMySQL.cerrar()
        return productos

    def fillDatos(self, registro=None):
        c = Categoria()
        c.id = registro["idCategoria"]  # type: ignore
        c.nombre = registro.get("nombreCategoria", "")  # type: ignore
        c.estatus = 1

        p = Producto()
        p.id = registro["idProducto"]  # type: ignore
        p.nombre = registro["nombre"]  # type: ignore
        p.preciocompra = registro["precioCompra"]  # type: ignore
        p.precioventa = registro["precioVenta"]  # type: ignore
        p.existencia = registro["existencia"]  # type: ignore
        p.estatus = registro["estatus"]  # type: ignore
        p.categoria = c
        return p

    def update(self, p=None):
        sql = """
            UPDATE producto
            SET nombre=%s, idCategoria=%s, precioCompra=%s, precioVenta=%s, existencia=%s, estatus=%s
            WHERE idProducto=%s
        """
        valores = (p.nombre, p.categoria.id, p.preciocompra, p.precioventa, p.existencia, p.estatus, p.id)  # type: ignore

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
        sql = "UPDATE producto SET estatus = 0 WHERE idProducto = %s"
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
            FROM v_producto
            WHERE estatus = 1
              AND (
                    nombre LIKE %s
                 OR nombreCategoria LIKE %s
                 OR SOUNDEX(nombre) = SOUNDEX(%s)
              )
            ORDER BY idProducto
        """
        texto = str(busqueda).strip()
        valor = "%" + texto + "%"
        valores = (valor, valor, texto)

        connMySQL = ConexionMySQL()
        conn = connMySQL.abrir()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql, valores)
        productos = []

        for registro in cursor:  # type: ignore
            p = self.fillDatos(registro)
            productos.append(p)

        cursor.close()
        connMySQL.cerrar()
        return productos
