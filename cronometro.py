import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import QTimer, Qt


class CronometroApp(QWidget):
    def __init__(self, username="", tarefa="Geral"):
        super().__init__()
        self.username = username
        self.tarefa = tarefa
        self.intervencoes = 0
        self.horas = 0
        self.minutos = 0
        self.segundos = 0
        self.milisegundos = 0

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.atualizar_tempo)

        self.label_tempo = QLabel("00:00:00.000")
        self.label_tempo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_tempo.setStyleSheet("font-size: 45px; font-weight: bold; color: #333;")

        layout_principal = QVBoxLayout(self)
        layout_principal.addWidget(self.label_tempo)
        self.setLayout(layout_principal)

    def tempo_total_ms(self):
        return (self.horas * 3600 + self.minutos * 60 + self.segundos) * 1000 + self.milisegundos

    def iniciar_cronometro(self):
        if not self.timer.isActive():
            self.intervencoes += 1
            self.timer.start(10)

    def pausar_cronometro(self):
        self.timer.stop()

    def reiniciar_cronometro(self):
        self.timer.stop()
        self.horas = 0
        self.minutos = 0
        self.segundos = 0
        self.milisegundos = 0
        self.intervencoes = 0
        self.label_tempo.setText("00:00:00.000")

    def atualizar_tempo(self):
        self.milisegundos += 10
        if self.milisegundos >= 1000:
            self.milisegundos = 0
            self.segundos += 1
        if self.segundos >= 60:
            self.segundos = 0
            self.minutos += 1
        if self.minutos >= 60:
            self.minutos = 0
            self.horas += 1
        texto_formatado = f"{self.horas:02d}:{self.minutos:02d}:{self.segundos:02d}.{self.milisegundos:03d}"
        self.label_tempo.setText(texto_formatado)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CronometroApp("teste")
    window.show()
    sys.exit(app.exec())
