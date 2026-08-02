import os
from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import QTableWidgetItem
from PySide6.QtWidgets import QMessageBox
import mysql.connector
from mysql.connector import Error
from modelo.venta import Venta
from modelo.vendedor import Vendedor
from control.controlventa import ControlVenta
from control.controlvendedor import ControlVendedor

base_path = os.path.dirname(__file__)

ui_path = os.path.join(base_path, "venta.ui")

ui_form, base_class = loadUiType(ui_path)  # type: ignore


class FrameVenta(base_class, ui_form):
    def __init__(self):
        super().__init__()
        self.vendedor = []
        self.venta = []
        self.setupUi(self)
        self.cargar_catalogo_vendedor()
        self.__agregarListeners()
        self.__ver_venta()

    def __agregarListeners(self):
        self.btn_insertar_vent.clicked.connect(self.__insertar_venta)
        self.btn_eliminar_vent.clicked.connect(self.__eliminar_venta)
        self.btn_modificar_vent.clicked.connect(self.__modificar_venta)
        self.btn_vertodo_vent.clicked.connect(self.__ver_venta)
        self.btn_buscar_vent.clicked.connect(self.__buscar_venta)
        self.tbl_vent.itemClicked.connect(self.__seleccionar_venta)

    def cargar_catalogo_vendedor(self):
        try:
            self.cmb_vendedor_vent.clear()
            cv = ControlVendedor()
            self.vendedor = cv.getAll()

            for v in self.vendedor:
                self.cmb_vendedor_vent.addItem(v.nombre, v)

            self.cmb_vendedor_vent.setCurrentIndex(-1)
            self.cmb_vendedor_vent.setPlaceholderText("Selecciona un vendedor")

        except mysql.connector.Error as e:
            QMessageBox.critical(self,
                                 "Error en la conexión",
                                 "Ocurrió un error en la conexión a la base de datos: " + str(e))

    def __insertar_venta(self):
        try:
            v = Venta()
            v.vendedor = self.cmb_vendedor_vent.currentData()
            v.fecha = self.txt_fecha_vent.text().strip()
            v.hora = self.txt_hora_vent.text().strip()

            if v.vendedor is None:
                QMessageBox.warning(self,
                                    "Aviso",
                                    "Selecciona un vendedor")
                return

            cv = ControlVenta()
            id = cv.insert(v)

            if id > 0:  # type: ignore
                QMessageBox.information(self,
                                        "Inserción correcta",
                                        "La inserción de la venta se realizó correctamente")
                self.txt_id_vent.clear()
                self.txt_fecha_vent.clear()
                self.txt_hora_vent.clear()
                self.txt_buscar_vent.clear()
                self.cmb_vendedor_vent.setCurrentIndex(-1)
                self.__ver_venta()

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
                                 "No fue posible insertar la venta: " + str(ex))

    def __ver_venta(self):
        try:
            cv = ControlVenta()
            self.venta = cv.getAll()

            self.tbl_vent.clearContents()
            self.tbl_vent.setColumnCount(4)
            self.tbl_vent.setRowCount(len(self.venta))
            self.tbl_vent.setHorizontalHeaderLabels([
                "ID", "VENDEDOR", "FECHA", "HORA"
            ])

            for i in range(0, len(self.venta)):
                v = self.venta[i]
                self.tbl_vent.setItem(i, 0, QTableWidgetItem(str(v.id)))
                self.tbl_vent.setItem(i, 1, QTableWidgetItem(str(v.vendedor.nombre if v.vendedor is not None else "")))
                self.tbl_vent.setItem(i, 2, QTableWidgetItem(str(v.fecha)))
                self.tbl_vent.setItem(i, 3, QTableWidgetItem(str(v.hora)))

            self.tbl_vent.resizeColumnsToContents()

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
                                 "No fue posible consultar las ventas: " + str(e))

    def __eliminar_venta(self):
        try:
            v = Venta()
            id_texto = self.txt_id_vent.text().strip()
            v.id = int(id_texto) if id_texto != "" else 0

            if v.id == 0:
                QMessageBox.warning(self,
                                    "Aviso",
                                    "Selecciona una venta para eliminar")
                return

            cv = ControlVenta()
            i = cv.delete(v)

            if i > 0:
                QMessageBox.information(self,
                                        "Exito en la operación",
                                        "Venta eliminada correctamente")
                self.txt_id_vent.clear()
                self.txt_fecha_vent.clear()
                self.txt_hora_vent.clear()
                self.txt_buscar_vent.clear()
                self.cmb_vendedor_vent.setCurrentIndex(-1)
                self.__ver_venta()

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
                                 "No fue posible eliminar la venta: " + str(e))

    def __buscar_venta(self):
        try:
            busqueda = self.txt_buscar_vent.text().strip()
            cv = ControlVenta()
            self.venta = cv.search(busqueda)

            self.tbl_vent.clearContents()
            self.tbl_vent.setColumnCount(4)
            self.tbl_vent.setRowCount(len(self.venta))
            self.tbl_vent.setHorizontalHeaderLabels([
                "ID", "VENDEDOR", "FECHA", "HORA"
            ])

            for i in range(0, len(self.venta)):
                v = self.venta[i]
                self.tbl_vent.setItem(i, 0, QTableWidgetItem(str(v.id)))
                self.tbl_vent.setItem(i, 1, QTableWidgetItem(str(v.vendedor.nombre if v.vendedor is not None else "")))
                self.tbl_vent.setItem(i, 2, QTableWidgetItem(str(v.fecha)))
                self.tbl_vent.setItem(i, 3, QTableWidgetItem(str(v.hora)))

            self.tbl_vent.resizeColumnsToContents()

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
                                 "No fue posible buscar la venta: " + str(e))

    def __seleccionar_venta(self, item):
        try:
            pos = item.row()
            if pos < 0 or pos >= len(self.venta):
                return

            vs = self.venta[pos]
            self.txt_id_vent.setText(str(vs.id))
            self.txt_fecha_vent.setText(str(vs.fecha))
            self.txt_hora_vent.setText(str(vs.hora))

            if vs.vendedor is not None:
                for i in range(self.cmb_vendedor_vent.count()):
                    vendedor = self.cmb_vendedor_vent.itemData(i)
                    if vendedor is not None and vendedor.id == vs.vendedor.id:
                        self.cmb_vendedor_vent.setCurrentIndex(i)
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
                                 "No fue posible seleccionar la venta: " + str(e))
