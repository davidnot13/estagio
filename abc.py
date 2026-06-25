import sys
from PySide6.QtWidgets import (QApplication, QTableWidget, QTableWidgetItem,
                               QVBoxLayout, QWidget, QPushButton, QMessageBox, QHeaderView)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Botão na Tabela - PySide6")
        self.showMaximized()
        layout = QVBoxLayout(self)
        layout.addSpacing(30)
        self.table = QTableWidget(5, 3)
        self.table.setFixedHeight(400)
        layout.addStretch()
        self.table.setHorizontalHeaderLabels(["Nome", "Cargo", "Ação"])
        self.table.verticalHeader().setDefaultSectionSize(60)
        dados = [
            ("Ana", "Engenheira"),
            ("Bruno", "Designer"),
            ("Carlos", "Programador"),
            ("a", "b"),
            ("c", "d")
        ]
        for linha, (nome, cargo) in enumerate(dados):
            self.table.setItem(linha, 0, QTableWidgetItem(nome))
            self.table.setItem(linha, 1, QTableWidgetItem(cargo))

            botao = QPushButton("Start")

            botao.clicked.connect(lambda checked=False, r=linha: self.botao_clicado(r))
            self.table.setCellWidget(linha, 2, botao)

        layout.addWidget(self.table)

    def botao_clicado(self, linha):
        nome = self.table.item(linha, 0).text()
        QMessageBox.information(self, "Ação", "Botão clicado")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
