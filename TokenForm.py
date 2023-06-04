
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Tokenfield(object):
    def setupUi(self, Tokenfield):
        Tokenfield.setObjectName("Tokenfield")
        Tokenfield.resize(800, 480)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(36)
        Tokenfield.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/background/Images/logo192x192.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Tokenfield.setWindowIcon(icon)
        Tokenfield.setStyleSheet("background-color: rgb(231, 229, 213);\n"
"background-image: url(:/background/Images/background-removebg-preview.png);\n"
"background-position: center;\n"
"")
        self.TokenID = QtWidgets.QLineEdit(Tokenfield)
        self.TokenID.setGeometry(QtCore.QRect(110, 180, 581, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(30)
        self.TokenID.setFont(font)
        self.TokenID.setStyleSheet("background: transparents;\n"
"color: rgb(156, 156, 156);\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid #3D989A;\n"
"border-radius: 40px;")
        self.TokenID.setAlignment(QtCore.Qt.AlignCenter)
        self.TokenID.setObjectName("TokenID")
        self.Continue = QtWidgets.QPushButton(Tokenfield)
        self.Continue.setGeometry(QtCore.QRect(420, 290, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Continue.setFont(font)
        self.Continue.setStyleSheet("border: none;\n"
"background: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"border-radius: 25px;\n"
"color: white;")
        self.Continue.setObjectName("Continue")
        self.Cancel = QtWidgets.QPushButton(Tokenfield)
        self.Cancel.setGeometry(QtCore.QRect(220, 290, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Cancel.setFont(font)
        self.Cancel.setStyleSheet("border: 2px solid #3D989A;\n"
"border-radius: 25px;\n"
"color: #3D989A;")
        self.Cancel.setObjectName("Cancel")

        self.retranslateUi(Tokenfield)
        QtCore.QMetaObject.connectSlotsByName(Tokenfield)

    def retranslateUi(self, Tokenfield):
        _translate = QtCore.QCoreApplication.translate
        Tokenfield.setWindowTitle(_translate("Tokenfield", "Frame"))
        self.TokenID.setText(_translate("Tokenfield", "Token ID"))
        self.Continue.setText(_translate("Tokenfield", "Continue"))
        self.Cancel.setText(_translate("Tokenfield", "Cancel"))


if __name__ == "__main__":
    import sys,background
    app = QtWidgets.QApplication(sys.argv)
    
    mainMenu = QtWidgets.QFrame()  # Create a QFrame instance
    
    ui = Ui_Tokenfield()  # Create an instance of the UI class
    ui.setupUi(mainMenu)  # Setup the UI on the QFrame
    
    mainMenu.show()  # Show the QFrame
    
    sys.exit(app.exec_())