import os
from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import QTableWidgetItem
from PySide6.QtWidgets import QMessageBox
import mysql.connector
from mysql.connector import Error
from modelo.producto import Producto
from modelo.categoria import Categoria
from control.controlproducto import ControlProducto
from control.controlcategoria import ControlCategoria

base_path = os.path.dirname(__file__)

ui_path = os.path.join(base_path, "producto.ui")

ui_form, base_class = loadUiType(ui_path)  # type: ignore


class FrameProducto(base_class, ui_form):
    def __init__(self):
        super().__init__()
        self.categorias = []
        self.producto = []
        self.setupUi(self)
        self.cargar_catalogo_categorias()
        self.__agregarListeners()
        self.__ver_producto()

    def __agregarListeners(self):
        self.btn_eliminar_prod.clicked.connect(self.__eliminar_producto)
        self.btn_modificar_prod.clicked.connect(self.__modificar_producto)
        self.btn_ver_prod.clicked.connect(self.__ver_producto)
        self.btn_buscar_prod.clicked.connect(self.__buscar_producto)
        self.tbl_prod.itemClicked.connect(self.__seleccionar_producto)

    def cargar_catalogo_categorias(self):
        try:
            self.cmb_categoria_prod.clear()
            cc = ControlCategoria()
            self.categorias = cc.getAll()

            for c in self.categorias:
                self.cmb_categoria_prod.addItem(c.nombre, c)

            self.cmb_categoria_prod.setCurrentIndex(-1)
            self.cmb_categoria_prod.setPlaceholderText("Selecciona una categoría")
        except mysql.connector.Error as e:
            QMessageBox.critical(self,
                                 "Error en la conexión",
                                 "Ocurrión un error en la conexión a la base de datos: " + str(e))

    def __modificar_producto(self):
        try:
            p = Producto()
            id_texto = self.txt_id_prod.text().strip()
            p.id = int(id_texto) if id_texto != "" else 0
            p.categoria = self.cmb_categoria_prod.currentData()
            p.estatus = 1 if self.chb_estatus_prod.isChecked() else 0
            p.existencia = int(self.txt_existencia_prod.text().strip())
            p.nombre = self.txt_nombre_prod.text().strip()
            p.preciocompra = float(self.txt_precio_compra_prod.text().strip())
            p.precioventa = float(self.txt_precio_venta_prod.text().strip())

            if p.id == 0:
                QMessageBox.warning(self,
                                    "Aviso",
                                    "Selecciona un producto para modificar")
                return
            if p.categoria is None:
                QMessageBox.warning(self,
                                    "Aviso",
                                    "Selecciona una categoría")
                return

            cp = ControlProducto()
            i = cp.update(p)

            if i > 0:
                QMessageBox.information(self,
                                        "Exito en la operación",
                                        "Producto actualizado correctamente")
                self.txt_id_prod.clear()
                self.txt_nombre_prod.clear()
                self.txt_precio_compra_prod.clear()
                self.txt_precio_venta_prod.clear()
                self.txt_existencia_prod.clear()
                self.txt_buscar_prod.clear()
                self.cmb_categoria_prod.setCurrentIndex(-1)
                self.chb_estatus_prod.setChecked(True)
                self.__ver_producto()

        except mysql.connector.Error as e:
            print(e)
            QMessageBox.critical(self,
                                 "Error en la conexión",
                                 "Ocurrió un error en la conexión con la base de datos: " + str(e))

        except ValueError as ve:
            print(ve)
            QMessageBox.warning(self,
                                "Valor inválido",
                                "Asegurate de que los datos capturados son correctos: " + str(ve))

        except Exception as e:
            print(e)
            QMessageBox.critical(self,
                                 "Error en la operación",
                                 "No fue posible actualizar el producto: " + str(e))

    def __ver_producto(self):
        try:
            cp = ControlProducto()
            self.producto = cp.getAll()

            self.tbl_prod.clearContents()
            self.tbl_prod.setColumnCount(7)
            self.tbl_prod.setRowCount(len(self.producto))
            self.tbl_prod.setHorizontalHeaderLabels([
                "ID", "NOMBRE", "CATEGORIA", "PRECIO COMPRA",
                "PRECIO VENTA", "EXISTENCIA", "ESTATUS"
            ])

            for i in range(0, len(self.producto)):
                p = self.producto[i]
                self.tbl_prod.setItem(i, 0, QTableWidgetItem(str(p.id)))
                self.tbl_prod.setItem(i, 1, QTableWidgetItem(str(p.nombre)))
                self.tbl_prod.setItem(i, 2, QTableWidgetItem(str(p.categoria.nombre if p.categoria is not None else "")))
                self.tbl_prod.setItem(i, 3, QTableWidgetItem(str(p.preciocompra)))
                self.tbl_prod.setItem(i, 4, QTableWidgetItem(str(p.precioventa)))
                self.tbl_prod.setItem(i, 5, QTableWidgetItem(str(p.existencia)))
                self.tbl_prod.setItem(i, 6, QTableWidgetItem(str(p.estatus)))

            self.tbl_prod.resizeColumnsToContents()

        except mysql.connector.Error as e:
            print(e)
            QMessageBox.critical(self,
                                 "Error en la conexión",
                                 "Ocurrió un error en la conexión con la base de datos: " + str(e))
            
        except ValueError as ve:
            print(ve)
            QMessageBox.warning(self,
                                "Valor inválido",
                                "Asegurate de que los datos capturados son correctos: " + str(ve))

        except Exception as e:
            print(e)
            QMessageBox.critical(self,
                                 "Error en la operación",
                                 "No fue posible consultar los productos: " + str(e))

    def __eliminar_producto(self):
        try:
            p = Producto()
            id_texto = self.txt_id_prod.text().strip()
            p.id = int(id_texto) if id_texto != "" else 0

            if p.id == 0:
                QMessageBox.warning(self,
                                    "Aviso",
                                    "Selecciona un producto para eliminar")
                return

            cp = ControlProducto()
            i = cp.delete(p)

            if i > 0:
                QMessageBox.information(self,
                                        "Exito en la operación",
                                        "Producto eliminado correctamente")
                self.txt_id_prod.clear()
                self.txt_nombre_prod.clear()
                self.txt_precio_compra_prod.clear()
                self.txt_precio_venta_prod.clear()
                self.txt_existencia_prod.clear()
                self.txt_buscar_prod.clear()
                self.cmb_categoria_prod.setCurrentIndex(-1)
                self.chb_estatus_prod.setChecked(True)
                self.__ver_producto()

        except mysql.connector.Error as e:
            print(e)
            QMessageBox.critical(self,
                                 "Error en la conexión",
                                 "Ocurrió un error en la conexión con la base de datos: " + str(e))
        
        except ValueError as ve:
            print(ve)
            QMessageBox.warning(self,
                                "Valor inválido",
                                "Asegurate de que los datos capturados son correctos: " + str(ve))

        except Exception as e:
            QMessageBox.critical(self,
                                 "Error en la operación",
                                 "No fue posible eliminar el producto: " + str(e))

    def __buscar_producto(self):
        try:
            busqueda = self.txt_buscar_prod.text().strip()
            cp = ControlProducto()
            self.producto = cp.search(busqueda)

            self.tbl_prod.clearContents()
            self.tbl_prod.setColumnCount(7)
            self.tbl_prod.setRowCount(len(self.producto))
            self.tbl_prod.setHorizontalHeaderLabels([
                "ID", "NOMBRE", "CATEGORIA", "PRECIO COMPRA",
                "PRECIO VENTA", "EXISTENCIA", "ESTATUS"
            ])

            for i in range(0, len(self.producto)):
                p = self.producto[i]
                self.tbl_prod.setItem(i, 0, QTableWidgetItem(str(p.id)))
                self.tbl_prod.setItem(i, 1, QTableWidgetItem(str(p.nombre)))
                self.tbl_prod.setItem(i, 2, QTableWidgetItem(str(p.categoria.nombre if p.categoria is not None else "")))
                self.tbl_prod.setItem(i, 3, QTableWidgetItem(str(p.preciocompra)))
                self.tbl_prod.setItem(i, 4, QTableWidgetItem(str(p.precioventa)))
                self.tbl_prod.setItem(i, 5, QTableWidgetItem(str(p.existencia)))
                self.tbl_prod.setItem(i, 6, QTableWidgetItem(str(p.estatus)))

            self.tbl_prod.resizeColumnsToContents()

        except mysql.connector.Error as e:
            print(e)
            QMessageBox.critical(self,
                                 "Error en la conexión",
                                 "Ocurrió un error en la conexión con la base de datos: " + str(e))
            
        except ValueError as ve:
            print(ve)
            QMessageBox.warning(self,
                                "Valor inválido",
                                "Asegurate de que los datos capturados son correctos: " + str(ve))
            
        except Exception as e:
            QMessageBox.critical(self,
                                 "Error en la operación",
                                 "No fue posible buscar el producto: " + str(e))

    def __seleccionar_producto(self, item):
        try:
            pos = item.row()
            if pos < 0 or pos >= len(self.producto):
                return

            ps = self.producto[pos]
            self.txt_id_prod.setText(str(ps.id))
            self.txt_nombre_prod.setText(str(ps.nombre))
            self.txt_precio_compra_prod.setText(str(ps.preciocompra))
            self.txt_precio_venta_prod.setText(str(ps.precioventa))
            self.txt_existencia_prod.setText(str(ps.existencia))

            if ps.categoria is not None:
                for i in range(self.cmb_categoria_prod.count()):
                    categoria = self.cmb_categoria_prod.itemData(i)
                    if categoria is not None and categoria.id == ps.categoria.id:
                        self.cmb_categoria_prod.setCurrentIndex(i)
                        break

            if ps.estatus == 1:
                self.chb_estatus_prod.setChecked(True)
            else:
                self.chb_estatus_prod.setChecked(False)

        except mysql.connector.Error as e:
            print(e)
            QMessageBox.critical(self,
                                 "Error en la conexión",
                                 "Ocurrió un error en la conexión con la base de datos: " + str(e))
            
        except ValueError as ve:
            print(ve)
            QMessageBox.warning(self,
                                "Valor inválido",
                                "Asegurate de que los datos capturados son correctos: " + str(ve))
            
        except Exception as e:
            print(e)
            QMessageBox.critical(self,
                                 "Error en la operación",
                                 "No fue posible seleccionar el producto: " + str(e))
        
