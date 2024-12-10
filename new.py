import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QPushButton, QLabel
from PyQt6.QtCore import Qt, QTimer
import torch
from transformers import pipeline

# Prüfen, welches System verfügbar ist, ob CUDA, MPS oder CPU
if torch.cuda.is_available():
    device = torch.device('cuda')
# Prüfen, ob MPS (Apple Silicon) verfügbar ist
elif torch.backends.mps.is_available():
    device = torch.device('mps')
# Wenn keines der beiden verfügbar ist, auf CPU zurückgreifen
else:
    device = torch.device('cpu')

print(f"Verwendetes Gerät: {device}")

# Laden der Modelle deutsch / englisch und umgekehrt
de_to_en = pipeline("translation", model="Helsinki-NLP/opus-mt-de-en", device=device)
en_to_de = pipeline("translation", model="Helsinki-NLP/opus-mt-en-de", device=device)

# Laden der Modelle französisch / deutsch und umgekehrt
de_to_fr = pipeline("translation", model="Helsinki-NLP/opus-mt-de-fr", device=device)
fr_to_de = pipeline("translation", model="Helsinki-NLP/opus-mt-fr-de", device=device)

class Uebersetzer(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 1280, 896)
        self.setWindowTitle('Deutsch-Englisch und Deutsch-Französisch Übersetzer und umgekehrt')

        layout = QVBoxLayout()
        self.setLayout(layout)

        # Deutsch-Englisch
        de_en_layout = QHBoxLayout()
        layout.addLayout(de_en_layout)
        self.de_input = QTextEdit()
        self.de_input.setPlaceholderText("Deutscher Text")
        self.de_input.setFixedHeight(150)
        de_en_layout.addWidget(self.de_input)
        self.en_output = QTextEdit()
        self.en_output.setPlaceholderText("Englische Übersetzung")
        self.en_output.setReadOnly(True)
        self.en_output.setFixedHeight(150)
        de_en_layout.addWidget(self.en_output)
        de_to_en_btn = QPushButton("Deutsch -> Englisch")
        de_to_en_btn.setFixedWidth(150)
        de_to_en_btn.setStyleSheet("QPushButton { background-color: white; color: black; } QPushButton:hover { background-color: lightgreen; }")
        de_to_en_btn.clicked.connect(lambda: self.translate_and_flash(de_to_en_btn, self.translate_de_to_en))
        de_en_layout.addWidget(de_to_en_btn)

        # Englisch-Deutsch
        en_de_layout = QHBoxLayout()
        layout.addLayout(en_de_layout)
        self.en_input = QTextEdit()
        self.en_input.setPlaceholderText("Englischer Text")
        self.en_input.setFixedHeight(150)
        en_de_layout.addWidget(self.en_input)
        self.de_output = QTextEdit()
        self.de_output.setPlaceholderText("Deutsche Übersetzung")
        self.de_output.setReadOnly(True)
        self.de_output.setFixedHeight(150)
        en_de_layout.addWidget(self.de_output)
        en_to_de_btn = QPushButton("Englisch -> Deutsch")
        en_to_de_btn.setFixedWidth(150)
        en_to_de_btn.setStyleSheet("QPushButton { background-color: white; color: black; } QPushButton:hover { background-color: lightgreen; }")
        en_to_de_btn.clicked.connect(lambda: self.translate_and_flash(en_to_de_btn, self.translate_en_to_de))
        en_de_layout.addWidget(en_to_de_btn)

        # Deutsch-Französisch
        de_fr_layout = QHBoxLayout()
        layout.addLayout(de_fr_layout)
        self.de_fr_input = QTextEdit()
        self.de_fr_input.setPlaceholderText("Deutscher Text")
        self.de_fr_input.setFixedHeight(150)
        de_fr_layout.addWidget(self.de_fr_input)
        self.fr_output = QTextEdit()
        self.fr_output.setPlaceholderText("Französische Übersetzung")
        self.fr_output.setReadOnly(True)
        self.fr_output.setFixedHeight(150)
        de_fr_layout.addWidget(self.fr_output)
        de_to_fr_btn = QPushButton("Deutsch -> Französisch")
        de_to_fr_btn.setFixedWidth(150)
        de_to_fr_btn.setStyleSheet("QPushButton { background-color: white; color: black; } QPushButton:hover { background-color: lightgreen; }")
        de_to_fr_btn.clicked.connect(lambda: self.translate_and_flash(de_to_fr_btn, self.translate_de_to_fr))
        de_fr_layout.addWidget(de_to_fr_btn)

        # Französisch-Deutsch
        fr_de_layout = QHBoxLayout()
        layout.addLayout(fr_de_layout)
        self.fr_de_input = QTextEdit()
        self.fr_de_input.setPlaceholderText("Französischer Text")
        self.fr_de_input.setFixedHeight(150)
        fr_de_layout.addWidget(self.fr_de_input)
        self.de_fr_output = QTextEdit()
        self.de_fr_output.setPlaceholderText("Deutsche Übersetzung")
        self.de_fr_output.setReadOnly(True)
        self.de_fr_output.setFixedHeight(150)
        fr_de_layout.addWidget(self.de_fr_output)
        fr_to_de_btn = QPushButton("Französisch -> Deutsch")
        fr_to_de_btn.setFixedWidth(150)
        fr_to_de_btn.setStyleSheet("QPushButton { background-color: white; color: black; } QPushButton:hover { background-color: lightgreen; }")
        fr_to_de_btn.clicked.connect(lambda: self.translate_and_flash(fr_to_de_btn, self.translate_fr_to_de))
        fr_de_layout.addWidget(fr_to_de_btn)

        self.center()

    def center(self):
        frame_geometry = self.frameGeometry()
        screen_center = self.screen().availableGeometry().center()
        frame_geometry.moveCenter(screen_center)
        self.move(frame_geometry.topLeft())

    def translate_and_flash(self, button, translate_function):
        button.setStyleSheet("QPushButton { background-color: red; color: white; }")
        QTimer.singleShot(100, lambda: button.setStyleSheet("QPushButton { background-color: white; color: black; }"))
        translate_function()

    def translate_de_to_en(self):
        text = self.de_input.toPlainText()
        translation = de_to_en(text)[0]['translation_text']
        self.en_output.setText(translation)

    def translate_en_to_de(self):
        text = self.en_input.toPlainText()
        translation = en_to_de(text)[0]['translation_text']
        self.de_output.setText(translation)

    def translate_de_to_fr(self):
        text = self.de_fr_input.toPlainText()
        translation = de_to_fr(text)[0]['translation_text']
        self.fr_output.setText(translation)

    def translate_fr_to_de(self):
        text = self.fr_de_input.toPlainText()
        translation = fr_to_de(text)[0]['translation_text']
        self.de_fr_output.setText(translation)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    uebersetzer = Uebersetzer()
    uebersetzer.show()
    sys.exit(app.exec())
