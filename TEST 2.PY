from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

from Raspberry.Raspberry import gpio_manual

from pages.Custom_MessageBox import MessageBox

import cv2

import dlib


class facialRegister(QtWidgets.QFrame):
    def __init__(self,main_menu=None):
        super().__init__(main_menu)


        # message box
        self.MessageBox = MessageBox()
        self.MessageBox.setStyleSheet("""
                        QLabel{
                            min-width: 600px; 
                            min-height: 50px; 
                            font-size: 20px;
                            padding-top: 10px; 
                            padding-bottom: 10px; 
                        }
                        QPushButton { 
                            width: 250px; 
                            height: 30px; 
                            font-size: 15px;
                         }
                    """)
        
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # ========= for facial detection ========= #
        
        # facial status
        self.facial_result = ("","")
        self.result = "","",False,False,None

        # yellow
        self.R,self.G ,self.B = (255,255,0)
     
        # EAR of eye
        self.blink_threshold, self.blink_counter, self.blink, self.last_dilation_time = 0.3,0,False,0
    
        # haar cascade face detection
        self.face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        # dlib face detection
        self.dlib_faceDetcetoor = dlib.get_frontal_face_detector()

        # using dlib landmark detector
        self.landmark_detector = dlib.shape_predictor('Model/shape_predictor_68_face_landmarks.dat')

        # =============================================================================================================== #

        # frame
        self.setObjectName("Facial Login")
        self.resize(1024, 565)
        
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/background/Images/logo192x192.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setStyleSheet("background-color: rgb(231, 229, 213);\n"
            "background-image: url(:/background/Images/background-removebg-preview.png);\n"
            "background-position: center;\n"
            "\n"
            "")
        
        
        # video framing
        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(180, 50, 661, 471))
        self.widget.setStyleSheet("border: 2px solid rgb(61, 152, 154) ;\n"
            "border-radius: 50px;")
        self.widget.setObjectName("widget")
        
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 621, 431))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        # video for facial recognition
        self.video = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        
        self.video.setFont(font)
        self.video.setStyleSheet("border:none;\n color:  rgba(11, 131, 120, 219);")
        self.video.setText("")
        self.video.setPixmap(QtGui.QPixmap("Test/FACIAL.png"))
        self.video.setScaledContents(False)
        self.video.setAlignment(QtCore.Qt.AlignCenter)
        self.video.setObjectName("video")
        self.horizontalLayout.addWidget(self.video)
        
        # face status
        self.status = QtWidgets.QLabel(self)
        self.status.setGeometry(QtCore.QRect(0, 0, 1021, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.status.setFont(font)
        self.status.setStyleSheet("color:  rgba(11, 131, 120, 219)")
        self.status.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.status.setAlignment(QtCore.Qt.AlignCenter)
        self.status.setObjectName("status")

        # back to mainmenu button
        self.back = QtWidgets.QPushButton(self)
        self.back.setGeometry(QtCore.QRect(10, 10, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(False)
        font.setPointSize(12)
        self.back.setFont(font)
        self.back.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back.setAutoFillBackground(False)
        self.back.setStyleSheet("border:none;\n"
                "color:  rgba(11, 131, 120, 219);\n"
                "padding:10px")
        self.back.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/background/Images/return.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back.setIcon(icon1)
        self.back.setIconSize(QtCore.QSize(42, 42))
        self.back.setFlat(False)
        self.back.setObjectName("back")

        
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


        # Timer

        
        self.status.raise_()
        self.back.raise_()
        self.widget.raise_()
        
        
        # self.messageBoxShow(
        #     title="FACIAL LOGIN",
        #     text="Please not remove eye glasses or hat or facemask that remove your face,  if persist it may not recognize you as well",
        #     buttons=self.MessageBox.Ok)
                
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("facialLogin", "Frame"))
        self.status.setText(_translate("facialLogin", "<html><head/><body><p>Please blink at least 1 second.</p></body></html>"))
        self.back.setText(_translate("facialLogin", "Back "))

 
 
if __name__ == "__main__":

    import sys,background
    # Create a new QApplication object
    app = QApplication(sys.argv)

    New_menu = facialRegister()
    New_menu.show()

    sys.exit(app.exec_())


