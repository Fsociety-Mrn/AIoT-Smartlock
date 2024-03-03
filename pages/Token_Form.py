import os
import shutil
import cv2

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal
from Firebase.firebase import firebaseRead,firebaseTokenVerify,firebaseDeleteVerifiedToken
from pages.Custom_MessageBox import MessageBox
from Face_Recognition.JoloRecognition import JoloRecognition as Jolo
from Firebase.Offline import create_person_temporarily_banned
        
class TokenForm(QtWidgets.QFrame):
    data_passed = pyqtSignal(str)
    
    def __init__(self, parent):
        super().__init__(parent)
        
        self.main_menu = parent
        
        # name
        self.rearranged_string = ""
        
        # for video streaming variable
        self.videoStream = cv2.VideoCapture(1) if cv2.VideoCapture(1).isOpened() else cv2.VideoCapture(0)
        self.videoStream.set(4, 1080)
        
        # haar cascade face detection
        self.face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        
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
        
        # frame
        self.setObjectName("Tokenfield")
        self.resize(1024, 565)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/background/Images/logo192x192.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setStyleSheet("background-color: rgb(231, 229, 213);\n"
        "background-image: url(:/background/Images/background-removebg-preview.png);\n"
        "background-position: center;\n")
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        
        # Greetings
        self.greetings = QtWidgets.QLabel(self)
        self.greetings.setGeometry(QtCore.QRect(0, 0, 1021, 141))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(21)
        font.setBold(False)
        font.setWeight(50)
        self.greetings.setFont(font)
        self.greetings.setStyleSheet("color: #3D989A")
        self.greetings.setAlignment(QtCore.Qt.AlignCenter)
        self.greetings.setObjectName("greetings")
        
        # error messages
        self.errorMessage = QtWidgets.QLabel(self)
        self.errorMessage.setGeometry(QtCore.QRect(340, 105, 350, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(10)
        self.errorMessage.setFont(font)
        self.errorMessage.setStyleSheet("color: red")
        self.errorMessage.setAlignment(QtCore.Qt.AlignCenter)
        self.errorMessage.setObjectName("errorMessage")
        
        # Token Field
        self.TokenID = QtWidgets.QLineEdit(self)
        self.TokenID.setGeometry(QtCore.QRect(250, 140, 531, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        self.TokenID.setFont(font)
        self.TokenID.setStyleSheet("background: transparents;\n"
"color: #3D989A;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid #3D989A;\n"
"border-radius: 20px;")
        self.TokenID.setAlignment(QtCore.Qt.AlignCenter)
        self.TokenID.setPlaceholderText("Token ID")
        self.TokenID.setObjectName("TokenID")
        
        # continue
        # self.Continue = QtWidgets.QPushButton(self)
        # self.Continue.setGeometry(QtCore.QRect(420, 290, 181, 51))
        # font = QtGui.QFont()
        # font.setFamily("Segoe UI")
        # font.setPointSize(12)
        # font.setBold(True)
        # font.setWeight(75)
        # self.Continue.setFont(font)
        # self.Continue.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # self.Continue.setStyleSheet("border: none;\n"
        # "background: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
        # "border-radius: 25px;\n"
        # "color: white;")
        # self.Continue.setObjectName("Continue")
        
        # cancel
        self.Cancel = QtWidgets.QPushButton(self)
        self.Cancel.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Cancel.setGeometry(QtCore.QRect(20, 20, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Cancel.setFont(font)
        self.Cancel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Cancel.setStyleSheet("border: 2px solid #3D989A;\n"
        "border-radius: 25px;\n"
        "color: #3D989A;")
        self.Cancel.setObjectName("Cancel")
        
        self.KeyboardContainer_2 = QtWidgets.QWidget(self)
        self.KeyboardContainer_2.setGeometry(QtCore.QRect(20, 220, 971, 331))
        self.KeyboardContainer_2.setStyleSheet("border: 2px solid rgb(61, 152, 154) ;\n"
"border-radius: 50px;")
        self.KeyboardContainer_2.setObjectName("KeyboardContainer_2")
        self.Q = QtWidgets.QPushButton(self.KeyboardContainer_2)
        self.Q.setGeometry(QtCore.QRect(30, 30, 66, 66))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.Q.setFont(font)
        self.Q.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Q.setStyleSheet("QPushButton {\n"
"    background: transparent;\n"
"    border-radius: 10px;\n"
"    color: #23585A;\n"
"    border: 2px solid rgb(61, 152, 154);\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(61, 152, 154);\n"
"}")
        self.Q.setObjectName("Q")
        self.W = QtWidgets.QPushButton(self.KeyboardContainer_2)
        self.W.setGeometry(QtCore.QRect(100, 30, 66, 66))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.W.setFont(font)
        self.W.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.W.setStyleSheet("QPushButton {\n"
"    background: transparent;\n"
"    border-radius: 10px;\n"
"    color: #23585A;\n"
"    border: 2px solid rgb(61, 152, 154);\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(61, 152, 154);\n"
"}")
        self.W.setObjectName("W")
        self.E = QtWidgets.QPushButton(self.KeyboardContainer_2)
        self.E.setGeometry(QtCore.QRect(170, 30, 66, 66))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.E.setFont(font)
        self.E.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.E.setStyleSheet("QPushButton {\n"
"    background: transparent;\n"
"    border-radius: 10px;\n"
"    color: #23585A;\n"
"    border: 2px solid rgb(61, 152, 154);\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(61, 152, 154);\n"
"}")
        self.E.setObjectName("E")
        self.R = QtWidgets.QPushButton(self.KeyboardContainer_2)
        self.R.setGeometry(QtCore.QRect(240, 30, 66, 66))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.R.setFont(font)
        self.R.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.R.setStyleSheet("QPushButton {\n"
"    background: transparent;\n"
"    border-radius: 10px;\n"
"    color: #23585A;\n"
"    border: 2px solid rgb(61, 152, 154);\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(61, 152, 154);\n"
"}")
        self.R.setObjectName("R")
        self.T = QtWidgets.QPushButton(self.KeyboardContainer_2)
        self.T.setGeometry(QtCore.QRect(310, 30, 66, 66))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.T.setFont(font)
        self.T.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.T.setStyleSheet("QPushButton {\n"
"    background: transparent;\n"
"    border-radius: 10px;\n"
"    color: #23585A;\n"
"    border: 2px solid rgb(61, 152, 154);\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(61, 152, 154);\n"
"}")
        self.T.setObjectName("T")
        self.Y = QtWidgets.QPushButton(self.KeyboardContainer_2)
        self.Y.setGeometry(QtCore.QRect(380, 30, 66, 66))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.Y.setFont(font)
        self.Y.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Y.setStyleSheet("QPushButton {\n"
"    background: transparent;\n"
"    border-radius: 10px;\n"
"    color: #23585A;\n"
"    border: 2px solid rgb(61, 152, 154);\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(61, 152, 154);\n"
"}")
        self.Y.setObjectName("Y")
        self.U = QtWidgets.QPushButton(self.KeyboardContainer_2)
        self.U.setGeometry(QtCore.QRect(450, 30, 66, 66))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.U.setFont(font)
        self.U.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.U.setStyleSheet("QPushButton {\n"
"    background: transparent;\n"
"    border-radius: 10px;\n"
"    color: #23585A;\n"
"    border: 2px solid rgb(61, 152, 154);\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(61, 152, 154);\n"
"}")
        self.U.setObjectName("U")
        self.I = QtWidgets.QPushButton(self.KeyboardContainer_2)
        self.I.setGeometry(QtCore.QRect(520, 30, 66, 66))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.I.setFont(font)
        self.I.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.I.setStyleSheet("QPushButton {\n"
"    background: transparent;\n"
"    border-radius: 10px;\n"
"    color: #23585A;\n"
"    border: 2px solid rgb(61, 152, 154);\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(61, 152, 154);\n"
"}")
        self.I.setObjectName("I")
        self.O = QtWidgets.QPushButton(self.KeyboardContainer_2)
        self.O.setGeometry(QtCore.QRect(590, 30, 66, 66))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.O.setFont(font)
        self.O.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.O.setStyleSheet("QPushButton {\n"
"    background: transparent;\n"
"    border-radius: 10px;\n"
"    color: #23585A;\n"
"    border: 2px solid rgb(61, 152, 154);\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(61, 152, 154);\n"
"}")
        self.O.setObjectName("O")
        self.P = QtWidgets.QPushButton(self.KeyboardContainer_2)
        self.P.setGeometry(QtCore.QRect(660, 30, 66, 66))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.P.setFont(font)
        self.P.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.P.setStyleSheet("QPushButton {\n"
"    background: transparent;\n"
"    border-radius: 10px;\n"
"    color: #23585A;\n"
"    border: 2px solid rgb(61, 152, 154);\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(61, 152, 154);\n"
"}")
        self.P.setObjectName("P")
        self.zero = QtWidgets.QPushButton(self.KeyboardContainer_2)
        self.zero.setGeometry(QtCore.QRect(800, 240, 66, 66))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.zero.setFont(font)
        self.zero.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.zero.setStyleSheet("QPushButton {\n"
"    background: transparent;\n"
"    border-radius: 10px;\n"
"    color: #23585A;\n"
"    border: 2px solid rgb(61, 152, 154);\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(61, 152, 154);\n"
"}")
        self.zero.setObjectName("zero")
        self.one = QtWidgets.QPushButton(self.KeyboardContainer_2)
        self.one.setGeometry(QtCore.QRect(870, 170, 66, 66))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.one.setFont(font)
        self.one.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.one.setStyleSheet("QPushButton {\n"
"    background: transparent;\n"
"    border-radius: 10px;\n"
"    color: #23585A;\n"
"    border: 2px solid rgb(61, 152, 154);\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(61, 152, 154);\n"
"}")
        self.one.setObjectName("one")
        self.six = QtWidgets.QPushButton(self.KeyboardContainer_2)
        self.six.setGeometry(QtCore.QRect(870, 100, 66, 66))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.six.setFont(font)
        self.six.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.six.setStyleSheet("QPushButton {\n"
"    background: transparent;\n"
"    border-radius: 10px;\n"
"    color: #23585A;\n"
"    border: 2px solid rgb(61, 152, 154);\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(61, 152, 154);\n"
"}")
        self.six.setObjectName("six")
        self.three = QtWidgets.QPushButton(self.KeyboardContainer_2)
        self.three.setGeometry(QtCore.QRect(730, 170, 66, 66))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.three.setFont(font)
        self.three.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.three.setStyleSheet("QPushButton {\n"
"    background: transparent;\n"
"    border-radius: 10px;\n"
"    color: #23585A;\n"
"    border: 2px solid rgb(61, 152, 154);\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(61, 152, 154);\n"
"}")
        self.three.setObjectName("three")
        self.four = QtWidgets.QPushButton(self.KeyboardContainer_2)
        self.four.setGeometry(QtCore.QRect(730, 100, 66, 66))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.four.setFont(font)
        self.four.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.four.setStyleSheet("QPushButton {\n"
"    background: transparent;\n"
"    border-radius: 10px;\n"
"    color: #23585A;\n"
"    border: 2px solid rgb(61, 152, 154);\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(61, 152, 154);\n"
"}")
        self.four.setObjectName("four")
        self.nine = QtWidgets.QPushButton(self.KeyboardContainer_2)
        self.nine.setGeometry(QtCore.QRect(870, 30, 66, 66))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.nine.setFont(font)
        self.nine.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nine.setStyleSheet("QPushButton {\n"
"    background: transparent;\n"
"    border-radius: 10px;\n"
"    color: #23585A;\n"
"    border: 2px solid rgb(61, 152, 154);\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(61, 152, 154);\n"
"}")
        self.nine.setObjectName("nine")
        self.five = QtWidgets.QPushButton(self.KeyboardContainer_2)
        self.five.setGeometry(QtCore.QRect(800, 100, 66, 66))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.five.setFont(font)
        self.five.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.five.setStyleSheet("QPushButton {\n"
"    background: transparent;\n"
"    border-radius: 10px;\n"
"    color: #23585A;\n"
"    border: 2px solid rgb(61, 152, 154);\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(61, 152, 154);\n"
"}")
        self.five.setObjectName("five")
        self.eight = QtWidgets.QPushButton(self.KeyboardContainer_2)
        self.eight.setGeometry(QtCore.QRect(800, 30, 66, 66))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.eight.setFont(font)
        self.eight.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.eight.setStyleSheet("QPushButton {\n"
"    background: transparent;\n"
"    border-radius: 10px;\n"
"    color: #23585A;\n"
"    border: 2px solid rgb(61, 152, 154);\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(61, 152, 154);\n"
"}")
        self.eight.setObjectName("eight")
        self.two = QtWidgets.QPushButton(self.KeyboardContainer_2)
        self.two.setGeometry(QtCore.QRect(800, 170, 66, 66))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.two.setFont(font)
        self.two.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.two.setStyleSheet("QPushButton {\n"
"    background: transparent;\n"
"    border-radius: 10px;\n"
"    color: #23585A;\n"
"    border: 2px solid rgb(61, 152, 154);\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(61, 152, 154);\n"
"}")
        self.two.setObjectName("two")
        self.seven = QtWidgets.QPushButton(self.KeyboardContainer_2)
        self.seven.setGeometry(QtCore.QRect(730, 30, 66, 66))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.seven.setFont(font)
        self.seven.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.seven.setStyleSheet("QPushButton {\n"
"    background: transparent;\n"
"    border-radius: 10px;\n"
"    color: #23585A;\n"
"    border: 2px solid rgb(61, 152, 154);\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(61, 152, 154);\n"
"}")
        self.seven.setObjectName("seven")
        self.A = QtWidgets.QPushButton(self.KeyboardContainer_2)
        self.A.setGeometry(QtCore.QRect(50, 100, 66, 66))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.A.setFont(font)
        self.A.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.A.setStyleSheet("QPushButton {\n"
"    background: transparent;\n"
"    border-radius: 10px;\n"
"    color: #23585A;\n"
"    border: 2px solid rgb(61, 152, 154);\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(61, 152, 154);\n"
"}")
        self.A.setObjectName("A")
        self.H = QtWidgets.QPushButton(self.KeyboardContainer_2)
        self.H.setGeometry(QtCore.QRect(400, 100, 66, 66))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.H.setFont(font)
        self.H.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.H.setStyleSheet("QPushButton {\n"
"    background: transparent;\n"
"    border-radius: 10px;\n"
"    color: #23585A;\n"
"    border: 2px solid rgb(61, 152, 154);\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(61, 152, 154);\n"
"}")
        self.H.setObjectName("H")
        self.D = QtWidgets.QPushButton(self.KeyboardContainer_2)
        self.D.setGeometry(QtCore.QRect(190, 100, 66, 66))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.D.setFont(font)
        self.D.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.D.setStyleSheet("QPushButton {\n"
"    background: transparent;\n"
"    border-radius: 10px;\n"
"    color: #23585A;\n"
"    border: 2px solid rgb(61, 152, 154);\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(61, 152, 154);\n"
"}")
        self.D.setObjectName("D")
        self.F = QtWidgets.QPushButton(self.KeyboardContainer_2)
        self.F.setGeometry(QtCore.QRect(260, 100, 66, 66))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.F.setFont(font)
        self.F.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.F.setStyleSheet("QPushButton {\n"
"    background: transparent;\n"
"    border-radius: 10px;\n"
"    color: #23585A;\n"
"    border: 2px solid rgb(61, 152, 154);\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(61, 152, 154);\n"
"}")
        self.F.setObjectName("F")
        self.L = QtWidgets.QPushButton(self.KeyboardContainer_2)
        self.L.setGeometry(QtCore.QRect(610, 100, 66, 66))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.L.setFont(font)
        self.L.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.L.setStyleSheet("QPushButton {\n"
"    background: transparent;\n"
"    border-radius: 10px;\n"
"    color: #23585A;\n"
"    border: 2px solid rgb(61, 152, 154);\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(61, 152, 154);\n"
"}")
        self.L.setObjectName("L")
        self.G = QtWidgets.QPushButton(self.KeyboardContainer_2)
        self.G.setGeometry(QtCore.QRect(330, 100, 66, 66))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.G.setFont(font)
        self.G.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.G.setStyleSheet("QPushButton {\n"
"    background: transparent;\n"
"    border-radius: 10px;\n"
"    color: #23585A;\n"
"    border: 2px solid rgb(61, 152, 154);\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(61, 152, 154);\n"
"}")
        self.G.setObjectName("G")
        self.K = QtWidgets.QPushButton(self.KeyboardContainer_2)
        self.K.setGeometry(QtCore.QRect(540, 100, 66, 66))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.K.setFont(font)
        self.K.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.K.setStyleSheet("QPushButton {\n"
"    background: transparent;\n"
"    border-radius: 10px;\n"
"    color: #23585A;\n"
"    border: 2px solid rgb(61, 152, 154);\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(61, 152, 154);\n"
"}")
        self.K.setObjectName("K")
        self.S = QtWidgets.QPushButton(self.KeyboardContainer_2)
        self.S.setGeometry(QtCore.QRect(120, 100, 66, 66))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.S.setFont(font)
        self.S.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.S.setStyleSheet("QPushButton {\n"
"    background: transparent;\n"
"    border-radius: 10px;\n"
"    color: #23585A;\n"
"    border: 2px solid rgb(61, 152, 154);\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(61, 152, 154);\n"
"}")
        self.S.setObjectName("S")
        self.J = QtWidgets.QPushButton(self.KeyboardContainer_2)
        self.J.setGeometry(QtCore.QRect(470, 100, 66, 66))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.J.setFont(font)
        self.J.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.J.setStyleSheet("QPushButton {\n"
"    background: transparent;\n"
"    border-radius: 10px;\n"
"    color: #23585A;\n"
"    border: 2px solid rgb(61, 152, 154);\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(61, 152, 154);\n"
"}")
        self.J.setObjectName("J")
        self.B = QtWidgets.QPushButton(self.KeyboardContainer_2)
        self.B.setGeometry(QtCore.QRect(370, 170, 66, 66))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.B.setFont(font)
        self.B.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.B.setStyleSheet("QPushButton {\n"
"    background: transparent;\n"
"    border-radius: 10px;\n"
"    color: #23585A;\n"
"    border: 2px solid rgb(61, 152, 154);\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(61, 152, 154);\n"
"}")
        self.B.setObjectName("B")
        self.V = QtWidgets.QPushButton(self.KeyboardContainer_2)
        self.V.setGeometry(QtCore.QRect(300, 170, 66, 66))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.V.setFont(font)
        self.V.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.V.setStyleSheet("QPushButton {\n"
"    background: transparent;\n"
"    border-radius: 10px;\n"
"    color: #23585A;\n"
"    border: 2px solid rgb(61, 152, 154);\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(61, 152, 154);\n"
"}")
        self.V.setObjectName("V")
        self.M = QtWidgets.QPushButton(self.KeyboardContainer_2)
        self.M.setGeometry(QtCore.QRect(510, 170, 66, 66))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.M.setFont(font)
        self.M.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.M.setStyleSheet("QPushButton {\n"
"    background: transparent;\n"
"    border-radius: 10px;\n"
"    color: #23585A;\n"
"    border: 2px solid rgb(61, 152, 154);\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(61, 152, 154);\n"
"}")
        self.M.setObjectName("M")
        self.C = QtWidgets.QPushButton(self.KeyboardContainer_2)
        self.C.setGeometry(QtCore.QRect(230, 170, 66, 66))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.C.setFont(font)
        self.C.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.C.setStyleSheet("QPushButton {\n"
"    background: transparent;\n"
"    border-radius: 10px;\n"
"    color: #23585A;\n"
"    border: 2px solid rgb(61, 152, 154);\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(61, 152, 154);\n"
"}")
        self.C.setObjectName("C")
        self.Z = QtWidgets.QPushButton(self.KeyboardContainer_2)
        self.Z.setGeometry(QtCore.QRect(90, 170, 66, 66))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.Z.setFont(font)
        self.Z.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Z.setStyleSheet("QPushButton {\n"
"    background: transparent;\n"
"    border-radius: 10px;\n"
"    color: #23585A;\n"
"    border: 2px solid rgb(61, 152, 154);\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(61, 152, 154);\n"
"}")
        self.Z.setObjectName("Z")
        self.X = QtWidgets.QPushButton(self.KeyboardContainer_2)
        self.X.setGeometry(QtCore.QRect(160, 170, 66, 66))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.X.setFont(font)
        self.X.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.X.setStyleSheet("QPushButton {\n"
"    background: transparent;\n"
"    border-radius: 10px;\n"
"    color: #23585A;\n"
"    border: 2px solid rgb(61, 152, 154);\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(61, 152, 154);\n"
"}")
        self.X.setObjectName("X")
        self.N = QtWidgets.QPushButton(self.KeyboardContainer_2)
        self.N.setGeometry(QtCore.QRect(440, 170, 66, 66))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.N.setFont(font)
        self.N.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.N.setStyleSheet("QPushButton {\n"
"    background: transparent;\n"
"    border-radius: 10px;\n"
"    color: #23585A;\n"
"    border: 2px solid rgb(61, 152, 154);\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(61, 152, 154);\n"
"}")
        self.N.setObjectName("N")
        self.pushButton_76 = QtWidgets.QPushButton(self.KeyboardContainer_2)
        self.pushButton_76.setGeometry(QtCore.QRect(640, 240, 156, 66))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.pushButton_76.setFont(font)
        self.pushButton_76.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_76.setStyleSheet("QPushButton {\n"
"    background: transparent;\n"
"    border-radius: 10px;\n"
"    color: #23585A;\n"
"    border: 2px solid rgb(61, 152, 154);\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(61, 152, 154);\n"
"}")
        self.pushButton_76.setObjectName("pushButton_76")
        self.pushButton_77 = QtWidgets.QPushButton(self.KeyboardContainer_2)
        self.pushButton_77.setGeometry(QtCore.QRect(580, 170, 146, 66))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.pushButton_77.setFont(font)
        self.pushButton_77.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_77.setStyleSheet("QPushButton {\n"
"    background: transparent;\n"
"    border-radius: 10px;\n"
"    color: #23585A;\n"
"    border: 2px solid rgb(61, 152, 154);\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(61, 152, 154);\n"
"}")
        self.pushButton_77.setObjectName("pushButton_77")
        self.pushButton_78 = QtWidgets.QPushButton(self.KeyboardContainer_2)
        self.pushButton_78.setGeometry(QtCore.QRect(40, 240, 591, 66))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.pushButton_78.setFont(font)
        self.pushButton_78.setStyleSheet("QPushButton {\n"
"    background: transparent;\n"
"    border-radius: 10px;\n"
"    color: #23585A;\n"
"    border: 2px solid rgb(61, 152, 154);\n"
"    background-color: rgb(61, 152, 154);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"\n"
"    background-color: white;\n"
"}")
        self.pushButton_78.setText("")
        self.pushButton_78.setObjectName("pushButton_78")
        
        # Timer
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.videoStreaming)
        self.timer.start()
       
        
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Tokenfield", "Frame"))
        self.TokenID.setPlaceholderText(_translate("Tokenfield", "eg: XXXXX"))
        self.greetings.setText(_translate("Tokenfield", "Hello Friend,\n"
                "Please enter your Token code below"))       
        # self.Continue.setText(_translate("Tokenfield", "Continue"))
        # self.Continue.clicked.connect(self.continueTo)
        
        self.Cancel.setText(_translate("Tokenfield", "Cancel"))
        self.Cancel.clicked.connect(self.backTomain)
        
        self.greetings.setText(_translate("Tokenfield", "Hello Friend,\n"
        "Please enter your Token ID below"))

        self.Q.setText(_translate("Tokenfield", "Q"))
        self.W.setText(_translate("Tokenfield", "W"))
        self.E.setText(_translate("Tokenfield", "E"))
        self.R.setText(_translate("Tokenfield", "R"))
        self.T.setText(_translate("Tokenfield", "T"))
        self.Y.setText(_translate("Tokenfield", "Y"))
        self.U.setText(_translate("Tokenfield", "U"))
        self.I.setText(_translate("Tokenfield", "I"))
        self.O.setText(_translate("Tokenfield", "O"))
        self.P.setText(_translate("Tokenfield", "P"))
        self.zero.setText(_translate("Tokenfield", "0"))
        self.one.setText(_translate("Tokenfield", "1"))
        self.six.setText(_translate("Tokenfield", "6"))
        self.three.setText(_translate("Tokenfield", "3"))
        self.four.setText(_translate("Tokenfield", "4"))
        self.nine.setText(_translate("Tokenfield", "9"))
        self.five.setText(_translate("Tokenfield", "5"))
        self.eight.setText(_translate("Tokenfield", "8"))
        self.two.setText(_translate("Tokenfield", "2"))
        self.seven.setText(_translate("Tokenfield", "7"))
        self.A.setText(_translate("Tokenfield", "A"))
        self.H.setText(_translate("Tokenfield", "H"))
        self.D.setText(_translate("Tokenfield", "D"))
        self.F.setText(_translate("Tokenfield", "F"))
        self.L.setText(_translate("Tokenfield", "L"))
        self.G.setText(_translate("Tokenfield", "G"))
        self.K.setText(_translate("Tokenfield", "K"))
        self.S.setText(_translate("Tokenfield", "S"))
        self.J.setText(_translate("Tokenfield", "J"))
        self.B.setText(_translate("Tokenfield", "B"))
        self.V.setText(_translate("Tokenfield", "V"))
        self.M.setText(_translate("Tokenfield", "M"))
        self.C.setText(_translate("Tokenfield", "C"))
        self.Z.setText(_translate("Tokenfield", "Z"))
        self.X.setText(_translate("Tokenfield", "X"))
        self.N.setText(_translate("Tokenfield", "N"))
        # self.errorMessage.setText(_translate("Tokenfield", "Invalid Token"))
        
        self.pushButton_76.setText(_translate("Tokenfield", "Enter"))
        self.pushButton_77.setText(_translate("Tokenfield", "Backspace"))
        
        # Numpad
        self.one.clicked.connect(lambda: self.input_digit('1'))
        self.two.clicked.connect(lambda: self.input_digit('2'))
        self.three.clicked.connect(lambda: self.input_digit('3'))
        self.four.clicked.connect(lambda: self.input_digit('4'))
        self.five.clicked.connect(lambda: self.input_digit('5'))
        self.six.clicked.connect(lambda: self.input_digit('6'))
        self.seven.clicked.connect(lambda: self.input_digit('7'))
        self.eight.clicked.connect(lambda: self.input_digit('8'))
        self.nine.clicked.connect(lambda: self.input_digit('9'))
        self.zero.clicked.connect(lambda: self.input_digit('0'))
        
        # qwertypad
        self.Q.clicked.connect(lambda: self.input_digit('Q'))
        self.W.clicked.connect(lambda: self.input_digit('W'))
        self.E.clicked.connect(lambda: self.input_digit('E'))
        self.R.clicked.connect(lambda: self.input_digit('R'))
        self.T.clicked.connect(lambda: self.input_digit('T'))
        self.Y.clicked.connect(lambda: self.input_digit('Y'))
        self.U.clicked.connect(lambda: self.input_digit('U'))
        self.I.clicked.connect(lambda: self.input_digit('I'))
        self.O.clicked.connect(lambda: self.input_digit('O'))
        self.P.clicked.connect(lambda: self.input_digit('P'))
        
        self.A.clicked.connect(lambda: self.input_digit('A'))
        self.S.clicked.connect(lambda: self.input_digit('S'))
        self.D.clicked.connect(lambda: self.input_digit('D'))
        self.F.clicked.connect(lambda: self.input_digit('F'))
        self.G.clicked.connect(lambda: self.input_digit('G'))
        self.H.clicked.connect(lambda: self.input_digit('H'))
        self.J.clicked.connect(lambda: self.input_digit('J'))
        self.K.clicked.connect(lambda: self.input_digit('K'))
        self.L.clicked.connect(lambda: self.input_digit('L'))
        
        self.Z.clicked.connect(lambda: self.input_digit('Z'))
        self.X.clicked.connect(lambda: self.input_digit('X'))
        self.C.clicked.connect(lambda: self.input_digit('C'))
        self.V.clicked.connect(lambda: self.input_digit('V'))
        self.B.clicked.connect(lambda: self.input_digit('B'))
        self.N.clicked.connect(lambda: self.input_digit('N'))
        self.M.clicked.connect(lambda: self.input_digit('M'))

        self.pushButton_77.clicked.connect(self.backspace)
        self.pushButton_76.clicked.connect(self.continueTo)
        self.pushButton_78.clicked.connect(self.SPACEBAR)

    def input_digit(self, digit):
            
        # self.errorMessage.setText("")
        current_text = self.TokenID.text()
        # if len(current_text) == 1:
        #         current_text = current_text + "-"

        
        if len(current_text) != 6:   
            self.TokenID.setText(current_text + digit) 
                
        # self.TokenID.setText(current_text + digit)
                
    def backspace(self):
        current_text = self.TokenID.text()
        if current_text:
            updated_text = current_text[:-1]  # Remove the last character
            self.TokenID.setText(updated_text)
           
    def SPACEBAR(self):
        current_text = self.TokenID.text()
        if current_text:
            current_text = current_text + " "
            self.TokenID.setText(current_text)
                  
    def backTomain(self):
        self.stop_streaming()
        
        self.main_menu.upload_banned_person()
        self.main_menu.timers(False)  
        self.close()
    
    # Function to delete folders recursively
    def delete_folders(self): 
        path= "Known_Faces"
        
        # Read data from Firebase
        data = firebaseRead("LOCK")
        
        if data == False:
            return
        
        folders_to_keep = list(data.keys())

        for root, dirs, files in os.walk(path, topdown=False):
            for folder in dirs:
                folder_path = os.path.join(root, folder)
                if folder not in folders_to_keep:
                    print(f"Deleting folder: {folder_path}")
                    shutil.rmtree(folder_path)
                
    def continueTo(self):
            
        # delete unregistered folder
        self.delete_folders()
        
        # check if TokenID is not empty
        if not self.TokenID.text():
            return self.messageBoxShow(
                title="AIoT Smartlock",
                text="Token field cannot be empty",
                buttons=self.MessageBox.Ok)
            
        # spam recognition result
        text,result_spam,__,__ = self.anti_spam()
        
        if result_spam:
                
            self.backTomain()
            
            return self.messageBoxShow(
                title="AIoT Smartlock",
                text=text,
                buttons=self.MessageBox.Ok)
        
        result = firebaseTokenVerify(self.TokenID.text())  
        
        # if invalid Token
        if result == None:
            formatted_text = "<b>Invalid Token Detected!</b>"
            
            return self.messageBoxShow(
                title="AIoT Smartlock",
                text=formatted_text + " To perform Facial Updates/Facial Register, you must generate a valid token from the AIoT Smartlock webApp.",
                buttons=self.MessageBox.Ok)
        
        # words = str(result).split(',')
        self.rearranged_string = str(result)

        # Define the path for the known faces folder
        path = f"Known_Faces/{str(result)}"
        
        if os.path.exists(path):
            # Remove all contents of the folder
            shutil.rmtree(path)

        # Create the known faces folder if it doesn't exist
        os.makedirs(path, exist_ok=True)

        # pass the {self.TokenID.text()} into facialRegister username label
        self.errorMessage.setText("Loading..............")   
        
        self.pushButton_76.setEnabled(False)
        self.Cancel.setEnabled(False)
        
        firebaseDeleteVerifiedToken(str(result))
        
        self.stop_streaming()
        
        # Delay the creation of the toFacialRegister object by 100 milliseconds
        QtCore.QTimer.singleShot(50, self.toFacialRegister)
            
    def toFacialRegister(self):
        
        from pages.Facial_Register import facialRegister
        
        FacialRegister = facialRegister(self)
        
        self.data_passed.connect(FacialRegister.receive)
        self.data_passed.emit(self.rearranged_string)
        # self.data_passed.emit(self.TokenID.text())
        
        FacialRegister.show()
        self.TokenID.setText("")
        self.errorMessage.setText("")

    def messageBoxShow(self, title=None, text=None, buttons=None):

        # Set the window icon, title, and text
        self.MessageBox.setWindowTitle(title)
        self.MessageBox.setText(text)

        # Set the window size
        self.MessageBox.setFixedWidth(400)

        # Set the standard buttons
        self.MessageBox.setStandardButtons(buttons)

        result = self.MessageBox.exec_()

        self.MessageBox.close()
        # Show the message box and return the result
        return result

    # for video streaming
    def videoStreaming(self):
        ret, frame = self.videoStream.read()
        
        # if no detected frames
        if not ret:
            self.messageBoxShow(
                title="FACIAL REGISTER",
                text="Unable to open camera. Please contact the administrator for assistance.",
                buttons=self.MessageBox.Ok
            )
            self.backTomain()
            return
        
        # process the frame
        frame = cv2.flip(frame, 1)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
        # load facial detector haar
        faces = self.face_detector.detectMultiScale(gray,
                                                    scaleFactor=1.1,
                                                    minNeighbors=20,
                                                    minSize=(100, 100),
                                                    flags=cv2.CASCADE_SCALE_IMAGE)
        

        # detect one face only
        if len(faces) == 1:
            
            x, y, w, h = faces[0]
            faceCrop = frame[y:y+h, x:x+w]
            face_gray = cv2.cvtColor(faceCrop, cv2.COLOR_BGR2GRAY)
            
            
            # Calculate the Laplacian
            laplacian = cv2.Laplacian(face_gray, cv2.CV_64F)
    
            # Calculate the variance of the Laplacian
            variance = laplacian.var()
            
            # blurred level
            Face_blurred = float("{:.2f}".format(variance))
            
            self.greetings.setText("Hello Friend,\nPlease enter your Token code below")

            if Face_blurred < 0:
                self.greetings.setText("Camera feed is blurred. Please ensure the camera is clean")
             

        # Multiple Face Detected
        elif len(faces) >= 1:    
            self.greetings.setText("Multiple faces detected. Please ensure only one face is visible")

        # No face detected
        else:
            self.greetings.setText("No face detected. Please ensure your face is visible.")
        
    # spam recognition
    def anti_spam(self):
                
        ret, image = self.videoStream.read()
        
        if not ret:
            return "camera unable to capture"
        
            # process the frame
        image = cv2.flip(image, 1)
                        
            # check spam detection
        result = Jolo().spam_detection(image=image,threshold=0.7)
        
        person = result[0]  # None 
        spam_detected = result[2] # if detected
        error_occur = result[3]
        
        text,result = "",False

        # if detected it will save images
        if spam_detected and error_occur == None:
            
            # verify person is in database
            text,result = create_person_temporarily_banned(person,"Facial")
        
        # return Text result 
        return text,result,person,image

    def stop_streaming(self):
        self.videoStream.release()
        cv2.destroyAllWindows()
        self.timer.stop()
            
if __name__ == "__main__":
    
    import sys,background
    # Create a new QApplication object
    app = QApplication(sys.argv)

    New_menu = TokenForm()
    New_menu.show()

    sys.exit(app.exec_())
