from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets

class QwertyKeyboard(QtWidgets.QFrame):
    def __init__(self, parent=None):
        super().__init__()
        
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
        
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        
        
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Pincode", "Frame"))
#         self.TokenID_3.setText(_translate("MainWindow", "eg: XXXXXX"))
#         self.TokenID_3.setPlaceholderText(_translate("MainWindow", "Token ID"))

#         self.seven_2.setText(_translate("MainWindow", "1"))
#         self.seven_3.setText(_translate("MainWindow", "2"))
#         self.seven_4.setText(_translate("MainWindow", "3"))
#         self.seven_5.setText(_translate("MainWindow", "5"))
#         self.seven_6.setText(_translate("MainWindow", "4"))
#         self.seven_7.setText(_translate("MainWindow", "6"))
#         self.seven_8.setText(_translate("MainWindow", "9"))
#         self.seven_9.setText(_translate("MainWindow", "7"))
#         self.seven_10.setText(_translate("MainWindow", "8"))
#         self.seven_13.setText(_translate("MainWindow", "0"))

        self.Cancel_2.setText(_translate("MainWindow", "Cancel"))

#         self.greetings.setText(_translate("MainWindow", "Hello Friend,\n"
# "Please choose your name and enter your pincode"))
#         self.checkBox.setText(_translate("MainWindow", "Show Password"))





if __name__ == "__main__":
    
    import sys,background
    # Create a new QApplication object
    app = QApplication(sys.argv)

    New_menu = QwertyKeyboard()
    New_menu.show() 

    sys.exit(app.exec_())
