import os
from PySide6.QtUiTools import loadUiType
from Modelo.categoria import Categoria

base_path = os.path.dirname(__file__)

ui_path = os.path.join(base_path, "vistaCategoria.ui")

ui_form, base_class = loadUiType(ui_path) # type: ignore

class FrameCategoria(base_class, ui_form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

#Zamudio Juarez Mauricio