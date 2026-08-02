import os
from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import QTableWidgetItem
from PySide6.QtWidgets import QMessageBox
import mysql.connector
from mysql.connector import Error
from modelo.compra import Compra
from modelo.proveedor import Proveedor
from control.controlcompra import ControlCompra
from control.controlproveedor import ControlProveedor

base_path = os.path.dirname(__file__)

ui_path = os.path.join(base_path, "compra.ui")

ui_form, base_class = loadUiType(ui_path)  # type: ignore


class FrameCompra(base_class, ui_form):
    def __init__(self):
        super().__init__()
        self.proveedor = []
        self.compra = []
        self.setupUi(self)
        self.cargar_catalogo_proveedor()
        self.__agregarListeners()
        self.__ver_compra()

    def __agregarListeners(self):
        self.btn_insertar_comp.clicked.connect(self.__insertar_compra)
        self.btn_eliminar_comp.clicked.connect(self.__eliminar_compra)
        self.btn_modificar_comp.clicked.connect(self.__modificar_compra)
        self.btn_vertodo_comp.clicked.connect(self.__ver_compra)
        self.btn_buscar_comp.clicked.connect(self.__buscar_compra)
        self.tbl_comp.itemClicked.connect(self.__seleccionar_compra)

    def cargar_catalogo_proveedor(self):
        try:
            self.cmb_proveedor_comp.clear()
            cp = ControlProveedor()
            self.proveedor = cp.getAll()

            for p in self.proveedor:
                self.cmb_proveedor_comp.addItem(p.nombre, p)

            self.cmb_proveedor_comp.setCurrentIndex(-1)
            self.cmb_proveedor_comp.setPlaceholderText("Selecciona un proveedor")

        except mysql.connector.Error as e:
            QMessageBox.critical(self,
                                 "Error en la conexión",
                                 "Ocurrió un error en la conexión a la base de datos: " + str(e))

    def __insertar_compra(self):
        try:
            c = Compra()
            c.proveedor = self.cmb_proveedor_comp.currentData()
            c.fecha = self.txt_fecha_comp.text().strip()
            c.hora = self.txt_hora_comp.text().strip()

            if c.proveedor is None:
                QMessageBox.warning(self,
                                    "Aviso",
                                    "Selecciona un proveedor")
                return

            cc = ControlCompra()
            id = cc.insert(c)

            if id > 0:  # type: ignore
                QMessageBox.information(self,
                                        "Inserción correcta",
                                        "La inserción de la compra se realizó correctamente")
                self.txt_id_comp.clear()
                self.txt_fecha_comp.clear()
                self.txt_hora_comp.clear()
                self.txt_buscar_comp.clear()
                self.cmb_proveedor_comp.setCurrentIndex(-1)
                self.__ver_compra()

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

        except Exception as ex:
            print(ex)
            QMessageBox.critical(self,
                                 "Error en la operación",
                                 "No fue posible insertar la compra: " + str(ex))

    def __ver_compra(self):
        try:
            cc = ControlCompra()
            self.compra = cc.getAll()

            self.tbl_comp.clearContents()
            self.tbl_comp.setColumnCount(4)
            self.tbl_comp.setRowCount(len(self.compra))
            self.tbl_comp.setHorizontalHeaderLabels([
                "ID", "PROVEEDOR", "FECHA", "HORA"
            ])

            for i in range(0, len(self.compra)):
                c = self.compra[i]
                self.tbl_comp.setItem(i, 0, QTableWidgetItem(str(c.id)))
                self.tbl_comp.setItem(i, 1, QTableWidgetItem(str(c.proveedor.nombre if c.proveedor is not None else "")))
                self.tbl_comp.setItem(i, 2, QTableWidgetItem(str(c.fecha)))
                self.tbl_comp.setItem(i, 3, QTableWidgetItem(str(c.hora)))

            self.tbl_comp.resizeColumnsToContents()

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
                                 "No fue posible consultar las compras: " + str(e))

    def __eliminar_compra(self):
        try:
            c = Compra()
            id_texto = self.txt_id_comp.text().strip()
            c.id = int(id_texto) if id_texto != "" else 0

            if c.id == 0:
                QMessageBox.warning(self,
                                    "Aviso",
                                    "Selecciona una compra para eliminar")
                return

            cc = ControlCompra()
            i = cc.delete(c)

            if i > 0:
                QMessageBox.information(self,
                                        "Exito en la operación",
                                        "Compra eliminada correctamente")
                self.txt_id_comp.clear()
                self.txt_fecha_comp.clear()
                self.txt_hora_comp.clear()
                self.txt_buscar_comp.clear()
                self.cmb_proveedor_comp.setCurrentIndex(-1)
                self.__ver_compra()

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
                                 "No fue posible eliminar la compra: " + str(e))

    def __buscar_compra(self):
        try:
            busqueda = self.txt_buscar_comp.text().strip()
            cc = ControlCompra()
            self.compra = cc.search(busqueda)

            self.tbl_comp.clearContents()
            self.tbl_comp.setColumnCount(4)
            self.tbl_comp.setRowCount(len(self.compra))
            self.tbl_comp.setHorizontalHeaderLabels([
                "ID", "PROVEEDOR", "FECHA", "HORA"
            ])

            for i in range(0, len(self.compra)):
                c = self.compra[i]
                self.tbl_comp.setItem(i, 0, QTableWidgetItem(str(c.id)))
                self.tbl_comp.setItem(i, 1, QTableWidgetItem(str(c.proveedor.nombre if c.proveedor is not None else "")))
                self.tbl_comp.setItem(i, 2, QTableWidgetItem(str(c.fecha)))
                self.tbl_comp.setItem(i, 3, QTableWidgetItem(str(c.hora)))

            self.tbl_comp.resizeColumnsToContents()

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
                                 "No fue posible buscar la compra: " + str(e))

    def __seleccionar_compra(self, item):
        try:
            pos = item.row()
            if pos < 0 or pos >= len(self.compra):
                return

            cs = self.compra[pos]
            self.txt_id_comp.setText(str(cs.id))
            self.txt_fecha_comp.setText(str(cs.fecha))
            self.txt_hora_comp.setText(str(cs.hora))

            if cs.proveedor is not None:
                for i in range(self.cmb_proveedor_comp.count()):
                    proveedor = self.cmb_proveedor_comp.itemData(i)
                    if proveedor is not None and proveedor.id == cs.proveedor.id:
                        self.cmb_proveedor_comp.setCurrentIndex(i)
                        break

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
                                 "No fue posible seleccionar la compra: " + str(e))
