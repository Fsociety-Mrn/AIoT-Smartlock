from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

from Raspberry.Raspberry import gpio_manual

from pages.Custom_MessageBox import MessageBox

import cv2

import dlib


class facialRegister(QtWidgets.QFrame):
    def __init__(self,parent=None):
            super().__init__(parent)
            
            self.main_menu = parent
            self.Show = True
            
            self.Light_PIN,self.lights_on = 25, True

            
            # message box
            self.MessageBox = MessageBox()
            self.MessageBox.setStyleSheet("""
                  QMessageBox { 
                      text-align: center;
                  }
                  QMessageBox::icon {
                      subcontrol-position: center;
                  }
                  QPushButton { 
                      width: 250px; 
                      height: 30px; 
                      font-size: 15px;
                  }
              """)

            # EAR of eye
            self.blink_threshold, self.blink_counter, self.blink, self.last_dilation_time = 0.35,0,False,0

            #frame
            self.setObjectName("facialRegistration")
            self.resize(1024, 565)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(":/background/Images/logo192x192.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.setWindowIcon(icon)
            self.setStyleSheet("background-color: rgb(231, 229, 213);\n"
            "background-image: url(:/background/Images/background-removebg-preview.png);\n"
            "background-position: center;\n"
            "")
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
                    
            # user name
            self.Name = QtWidgets.QLabel(self)
            self.Name.setGeometry(QtCore.QRect(0, 10, 211, 41))
            font = QtGui.QFont()
            font.setFamily("Segoe UI")
            font.setPointSize(12)
            font.setBold(True)
            font.setWeight(75)
            self.Name.setFont(font)
            self.Name.setStyleSheet("color: #3D989A")
            self.Name.setAlignment(QtCore.Qt.AlignCenter)
            self.Name.setObjectName("Name")
            
            #camera
            self.widget = QtWidgets.QWidget(self)
            self.widget.setGeometry(QtCore.QRect(180, 50, 661, 471))
            self.widget.setStyleSheet("border: 2px solid rgb(61, 152, 154) ;\n"
            "border-radius: 50px;")
            self.widget.setObjectName("widget")
            
            self.horizontalLayoutWidget = QtWidgets.QWidget(self.widget)
            # self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 631, 321))
            self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 621, 431))
            self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
            self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
            self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            self.horizontalLayout.setObjectName("horizontalLayout")

            # camera video label
            self.video = QtWidgets.QLabel(self.horizontalLayoutWidget)
            self.video.setStyleSheet("border:none;")
            self.video.setText("")
            self.video.setPixmap(QtGui.QPixmap("Images/Align.png"))
            self.video.setScaledContents(True)
            self.video.setAlignment(QtCore.Qt.AlignCenter)
            self.video.setObjectName("video")
            self.horizontalLayout.addWidget(self.video)
            
            # Set the default image to your custom image
            self.default_image = QtGui.QPixmap("Images/loading.png")

            self.captureStat = 1
            # camera capture
            self.label = QtWidgets.QLabel(self)
            self.label.setGeometry(QtCore.QRect(600, 5, 41, 41))
            self.label.setText("")
            self.label.setPixmap(QtGui.QPixmap(":/background/Images/capture.png"))
            self.label.setAlignment(QtCore.Qt.AlignCenter)
            self.label.setObjectName("label")
        
            self.capture = QtWidgets.QLabel(self)
            self.capture.setGeometry(QtCore.QRect(660, 10, 21, 31))
            font = QtGui.QFont()
            font.setFamily("Segoe UI")
            font.setPointSize(12)
            font.setBold(True)
            font.setWeight(75)
            self.capture.setFont(font)
            self.capture.setStyleSheet("color: #3D989A")
            self.capture.setAlignment(QtCore.Qt.AlignCenter)
            self.capture.setObjectName("capture")
            
            # status
            self.status = QtWidgets.QLabel(self)
            self.status.setGeometry(QtCore.QRect(200, 10, 400, 31))
            font = QtGui.QFont()
            font.setFamily("Segoe UI")
            font.setPointSize(12)
            font.setBold(True)
            font.setWeight(75)
            self.status.setFont(font)
            self.status.setStyleSheet("color: #3D989A")
            self.status.setAlignment(QtCore.Qt.AlignCenter)
            self.status.setObjectName("status")

            # open camera
            self.cap = cv2.VideoCapture(1) if cv2.VideoCapture(1).isOpened() else cv2.VideoCapture(0)
            self.cap.set(4, 1080)
            
            # face detector: Haar, dlib,landmark
            self.face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            self.dlib_faceDetcetoor = dlib.get_frontal_face_detector()
            self.landmark_detector = dlib.shape_predictor('Model/shape_predictor_68_face_landmarks.dat')

            # turn on the switch 
            self.Lights = QtWidgets.QPushButton(self)
            self.Lights.setGeometry(QtCore.QRect(910 - 30, 250, 101, 41))
            font = QtGui.QFont()
            font.setFamily("Segoe UI")
            font.setBold(False)
            font.setPointSize(12)
            self.Lights.setFont(font)
            self.Lights.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.Lights.setAutoFillBackground(False)
            self.Lights.setStyleSheet("border:none;\n"
                "color:  rgba(11, 131, 120, 219);\n"
                "padding:10px")
            self.Lights.setText("")
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap("Images/lights_on.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.Lights.setIcon(icon1)
            self.Lights.setIconSize(QtCore.QSize(42, 42))
            self.Lights.setFlat(False)
            self.Lights.setObjectName("back")



            self.retranslateUi()
            QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("facialRegistration", "Facial Registration"))
        self.capture.setText(_translate("facialRegistration", "0"))
        self.status.setText(_translate("facialRegistration", "Please be ready at 5"))
        self.Name.setText(_translate("facialRegistration", ""))
        gpio_manual(self.Light_PIN,False)
        
 

 
 
if __name__ == "__main__":

    import sys,background
    # Create a new QApplication object
    app = QApplication(sys.argv)

    New_menu = facialRegister()
    New_menu.show()

    sys.exit(app.exec_())


