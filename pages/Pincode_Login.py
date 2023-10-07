from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets


class PincodeLogin(QtWidgets.QFrame):
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
        
        # Greetings
        self.greetings = QtWidgets.QLabel(self)
        self.greetings.setGeometry(QtCore.QRect(-10, 0, 1031, 181))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(21)
        font.setBold(False)
        font.setWeight(50)
        self.greetings.setFont(font)
        self.greetings.setStyleSheet("color: #3D989A")
        self.greetings.setAlignment(QtCore.Qt.AlignCenter)
        self.greetings.setObjectName("greetings")
        
        # show password
        self.checkBox = QtWidgets.QCheckBox(self)
        self.checkBox.setGeometry(QtCore.QRect(140, 370, 131, 17))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("    QCheckBox {\n"
"                                                    color: #3D989A;\n"
"                                                }\n"
"                                                QCheckBox::indicator:checked {\n"
"                                                    background-color: #3D989A;\n"
"                                                    border: 1px solid #3D989A;\n"
"                                                }\n"
"                                                QCheckBox::indicator:unchecked {\n"
"                                                    background-color: transparent;\n"
"                                                    border: 1px solid #3D989A;\n"
"                                                }")  
        
        # cancel button
        self.Cancel_2 = QtWidgets.QPushButton(self)
        self.Cancel_2.setGeometry(QtCore.QRect(20, 20, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Cancel_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Cancel_2.setFont(font)
        self.Cancel_2.setStyleSheet("QPushButton {\n"
                "    background: transparent;\n"
                "    background-color: white;\n"
                "    border-radius: 25px;\n"
                "    color: #23585A;\n"
                "    border: 2px solid rgb(61, 152, 154);\n"
                "}\n"
                "\n"
                "QPushButton:hover {\n"
                "    background-color: rgb(61, 152, 154);\n"
                "}")
        self.Cancel_2.setObjectName("Cancel_2")   
        
        # combobox
        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(130, 220, 431, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("background: transparents;\n"
            "color: #3D989A;\n"
            "background-color: rgb(255, 255, 255);\n"
            "border: 1px solid #3D989A;\n"
        "")
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        
        self.TokenID_3 = QtWidgets.QLineEdit(self)
        self.TokenID_3.setGeometry(QtCore.QRect(130, 290, 431, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.TokenID_3.setFont(font)
        self.TokenID_3.setStyleSheet("background: transparents;\n"
            "color: #3D989A;\n"
            "background-color: rgb(255, 255, 255);\n"
            "border: 1px solid #3D989A;\n"
            "border-radius: 25px;\n"
        "")
        self.TokenID_3.setAlignment(QtCore.Qt.AlignCenter)
        self.TokenID_3.setObjectName("TokenID_3")
        
        # Keypad
        self.KeyboardContainer_3 = QtWidgets.QWidget(self)
        self.KeyboardContainer_3.setGeometry(QtCore.QRect(610, 170, 261, 341))
        self.KeyboardContainer_3.setObjectName("KeyboardContainer_3")
        
        # one
        self.seven_2 = QtWidgets.QPushButton(self.KeyboardContainer_3)
        self.seven_2.setGeometry(QtCore.QRect(20, 20, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.seven_2.setFont(font)
        self.seven_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.seven_2.setStyleSheet("QPushButton {\n"
        "    background: transparent;\n"
        "    background-color: white;\n"
        "    border-radius: 30px;\n"
        "    color: #23585A;\n"
        "    border: 2px solid rgb(61, 152, 154);\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(61, 152, 154);\n"
        "}")
        self.seven_2.setObjectName("seven_2")
        
        # 2
        self.seven_3 = QtWidgets.QPushButton(self.KeyboardContainer_3)
        self.seven_3.setGeometry(QtCore.QRect(100, 20, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.seven_3.setFont(font)
        self.seven_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.seven_3.setStyleSheet("QPushButton {\n"
            "    background: transparent;\n"
            "    border-radius: 30px;\n"
            "    color: #23585A;\n"
            "    border: 2px solid rgb(61, 152, 154);\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: rgb(61, 152, 154);\n"
        "}")
        self.seven_3.setObjectName("seven_3")
        
        # 3
        self.seven_4 = QtWidgets.QPushButton(self.KeyboardContainer_3)
        self.seven_4.setGeometry(QtCore.QRect(180, 20, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.seven_4.setFont(font)
        self.seven_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.seven_4.setStyleSheet("QPushButton {\n"
"    background: transparent;\n"
"    border-radius: 30px;\n"
"    color: #23585A;\n"
"    border: 2px solid rgb(61, 152, 154);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(61, 152, 154);\n"
"}")
        self.seven_4.setObjectName("seven_4")
        
        # 4
        self.seven_5 = QtWidgets.QPushButton(self.KeyboardContainer_3)
        self.seven_5.setGeometry(QtCore.QRect(100, 100, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.seven_5.setFont(font)
        self.seven_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.seven_5.setStyleSheet("QPushButton {\n"
"    background: transparent;\n"
"    border-radius: 30px;\n"
"    color: #23585A;\n"
"    border: 2px solid rgb(61, 152, 154);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(61, 152, 154);\n"
"}")
        self.seven_5.setObjectName("seven_5")
        
        # 5
        self.seven_6 = QtWidgets.QPushButton(self.KeyboardContainer_3)
        self.seven_6.setGeometry(QtCore.QRect(20, 100, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.seven_6.setFont(font)
        self.seven_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.seven_6.setStyleSheet("QPushButton {\n"
"    background: transparent;\n"
"    border-radius: 30px;\n"
"    color: #23585A;\n"
"    border: 2px solid rgb(61, 152, 154);\n"
"    background-color:white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(61, 152, 154);\n"
"}")
        self.seven_6.setObjectName("seven_6")
        
        # 6
        self.seven_7 = QtWidgets.QPushButton(self.KeyboardContainer_3)
        self.seven_7.setGeometry(QtCore.QRect(180, 100, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.seven_7.setFont(font)
        self.seven_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.seven_7.setStyleSheet("QPushButton {\n"
"    background: transparent;\n"
"    border-radius: 30px;\n"
"    color: #23585A;\n"
"    border: 2px solid rgb(61, 152, 154);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(61, 152, 154);\n"
"}")
        self.seven_7.setObjectName("seven_7")
        
        # 7
        self.seven_8 = QtWidgets.QPushButton(self.KeyboardContainer_3)
        self.seven_8.setGeometry(QtCore.QRect(180, 180, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.seven_8.setFont(font)
        self.seven_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.seven_8.setStyleSheet("QPushButton {\n"
"    background: transparent;\n"
"    border-radius: 30px;\n"
"    color: #23585A;\n"
"    border: 2px solid rgb(61, 152, 154);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(61, 152, 154);\n"
"}")
        self.seven_8.setObjectName("seven_8")
        
        # 8
        self.seven_9 = QtWidgets.QPushButton(self.KeyboardContainer_3)
        self.seven_9.setGeometry(QtCore.QRect(20, 180, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.seven_9.setFont(font)
        self.seven_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.seven_9.setStyleSheet("QPushButton {\n"
"    background: transparent;\n"
"    border-radius: 30px;\n"
"    color: #23585A;\n"
"    border: 2px solid rgb(61, 152, 154);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(61, 152, 154);\n"
"}")
        self.seven_9.setObjectName("seven_9")
        
        # 9
        self.seven_10 = QtWidgets.QPushButton(self.KeyboardContainer_3)
        self.seven_10.setGeometry(QtCore.QRect(100, 180, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.seven_10.setFont(font)
        self.seven_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.seven_10.setStyleSheet("QPushButton {\n"
"    background: transparent;\n"
"    border-radius: 30px;\n"
"    color: #23585A;\n"
"    border: 2px solid rgb(61, 152, 154);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(61, 152, 154);\n"
"}")
        self.seven_10.setObjectName("seven_10")
        
        # delete
        self.seven_11 = QtWidgets.QPushButton(self.KeyboardContainer_3)
        self.seven_11.setGeometry(QtCore.QRect(180, 260, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.seven_11.setFont(font)
        self.seven_11.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.seven_11.setStyleSheet("QPushButton {\n"
"    background: transparent;\n"
"    border-radius: 30px;\n"
"    color: #23585A;\n"
"    border: 2px solid rgb(61, 152, 154);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(61, 152, 154);\n"
"}")
        self.seven_11.setText("")
        
        icon = QtGui.QIcon()
        pixmap = QtGui.QPixmap("Images/check.png")
        icon.addPixmap(pixmap, QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.seven_11.setIcon(icon)
        self.seven_11.setIconSize(QtCore.QSize(20, 20))
        self.seven_11.setObjectName("seven_11")
        
        # eneter
        self.seven_12 = QtWidgets.QPushButton(self.KeyboardContainer_3)
        self.seven_12.setGeometry(QtCore.QRect(20, 260, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.seven_12.setFont(font)
        self.seven_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.seven_12.setStyleSheet("QPushButton {\n"
"    background: transparent;\n"
"    border-radius: 30px;\n"
"    color: #23585A;\n"
"    border: 2px solid rgb(61, 152, 154);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(61, 152, 154);\n"
"}")
        self.seven_12.setText("")
        icon1 = QtGui.QIcon()
        pixmap = QtGui.QPixmap("Images/backspace.png")
        icon1.addPixmap(pixmap, QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.seven_12.setIcon(icon1)
        self.seven_12.setIconSize(QtCore.QSize(24, 24))
        self.seven_12.setFlat(False)
        self.seven_12.setObjectName("seven_12")
        
        # 0
        self.seven_13 = QtWidgets.QPushButton(self.KeyboardContainer_3)
        self.seven_13.setGeometry(QtCore.QRect(100, 260, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.seven_13.setFont(font)
        self.seven_13.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.seven_13.setStyleSheet("QPushButton {\n"
"    background: transparent;\n"
"    border-radius: 30px;\n"
"    color: #23585A;\n"
"    border: 2px solid rgb(61, 152, 154);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(61, 152, 154);\n"
"}")
        self.seven_13.setObjectName("seven_13")
        
        self.Cancel_2 = QtWidgets.QPushButton(self)
        self.Cancel_2.setGeometry(QtCore.QRect(20, 20, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Cancel_2.setFont(font)
        self.Cancel_2.setStyleSheet("QPushButton {\n"
"    background: transparent;\n"
"    background-color: white;\n"
"    border-radius: 25px;\n"
"    color: #23585A;\n"
"    border: 2px solid rgb(61, 152, 154);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(61, 152, 154);\n"
"}")
        self.Cancel_2.setObjectName("Cancel_2")
        self.Cancel_2.clicked.connect(self.cancel)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        
        
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Pincode", "Frame"))
        self.TokenID_3.setPlaceholderText(_translate("MainWindow", "eg: XXXXXX"))

        self.seven_2.setText(_translate("MainWindow", "1"))
        self.seven_3.setText(_translate("MainWindow", "2"))
        self.seven_4.setText(_translate("MainWindow", "3"))
        self.seven_5.setText(_translate("MainWindow", "5"))
        self.seven_6.setText(_translate("MainWindow", "4"))
        self.seven_7.setText(_translate("MainWindow", "6"))
        self.seven_8.setText(_translate("MainWindow", "9"))
        self.seven_9.setText(_translate("MainWindow", "7"))
        self.seven_10.setText(_translate("MainWindow", "8"))
        self.seven_13.setText(_translate("MainWindow", "0"))
        
        self.seven_12.clicked.connect(self.backspace)

        
        self.seven_2.clicked.connect(lambda: self.input_digit('1'))
        self.seven_3.clicked.connect(lambda: self.input_digit('2'))
        self.seven_4.clicked.connect(lambda: self.input_digit('3'))
        self.seven_5.clicked.connect(lambda: self.input_digit('4'))
        self.seven_6.clicked.connect(lambda: self.input_digit('5'))
        self.seven_7.clicked.connect(lambda: self.input_digit('6'))
        self.seven_8.clicked.connect(lambda: self.input_digit('7'))
        self.seven_9.clicked.connect(lambda: self.input_digit('8'))
        self.seven_10.clicked.connect(lambda: self.input_digit('9'))
        self.seven_13.clicked.connect(lambda: self.input_digit('0'))


        self.Cancel_2.setText(_translate("MainWindow", "Cancel"))

        self.greetings.setText(_translate("MainWindow", "Hello Friend,\n"
        "\Please choose your name and enter your pincode"))
        self.checkBox.setText(_translate("MainWindow", "Show Password"))

    def input_digit(self, digit):
        current_text = self.TokenID_3.text()
        self.TokenID_3.setText(current_text + digit)
        
        
    def backspace(self):
        current_text = self.TokenID_3.text()
        if current_text:
            updated_text = current_text[:-1]  # Remove the last character
            self.TokenID_3.setText(updated_text)
            
    def cancel(self):
        from pages.Main_Menu import MainWindow
        
        print("go back to main menu")

        # self.resize(1024, 565)
        # MainWindow(self).show()
        self.close()


if __name__ == "__main__":
    
    import sys,background
    # Create a new QApplication object
    app = QApplication(sys.argv)

    New_menu = PincodeLogin()
    New_menu.show() 

    sys.exit(app.exec_())
