import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QTableWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.table = QTableWidget(5, 4)
        self.tabela.setItem(0, 0, QTableWidgetItem("abc"))
        self.tabela.setItem(0, 1, QTableWidgetItem(button))


        button = button = QPushButton("Press Me!")
        button.setFixedWidth(150)
        button.setFixedHeight(40)
        self.showMaximized()
        button.move(500, 500)

        self.table.setHorizontalHeaderLabels(["Partidos: "])
        #self.addWidget()



        layout.addWidget(self.tabela)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

