import typing
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget

class TokenForm(QtWidgets.QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # frame
        self.setObjectName("Tokenfield")
        self.resize(800, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/background/Images/logo192x192.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setStyleSheet("background-color: rgb(231, 229, 213);\n"
        "background-image: url(:/background/Images/background-removebg-preview.png);\n"
        "background-position: center;\n")
        
    def retranslateUi(self, Tokenfield):
        _translate = QtCore.QCoreApplication.translate
        # Tokenfield.setWindowTitle(_translate("Tokenfield", "Frame"))
        # self.TokenID.setText(_translate("Tokenfield", "Token ID"))
        # self.Continue.setText(_translate("Tokenfield", "Continue"))
        # self.Cancel.setText(_translate("Tokenfield", "Cancel"))
        
        
if __name__ == "__main__":
    
    import sys,background
    # Create a new QApplication object
    app = QApplication(sys.argv)

    New_menu = TokenForm()
    New_menu.show()

    sys.exit(app.exec_())