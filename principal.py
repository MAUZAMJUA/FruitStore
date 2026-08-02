import sys
from PySide6.QtWidgets import QApplication
from vista.main import Main

app = QApplication(sys.argv)

ventana = Main()

ventana.show()

sys.exit(app.exec())