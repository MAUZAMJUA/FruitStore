import sys
from PySide6.QtWidgets import QApplication
from Vista.main import Main

app = QApplication(sys.argv)

ventana = Main()

ventana.show()

sys.exit(app.exec())

#Zamudio Juarez Mauricio