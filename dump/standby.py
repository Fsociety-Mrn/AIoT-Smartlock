from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialize the timer
        self.standby_timer = QTimer()
        self.standby_timer.timeout.connect(self.activate_standby_mode)
        self.standby_duration = 5000  # 5 seconds of inactivity

        # Connect activity events to reset the timer
        self.setMouseTracking(True)
        self.keyPressEvent = self.reset_standby_timer

    def reset_standby_timer(self, event):
        # Reset the timer on user activity events
        self.standby_timer.start(self.standby_duration)

    def activate_standby_mode(self):
        # Perform standby mode actions
        print("Standby mode activated")

app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
