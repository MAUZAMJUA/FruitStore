import os
from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import QTableWidgetItem
from PySide6.QtWidgets import QMessageBox
import mysql.connector
from mysql.connector import Error
from modelo.proveedor import Proveedor
from control.controlproveedor import ControlProveedor

base_path = os.path.dirname(__file__)

ui_path = os.path.join(base_path, "proveedor.ui")

ui_form, base_class = loadUiType(ui_path)  # type: ignore


class FrameProveedor(base_class, ui_form):
    def __init__(self):
        super().__init__()
        self.proveedor = []
        self.setupUi(self)
        self.__agregarListeners()
        self.__ver_proveedor()

    def __agregarListeners(self):
        self.btn_insertar_prov.clicked.connect(self.__insertar_proveedor)
        self.btn_eliminar_prov.clicked.connect(self.__eliminar_proveedor)
        self.btn_modificar_prov.clicked.connect(self.__modificar_proveedor)
        self.btn_vertodo_prov.clicked.connect(self.__ver_proveedor)
        self.btn_buscar_prov.clicked.connect(self.__buscar_proveedor)
        self.tbl_prov.itemClicked.connect(self.__seleccionar_proveedor)

    def __insertar_proveedor(self):
        try:
            p = Proveedor()
            p.nombre = self.txt_nombre_prov.text().strip()
            p.razon_social = self.txt_razon_social_prov.text().strip()
            p.RFC = self.txt_rfc_prov.text().strip()
            p.direccion = self.txt_direccion_prov.text().strip()
            p.email = self.txt_email_prov.text().strip()
            p.tel = self.txt_tel_prov.text().strip()
            p.cel = self.txt_cel_prov.text().strip()
            p.estatus = 1 if self.chb_estatus_prov.isChecked() else 0

            cp = ControlProveedor()
            id = cp.insert(p)

            if id > 0:  # type: ignore
                QMessageBox.information(self,
                                        "Inserción correcta",
                                        "La inserción del proveedor se realizó correctamente")
                self.txt_id_prov.clear()
                self.txt_nombre_prov.clear()
                self.txt_razon_social_prov.clear()
                self.txt_rfc_prov.clear()
                self.txt_direccion_prov.clear()
                self.txt_email_prov.clear()
                self.txt_tel_prov.clear()
                self.txt_cel_prov.clear()
                self.txt_buscar_prov.clear()
                self.chb_estatus_prov.setChecked(True)
                self.__ver_proveedor()

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
                                 "No fue posible insertar el proveedor: " + str(ex))

    def __modificar_proveedor(self):
        try:
            p = Proveedor()
            id_texto = self.txt_id_prov.text().strip()
            p.id = int(id_texto) if id_texto != "" else 0
            p.nombre = self.txt_nombre_prov.text().strip()
            p.razon_social = self.txt_razon_social_prov.text().strip()
            p.RFC = self.txt_rfc_prov.text().strip()
            p.direccion = self.txt_direccion_prov.text().strip()
            p.email = self.txt_email_prov.text().strip()
            p.tel = self.txt_tel_prov.text().strip()
            p.cel = self.txt_cel_prov.text().strip()
            p.estatus = 1 if self.chb_estatus_prov.isChecked() else 0

            if p.id == 0:
                QMessageBox.warning(self,
                                    "Aviso",
                                    "Selecciona un proveedor para modificar")
                return

            cp = ControlProveedor()
            i = cp.update(p)

            if i > 0:
                QMessageBox.information(self,
                                        "Exito en la operación",
                                        "Proveedor actualizado correctamente")
                self.txt_id_prov.clear()
                self.txt_nombre_prov.clear()
                self.txt_razon_social_prov.clear()
                self.txt_rfc_prov.clear()
                self.txt_direccion_prov.clear()
                self.txt_email_prov.clear()
                self.txt_tel_prov.clear()
                self.txt_cel_prov.clear()
                self.txt_buscar_prov.clear()
                self.chb_estatus_prov.setChecked(True)
                self.__ver_proveedor()

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
                                 "No fue posible actualizar el proveedor: " + str(e))

    def __ver_proveedor(self):
        try:
            cp = ControlProveedor()
            self.proveedor = cp.getAll()

            self.tbl_prov.clearContents()
            self.tbl_prov.setColumnCount(9)
            self.tbl_prov.setRowCount(len(self.proveedor))
            self.tbl_prov.setHorizontalHeaderLabels([
                "ID", "NOMBRE", "RAZÓN SOCIAL", "RFC", "DIRECCIÓN",
                "EMAIL", "TELÉFONO", "CELULAR", "ESTATUS"
            ])

            for i in range(0, len(self.proveedor)):
                p = self.proveedor[i]
                self.tbl_prov.setItem(i, 0, QTableWidgetItem(str(p.id)))
                self.tbl_prov.setItem(i, 1, QTableWidgetItem(str(p.nombre)))
                self.tbl_prov.setItem(i, 2, QTableWidgetItem(str(p.razon_social)))
                self.tbl_prov.setItem(i, 3, QTableWidgetItem(str(p.RFC)))
                self.tbl_prov.setItem(i, 4, QTableWidgetItem(str(p.direccion)))
                self.tbl_prov.setItem(i, 5, QTableWidgetItem(str(p.email)))
                self.tbl_prov.setItem(i, 6, QTableWidgetItem(str(p.tel)))
                self.tbl_prov.setItem(i, 7, QTableWidgetItem(str(p.cel)))
                self.tbl_prov.setItem(i, 8, QTableWidgetItem(str(p.estatus)))

            self.tbl_prov.resizeColumnsToContents()

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
                                 "No fue posible consultar los proveedores: " + str(e))

    def __eliminar_proveedor(self):
        try:
            p = Proveedor()
            id_texto = self.txt_id_prov.text().strip()
            p.id = int(id_texto) if id_texto != "" else 0

            if p.id == 0:
                QMessageBox.warning(self,
                                    "Aviso",
                                    "Selecciona un proveedor para eliminar")
                return

            cp = ControlProveedor()
            i = cp.delete(p)

            if i > 0:
                QMessageBox.information(self,
                                        "Exito en la operación",
                                        "Proveedor eliminado correctamente")
                self.txt_id_prov.clear()
                self.txt_nombre_prov.clear()
                self.txt_razon_social_prov.clear()
                self.txt_rfc_prov.clear()
                self.txt_direccion_prov.clear()
                self.txt_email_prov.clear()
                self.txt_tel_prov.clear()
                self.txt_cel_prov.clear()
                self.txt_buscar_prov.clear()
                self.chb_estatus_prov.setChecked(True)
                self.__ver_proveedor()

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
                                 "No fue posible eliminar el proveedor: " + str(e))

    def __buscar_proveedor(self):
        try:
            busqueda = self.txt_buscar_prov.text().strip()
            cp = ControlProveedor()
            self.proveedor = cp.search(busqueda)

            self.tbl_prov.clearContents()
            self.tbl_prov.setColumnCount(9)
            self.tbl_prov.setRowCount(len(self.proveedor))
            self.tbl_prov.setHorizontalHeaderLabels([
                "ID", "NOMBRE", "RAZÓN SOCIAL", "RFC", "DIRECCIÓN",
                "EMAIL", "TELÉFONO", "CELULAR", "ESTATUS"
            ])

            for i in range(0, len(self.proveedor)):
                p = self.proveedor[i]
                self.tbl_prov.setItem(i, 0, QTableWidgetItem(str(p.id)))
                self.tbl_prov.setItem(i, 1, QTableWidgetItem(str(p.nombre)))
                self.tbl_prov.setItem(i, 2, QTableWidgetItem(str(p.razon_social)))
                self.tbl_prov.setItem(i, 3, QTableWidgetItem(str(p.RFC)))
                self.tbl_prov.setItem(i, 4, QTableWidgetItem(str(p.direccion)))
                self.tbl_prov.setItem(i, 5, QTableWidgetItem(str(p.email)))
                self.tbl_prov.setItem(i, 6, QTableWidgetItem(str(p.tel)))
                self.tbl_prov.setItem(i, 7, QTableWidgetItem(str(p.cel)))
                self.tbl_prov.setItem(i, 8, QTableWidgetItem(str(p.estatus)))

            self.tbl_prov.resizeColumnsToContents()

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
                                 "No fue posible buscar el proveedor: " + str(e))

    def __seleccionar_proveedor(self, item):
        try:
            pos = item.row()
            if pos < 0 or pos >= len(self.proveedor):
                return

            ps = self.proveedor[pos]
            self.txt_id_prov.setText(str(ps.id))
            self.txt_nombre_prov.setText(str(ps.nombre))
            self.txt_razon_social_prov.setText(str(ps.razon_social))
            self.txt_rfc_prov.setText(str(ps.RFC))
            self.txt_direccion_prov.setText(str(ps.direccion))
            self.txt_email_prov.setText(str(ps.email))
            self.txt_tel_prov.setText(str(ps.tel))
            self.txt_cel_prov.setText(str(ps.cel))

            if ps.estatus == 1:
                self.chb_estatus_prov.setChecked(True)
            else:
                self.chb_estatus_prov.setChecked(False)

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
                                 "No fue posible seleccionar el proveedor: " + str(e))
