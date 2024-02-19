
import time
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets

from Firebase.firebase import firebaseHistory
from Firebase.Offline import pinCodeLogin,offline_history,delete_table,offline_insert
from Raspberry.Raspberry import OpenLockers

from pages.Custom_MessageBox import MessageBox


class PincodeLogin(QtWidgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.main_menu = parent
        
        self.failed = 1
        
        # message box
        self.MessageBox = MessageBox()
        self.MessageBox.setStyleSheet("""
                      QLabel{
                          min-width: 600px; 
                          min-height: 50px; 
                          font-size: 20px;
                           padding-top: 10px; /* Add padding at the top */
                padding-bottom: 10px; /* Add padding at the bottom */
                        }
                QPushButton { 
                      width: 250px; 
                      height: 30px; 
                      font-size: 15px;
                  }
                    """)
        
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
        self.greetings.setGeometry(QtCore.QRect(-18, 20, 1031, 181))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(70)
        self.greetings.setFont(font)
        self.greetings.setStyleSheet("color: #3D989A")
        self.greetings.setAlignment(QtCore.Qt.AlignCenter)
        self.greetings.setObjectName("greetings")
        
        # show password
        self.checkBox = QtWidgets.QCheckBox(self)
        self.checkBox.setGeometry(QtCore.QRect(130, 300, 135, 17))
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
        

        # Token ID
        self.TokenID_3 = QtWidgets.QLineEdit(self)
        self.TokenID_3.setGeometry(QtCore.QRect(130, 230, 431, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        self.TokenID_3.setFont(font)
        self.TokenID_3.setStyleSheet("background: transparents;\n"
            "color: #3D989A;\n"
            "background-color: rgb(255, 255, 255);\n"
            "border: 1px solid #3D989A;\n"
            "border-radius: 25px;\n"
        "")
        self.TokenID_3.setAlignment(QtCore.Qt.AlignCenter)
        self.TokenID_3.setObjectName("TokenID_3")
        
        # Greetings
        self.errorMessage = QtWidgets.QLabel(self)
        self.errorMessage.setGeometry(QtCore.QRect(180, 190, 350, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(10)
        self.errorMessage.setFont(font)
        self.errorMessage.setStyleSheet("color: red")
        self.errorMessage.setAlignment(QtCore.Qt.AlignCenter)
        self.errorMessage.setObjectName("errorMessage")
        
        # Keypad
        self.KeyboardContainer_3 = QtWidgets.QWidget(self)
        self.KeyboardContainer_3.setGeometry(QtCore.QRect(610, 160, 301, 371))
        self.KeyboardContainer_3.setObjectName("KeyboardContainer_3")
        
        # one
        self.seven_2 = QtWidgets.QPushButton(self.KeyboardContainer_3)
        self.seven_2.setGeometry(QtCore.QRect(20, 20, 70, 70))
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
        self.seven_3.setGeometry(QtCore.QRect(110, 20, 70, 70))
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
        self.seven_4.setGeometry(QtCore.QRect(200, 20, 70, 70))
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
        self.seven_5.setGeometry(QtCore.QRect(110, 100, 70, 70))
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
        self.seven_6.setGeometry(QtCore.QRect(20, 100, 70, 70))
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
        self.seven_7.setGeometry(QtCore.QRect(200, 100, 70, 70))
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
        self.seven_8.setGeometry(QtCore.QRect(200, 180, 70, 70))
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
        self.seven_9.setGeometry(QtCore.QRect(20, 180, 70, 70))
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
        self.seven_10.setGeometry(QtCore.QRect(110, 180, 70, 70))
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
        self.seven_11.setGeometry(QtCore.QRect(200, 260, 70, 70))
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
        self.seven_12.setGeometry(QtCore.QRect(20, 260, 70, 70))
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
        self.seven_13.setGeometry(QtCore.QRect(110, 260, 70, 70))
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
        
        self.state = True

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
           
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Pincode", "Frame"))
        self.TokenID_3.setPlaceholderText(_translate("MainWindow", "eg: LN-XXXX"))

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
        self.seven_5.clicked.connect(lambda: self.input_digit('5'))
        self.seven_6.clicked.connect(lambda: self.input_digit('4'))
        self.seven_7.clicked.connect(lambda: self.input_digit('6'))
        self.seven_8.clicked.connect(lambda: self.input_digit('9'))
        self.seven_9.clicked.connect(lambda: self.input_digit('7'))
        self.seven_10.clicked.connect(lambda: self.input_digit('8'))
        self.seven_13.clicked.connect(lambda: self.input_digit('0'))
        
        self.TokenID_3.setEchoMode(QLineEdit.Password)
        
        self.checkBox.setChecked(False)
        self.checkBox.stateChanged.connect(self.toggle_password_visibility)

        # enter
        self.seven_11.clicked.connect(self.enterPINcode)

        self.Cancel_2.setText(_translate("MainWindow", "Cancel"))

        self.greetings.setText(_translate("MainWindow", "Hello Friend,\n"
        "Kindly provide your locker number and PIN for access."))
        self.checkBox.setText(_translate("MainWindow", "Show Password"))
             
    def toggle_password_visibility(self,state):
      
        if state != self.checkBox.isChecked():
                self.TokenID_3.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
                self.TokenID_3.setEchoMode(QtWidgets.QLineEdit.Password)
                
        # self.TokenID_3.setEchoMode(QtWidgets.QLineEdit.Password if state else QtWidgets.QLineEdit.Normal)

    def input_digit(self, digit):
            
        self.errorMessage.setText("")
        current_text = self.TokenID_3.text()
        if len(current_text) == 2:
                current_text = current_text + "-"
                
        if len(current_text) != 7:   
                self.TokenID_3.setText(current_text + digit)

    def backspace(self):
        current_text = self.TokenID_3.text()
        if current_text:
            updated_text = current_text[:-1]  # Remove the last character
            self.TokenID_3.setText(updated_text)
            
    def cancel(self):
        self.main_menu.timers(False)
        self.close()
        
    def enterPINcode(self):
            
        self.checkFail()
        
        current_date = QtCore.QDate.currentDate().toString("MMM d yyyy")
        current_time = QtCore.QTime.currentTime().toString("h:mm:ss AP")
        
        if self.TokenID_3.text() == "":
            return
        
        if len(self.TokenID_3.text()) < 3:
            return
        
        pins = self.TokenID_3.text().split("-")        
            
        data = pinCodeLogin(pin=str(int(pins[0])) + "-" + pins[1])
        
        self.errorMessage.setText("")
        
        if data[0] == None:
                
           self.errorMessage.setText("Wrong PIN, please try again.")
           self.TokenID_3.setText("")
           result = firebaseHistory(
                        name="No match detected",
                        date=current_date,
                        time=current_time,
                        access_type="PIN Login")
            
        
           if not result:
                offline_history(
                        name="No match detected",
                        date=current_date,
                        time=current_time,
                        access_type="PIN Login")
                
           self.failed = self.failed + 1
                
           
        else:

            
            
            result = firebaseHistory(
                        name=data[0],
                        date=current_date,
                        time=current_time,
                        access_type="PIN Login")
            
        
            if not result:
                offline_history(  
                        name=data[0],
                        date=current_date,
                        time=current_time,
                        access_type="PIN Login")
                
            self.messageBoxShow(
                icon=self.MessageBox.Information,
                title="PIN LOGIN",
                text="Welcome " + str(data[0]) + "!<br>Locker Number: " + str(data[1]),
                buttons=self.MessageBox.Ok
            )
            
            # for open the Locker
            OpenLockers(str(data[0]),key=int(data[1]),value=True)
       
            
            delete_table("Failed attempt")
            delete_table("Fail History")
            self.cancel()
                    
    # message box
    def messageBoxShow(self, icon=None, title=None, text=None, buttons=None):

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

    def checkFail(self):
        if self.failed == 3:
           offline_insert(data={'Fail': "Wrong PIN"},TableName= "Fail History")
           self.cancel()
if __name__ == "__main__":
    
    import sys,background
    # Create a new QApplication object
    app = QApplication(sys.argv)

    New_menu = PincodeLogin()
    New_menu.show() 

    sys.exit(app.exec_())

