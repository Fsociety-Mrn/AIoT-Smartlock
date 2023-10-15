from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets


class AdminLock(QtWidgets.QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # frame settings
        self.setObjectName("Facial Login")
        self.resize(1024, 565)

        self.widget = QtWidgets.QWidget(self)
        self.widget.setObjectName("centralwidget")
        self.setStyleSheet("background-color: rgb(231, 229, 213);\n"
            "background-image: url(:/background/Images/background.jpg);\n"
            "background-position: center;\n"
            "\n""")
        
        self.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.setFrameShadow(QtWidgets.QFrame.Raised)
        self.setObjectName("frame")   
        
        # greetings
        self.greetings = QtWidgets.QLabel(self)
        self.greetings.setGeometry(QtCore.QRect(0, 0, 1021, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.greetings.setFont(font)
        self.greetings.setStyleSheet("color: #3D989A")
        self.greetings.setAlignment(QtCore.Qt.AlignCenter)
        self.greetings.setObjectName("greetings")
        
        # warning
        self.warning = QtWidgets.QLabel(self)
        self.warning.setGeometry(QtCore.QRect(0, 50, 1021, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.warning.setFont(font)
        self.warning.setStyleSheet("color: #3D989A")
        self.warning.setAlignment(QtCore.Qt.AlignCenter)
        self.warning.setObjectName("greetings")
        
        # Token ID
        self.TokenID = QtWidgets.QLineEdit(self)
        self.TokenID.setGeometry(QtCore.QRect(230, 140, 531, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        self.TokenID.setFont(font)
        self.TokenID.setStyleSheet("background: transparents;\n"
"color: #3D989A;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid #3D989A;\n"
"border-radius: 20px;")
        self.TokenID.setText("")
        self.TokenID.setAlignment(QtCore.Qt.AlignCenter)
        self.TokenID.setObjectName("TokenID")
        
        # Container
        self.KeyboardContainer = QtWidgets.QWidget(self)
        self.KeyboardContainer.setGeometry(QtCore.QRect(25, 220, 971, 331))
        self.KeyboardContainer.setStyleSheet("border: 2px solid rgb(61, 152, 154) ;\n"
"border-radius: 50px;")
        
        self.Q = QtWidgets.QPushButton(self.KeyboardContainer)
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
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(61, 152, 154);\n"
"}")
        self.Q.setObjectName("Q")

        self.W = QtWidgets.QPushButton(self.KeyboardContainer)
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
        
        self.E = QtWidgets.QPushButton(self.KeyboardContainer)
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
        self.R = QtWidgets.QPushButton(self.KeyboardContainer)
        
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
        
        self.T = QtWidgets.QPushButton(self.KeyboardContainer)
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
        
        self.Y = QtWidgets.QPushButton(self.KeyboardContainer)
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
        
        self.U = QtWidgets.QPushButton(self.KeyboardContainer)
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
        
        self.I = QtWidgets.QPushButton(self.KeyboardContainer)
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
        
        self.O = QtWidgets.QPushButton(self.KeyboardContainer)
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
        
        self.P = QtWidgets.QPushButton(self.KeyboardContainer)
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
        
        self.zero = QtWidgets.QPushButton(self.KeyboardContainer)
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
        
        self.one = QtWidgets.QPushButton(self.KeyboardContainer)
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
        
        self.six = QtWidgets.QPushButton(self.KeyboardContainer)
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
        
        self.three = QtWidgets.QPushButton(self.KeyboardContainer)
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
        
        self.four = QtWidgets.QPushButton(self.KeyboardContainer)
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
        
        self.nine = QtWidgets.QPushButton(self.KeyboardContainer)
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
        
        self.five = QtWidgets.QPushButton(self.KeyboardContainer)
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
        
        self.eight = QtWidgets.QPushButton(self.KeyboardContainer)
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
        
        self.two = QtWidgets.QPushButton(self.KeyboardContainer)
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
        
        self.seven = QtWidgets.QPushButton(self.KeyboardContainer)
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
        
        self.A = QtWidgets.QPushButton(self.KeyboardContainer)
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
        
        self.H = QtWidgets.QPushButton(self.KeyboardContainer)
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
        
        self.D = QtWidgets.QPushButton(self.KeyboardContainer)
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
        
        self.F = QtWidgets.QPushButton(self.KeyboardContainer)
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
        
        self.L = QtWidgets.QPushButton(self.KeyboardContainer)
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
        
        self.G = QtWidgets.QPushButton(self.KeyboardContainer)
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
        
        self.K = QtWidgets.QPushButton(self.KeyboardContainer)
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
        
        self.S = QtWidgets.QPushButton(self.KeyboardContainer)
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
        
        self.J = QtWidgets.QPushButton(self.KeyboardContainer)
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
        
        self.B = QtWidgets.QPushButton(self.KeyboardContainer)
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
        
        self.V = QtWidgets.QPushButton(self.KeyboardContainer)
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
        
        self.M = QtWidgets.QPushButton(self.KeyboardContainer)
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
        
        self.C = QtWidgets.QPushButton(self.KeyboardContainer)
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
        
        self.Z = QtWidgets.QPushButton(self.KeyboardContainer)
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
        
        self.X = QtWidgets.QPushButton(self.KeyboardContainer)
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
        
        self.N = QtWidgets.QPushButton(self.KeyboardContainer)
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
        
        self.pushButton_76 = QtWidgets.QPushButton(self.KeyboardContainer)
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
        
        self.pushButton_77 = QtWidgets.QPushButton(self.KeyboardContainer)
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
        
        self.pushButton_78 = QtWidgets.QPushButton(self.KeyboardContainer)
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
        
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.greetings.setText(_translate("Admin Lock", "AIoT Smartlock is Online"))
        self.warning.setText(_translate("Admin Lock", "Please enter the token ID to unlock the AIoT Smartlock"))
        self.TokenID.setPlaceholderText(_translate("Admin Lock", "eg: EEE-XXXXX"))

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
        self.pushButton_76.setText(_translate("Tokenfield", "Enter"))
        self.pushButton_77.setText(_translate("Tokenfield", "Backspace"))
        
        
# ************************** functions ************************** #

        # LETTER
        self.Q.clicked.connect(lambda: self.input_texts('Q'))
        self.W.clicked.connect(lambda: self.input_texts('W'))
        self.E.clicked.connect(lambda: self.input_texts('E'))
        self.R.clicked.connect(lambda: self.input_texts('R'))
        self.T.clicked.connect(lambda: self.input_texts('T'))
        self.Y.clicked.connect(lambda: self.input_texts('Y'))
        self.U.clicked.connect(lambda: self.input_texts('U'))
        self.I.clicked.connect(lambda: self.input_texts('I'))
        self.O.clicked.connect(lambda: self.input_texts('O'))
        self.P.clicked.connect(lambda: self.input_texts('P'))
        
        self.A.clicked.connect(lambda: self.input_texts('A'))
        self.S.clicked.connect(lambda: self.input_texts('S'))
        self.D.clicked.connect(lambda: self.input_texts('D'))
        self.F.clicked.connect(lambda: self.input_texts('F'))
        self.G.clicked.connect(lambda: self.input_texts('G'))
        self.H.clicked.connect(lambda: self.input_texts('H'))
        self.J.clicked.connect(lambda: self.input_texts('J'))
        self.K.clicked.connect(lambda: self.input_texts('K'))
        self.L.clicked.connect(lambda: self.input_texts('L'))
        
        self.Z.clicked.connect(lambda: self.input_texts('Z'))
        self.X.clicked.connect(lambda: self.input_texts('X'))
        self.C.clicked.connect(lambda: self.input_texts('C'))
        self.V.clicked.connect(lambda: self.input_texts('V'))
        self.B.clicked.connect(lambda: self.input_texts('B'))
        self.N.clicked.connect(lambda: self.input_texts('N'))
        self.M.clicked.connect(lambda: self.input_texts('M'))

        # numpad
        self.one.clicked.connect(lambda: self.input_texts('1'))
        self.two.clicked.connect(lambda: self.input_texts('2'))
        self.three.clicked.connect(lambda: self.input_texts('3'))
        self.four.clicked.connect(lambda: self.input_texts('4'))
        self.five.clicked.connect(lambda: self.input_texts('5'))
        self.six.clicked.connect(lambda: self.input_texts('6'))
        self.seven.clicked.connect(lambda: self.input_texts('7'))
        self.eight.clicked.connect(lambda: self.input_texts('8'))
        self.nine.clicked.connect(lambda: self.input_texts('9'))
        self.zero.clicked.connect(lambda: self.input_texts('0'))
        
        # BACKSPACE
        self.pushButton_77.clicked.connect(self.backspace)
        
    def input_texts(self, text):
        current_text = self.TokenID.text()
        self.TokenID.setText(current_text + text)
        
    def backspace(self):
        current_text = self.TokenID.text()
        if current_text:
            updated_text = current_text[:-1]  # Remove the last character
            self.TokenID.setText(updated_text)

if __name__ == "__main__":
    
    import sys,background
    # Create a new QApplication object
    app = QApplication(sys.argv)

    New_menu = AdminLock()
    New_menu.show() 

    sys.exit(app.exec_())
