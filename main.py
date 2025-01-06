import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QPushButton, QLabel
)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QClipboard, QFont
from functools import partial

# Hauptcode
from utils import load_translation_models

translation_models = load_translation_models()
de_to_en = translation_models['de_to_en']
en_to_de = translation_models['en_to_de']
de_to_fr = translation_models['de_to_fr']
fr_to_de = translation_models['fr_to_de']

# StyleSheets für die Buttons
TRANSLATE_BTN_STYLE = """QPushButton {
    background-color: white;
    color: black;
}
QPushButton:hover {
    background-color: lightgreen;
}"""

COPY_BTN_STYLE = """QPushButton {
    background-color: white;
    color: black;
}
QPushButton:hover {
    background-color: lightblue;
}"""


class Uebersetzer(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.blink_timer = QTimer(self)  # Timer für das Blinken
        self.blink_timer.timeout.connect(self.blink_text)
        self.blink_state = False  # Aktueller Blink-Zustand

        # Schriftart und -größe festlegen
        font = QFont()
        font.setPointSize(16)
        self.setFont(font)

    def initUI(self):
        self.setGeometry(100, 100, 1200, 800)  # Angepasste Größe für mehr Platz
        self.setWindowTitle('Deutsch-Englisch und Deutsch-Französisch Übersetzer und umgekehrt')

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # Hinzufügen von Übersetzungskategorien
        self.widgets = []
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
        self.message_label = QLabel("")
        self.message_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.message_label.setStyleSheet("color: green; font-weight: bold;")
        main_layout.addWidget(self.message_label)

    def create_translation_layout(self, input_placeholder, output_placeholder, translate_label, translate_func, copy_func):
        """
        Erstellt ein Layout für eine Übersetzungsrichtung.
        """
        layout = QHBoxLayout()

        # Eingabefeld
        input_layout = QVBoxLayout()
        input_text = QTextEdit()
        input_text.setPlaceholderText(input_placeholder)
        input_text.setMinimumHeight(100)
        input_text.setMinimumWidth(300)
        input_layout.addWidget(input_text)

        translate_btn = QPushButton(translate_label)
        translate_btn.setFixedWidth(150)
        # Hier setzen wir das komplette StyleSheet mit Hover-Regel
        translate_btn.setStyleSheet(TRANSLATE_BTN_STYLE)
        translate_btn.clicked.connect(
            partial(self.translate_and_flash, translate_btn, translate_func, input_text, None))
        input_layout.addWidget(translate_btn)
        input_layout.addStretch()
        layout.addLayout(input_layout)

        # Ausgabefeld
        output_layout = QVBoxLayout()
        output_text = QTextEdit()
        output_text.setPlaceholderText(output_placeholder)
        output_text.setReadOnly(True)
        output_text.setMinimumHeight(100)
        output_text.setMinimumWidth(300)
        output_layout.addWidget(output_text)

        copy_btn = QPushButton("Kopieren")
        copy_btn.setFixedWidth(150)
        # Hier setzen wir das komplette StyleSheet mit Hover-Regel für den Kopier-Button
        copy_btn.setStyleSheet(COPY_BTN_STYLE)
        copy_btn.clicked.connect(partial(copy_func, output_text))
        output_layout.addWidget(copy_btn)
        output_layout.addStretch()
        layout.addLayout(output_layout)

        # Speicherung der Widgets für spätere Verwendung
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
        for widget in self.widgets:
            if widget['translate_btn'] == button:
                output_text = widget['output']
                break

        # Temporär Rot setzen
        button.setStyleSheet("QPushButton { background-color: red; color: white; }")
        # Nach 100 ms wieder das Original-Style (inkl. Hover-Effekt) zurücksetzen
        QTimer.singleShot(100, lambda btn=button: btn.setStyleSheet(TRANSLATE_BTN_STYLE))

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

    def copy_to_clipboard(self, text_edit):
        text = text_edit.toPlainText()
        if text:
            clipboard = QApplication.clipboard()
            clipboard.setText(text)
            self.message_label.setText("Text kopiert!")
            self.start_blinking("green")  # Grün blinken lassen
        else:
            self.message_label.setText("Kein Text zum Kopieren!")
            self.start_blinking("red")  # Rot blinken lassen

    def start_blinking(self, color):
        self.current_color = color
        self.blink_state = False  # Beginne mit unsichtbarem Zustand
        self.blink_timer.start(250)  # Starte den Timer (500ms = 0,5 Sekunden Intervall)
        QTimer.singleShot(2000, self.stop_blinking)  # Nach 2 Sekunden aufhören

    def stop_blinking(self):
        self.blink_timer.stop()
        self.message_label.setText("")
        self.message_label.setStyleSheet(f"color: {self.current_color}; font-weight: bold;")  # Setzt ursprüngliche Farbe wieder
        self.blink_state = False

    def blink_text(self):
        # Wechsle den Blink-Zustand
        self.blink_state = not self.blink_state

        if self.blink_state:
            # Mache den Text sichtbar
            self.message_label.setStyleSheet(f"color: {self.current_color}; font-weight: bold;")
        else:
            # Mache den Text unsichtbar
            self.message_label.setStyleSheet("color: transparent; font-weight: bold;")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    uebersetzer = Uebersetzer()
    uebersetzer.show()
    sys.exit(app.exec())
