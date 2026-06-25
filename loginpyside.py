import sys
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout,
                               QLabel, QLineEdit, QPushButton, QMessageBox)
from PySide6.QtCore import Qt
from db import Database
from main import MainWindow

class mainwindow(QWidget):
    def __init__(self):
        super().__init__()
        self.database = Database()

        self.database.configurar_base_dados()
        self.resize(350, 400)

        self.layout_principal = QVBoxLayout()
        self.setLayout(self.layout_principal)

        self.entrar_login()

    def entrar_login(self):
        self.setWindowTitle("Login")
        self.limpar_janela()

        self.label_titulo = QLabel("Login")
        self.label_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.input_username = QLineEdit()
        self.input_username.setPlaceholderText("Introduza o username")

        self.input_password = QLineEdit()
        self.input_password.setPlaceholderText("Introduza a password")
        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.botao_submeter = QPushButton("Entrar na conta")
        self.botao_submeter.clicked.connect(self.criar_conta)

        self.botao_registar_utilizador = QPushButton("Criar conta")
        self.botao_registar_utilizador.clicked.connect(self.registar)

        self.layout_principal.addWidget(self.label_titulo)
        self.layout_principal.addWidget(QLabel("Username:"))
        self.layout_principal.addWidget(self.input_username)
        self.layout_principal.addWidget(QLabel("Password:"))
        self.layout_principal.addWidget(self.input_password)

        self.layout_principal.addSpacing(15)
        self.layout_principal.addWidget(self.botao_submeter)
        self.layout_principal.addWidget(self.botao_registar_utilizador)

    def registar(self):
        self.setWindowTitle("Criar conta")
        self.limpar_janela()

        self.label_titulo = QLabel("Registo do utilizador")
        self.label_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.input_username = QLineEdit()
        self.input_username.setPlaceholderText("Introduza o username")

        self.input_password = QLineEdit()
        self.input_password.setPlaceholderText("Introduza a password")
        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.botao_registar = QPushButton("Criar utilizador")
        self.botao_registar.clicked.connect(self.processar_registo)

        self.botao_voltar_login = QPushButton("Voltar para o Login")
        self.botao_voltar_login.clicked.connect(self.entrar_login)

        self.layout_principal.addWidget(self.label_titulo)
        self.layout_principal.addWidget(QLabel("Username:"))
        self.layout_principal.addWidget(self.input_username)
        self.layout_principal.addWidget(QLabel("Password:"))
        self.layout_principal.addWidget(self.input_password)

        self.layout_principal.addSpacing(15)
        self.layout_principal.addWidget(self.botao_registar)
        self.layout_principal.addWidget(self.botao_voltar_login)

    def criar_conta(self):
        username = self.input_username.text().strip()
        password = self.input_password.text().strip()

        if not username or not password:
            QMessageBox.warning(self, "Erro", "Preencha todos os campos!")
            return

        self.database.insert_utilizadores(username, password)
        self.input_username.clear()
        self.input_password.clear()
        QMessageBox.information(self, "Sucesso", f"Bem vindo '{username}'!")
        try:
            self.janela_principal= MainWindow()
            self.janela_principal.show()
            self.close()
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Algo de errado não tá certo: {e}")
    def processar_registo(self):
        username2 = self.input_username.text().strip()
        password2 = self.input_password.text().strip()

        if not username2 or not password2:
            QMessageBox.warning(self, "Erro", "Por favor, preencha todos os campos!")
            return
        try:
            self.database.insert_utilizadores(username2, password2)
            QMessageBox.information(self, "Sucesso", f"Bem vindo '{username2}'!")
            self.input_username.clear()
            self.input_password.clear()
            self.entrar_login()
        except Exception as e:
            QMessageBox.critical(self, "Erro na BD", f"Não foi possível guardar os dados: {e}")

    def limpar_janela(self):
        if self.layout_principal is not None:
            while self.layout_principal.count():
                item = self.layout_principal.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainwindow()
    window.show()
    sys.exit(app.exec())
