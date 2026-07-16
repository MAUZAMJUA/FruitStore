import os
from PySide6.QtUiTools import loadUiType
from Modelo.compra import Compra

base_path = os.path.dirname(__file__)

ui_path = os.path.join(base_path, "vistaCompra.ui")

ui_form, base_class = loadUiType(ui_path) # type: ignore

class FrameCompra(base_class, ui_form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

#Zamudio Juarez Mauricio