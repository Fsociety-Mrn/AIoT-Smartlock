import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit

class QwertyKeyboard(QMainWindow):
    def __init__(self, input_field):
        super().__init__()

        self.input_field = input_field
        self.initUI()

    def initUI(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        self.text_edit = QLineEdit()
        layout.addWidget(self.text_edit)

        keyboard_layout = QGridLayout()  # Create a grid layout for the keyboard

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

        keyboard_widget = QWidget()
        keyboard_widget.setLayout(keyboard_layout)
        layout.addWidget(keyboard_widget)

        central_widget.setLayout(layout)

        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('QWERTY Keyboard')
        self.show()

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

def main():
    app = QApplication(sys.argv)
    input_field = QLineEdit()
    keyboard = QwertyKeyboard(input_field)
    main_window = QMainWindow()
    main_window.setCentralWidget(input_field)
    main_window.setWindowTitle('Text Input with Virtual Keyboard')
    main_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
