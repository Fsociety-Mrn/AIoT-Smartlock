
import cv2
import os
import uuid
import shutil

from Face_Recognition.JoloRecognition import JoloRecognition as Jolo
from PyQt5.QtWidgets import  QLineEdit
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets

from Firebase.firebase import firebaseHistory
from Firebase.Offline import pinCodeLogin,offline_history,delete_table,create_person_temporarily_banned
from Raspberry.Raspberry import OpenLockers,gpio_manual

from pages.Custom_MessageBox import MessageBox


class PincodeLogin(QtWidgets.QFrame):
    
    def __init__(self, parent):
        super().__init__(parent)
        
        self.main_menu = parent
        self.Light_PIN = 25
                
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
        font.setBold(True)
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
        pixmap = QtGui.QPixmap("/home/aiotsmartlock/Downloads/AIoT_Smart-lock/Images/check.png")
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
        pixmap = QtGui.QPixmap("/home/aiotsmartlock/Downloads/AIoT_Smart-lock/Images/backspace.png")
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
        
        # Timer
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.videoStreaming)
        self.timer.start()
        
        self.state = True

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
           
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Pincode", "Frame"))
        self.TokenID_3.setPlaceholderText(_translate("MainWindow", "eg: LN-XXXX"))

        self.errorMessage.setText(_translate("MainWindow", "<strong> Enter your Locker Number </strong>"))
               
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
        self.checkBox.setText(_translate("MainWindow", "Show pin"))
        gpio_manual(self.Light_PIN,False)
             
    def toggle_password_visibility(self,state):
      
        if state != self.checkBox.isChecked():
                self.TokenID_3.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
                self.TokenID_3.setEchoMode(QtWidgets.QLineEdit.Password)
                
        # self.TokenID_3.setEchoMode(QtWidgets.QLineEdit.Password if state else QtWidgets.QLineEdit.Normal)
    
    def input_digit_instruction(self, text):

        if len(text) < 1:
            self.errorMessage.setText("<strong> Enter your Locker Number </strong>")
            return
                
        self.errorMessage.setText("<strong> Enter your 4 digit pin code </strong>")
                
        if len(text) >= 6:
            self.errorMessage.setText("<strong> You can now proceed with PIN login. </strong>")

    def input_digit(self, digit):
            
        current_text = self.TokenID_3.text()
        self.input_digit_instruction(current_text)
        
        if len(current_text) == 2:
            current_text = current_text + "-"
                
        if len(current_text) != 7:   
            self.TokenID_3.setText(current_text + digit)
                
    def backspace(self):
        current_text = self.TokenID_3.text()
        if current_text:
            updated_text = current_text[:-1]  # Remove the last character
            self.TokenID_3.setText(updated_text)
            
        self.input_digit_instruction(current_text)
            
    def cancel(self):
        gpio_manual(self.Light_PIN,True)
        self.videoStream.release()
        cv2.destroyAllWindows()
        self.timer.stop()
        
        self.main_menu.upload_banned_person()
        self.main_menu.timers(False)

        self.close()
        
    def enterPINcode(self):

        pin_code = self.TokenID_3.text()
        
        # filter the text box
        if pin_code == "":
            self.errorMessage.setText("Please enter your PIN to proceed.")
            return
        
        if len(pin_code) < 3:
            self.errorMessage.setText("PIN must be 6 characters long. Please try again.")
            return
        
        # check person is suspended and banned
        name,result,person,frame = self.anti_spam()
        
        if result:
            
            # check if person is suspended
            self.messageBoxShow(
                title="PIN LOGIN",
                text=name,
                buttons=self.MessageBox.Ok
            )
            
            self.cancel()
            return
            
        
        # pin code splitting text
        pins = pin_code.split("-")        
        
        # get current date and time
        current_date = QtCore.QDate.currentDate().toString("MMM d yyyy")
        current_time = QtCore.QTime.currentTime().toString("h:mm:ss AP")  
  
        data = pinCodeLogin(pin=str(int(pins[0])) + "-" + pins[1])
        
        # pin verify
        if data[0] == None:
            errorMessage = "<strong> Invalid PIN, please try again. </strong>"
            name = "No match detected"
            text = self.create_dir(person=person,image=frame)
        else:
            name = data[0]
            errorMessage = ""
            text="Welcome " + str(data[0]) + "!<br>Locker Number: " + str(data[1])
            delete_table(Table_Name=person,dir="/home/aiotsmartlock/Downloads/AIoT_Smart-lock/Firebase/banned_and_temporary_list.json")
            self.delete_folder(person)

        offline_history(
                name=name,
                date=current_date,
                time=current_time,
                access_type="PIN Login")

        
        self.errorMessage.setText(errorMessage)
        self.TokenID_3.setText("")
            
        self.messageBoxShow(
            title="PIN LOGIN",
            text=text,
            buttons=self.MessageBox.Ok
        )
        
        # for open the Locker
        if not data[0] == None:
            OpenLockers(str(data[0]),key=int(data[1]),value=True)
            self.cancel()
                    
    # message box
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
                title="PIN LOGIN",
                text="Unable to open camera. Please contact the administrator for assistance.",
                buttons=self.MessageBox.Ok
            )
            self.cancel()
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
            
            self.greetings.setText("Kindly provide your Locker number and PIN \n(in the format ex: 16-9259) for access.")
            self.seven_11.setDisabled(False)
            
            if Face_blurred < 300:
                self.greetings.setText("Camera feed is blurred. Please ensure the camera is clean")
                self.seven_11.setDisabled(True)
        

        # Multiple Face Detected
        elif len(faces) >= 1:    
            self.greetings.setText("Multiple faces detected. Please ensure only one face is visible")
            self.seven_11.setDisabled(True)
        # No face detected
        else:
            self.greetings.setText("No face detected. Please ensure your face is visible.")
            self.seven_11.setDisabled(True)
            
    # LIFO
    def LastIn_FirstOut(self,directory=None,new_image=None,batch=19):
                
        # Get the list of files in the directory
        files = os.listdir(directory)
        
        # Filter the list to include only image files
        image_files = [file for file in files if file.endswith((".png", ".jpg", ".jpeg"))]

        # Sort the image file names numerically in ascending order
        sorted_image_files = sorted(image_files, key=lambda x: int(os.path.splitext(x)[0]))

        # Get the highest numeric value in the remaining image files 
        highest_value = max([int(os.path.splitext(file)[0]) for file in sorted_image_files]) if sorted_image_files else 0

        # Generate the new image path with an incremental value
        new_value = highest_value + 1
        new_image_name = f"{new_value}.png"
        new_image_path = os.path.join(directory, new_image_name)

        # Save the new image using cv2.imwrite()
        cv2.imwrite(new_image_path, new_image)
        
        # remove first image if images are greather than 20
        if len(files) > batch:
            oldest_image = sorted_image_files[0]
            os.remove(os.path.join(directory, oldest_image))
            sorted_image_files = sorted_image_files[1:]
    
    # create directory
    def create_dir(self,image,person):
        
        directory = "/home/aiotsmartlock/Downloads/AIoT_Smart-lock/spam_detection"
                
        # Generate a random UUID (version 4)
        unique_id = uuid.uuid4()
        
        # person is none create folder and save images
        if person == None:
            
            # Convert UUID to a hexadecimal string and return the first 8 characters
            personID = "person_" + str(unique_id).upper()[:5]
            new_dir = f"{directory}/{personID}"
        
            os.makedirs(new_dir, exist_ok=True)
            try:
                self.LastIn_FirstOut(directory=new_dir, new_image=image,batch=2)
            except:
                self.delete_folder(person=personID)
                return "please make sure your face is properly aligned at the center of the camera"
        else:
            new_dir=f"{directory}/{person}"
            try:
                self.LastIn_FirstOut(directory=new_dir, new_image=image,batch=2)
            except:
                return "please make sure your face is properly aligned at the center of the camera"
            
        return create_person_temporarily_banned(person,"Facial")[0]
         
    # spam recognition
    def anti_spam(self):
         
        ret, image = self.videoStream.read()
        
        if not ret:
            return "camera unable to capture"
        
        # process the frame
        image = cv2.flip(image, 1)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # load facial detector haar
        faces = self.face_detector.detectMultiScale(gray,
                                                    scaleFactor=1.1,
                                                    minNeighbors=20,
                                                    minSize=(100, 100),
                                                    flags=cv2.CASCADE_SCALE_IMAGE)
        
        x, y, w, h = faces[0]
  
        # Calculate new width and height
        scale_factor = 1.2
        new_w = int(w * scale_factor)
        new_h = int(h * scale_factor)

        # Adjust x and y to keep the center of the face in the crop
        new_x = max(0, x - (new_w - w) // 2)
        new_y = max(0, y - (new_h - h) // 2)
        
        # Crop the image with the new dimensions
        faceCrop = image[new_y-40:new_y+new_h+30, new_x-40:new_x+new_w+30]

        result = Jolo().spam_detection(image=faceCrop,threshold=0.7)
        
        person = result[0]  # None 
        spam_detected = result[2] # if detected
        error_occur = result[3]
        
        # verify person is in database
        text,result = create_person_temporarily_banned(person,"Facial",False)
        
        # if detected it will save images
        if spam_detected and error_occur == None and result:
            create_person_temporarily_banned(person,"Facial")
            
        # return Text result 
        return text,result,person,faceCrop

    def delete_folder(self,person):
        try:
            dir = f"/home/aiotsmartlock/Downloads/AIoT_Smart-lock/spam_detection/{person}"
            shutil.rmtree(dir)
            print(f"Folder '{dir}' deleted successfully.")
        except Exception as e:
            print(f"Error: {dir} : {e}")
        
if __name__ == "__main__":
    
    import sys,background
    # Create a new QApplication object
    app = QApplication(sys.argv)

    New_menu = PincodeLogin()
    New_menu.show() 

    sys.exit(app.exec_())

