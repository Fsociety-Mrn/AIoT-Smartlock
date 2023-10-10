import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import QTimer, Qt

class CountdownTimer(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Countdown Timer')
        self.setGeometry(100, 100, 300, 150)

        self.layout = QVBoxLayout()

        self.label = QLabel()
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.label)

        self.start_button = QPushButton('Start')
        self.start_button.clicked.connect(self.startTimer)
        self.layout.addWidget(self.start_button)

        self.setLayout(self.layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.updateCountdown)
        self.seconds_left = 30

    def startTimer(self):
        self.timer.start(1000)
        self.updateCountdown()

    def updateCountdown(self):
        if self.seconds_left > 0:
            self.label.setText(f'Time Left: {self.seconds_left} seconds')
            self.seconds_left -= 1
        else:
            self.timer.stop()
            self.label.setText('Countdown Finished!')
            self.start_button.setText('Restart')  # Change button text to "Restart"
            self.start_button.clicked.disconnect(self.startTimer)  # Disconnect previous signal
            self.start_button.clicked.connect(self.restartTimer)  # Connect to restart function

    def restartTimer(self):
        self.seconds_left = 30  # Reset the countdown time
        self.start_button.setText('Start')  # Change button text back to "Start"
        self.start_button.clicked.disconnect(self.restartTimer)  # Disconnect previous signal
        self.start_button.clicked.connect(self.startTimer)  # Connect to start function
        self.updateCountdown()  # Start the countdown again

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CountdownTimer()
    window.show()
    sys.exit(app.exec_())
