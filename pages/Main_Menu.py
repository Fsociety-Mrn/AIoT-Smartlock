from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

from Firebase.Offline import total_fail,delete_table,offline_insert,updateToDatabase,delete_table
from Firebase.firebase import firebaseVerifyPincode,lockerList

from Raspberry.Raspberry import openLocker
import socket
import os

class MainWindow(QtWidgets.QFrame):
    def __init__(self,parent=None):
        super().__init__(parent)
        
        self.Light_PIN = 25
        
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
        self.setObjectName("mainMenu")
        self.resize(1024, 565)
        
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap(":/background/Images/logo192x192.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(self.icon)
        
        self.setAutoFillBackground(False)
        self.setStyleSheet("background-color: rgb(231, 229, 213);\n")
        self.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.setLineWidth(2)
        
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        # first widget
        self.widget = QtWidgets.QWidget(self)
        self.widget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
        "border-top-left-radius: 50px;")
        self.widget.setObjectName("widget")
        
        # website instruction
        self.admin_2 = QtWidgets.QLabel(self.widget)
        self.admin_2.setGeometry(QtCore.QRect(30, 490, 281, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setStrikeOut(False)
        font.setBold(True) 
        self.admin_2.setFont(font)
        self.admin_2.setStyleSheet("color:  #ffffff;")
        self.admin_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.admin_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.admin_2.setObjectName("admin_2")
        
        self.admin_1 = QtWidgets.QLabel(self.widget)
        self.admin_1.setGeometry(QtCore.QRect(30, 470, 281, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setStrikeOut(False)
   
        self.admin_1.setFont(font)
        self.admin_1.setStyleSheet("color:  #ffffff;")
        self.admin_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.admin_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.admin_1.setObjectName("admin_1")
        
        self.user_3 = QtWidgets.QLabel(self.widget)
        self.user_3.setGeometry(QtCore.QRect(30, 420, 281, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setStrikeOut(False)
        font.setBold(True)
        self.user_3.setFont(font)
        self.user_3.setStyleSheet("color: #ffffff;")
        self.user_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.user_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.user_3.setObjectName("user_3")
        
        self.user_2 = QtWidgets.QLabel(self.widget)
        self.user_2.setGeometry(QtCore.QRect(30, 400, 281, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setStrikeOut(False)
        self.user_2.setFont(font)
        self.user_2.setStyleSheet("color: #ffffff;")
        self.user_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.user_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.user_2.setObjectName("user_2")
        
        self.user_1 = QtWidgets.QLabel(self.widget)
        self.user_1.setGeometry(QtCore.QRect(30, 380, 281, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setStrikeOut(False)
        self.user_1.setFont(font)
        self.user_1.setStyleSheet("color: #ffffff;")
        self.user_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.user_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.user_1.setObjectName("user_1")
        
        # qr code
        self.qr = QtWidgets.QPushButton(self.widget)
        self.qr.setEnabled(True)
        self.qr.setGeometry(QtCore.QRect(320, 370, 151, 151))
        self.qr.setStyleSheet("border-radius: 100px;")
        self.qr.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Images/USER_QR.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.qr.setIcon(icon1)
        self.qr.setIconSize(QtCore.QSize(150, 150))
        self.qr.setObjectName("qr")
                
        # Locker CEA label
        self.label_locker_2 = QtWidgets.QLabel(self.widget)
        self.label_locker_2.setGeometry(QtCore.QRect(30, 300, 441, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setStrikeOut(False)
        self.label_locker_2.setFont(font)
        self.label_locker_2.setStyleSheet("color: #ffffff;\n"
        "border-top-left-radius: 0px;")
        self.label_locker_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_locker_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_locker_2.setObjectName("label_locker_2")
        
        self.label_locker = QtWidgets.QLabel(self.widget)
        self.label_locker.setGeometry(QtCore.QRect(30, 280, 441, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setStrikeOut(False)
        self.label_locker.setFont(font)
        self.label_locker.setStyleSheet("color: #ffffff;")
        self.label_locker.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_locker.setAlignment(QtCore.Qt.AlignCenter)
        self.label_locker.setObjectName("label_locker")
        
        # Locker Status / List
        self._20 = QtWidgets.QPushButton(self.widget)
        self._20.setGeometry(QtCore.QRect(70, 30, 121, 121))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        self._20.setFont(font)
        self._20.setStyleSheet("background-color:#F5F0F0;\n"
"border-top-left-radius: 20px;\n"
"border: 2px solid #63727B;\n"
"color:#63727B;")
        self._20.setObjectName("_20")
        
        self._12 = QtWidgets.QPushButton(self.widget)
        self._12.setGeometry(QtCore.QRect(70, 150, 121, 121))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        self._12.setFont(font)
        self._12.setStyleSheet("background-color:#F5F0F0;\n"
"border-top-left-radius: 0px;\n"
"border-bottom-left-radius: 20px;\n"
"border: 2px solid #63727B;\n"
"color:#63727B;")
        self._12.setObjectName("_12")
        
        self._21 = QtWidgets.QPushButton(self.widget)
        self._21.setGeometry(QtCore.QRect(190, 30, 121, 121))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        self._21.setFont(font)
        self._21.setStyleSheet("background-color:#F5F0F0;\n"
"border-top-left-radius: 0px;\n"
"border: 2px solid red;\n"
"color:red;")
        self._21.setIconSize(QtCore.QSize(30, 30))
        self._21.setObjectName("_21")
        
        self._7 = QtWidgets.QPushButton(self.widget)
        self._7.setGeometry(QtCore.QRect(190, 150, 121, 121))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        self._7.setFont(font)
        self._7.setStyleSheet("background-color:#F5F0F0;\n"
"border-top-left-radius: 0px;\n"
"border: 2px solid #63727B;\n"
"color:#63727B;")
        self._7.setObjectName("_7")
        
        self._16 = QtWidgets.QPushButton(self.widget)
        self._16.setGeometry(QtCore.QRect(310, 30, 121, 121))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        self._16.setFont(font)
        self._16.setStyleSheet("background-color:#F5F0F0;\n"
"border-top-left-radius: 0px;\n"
"border-top-right-radius: 20px;\n"
"border: 2px solid #63727B;\n"
"color:#63727B;")
        self._16.setObjectName("_16")
        
        self._8 = QtWidgets.QPushButton(self.widget)
        self._8.setGeometry(QtCore.QRect(310, 150, 121, 121))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        self._8.setFont(font)
        self._8.setStyleSheet("background-color:#F5F0F0;\n"
"color:#63727B;\n"
"border-top-left-radius: 0px;\n"
"border-bottom-right-radius: 20px;\n"
"border: 2px solid #63727B;")
        self._8.setObjectName("_8")
        
        self.horizontalLayout.addWidget(self.widget)
        
        # second widget
        self.widget_2 = QtWidgets.QWidget(self)
        self.widget_2.setAutoFillBackground(False)
        self.widget_2.setStyleSheet("background-color:#F5F0F0;\n"
"border-bottom-right-radius: 50px;\n"
"\n"
"")
        self.widget_2.setObjectName("widget_2")
        
        # facial register
        self.facialRegister = QtWidgets.QPushButton(self.widget_2)
        self.facialRegister.setGeometry(QtCore.QRect(60, 420, 380, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.facialRegister.setFont(font)
        self.facialRegister.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.facialRegister.setAutoFillBackground(False)
        self.facialRegister.setStyleSheet("background: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
        "border: none;\n"
        "border-radius: 25px;\n"
        "color: white;\n"
        "padding: 10px;")
        self.facialRegister.setObjectName("facialRegister")
        
        # facial login
        self.facialLogin = QtWidgets.QPushButton(self.widget_2)
        self.facialLogin.setGeometry(QtCore.QRect(60, 300, 380, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.facialLogin.setFont(font)
        self.facialLogin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.facialLogin.setAutoFillBackground(False)
        self.facialLogin.setStyleSheet("background: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
        "\n"
        "border-radius: 25px;\n"
        "color: white;\n"
        "padding: 10px;")
        self.facialLogin.setObjectName("facialLogin")
        
        # pin code login
        self.pincodeLogin = QtWidgets.QPushButton(self.widget_2)
        self.pincodeLogin.setGeometry(QtCore.QRect(60, 360 , 380, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.pincodeLogin.setFont(font)
        self.pincodeLogin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pincodeLogin.setAutoFillBackground(False)
        self.pincodeLogin.setStyleSheet("background: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
        "\n"
        "border-radius: 25px;\n"
        "color: white;\n"
        "padding: 10px;")
        self.pincodeLogin.setObjectName("pincodeLogin")
        
        # paro paro g
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(140, 80, 221, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setStyleSheet("color:  rgba(11, 131, 120, 219)")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        
        # icon
        self.label_6 = QtWidgets.QPushButton(self.widget_2)
        self.label_6.setEnabled(True)
        self.label_6.setGeometry(QtCore.QRect(0, 20, 501, 61))
        self.label_6.setStyleSheet("border-radius: 100px;")
        self.label_6.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/background/Images/logo192x192.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.label_6.setIcon(icon3)
        self.label_6.setIconSize(QtCore.QSize(40, 40))
        self.label_6.setObjectName("label_6")
        
        # settings
        self.settings = QtWidgets.QPushButton(self.widget_2)
        self.settings.setEnabled(True)
        self.settings.setGeometry(QtCore.QRect(440, 10, 51, 51))
        self.settings.setStyleSheet("border-radius: 100px;")
        self.settings.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Images/setting.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings.setIcon(icon1)
        self.settings.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.settings.setIconSize(QtCore.QSize(32, 32))
        self.settings.setObjectName("settings")
        
        # time
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(10, 130, 481, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(42)
        font.setStrikeOut(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:  rgba(11, 131, 120, 219)")
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        
        # face status
        self.checkFail = QtWidgets.QLabel(self.widget_2)
        self.checkFail.setGeometry(QtCore.QRect(0, 270, 501, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.checkFail.setFont(font)
        self.checkFail.setStyleSheet("color:  red;")
        self.checkFail.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.checkFail.setAlignment(QtCore.Qt.AlignCenter)
        self.checkFail.setObjectName("status")
        
        # date
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(10, 210, 481, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        font.setStrikeOut(False)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:  rgba(11, 131, 120, 219)")
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
    
        # for countdown
        self.failedCountdown = QtCore.QTimer(self)
        self.failedCountdown.timeout.connect(self.updateCountdown)
        self.seconds_left = 30
        self.Fail = True
        self.failedAttempt= 0
        
        # This timer whether the system is lock or not
        self.checkFailDetailsssss = QtCore.QTimer(self)
        self.checkFailDetailsssss.timeout.connect(self.checkFailss)
        self.checkFailDetailsssss.start(1000)

        self.updateData = QtCore.QTimer(self)
        self.updateData.timeout.connect(self.update_data)
        self.updateData.start(1000)
        
        self.closeEvent = self.closeEvent
        self.horizontalLayout.addWidget(self.widget_2) 
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        
        # main menu
        self.menu = QMenu(self)

        self.menu.addAction(QAction("Facial Update", self, triggered=self.updateFace))
        self.menu.addAction(QAction("Restart", self, triggered=self.rebootEvent))
        self.menu.addAction(QAction("Shutdown", self, triggered=self.closeEvent))

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        
        self.setWindowTitle(_translate("mainMenu", "AIoT Smartlock"))
        
        self.facialRegister.setText(_translate("mainMenu", "Facial Register"))
        self.facialRegister.clicked.connect(self.openFacialRegister)
        
        self.facialLogin.setText(_translate("mainMenu", "Facial Login"))
        self.facialLogin.clicked.connect(self.openFacialLogin)\
        
        self.admin_2.setText(_translate("mainMenu", "  https://aiot-smartlock.firebaseapp.com"))
        self.admin_1.setText(_translate("mainMenu", "  for admin website just visit this"))
     
        self.user_3.setText(_translate("mainMenu", "  https://user-aiot-smartlock.web.app"))
        self.user_2.setText(_translate("mainMenu", "  or just visit this:"))
        self.user_1.setText(_translate("mainMenu", "  Scan this qr code for user website ---->"))
        
        self._20.setText(_translate("mainMenu", "20"))
        self._12.setText(_translate("mainMenu", "12"))
        self._21.setText(_translate("mainMenu", "21"))
        self._7.setText(_translate("mainMenu", "7"))
        self._16.setText(_translate("mainMenu", "16"))
        self._8.setText(_translate("mainMenu", "8"))
        
        self.label_locker.setText(_translate("mainMenu", "CEA FACULTY LOCKER IN RTU PASIG CAMPUS"))
        self.label_locker_2.setText(_translate("mainMenu", "NOTE: Red color indicates your locker is open,<br> default color signifies your locker is closed."))

        self.pincodeLogin.setText(_translate("mainMenu", "Pin Login"))
        self.pincodeLogin.clicked.connect(self.openPincodeLogin)
        
        self.label.setText(_translate("mainMenu", "paro paro g fly high butterfly"))
        
        self.label_2.setText(_translate("mainMenu", "12:00 PM"))
        
        self.label_3.setText(_translate("mainMenu", "Wed,Jun 3 2023"))
        
        self.settings.clicked.connect(self.showMenu)

    def checkFacialUpdate(self):
        if total_fail("Facial_update") >= 6:
            self.updateFace(delay=500)
            delete_table("Facial_update")
        
        return

              
# ******* LOCK FAILED
    def __showLocked(self):
        from pages.Admin_Lock import AdminLock
        
        self.timers(isAble=True)
        
        self.resize(1024, 565)
        Token = AdminLock(self)

        Token.show()
    
    # ========== to stop the timer and start it again ========== #
    def timers(self, isAble): 
        if isAble:
            self.checkFailDetailsssss.stop()
            self.timer.stop()
            self.failedCountdown.stop()
        else:
            self.checkFailDetailsssss.start()
            self.timer.start()
    
    def checkFailss(self):
        
        self.seconds_left = 30
        
 

        if int(total_fail("Failed attempt")) >= 3:
            self.__showLocked()
            return 
        
        if int(total_fail("Fail History")) >= 1:
            attempLeft = 3 - int(total_fail("Fail History"))
            self.checkFail.setText(f'you have {attempLeft} attempt left')
            

        if int(total_fail("Fail History")) >= 3:
            self.failedCountdown.start(1000)
            self.updateCountdown()
            self.checkFailDetailsssss.stop()
            
            self.failedAttempt =  self.failedAttempt + 1
            
            offline_insert(TableName="Failed attempt",data={"attempt": int(self.failedAttempt)})
            
            self.Fail = False
            self.disabled(isEnable=False)
      
    def disabled(self,isEnable):
        self.facialLogin.setEnabled(isEnable)
        self.facialRegister.setEnabled(isEnable)
        self.pincodeLogin.setEnabled(isEnable)
        self.settings.setEnabled(isEnable)
        
        if not isEnable:
            self.facialLogin.setText("...........")
            self.facialRegister.setText("...........")
            self.pincodeLogin.setText("...........")
        else:
            self.facialRegister.setText("Facial Register")
            self.pincodeLogin.setText("Pin Login")
            self.facialLogin.setText("Facial Login")
            
    # failed
    def updateCountdown(self):
        if self.seconds_left > 0:
            self.checkFail.setText(f'AIoT Smartlock is disabled try again in {self.seconds_left} seconds')
            self.seconds_left -= 1
        else:
            self.failedCountdown.stop()
            self.checkFail.setText('')
            delete_table("Fail History")
            self.checkFailDetailsssss.start(100)
            self.failedCountdown.stop()
            self.Fail = True
            self.disabled(isEnable=True)
            
    # message box
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
    
    def updateFace(self,delay=100):
        
        self.facialLogin.setText("Face Recognition is Updating")
        self.facialRegister.setText("Please bear with me")
        self.pincodeLogin.setText("............")
        
        self.facialLogin.isEnabled = False
        self.facialRegister.isEnabled = False
        self.pincodeLogin.isEnabled = False

        # Delay the creation of the FacialLogin object by 100 milliseconds
        QtCore.QTimer.singleShot(delay, self.update_face)
    
    # update facial recognition
    def update_face(self):

        from Face_Recognition.JoloRecognition import JoloRecognition
        JoloRecognition().Face_Train()
        
        self.messageBoxShow(
                icon=self.MessageBox.Information,
                title="AIoT Smartlock",
                text="Facial Updating is done",
                buttons=self.MessageBox.Ok
            )
        
        self.facialRegister.setText("Facial Register")
        self.pincodeLogin.setText("Pin Login")
        self.facialLogin.setText("Facial Login")
        
        
        
        self.facialLogin.isEnabled = True
        self.facialRegister.isEnabled = True
        self.pincodeLogin.isEnabled = True

    # ********************** check time ********************** #
    def update_time(self):

        current_date = QtCore.QDate.currentDate().toString("ddd, MMM d yyyy")
        
        current_time = QtCore.QTime.currentTime().toString("h:mm AP")
        
        self.check_internet_connection()
        
        self.label_2.setText(current_time)
        self.label_3.setText(current_date)
    
    # ********************* Offline Mode ********************* #
    
    # download pincode
    def pinCode(self):
        data = firebaseVerifyPincode()
        
        if not data == None:
            delete_table("PIN")
            for key in data:
                offline_insert(TableName="PIN", data=key)
                
    # List of Locker
    def locker(self):
        data = lockerList()
        
        if not data == None:
            delete_table("LOCK")
            for key in data:
                offline_insert(TableName="LOCK", data=key)
            
    # check internet
    def check_internet_connection(self):
        try:
            
            if self.Fail:
                self.facialRegister.setEnabled(True)
                self.facialRegister.setText("Facial Register")
            
            self.checkFacialUpdate()

            # Attempt to create a socket connection to a known server (e.g., Google DNS)
            socket.create_connection(("8.8.8.8", 53))
            self.label.setText("<html><head/><body><p>AIoT Smartlock is <Strong>online<strong/></p></body></html>")
            
        except OSError:
            
            pass
            
            self.facialRegister.setEnabled(False)
            self.facialRegister.setText(".......")
            self.label.setText("<html><head/><body><p><Strong>No Internet<strong/> Connection</p></body></html>")
            
            self.checkFacialUpdate()
            
    def update_data(self):
        try:
            
            updateToDatabase()
            openLocker()
            
        except OSError:
            
            pass
            print("No Internet")
    # ===================== open facial Login ===================== #

    def openFacialLogin(self):
        self.facialLogin.setText("Loading..........")
        self.facialLogin.isEnabled = False
        self.facialRegister.isEnabled = False
        self.pincodeLogin.isEnabled = False
        
        # download updated Locker Number
        self.locker()

        # Delay the creation of the FacialLogin object by 100 milliseconds
        QtCore.QTimer.singleShot(100, self.clickFacialLogin)

    def clickFacialLogin(self):

        from pages.Facial_Login import FacialLogin
        print("start loading facuial login")
        
        self.timers(True)

        self.resize(1024, 565)
        Facial_Login = FacialLogin(self)
        Facial_Login.show()
        

        self.facialLogin.setText("Facial Login")

    # ===================== open Facial Register ===================== #

    def openFacialRegister(self):

        self.facialRegister.setText("Loading..............")
        self.facialLogin.isEnabled = False
        self.facialRegister.isEnabled = False
        self.pincodeLogin.isEnabled = False

        # Delay the creation of the FacialLogin object by 100 milliseconds
        QtCore.QTimer.singleShot(100, self.clickFacialRegister)

    def clickFacialRegister(self):
     
        from pages.Token_Form import TokenForm

        self.resize(1024, 565)
        Token = TokenForm(self)
    
        self.timers(True)
        
        Token.show()
        self.facialRegister.setText("Facial Register")
    
    # ===================== open PIN LOGIN ===================== #
    def openPincodeLogin(self):
    
        self.pincodeLogin.setText("Loading..............")
        self.pincodeLogin.isEnabled = False
        self.facialLogin.isEnabled = False
        self.facialRegister.isEnabled = False

        self.pinCode()
        
        self.timers(True)
        
        # Delay the creation of the FacialLogin object by 100 milliseconds
        QtCore.QTimer.singleShot(100, self.clickPincodeLogin)

    def clickPincodeLogin(self):
     
        from pages.Pincode_Login import PincodeLogin
        
        Token = PincodeLogin(self)
        
        self.timers(True)

        Token.show()
        self.pincodeLogin.setText("Pincode Login")
        
    # when close the frame
    def close(self):
        QtWidgets.qApp.quit()

    def closeEvent(self, event):
        # show a message box asking for confirmation
        message_box = QtWidgets.QMessageBox(None)
        message_box.setWindowTitle('AIoT Smartlock')
        message_box.setText("Are you sure you want to shutdown this system ?")
        message_box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        message_box.setDefaultButton(QtWidgets.QMessageBox.No)

        reply = message_box.exec_()
        # if the user confirms, exit the application
        if reply == QtWidgets.QMessageBox.Yes:
            os.system("sudo shutdown now")
        else:
            message_box.close()
    def rebootEvent(self, event):
        
        # show a message box asking for confirmation
        message_box = QtWidgets.QMessageBox(None)
        message_box.setWindowTitle('AIoT Smartlock')
        message_box.setText("Are you sure you want to restart the system ?")
        message_box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        message_box.setDefaultButton(QtWidgets.QMessageBox.No)

        reply = message_box.exec_()
        # if the user confirms, exit the application
        if reply == QtWidgets.QMessageBox.Yes:
            os.system("sudo reboot")
        else:
            message_box.close()
            
    def showMenu(self):
        self.menu.exec_(self.settings.mapToGlobal(self.settings.rect().bottomLeft()))

    def hellofriend(self):
        print("hello friend")