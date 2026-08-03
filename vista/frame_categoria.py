import os
from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import QTableWidgetItem
from PySide6.QtWidgets import QMessageBox
import mysql.connector
from mysql.connector import Error
from modelo.categoria import Categoria
from control.controlcategoria import ControlCategoria

base_path = os.path.dirname(__file__)

ui_path = os.path.join(base_path, "categoria.ui")

ui_form, base_class = loadUiType(ui_path)  # type: ignore


class FrameCategoria(base_class, ui_form):
    def __init__(self):
        super().__init__()
        self.categoria = []
        self.setupUi(self)
        self.__agregarListeners()
        self.__ver_categoria()

    def __agregarListeners(self):
        self.btn_insertar_cat.clicked.connect(self.__insertar_categoria)
        self.btn_eliminar_cat.clicked.connect(self.__eliminar_categoria)
        self.btn_modificar_cat.clicked.connect(self.__modificar_categoria)
        self.btn_vertodo_cat.clicked.connect(self.__ver_categoria)
        self.btn_buscar_cat.clicked.connect(self.__buscar_categoria)
        self.tbl_cat.itemClicked.connect(self.__seleccionar_categoria)

    def __insertar_categoria(self):
        try:
            c = Categoria()
            c.nombre = self.txt_nombre_cat.text().strip()
            c.estatus = 1

            cc = ControlCategoria()
            id = cc.insert(c)

            if id > 0:  # type: ignore
                QMessageBox.information(self,
                                        "Inserción correcta",
                                        "La inserción de la categoría se realizó correctamente")
                self.txt_id_cat.clear()
                self.txt_nombre_cat.clear()
                self.txt_buscar_cat.clear()
                self.__ver_categoria()

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
                                 "No fue posible insertar la categoría: " + str(ex))

    def __modificar_categoria(self):
        try:
            c = Categoria()
            id_texto = self.txt_id_cat.text().strip()
            c.id = int(id_texto) if id_texto != "" else 0
            c.nombre = self.txt_nombre_cat.text().strip()
            c.estatus = 1

            if c.id == 0:
                QMessageBox.warning(self,
                                    "Aviso",
                                    "Selecciona una categoría para modificar")
                return

            cc = ControlCategoria()
            i = cc.update(c)

            if i > 0:
                QMessageBox.information(self,
                                        "Exito en la operación",
                                        "Categoría actualizada correctamente")
                self.txt_id_cat.clear()
                self.txt_nombre_cat.clear()
                self.txt_buscar_cat.clear()
                self.__ver_categoria()

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
                                 "No fue posible actualizar la categoría: " + str(e))

    def __ver_categoria(self):
        try:
            cc = ControlCategoria()
            self.categoria = cc.getAll()

            self.tbl_cat.clearContents()
            self.tbl_cat.setColumnCount(3)
            self.tbl_cat.setRowCount(len(self.categoria))
            self.tbl_cat.setHorizontalHeaderLabels([
                "ID", "NOMBRE", "ESTATUS"
            ])

            for i in range(0, len(self.categoria)):
                c = self.categoria[i]
                self.tbl_cat.setItem(i, 0, QTableWidgetItem(str(c.id)))
                self.tbl_cat.setItem(i, 1, QTableWidgetItem(str(c.nombre)))
                self.tbl_cat.setItem(i, 2, QTableWidgetItem(str(c.estatus)))

            self.tbl_cat.resizeColumnsToContents()

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
                                 "No fue posible consultar las categorías: " + str(e))

    def __eliminar_categoria(self):
        try:
            c = Categoria()
            id_texto = self.txt_id_cat.text().strip()
            c.id = int(id_texto) if id_texto != "" else 0

            if c.id == 0:
                QMessageBox.warning(self,
                                    "Aviso",
                                    "Selecciona una categoría para eliminar")
                return

            cc = ControlCategoria()
            i = cc.delete(c)

            if i > 0:
                QMessageBox.information(self,
                                        "Exito en la operación",
                                        "Categoría eliminada correctamente")
                self.txt_id_cat.clear()
                self.txt_nombre_cat.clear()
                self.txt_buscar_cat.clear()
                self.__ver_categoria()

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
                                 "No fue posible eliminar la categoría: " + str(e))

    def __buscar_categoria(self):
        try:
            busqueda = self.txt_buscar_cat.text().strip()
            cc = ControlCategoria()
            self.categoria = cc.search(busqueda)

            self.tbl_cat.clearContents()
            self.tbl_cat.setColumnCount(3)
            self.tbl_cat.setRowCount(len(self.categoria))
            self.tbl_cat.setHorizontalHeaderLabels([
                "ID", "NOMBRE", "ESTATUS"
            ])

            for i in range(0, len(self.categoria)):
                c = self.categoria[i]
                self.tbl_cat.setItem(i, 0, QTableWidgetItem(str(c.id)))
                self.tbl_cat.setItem(i, 1, QTableWidgetItem(str(c.nombre)))
                self.tbl_cat.setItem(i, 2, QTableWidgetItem(str(c.estatus)))

            self.tbl_cat.resizeColumnsToContents()

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
                                 "No fue posible buscar la categoría: " + str(e))

    def __seleccionar_categoria(self, item):
        try:
            pos = item.row()
            if pos < 0 or pos >= len(self.categoria):
                return

            cs = self.categoria[pos]
            self.txt_id_cat.setText(str(cs.id))
            self.txt_nombre_cat.setText(str(cs.nombre))

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
                                 "No fue posible seleccionar la categoría: " + str(e))
