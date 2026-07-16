from mysql.connector import Error
from bd.conexion_mysql import ConexionMySQL
from Control.controlCategoria import ControlCategoria
from Modelo.categoria import Categoria
from Control.controlProducto import ControlProducto
from Modelo.producto import Producto
 
 
p = Producto()
c = Categoria()
c.id = 1
p.categoria = c
p.id = 30
p.estatus = 1
p.existenciaDisponible = 10
p.nombre = "Maracuya"
p.precioCompra = 50
p.precioVenta = 70
 
 
controlProd = ControlProducto()
r = controlProd.insert(p)
r = controlProd.update(p)
r = controlProd.delete(p)
r = controlProd.search("Platanos")
print(r)
 

controlProd = ControlProducto()
productos = controlProd.getAll()
for p in productos:
    print(p)

controlCat= ControlCategoria()
Categorias = controlCat.getAll()
for c in Categorias:
    print(c)

conn_mysql = ConexionMySQL()
print("Abriendo conexion con Mysql...")
conecion = conn_mysql.abrir()
print("conexion abierta...")
conn_mysql.cerrar()
print("Conexion cerrada")