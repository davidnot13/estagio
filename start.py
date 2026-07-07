import sys
from PySide6.QtWidgets import QApplication
from loginpyside import LoginWindow
from main import MainWindow
from NovaJanela import NovaJanela

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = LoginWindow()
    login.show()
    sys.exit(app.exec())
