from mysql.connector import Error
from conexion_mysql import ConexionMySQL

conn_mysql = ConexionMySQL()
print('Abriendo conexion con MySQL...')
conexion = conn_mysql.abrir()
print('Conexion Abierta...')
conn_mysql.cerrar()
print('Conexion cerrada')