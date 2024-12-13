import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QPushButton, QLabel, QSizePolicy
)
from PyQt6.QtCore import Qt, QTimer
import torch
from transformers import pipeline
from PyQt6.QtGui import QClipboard


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
        self.setGeometry(100, 100, 1500, 800)  # Angepasste Größe für mehr Platz
        self.setWindowTitle('Deutsch-Englisch und Deutsch-Französisch Übersetzer und umgekehrt')

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # Hinzufügen von Übersetzungskategorien
        main_layout.addLayout(self.create_translation_layout(
            input_placeholder="Deutscher Text",
            output_placeholder="Englische Übersetzung",
            translate_label="Deutsch -> Englisch",
            translate_func=self.translate_de_to_en,
            copy_func=self.copy_en_output
        ))

        main_layout.addLayout(self.create_translation_layout(
            input_placeholder="Englischer Text",
            output_placeholder="Deutsche Übersetzung",
            translate_label="Englisch -> Deutsch",
            translate_func=self.translate_en_to_de,
            copy_func=self.copy_de_output
        ))

        main_layout.addLayout(self.create_translation_layout(
            input_placeholder="Deutscher Text",
            output_placeholder="Französische Übersetzung",
            translate_label="Deutsch -> Französisch",
            translate_func=self.translate_de_to_fr,
            copy_func=self.copy_fr_output
        ))

        main_layout.addLayout(self.create_translation_layout(
            input_placeholder="Französischer Text",
            output_placeholder="Deutsche Übersetzung",
            translate_label="Französisch -> Deutsch",
            translate_func=self.translate_fr_to_de,
            copy_func=self.copy_de_fr_output
        ))

        self.center()

        # Meldung für erfolgreiches Kopieren
        # Innerhalb der Uebersetzer Klasse, im initUI nach self.center()
        self.message_label = QLabel("")
        self.message_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.message_label.setStyleSheet("color: green; font-weight: bold;")
        main_layout.addWidget(self.message_label)

    def create_translation_layout(self, input_placeholder, output_placeholder, translate_label, translate_func, copy_func):
        """
        Erstellt ein Layout für eine Übersetzungsrichtung mit Eingabe, Ausgabe, Übersetzen-Button und Kopieren-Button.
        """
        layout = QHBoxLayout()

        # Eingabefeld
        input_text = QTextEdit()
        input_text.setPlaceholderText(input_placeholder)
        input_text.setFixedHeight(150)
        layout.addWidget(input_text)

        # Ausgabefeld
        output_text = QTextEdit()
        output_text.setPlaceholderText(output_placeholder)
        output_text.setReadOnly(True)
        output_text.setFixedHeight(150)
        layout.addWidget(output_text)

        # Buttons (Übersetzen und Kopieren) in vertikalem Layout
        button_layout = QVBoxLayout()

        translate_btn = QPushButton(translate_label)
        translate_btn.setFixedWidth(150)
        translate_btn.setStyleSheet("QPushButton { background-color: white; color: black; } QPushButton:hover { background-color: lightgreen; }")
        translate_btn.clicked.connect(lambda: self.translate_and_flash(translate_btn, translate_func, input_text, output_text))
        button_layout.addWidget(translate_btn)

        copy_btn = QPushButton("Kopieren")
        copy_btn.setFixedWidth(150)
        copy_btn.setStyleSheet("QPushButton { background-color: white; color: black; } QPushButton:hover { background-color: lightblue; }")
        copy_btn.clicked.connect(lambda: copy_func(output_text))
        button_layout.addWidget(copy_btn)

        # Platzhalter hinzufügen, um die Buttons oben zu halten
        button_layout.addStretch()

        layout.addLayout(button_layout)

        # Speicherung der Widgets für spätere Verwendung
        self.widgets = getattr(self, 'widgets', [])
        self.widgets.append({
            'input': input_text,
            'output': output_text,
            'translate_btn': translate_btn,
            'copy_btn': copy_btn
        })

        return layout

    def center(self):
        frame_geometry = self.frameGeometry()
        screen_center = self.screen().availableGeometry().center()
        frame_geometry.moveCenter(screen_center)
        self.move(frame_geometry.topLeft())

    def translate_and_flash(self, button, translate_function, input_text, output_text):
        button.setStyleSheet("QPushButton { background-color: red; color: white; }")
        QTimer.singleShot(100, lambda: button.setStyleSheet("QPushButton { background-color: white; color: black; }"))
        translate_function(input_text, output_text)

    def translate_de_to_en(self, input_widget, output_widget):
        text = input_widget.toPlainText().strip()
        if text:
            translation = de_to_en(text)[0]['translation_text']
            output_widget.setText(translation)

    def translate_en_to_de(self, input_widget, output_widget):
        text = input_widget.toPlainText().strip()
        if text:
            translation = en_to_de(text)[0]['translation_text']
            output_widget.setText(translation)

    def translate_de_to_fr(self, input_widget, output_widget):
        text = input_widget.toPlainText().strip()
        if text:
            translation = de_to_fr(text)[0]['translation_text']
            output_widget.setText(translation)

    def translate_fr_to_de(self, input_widget, output_widget):
        text = input_widget.toPlainText().strip()
        if text:
            translation = fr_to_de(text)[0]['translation_text']
            output_widget.setText(translation)

    def copy_en_output(self, output_widget):
        self.copy_to_clipboard(output_widget)

    def copy_de_output(self, output_widget):
        self.copy_to_clipboard(output_widget)

    def copy_fr_output(self, output_widget):
        self.copy_to_clipboard(output_widget)

    def copy_de_fr_output(self, output_widget):
        self.copy_to_clipboard(output_widget)

    def copy_to_clipboard(self, text_edit: QTextEdit):
        text = text_edit.toPlainText()
        if text:
            clipboard: QClipboard = QApplication.clipboard()
            clipboard.setText(text)
            self.message_label.setText("Text kopiert!")
            QTimer.singleShot(2000, lambda: self.message_label.setText(""))  # Meldung nach 2 Sekunden ausblenden


if __name__ == "__main__":
    app = QApplication(sys.argv)
    uebersetzer = Uebersetzer()
    uebersetzer.show()
    sys.exit(app.exec())
