from mysql.connector import Error
from bd.conexion_mysql import ConexionMySQL
from control.controlcategoria import ControlCategoria
from modelo.categoria import Categoria
from control.controlproducto import ControlProducto
from modelo.producto import Producto


p = Producto()
c = Categoria()
c.id = 1
p.id = 30
p.estatus = 1
p.existencia = 10
p.nombre = "Maracuya"
p.preciocompra = 50
p.precioventa = 70


controlProd = ControlProducto()
#r = controlProd.insert(p)
#r = controlProd.update(p)
#r = controlProd.delete(p)
#r = controlProd.search("Platanos")
#print(r)
 
"""""
controlProd = ControlProducto()
productos = controlProd.getAll()
for p in productos:
    print(p)
"""""
""""
controlCat= ControlCategoria()
Categorias = controlCat.getAll()
for c in Categorias:
    print(c)
"""
"""
conn_mysql = ConexionMySQL()
print("Abriendo conexion con Mysql...")
conecion = conn_mysql.abrir()
print("conexion abierta...")
conn_mysql.cerrar()
print("Conexion cerrada")
"""
 