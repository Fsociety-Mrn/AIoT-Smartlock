import typing
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget

class TokenForm(QtWidgets.QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # message box
        self.MessageBox = QtWidgets.QMessageBox()
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
        
        # frame
        self.setObjectName("Tokenfield")
        self.resize(800, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/background/Images/logo192x192.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setStyleSheet("background-color: rgb(231, 229, 213);\n"
        "background-image: url(:/background/Images/background-removebg-preview.png);\n"
        "background-position: center;\n")
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        
        # Greetings
        self.greetings = QtWidgets.QLabel(self)
        self.greetings.setGeometry(QtCore.QRect(200, 80, 421, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(21)
        font.setBold(False)
        font.setWeight(50)
        self.greetings.setFont(font)
        self.greetings.setStyleSheet("color: #3D989A")
        self.greetings.setAlignment(QtCore.Qt.AlignCenter)
        self.greetings.setObjectName("greetings")
        
        # Token Field
        self.TokenID = QtWidgets.QLineEdit(self)
        self.TokenID.setGeometry(QtCore.QRect(110, 180, 581, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(30)
        self.TokenID.setFont(font)
        self.TokenID.setStyleSheet("background: transparents;\n"
        "color: #3D989A;\n"
        "background-color: rgb(255, 255, 255);\n"
        "border: 2px solid #3D989A;\n"
        "border-radius: 40px;")
        self.TokenID.setAlignment(QtCore.Qt.AlignCenter)
        self.TokenID.setPlaceholderText("Token ID")
        self.TokenID.setObjectName("TokenID")
        
        # continue
        self.Continue = QtWidgets.QPushButton(self)
        self.Continue.setGeometry(QtCore.QRect(420, 290, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Continue.setFont(font)
        self.Continue.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Continue.setStyleSheet("border: none;\n"
        "background: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
        "border-radius: 25px;\n"
        "color: white;")
        self.Continue.setObjectName("Continue")
        
        # cancel
        self.Cancel = QtWidgets.QPushButton(self)
        self.Cancel.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Cancel.setGeometry(QtCore.QRect(220, 290, 181, 51))
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
        
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Tokenfield", "Frame"))
        
        self.Continue.setText(_translate("Tokenfield", "Continue"))
        self.Continue.clicked.connect(self.continueTo)
        
        self.Cancel.setText(_translate("Tokenfield", "Cancel"))
        self.Cancel.clicked.connect(self.backTomain)
        
        self.greetings.setText(_translate("Tokenfield", "Hello Friend,\n"
        "Please enter your Token ID below"))

    
    def backTomain(self):
        from pages.Main_Menu import MainWindow
        
        print("go back to main menu")

        self.resize(800, 480)
        MainWindow(self).show()
        self.close()
        
    def continueTo(self):
        
        # check if TokenID is not empty
        if not self.TokenID.text():
            self.messageBoxShow(
                icon=self.MessageBox.Warning,
                title="Facial Recognition",
                text="Name cannot be empty",
                buttons=self.MessageBox.Ok
                )
            return
    
    
    def messageBoxShow(self, icon=None, title=None, text=None, buttons=None):

                # Set the window icon, title, and text
                self.MessageBox.setIcon(icon)
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
        
if __name__ == "__main__":
    
    import sys,background
    # Create a new QApplication object
    app = QApplication(sys.argv)

    New_menu = TokenForm()
    New_menu.show()

    sys.exit(app.exec_())