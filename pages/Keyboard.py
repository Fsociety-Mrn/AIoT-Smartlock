from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit

class QwertyKeyboard(QWidget):
    def __init__(self, input_field):
        super().__init__()

        self.input_field = input_field
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        keyboard_layout = QGridLayout()

        buttons = [
            '1234567890',
            'qwertyuiop',
            'asdfghjkl',
            'zxcvbnm',
            'Backspace'
        ]

        row, col = 0, 0
        for row_data in buttons:
            col = 0
            for char in row_data:
                button = QPushButton(char)
                button.clicked.connect(self.on_button_click)
                keyboard_layout.addWidget(button, row, col)
                col += 1
            row += 1

        layout.addLayout(keyboard_layout)
        self.setLayout(layout)

    def on_button_click(self):
        button = self.sender()
        if button:
            text = button.text()
            if text == 'Backspace':
                current_text = self.input_field.text()
                self.input_field.setText(current_text[:-1])
            else:
                current_text = self.input_field.text()
                self.input_field.setText(current_text + text)
