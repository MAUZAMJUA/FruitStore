import os
from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import QTableWidgetItem
from PySide6.QtWidgets import QMessageBox
import mysql.connector
from mysql.connector import Error
from modelo.vendedor import Vendedor
from control.controlvendedor import ControlVendedor

base_path = os.path.dirname(__file__)

ui_path = os.path.join(base_path, "vendedor.ui")

ui_form, base_class = loadUiType(ui_path)  # type: ignore


class FrameVendedor(base_class, ui_form):
    def __init__(self):
        super().__init__()
        self.vendedor = []
        self.setupUi(self)
        self.cargar_catalogo_generos()
        self.__agregarListeners()
        self.__ver_vendedor()

    def __agregarListeners(self):
        self.btn_insertar_vend.clicked.connect(self.__insertar_vendedor)
        self.btn_eliminar_vend.clicked.connect(self.__eliminar_vendedor)
        self.btn_modificar_vend.clicked.connect(self.__modificar_vendedor)
        self.btn_vertodo_vend.clicked.connect(self.__ver_vendedor)
        self.btn_buscar_vend.clicked.connect(self.__buscar_vendedor)
        self.tbl_vend.itemClicked.connect(self.__seleccionar_vendedor)

    def cargar_catalogo_generos(self):
        self.cmb_genero_vend.clear()
        self.cmb_genero_vend.addItem("Masculino", "M")
        self.cmb_genero_vend.addItem("Femenino", "F")
        self.cmb_genero_vend.addItem("Otro", "O")
        self.cmb_genero_vend.setCurrentIndex(-1)
        self.cmb_genero_vend.setPlaceholderText("Selecciona un género")

    def __insertar_vendedor(self):
        try:
            v = Vendedor()
            v.nombre = self.txt_nombre_vend.text().strip()
            v.fecha_nacimiento = self.txt_fecha_nacimiento_vend.text().strip()
            v.genero = self.cmb_genero_vend.currentData()
            v.calle = self.txt_calle_vend.text().strip()
            v.num_ext = self.txt_num_ext_vend.text().strip()
            v.num_int = self.txt_num_int_vend.text().strip()
            v.CP = self.txt_cp_vend.text().strip()
            v.colonia = self.txt_colonia_vend.text().strip()
            v.ciudad = self.txt_ciudad_vend.text().strip()
            v.estado = self.txt_estado_vend.text().strip()
            v.pais = self.txt_pais_vend.text().strip()
            v.tel = self.txt_tel_vend.text().strip()
            v.fecha_ingreso = self.txt_fecha_ingreso_vend.text().strip()
            v.email = self.txt_email_vend.text().strip()
            v.estatus = 1 if self.chb_estatus_vend.isChecked() else 0

            if v.genero is None:
                QMessageBox.warning(self,
                                    "Aviso",
                                    "Selecciona un género")
                return

            cv = ControlVendedor()
            id = cv.insert(v)

            if id > 0:  # type: ignore
                QMessageBox.information(self,
                                        "Inserción correcta",
                                        "La inserción del vendedor se realizó correctamente")
                self.txt_id_vend.clear()
                self.txt_nombre_vend.clear()
                self.txt_fecha_nacimiento_vend.clear()
                self.txt_calle_vend.clear()
                self.txt_num_ext_vend.clear()
                self.txt_num_int_vend.clear()
                self.txt_cp_vend.clear()
                self.txt_colonia_vend.clear()
                self.txt_ciudad_vend.clear()
                self.txt_estado_vend.clear()
                self.txt_pais_vend.clear()
                self.txt_tel_vend.clear()
                self.txt_fecha_ingreso_vend.clear()
                self.txt_email_vend.clear()
                self.txt_buscar_vend.clear()
                self.cmb_genero_vend.setCurrentIndex(-1)
                self.chb_estatus_vend.setChecked(True)
                self.__ver_vendedor()

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
                                 "No fue posible insertar el vendedor: " + str(ex))

    def __modificar_vendedor(self):
        try:
            v = Vendedor()
            id_texto = self.txt_id_vend.text().strip()
            v.id = int(id_texto) if id_texto != "" else 0
            v.nombre = self.txt_nombre_vend.text().strip()
            v.fecha_nacimiento = self.txt_fecha_nacimiento_vend.text().strip()
            v.genero = self.cmb_genero_vend.currentData()
            v.calle = self.txt_calle_vend.text().strip()
            v.num_ext = self.txt_num_ext_vend.text().strip()
            v.num_int = self.txt_num_int_vend.text().strip()
            v.CP = self.txt_cp_vend.text().strip()
            v.colonia = self.txt_colonia_vend.text().strip()
            v.ciudad = self.txt_ciudad_vend.text().strip()
            v.estado = self.txt_estado_vend.text().strip()
            v.pais = self.txt_pais_vend.text().strip()
            v.tel = self.txt_tel_vend.text().strip()
            v.fecha_ingreso = self.txt_fecha_ingreso_vend.text().strip()
            v.email = self.txt_email_vend.text().strip()
            v.estatus = 1 if self.chb_estatus_vend.isChecked() else 0

            if v.id == 0:
                QMessageBox.warning(self,
                                    "Aviso",
                                    "Selecciona un vendedor para modificar")
                return

            if v.genero is None:
                QMessageBox.warning(self,
                                    "Aviso",
                                    "Selecciona un género")
                return

            cv = ControlVendedor()
            i = cv.update(v)

            if i > 0:
                QMessageBox.information(self,
                                        "Exito en la operación",
                                        "Vendedor actualizado correctamente")
                self.txt_id_vend.clear()
                self.txt_nombre_vend.clear()
                self.txt_fecha_nacimiento_vend.clear()
                self.txt_calle_vend.clear()
                self.txt_num_ext_vend.clear()
                self.txt_num_int_vend.clear()
                self.txt_cp_vend.clear()
                self.txt_colonia_vend.clear()
                self.txt_ciudad_vend.clear()
                self.txt_estado_vend.clear()
                self.txt_pais_vend.clear()
                self.txt_tel_vend.clear()
                self.txt_fecha_ingreso_vend.clear()
                self.txt_email_vend.clear()
                self.txt_buscar_vend.clear()
                self.cmb_genero_vend.setCurrentIndex(-1)
                self.chb_estatus_vend.setChecked(True)
                self.__ver_vendedor()

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
                                 "No fue posible actualizar el vendedor: " + str(e))

    def __ver_vendedor(self):
        try:
            cv = ControlVendedor()
            self.vendedor = cv.getAll()

            self.tbl_vend.clearContents()
            self.tbl_vend.setColumnCount(16)
            self.tbl_vend.setRowCount(len(self.vendedor))
            self.tbl_vend.setHorizontalHeaderLabels([
                "ID", "NOMBRE", "FECHA NACIMIENTO", "GÉNERO", "CALLE",
                "NÚM. EXT.", "NÚM. INT.", "C.P.", "COLONIA", "CIUDAD",
                "ESTADO", "PAÍS", "TELÉFONO", "FECHA INGRESO", "EMAIL",
                "ESTATUS"
            ])

            for i in range(0, len(self.vendedor)):
                v = self.vendedor[i]
                self.tbl_vend.setItem(i, 0, QTableWidgetItem(str(v.id)))
                self.tbl_vend.setItem(i, 1, QTableWidgetItem(str(v.nombre)))
                self.tbl_vend.setItem(i, 2, QTableWidgetItem(str(v.fecha_nacimiento)))
                self.tbl_vend.setItem(i, 3, QTableWidgetItem(str(v.genero)))
                self.tbl_vend.setItem(i, 4, QTableWidgetItem(str(v.calle)))
                self.tbl_vend.setItem(i, 5, QTableWidgetItem(str(v.num_ext)))
                self.tbl_vend.setItem(i, 6, QTableWidgetItem(str(v.num_int)))
                self.tbl_vend.setItem(i, 7, QTableWidgetItem(str(v.CP)))
                self.tbl_vend.setItem(i, 8, QTableWidgetItem(str(v.colonia)))
                self.tbl_vend.setItem(i, 9, QTableWidgetItem(str(v.ciudad)))
                self.tbl_vend.setItem(i, 10, QTableWidgetItem(str(v.estado)))
                self.tbl_vend.setItem(i, 11, QTableWidgetItem(str(v.pais)))
                self.tbl_vend.setItem(i, 12, QTableWidgetItem(str(v.tel)))
                self.tbl_vend.setItem(i, 13, QTableWidgetItem(str(v.fecha_ingreso)))
                self.tbl_vend.setItem(i, 14, QTableWidgetItem(str(v.email)))
                self.tbl_vend.setItem(i, 15, QTableWidgetItem(str(v.estatus)))

            self.tbl_vend.resizeColumnsToContents()

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
                                 "No fue posible consultar los vendedores: " + str(e))

    def __eliminar_vendedor(self):
        try:
            v = Vendedor()
            id_texto = self.txt_id_vend.text().strip()
            v.id = int(id_texto) if id_texto != "" else 0

            if v.id == 0:
                QMessageBox.warning(self,
                                    "Aviso",
                                    "Selecciona un vendedor para eliminar")
                return

            cv = ControlVendedor()
            i = cv.delete(v)

            if i > 0:
                QMessageBox.information(self,
                                        "Exito en la operación",
                                        "Vendedor eliminado correctamente")
                self.txt_id_vend.clear()
                self.txt_nombre_vend.clear()
                self.txt_fecha_nacimiento_vend.clear()
                self.txt_calle_vend.clear()
                self.txt_num_ext_vend.clear()
                self.txt_num_int_vend.clear()
                self.txt_cp_vend.clear()
                self.txt_colonia_vend.clear()
                self.txt_ciudad_vend.clear()
                self.txt_estado_vend.clear()
                self.txt_pais_vend.clear()
                self.txt_tel_vend.clear()
                self.txt_fecha_ingreso_vend.clear()
                self.txt_email_vend.clear()
                self.txt_buscar_vend.clear()
                self.cmb_genero_vend.setCurrentIndex(-1)
                self.chb_estatus_vend.setChecked(True)
                self.__ver_vendedor()

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
                                 "No fue posible eliminar el vendedor: " + str(e))

    def __buscar_vendedor(self):
        try:
            busqueda = self.txt_buscar_vend.text().strip()
            cv = ControlVendedor()
            self.vendedor = cv.search(busqueda)

            self.tbl_vend.clearContents()
            self.tbl_vend.setColumnCount(16)
            self.tbl_vend.setRowCount(len(self.vendedor))
            self.tbl_vend.setHorizontalHeaderLabels([
                "ID", "NOMBRE", "FECHA NACIMIENTO", "GÉNERO", "CALLE",
                "NÚM. EXT.", "NÚM. INT.", "C.P.", "COLONIA", "CIUDAD",
                "ESTADO", "PAÍS", "TELÉFONO", "FECHA INGRESO", "EMAIL",
                "ESTATUS"
            ])

            for i in range(0, len(self.vendedor)):
                v = self.vendedor[i]
                self.tbl_vend.setItem(i, 0, QTableWidgetItem(str(v.id)))
                self.tbl_vend.setItem(i, 1, QTableWidgetItem(str(v.nombre)))
                self.tbl_vend.setItem(i, 2, QTableWidgetItem(str(v.fecha_nacimiento)))
                self.tbl_vend.setItem(i, 3, QTableWidgetItem(str(v.genero)))
                self.tbl_vend.setItem(i, 4, QTableWidgetItem(str(v.calle)))
                self.tbl_vend.setItem(i, 5, QTableWidgetItem(str(v.num_ext)))
                self.tbl_vend.setItem(i, 6, QTableWidgetItem(str(v.num_int)))
                self.tbl_vend.setItem(i, 7, QTableWidgetItem(str(v.CP)))
                self.tbl_vend.setItem(i, 8, QTableWidgetItem(str(v.colonia)))
                self.tbl_vend.setItem(i, 9, QTableWidgetItem(str(v.ciudad)))
                self.tbl_vend.setItem(i, 10, QTableWidgetItem(str(v.estado)))
                self.tbl_vend.setItem(i, 11, QTableWidgetItem(str(v.pais)))
                self.tbl_vend.setItem(i, 12, QTableWidgetItem(str(v.tel)))
                self.tbl_vend.setItem(i, 13, QTableWidgetItem(str(v.fecha_ingreso)))
                self.tbl_vend.setItem(i, 14, QTableWidgetItem(str(v.email)))
                self.tbl_vend.setItem(i, 15, QTableWidgetItem(str(v.estatus)))

            self.tbl_vend.resizeColumnsToContents()

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
                                 "No fue posible buscar el vendedor: " + str(e))

    def __seleccionar_vendedor(self, item):
        try:
            pos = item.row()
            if pos < 0 or pos >= len(self.vendedor):
                return

            vs = self.vendedor[pos]
            self.txt_id_vend.setText(str(vs.id))
            self.txt_nombre_vend.setText(str(vs.nombre))
            self.txt_fecha_nacimiento_vend.setText(str(vs.fecha_nacimiento))
            self.txt_calle_vend.setText(str(vs.calle))
            self.txt_num_ext_vend.setText(str(vs.num_ext))
            self.txt_num_int_vend.setText(str(vs.num_int))
            self.txt_cp_vend.setText(str(vs.CP))
            self.txt_colonia_vend.setText(str(vs.colonia))
            self.txt_ciudad_vend.setText(str(vs.ciudad))
            self.txt_estado_vend.setText(str(vs.estado))
            self.txt_pais_vend.setText(str(vs.pais))
            self.txt_tel_vend.setText(str(vs.tel))
            self.txt_fecha_ingreso_vend.setText(str(vs.fecha_ingreso))
            self.txt_email_vend.setText(str(vs.email))

            for i in range(self.cmb_genero_vend.count()):
                genero = self.cmb_genero_vend.itemData(i)
                if genero == vs.genero or self.cmb_genero_vend.itemText(i) == vs.genero:
                    self.cmb_genero_vend.setCurrentIndex(i)
                    break

            if vs.estatus == 1:
                self.chb_estatus_vend.setChecked(True)
            else:
                self.chb_estatus_vend.setChecked(False)

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
                                 "No fue posible seleccionar el vendedor: " + str(e))
