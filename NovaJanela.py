import sys
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel,
                               QTableWidget, QTableWidgetItem, QHeaderView,
                               QTabWidget, QSizePolicy)
from PySide6.QtCore import Qt
from db import Database


def formatar_segundos(total_segundos):
    total_segundos = int(round(total_segundos))
    horas = total_segundos // 3600
    minutos = (total_segundos % 3600) // 60
    segundos = total_segundos % 60
    return f"{horas:02d}:{minutos:02d}:{segundos:02d}"


class NovaJanela(QWidget):
    def __init__(self, user_id, username=""):
        super().__init__()
        self.user_id = user_id
        self.username = username
        self.db = Database()

        self.setWindowTitle(f"Histórico — {username}")
        self.resize(700, 500)

        layout = QVBoxLayout(self)

        titulo = QLabel(f"Histórico de {username}")
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titulo.setStyleSheet("font-size: 18px; font-weight: bold; margin: 8px;")
        layout.addWidget(titulo)

        abas = QTabWidget()
        layout.addWidget(abas)

        # ---------- Totais por partido ----------
        self.tabela_totais = QTableWidget(0, 3)
        self.tabela_totais.setHorizontalHeaderLabels(["Partido", "Tempo Total", "Intervenções"])
        self.tabela_totais.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tabela_totais.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        abas.addTab(self.tabela_totais, "Totais por Partido")

        # ---------- Histórico detalhado ----------
        self.tabela_historico = QTableWidget(0, 3)
        self.tabela_historico.setHorizontalHeaderLabels(["Data", "Partido", "Duração"])
        self.tabela_historico.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tabela_historico.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        abas.addTab(self.tabela_historico, "Histórico Detalhado")

        self.carregar_dados()

    def carregar_dados(self):
        if self.user_id is None:
            return

        # Totais agrupados por partido
        totais = self.db.obter_totais_por_partido(self.user_id)
        self.tabela_totais.setRowCount(len(totais))
        for linha, (partido, duracao_total, num_intervencoes) in enumerate(totais):
            self.tabela_totais.setItem(linha, 0, QTableWidgetItem(partido))
            self.tabela_totais.setItem(linha, 1, QTableWidgetItem(formatar_segundos(duracao_total)))
            self.tabela_totais.setItem(linha, 2, QTableWidgetItem(str(num_intervencoes)))

        historico = self.db.obter_historico(self.user_id)
        self.tabela_historico.setRowCount(len(historico))
        for linha, (data, partido, duracao) in enumerate(historico):
            self.tabela_historico.setItem(linha, 0, QTableWidgetItem(data))
            self.tabela_historico.setItem(linha, 1, QTableWidgetItem(partido))
            self.tabela_historico.setItem(linha, 2, QTableWidgetItem(formatar_segundos(duracao)))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NovaJanela(1, "Admin")
    window.show()
    sys.exit(app.exec())
