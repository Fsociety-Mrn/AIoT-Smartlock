import cv2
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import QTimer

class VideoPlayer(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.label = QtWidgets.QLabel()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)
        
        self.cap = cv2.VideoCapture(0)  # Open the default camera (index 0)
        self.timer.start(30)  # Start the timer with an interval of 30ms
        
    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.flip(frame, 1)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = QtGui.QImage(frame, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888)
            self.label.setPixmap(QtGui.QPixmap.fromImage(img))
        
    def closeEvent(self, event):
        self.cap.release()
        
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    player = VideoPlayer()
    player.show()
    app.exec_()
