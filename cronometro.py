import sys
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout,
                               QLabel, QPushButton, QHBoxLayout)
from PySide6.QtCore import QTimer, Qt


class CronometroApp(QWidget):
    def __init__(self):
        super().__init__()

        self.horas = 0
        self.minutos = 0
        self.segundos = 0
        self.milisegundos = 0

        # 2. Configurar o motor do cronómetro (QTimer)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.atualizar_tempo)

        # 3. Criar os componentes visuais (Interface)
        self.label_tempo = QLabel("00:00:00.000")
        self.label_tempo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_tempo.setStyleSheet("font-size: 35px; font-weight: bold; color: #333;")

        self.botao_iniciar = QPushButton("Iniciar")
        self.botao_iniciar.clicked.connect(self.iniciar_cronometro)

        self.botao_pausar = QPushButton("Pausar")
        self.botao_pausar.clicked.connect(self.pausar_cronometro)

        self.botao_reiniciar = QPushButton("Reiniciar")
        self.botao_reiniciar.clicked.connect(self.reiniciar_cronometro)

        layout_botoes = QHBoxLayout()
        #layout_botoes.addWidget(self.botao_iniciar)
        #layout_botoes.addWidget(self.botao_pausar)
        #layout_botoes.addWidget(self.botao_reiniciar)

        layout_principal = QVBoxLayout(self)
        layout_principal.addWidget(self.label_tempo)
        layout_principal.addLayout(layout_botoes)

        self.setLayout(layout_principal)

    def iniciar_cronometro(self):
        if not self.timer.isActive():
            self.timer.start(10) # Dispara a cada 10 milisegundos

    def pausar_cronometro(self):
        self.timer.stop()

    def reiniciar_cronometro(self):
        self.timer.stop()
        self.horas = 0
        self.minutos = 0
        self.segundos = 0
        self.milisegundos = 0
        self.label_tempo.setText("00:00:00.000")

    def atualizar_tempo(self):
        # Avança de 10 em 10 milisegundos
        self.milisegundos += 10

        # Quando atinge 1000 milisegundos, passou 1 segundo real
        if self.milisegundos >= 1000:
            self.milisegundos = 0
            self.segundos += 1 # Adiciona 1 segundo (e não 10)

        if self.segundos >= 60:
            self.segundos = 0
            self.minutos += 1

        if self.minutos >= 60:
            self.minutos = 0
            self.horas += 1

        # Mostra o tempo bem formatado no ecrã
        texto_formatado = f"{self.horas:02d}:{self.minutos:02d}:{self.segundos:02d}.{self.milisegundos:03d}"
        self.label_tempo.setText(texto_formatado)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CronometroApp()
    window.show()
    sys.exit(app.exec())