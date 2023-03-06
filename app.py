import cv2
import sys
import time

from JoloRecognition import JoloRecognition as Jolo
from PyQt5 import QtCore,QtGui,QtWidgets

class Ui_SmartAIoT(object):
    def setupUi(self, SmartAIoT):
        
        SmartAIoT.setObjectName("SmartAIoT")
        SmartAIoT.setWindowModality(QtCore.Qt.ApplicationModal)
        SmartAIoT.resize(660, 691)
        SmartAIoT.setStyleSheet("background-color:rgb(0, 0, 127)")
        SmartAIoT.setAnimated(False)
        SmartAIoT.setDocumentMode(True)
        self.SmartAIoT_3 = QtWidgets.QWidget(SmartAIoT)
        self.SmartAIoT_3.setObjectName("SmartAIoT_3")
        
        # label
        self.label = QtWidgets.QLabel(self.SmartAIoT_3)
        self.label.setGeometry(QtCore.QRect(10, 10, 641, 561))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        
        # Timer
        self.timer = QtCore.QTimer(self.SmartAIoT_3)
        self.timer.timeout.connect(self.videoStreaming)
        
        # Register Button
        self.pushButton = QtWidgets.QPushButton(self.SmartAIoT_3)
        self.pushButton.setGeometry(QtCore.QRect(20, 600, 621, 71))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.pushButton.setObjectName("pushButton")
        SmartAIoT.setCentralWidget(self.SmartAIoT_3)

        self.retranslateUi(SmartAIoT)
        QtCore.QMetaObject.connectSlotsByName(SmartAIoT)

        # open cv2
        self.cap = cv2.VideoCapture(1) if cv2.VideoCapture(1).isOpened() else cv2.VideoCapture(0)
        self.cap.set(4,1080)
        # self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 400)
        # self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)

        # face detection
        self.face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.last_recognition_time = time.time()
        self.timer.start(30)
        
        # facial data 
        self.matchs = "Initializing face recognition"
        self.R=255
        self.G=255
        self.B=0
        
    def retranslateUi(self, SmartAIoT):
        _translate = QtCore.QCoreApplication.translate
        SmartAIoT.setWindowTitle(_translate("SmartAIoT", "MainWindow"))
        self.label.setText(_translate("SmartAIoT", "Loading"))
        self.pushButton.setToolTip(_translate("SmartAIoT", "click to register"))
        self.pushButton.setText(_translate("SmartAIoT", "Register"))
        
    def videoStreaming(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.flip(frame, 1)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert the frame to RGB
            
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=20, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
            
            current_time = time.time()
            
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (self.R,self.G , self.B), 2)
                cv2.putText(frame,str(self.matchs),(x,y+h+30),cv2.FONT_HERSHEY_COMPLEX,1,(self.R,self.G,self.B),1)
                
                if current_time - self.last_recognition_time >= 1:
                    self.last_recognition_time = current_time
                # get the result of Face_Compare script
                    result = Jolo().Face_Compare(frame)
                
                    if result is not None and result[0] == 'No match detected':
                        # do something
                        self.matchs = str(result[0])
                        self.R=255
                        self.G=0
                        self.B=0
                    else:
                        self.matchs = str(result[0])
                        self.R=0
                        self.G=255
                        self.B=0
         

            
            
            img = QtGui.QImage(frame, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888)  # Convert the frame to a QImage
            self.label.setPixmap(QtGui.QPixmap.fromImage(img))  # Set the label pixmap to the QImage
    

        
    def closeEvent(self, event):
        self.cap.release()  # Release the camera when the application is closed


if __name__ == "__main__":
    print("Loading.........")

    app = QtWidgets.QApplication(sys.argv)
    SmartAIoT = QtWidgets.QMainWindow()
    ui = Ui_SmartAIoT()
    ui.setupUi(SmartAIoT)
    print("Done loading.")
    SmartAIoT.show()
    sys.exit(app.exec_())
