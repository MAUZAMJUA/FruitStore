import os
from PySide6.QtUiTools import loadUiType
from Modelo.venta import Venta

base_path = os.path.dirname(__file__)

ui_path = os.path.join(base_path, "vistaVenta.ui")

ui_form, base_class = loadUiType(ui_path) # type: ignore

class FrameVenta(base_class, ui_form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
#Zamudio Juarez Mauricio