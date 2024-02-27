from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

from Firebase.Offline import total_fail,delete_table,offline_insert,updateToDatabase,delete_table
from Firebase.firebase import firebaseVerifyPincode,lockerList,locker_sensor

from Raspberry.Raspberry import openLocker,door_status
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
        self.admin_2.setGeometry(QtCore.QRect(15, 490, 295, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setStrikeOut(False)
        font.setBold(True) 
        self.admin_2.setFont(font)
        self.admin_2.setStyleSheet("color: #ffffff;background-color: rgba(255, 255, 255, 0);")
        self.admin_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.admin_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.admin_2.setObjectName("admin_2")
        
        self.admin_1 = QtWidgets.QLabel(self.widget)
        self.admin_1.setGeometry(QtCore.QRect(15, 470, 281, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setStrikeOut(False)
   
        self.admin_1.setFont(font)
        self.admin_1.setStyleSheet("color: #ffffff;background-color: rgba(255, 255, 255, 0);")
        self.admin_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.admin_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.admin_1.setObjectName("admin_1")
        
        self.user_3 = QtWidgets.QLabel(self.widget)
        self.user_3.setGeometry(QtCore.QRect(15, 420, 281, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setStrikeOut(False)
        font.setBold(True)
        self.user_3.setFont(font)
        self.user_3.setStyleSheet("color: #ffffff;background-color: rgba(255, 255, 255, 0);")
        self.user_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.user_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.user_3.setObjectName("user_3")
        
        self.user_2 = QtWidgets.QLabel(self.widget)
        self.user_2.setGeometry(QtCore.QRect(15, 400, 281, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setStrikeOut(False)
        self.user_2.setFont(font)
        self.user_2.setStyleSheet("color: #ffffff;background-color: rgba(255, 255, 255, 0);")
        self.user_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.user_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.user_2.setObjectName("user_2")
        
        self.user_1 = QtWidgets.QLabel(self.widget)
        self.user_1.setGeometry(QtCore.QRect(15, 380, 281+15, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setStrikeOut(False)
        self.user_1.setFont(font)
        self.user_1.setStyleSheet("color: #ffffff;background-color: rgba(255, 255, 255, 0);")
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
        self.label_locker_2.setStyleSheet("color: #ffffff;background-color: rgba(255, 255, 255, 0);")
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
        self.label_locker.setStyleSheet("color: #ffffff;background-color: rgba(255, 255, 255, 0);")
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
"border-top-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
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
"border-top-right-radius: 0px;\n"
"border-bottom-left-radius: 20px;\n"
"border-bottom-right-radius: 0px;\n"
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
"border-top-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border: 2px solid #63727B;\n"
"color:#63727B;")
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
"border-top-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
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
"border-bottom-left-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
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
"border-top-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
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
        self.label.setStyleSheet("color: rgba(11, 131, 120, 219)")
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
        self.label_2.setStyleSheet("background-color: rgba(0, 0, 0, 0); color: rgba(11, 131, 120, 219);")
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
        self.checkFail.setStyleSheet("color: red; background-color: rgba(255, 255, 255, 0);")
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
        self.label_3.setStyleSheet("color:  rgba(11, 131, 120, 219); background-color: rgba(255, 255, 255, 0);")
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        
        # for timer start()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start()        
        
        self.updateData = QtCore.QTimer(self)
        self.updateData.timeout.connect(self.update_data)
        self.updateData.start(1000)  
        self.run_once = True 
         
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
        self.user_1.setText(_translate("mainMenu", "  Scan this qr code for user website --->"))
        
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
            
    # ========== to stop the timer and start it again ========== #
    def timers(self, isAble): 
        if isAble:
            # print("timers: all stop")
            # self.checkFailDetailsssss.stop()
            self.timer.stop()
            # self.failedCountdown.stop()
            self.updateData.stop()
        else:
            # print("timers: start")
            # self.checkFailDetailsssss.start()
            self.timer.start()
            self.updateData.start()

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
        
        self.check_internet_connection()

        # Update Time
        current_date = QtCore.QDate.currentDate().toString("ddd, MMM d yyyy")
        current_time = QtCore.QTime.currentTime().toString("h:mm AP")
    
        self.label_2.setText(current_time)
        self.label_3.setText(current_date)

    # ********************* Offline Mode ********************* #
    
    # download pincode
    def pinCode(self):
        try:
            
            # Note: to update all PIN in locker
            socket.create_connection(("8.8.8.8", 53))
            data = firebaseVerifyPincode()
        
            if not data == None:
                delete_table("PIN")
                for key in data:
                    offline_insert(TableName="PIN", data=key)
                    
        except OSError:
            print("no internet")
                
    # List of Locker
    def locker(self):
        
        # Note: to update Locker Number
        try:
            socket.create_connection(("8.8.8.8", 53))
       
            data = lockerList()
        
            if not data == None:
                delete_table("LOCK")
                for key in data:
                    offline_insert(TableName="LOCK", data=key)
                    
        except OSError:
            print("no internet")
            
    # check internet
    def check_internet_connection(self):
        try:
            # Attempt to create a socket connection to a known server (e.g., Google DNS)
            socket.create_connection(("8.8.8.8", 53))
            self.label.setText("<html><head/><body><p>AIoT Smartlock is <Strong>online<strong/></p></body></html>")
            
            # Open the Locker Remotely
            openLocker()
            
        except OSError:
            pass
            self.facialRegister.setEnabled(False)
            self.facialRegister.setText(".......")
            self.label.setText("<html><head/><body><p><Strong>No Internet<strong/> Connection</p></body></html>")
            
    def update_data(self):
        try:
            
            socket.create_connection(("8.8.8.8", 53))
            
            # check door status
            self.door_sensor_locker()
            
            # Update to database
            if self.run_once == True:
                updateToDatabase()
                self.run_once = False
            
        except OSError:
            pass
            self.run_once = True
            print("No Internet")
    # ===================== open facial Login ===================== #

    def openFacialLogin(self):
        self.facialLogin.setText("Loading..........")
        self.facialLogin.isEnabled = False
        self.facialRegister.isEnabled = False
        self.pincodeLogin.isEnabled = False
        
        # download updated Locker Number
        self.locker()
        
        # disable all timers
        self.timers(True)

        # Delay the creation of the FacialLogin object by 100 milliseconds
        QtCore.QTimer.singleShot(50, self.clickFacialLogin)

    def clickFacialLogin(self):

        from pages.Facial_Login import FacialLogin
        print("start loading facial login")
        
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
        
        # disable all timers
        self.timers(True)

        # Delay the creation of the FacialLogin object by 100 milliseconds
        QtCore.QTimer.singleShot(50, self.clickFacialRegister)

    def clickFacialRegister(self):
     
        from pages.Token_Form import TokenForm

        self.resize(1024, 565)
        Token = TokenForm(self)

        Token.show()
        self.facialRegister.setText("Facial Register")
    
    # ===================== open PIN LOGIN ===================== #
    def openPincodeLogin(self):
    
        self.pincodeLogin.setText("Loading..............")
        self.pincodeLogin.isEnabled = False
        self.facialLogin.isEnabled = False
        self.facialRegister.isEnabled = False

        self.pinCode()
        
        # disable all timers
        self.timers(True)
               
        # Delay the creation of the FacialLogin object by 100 milliseconds
        QtCore.QTimer.singleShot(50, self.clickPincodeLogin)

    def clickPincodeLogin(self):
     
        from pages.Pincode_Login import PincodeLogin
        
        Token = PincodeLogin(self)
    
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

    def hello_friend(self):
        print("hello friend")
        
    # ========================== change locker status ========================== #
    def change_status(self, status, button):
        
        text_color = "red" if status else "#63727B"
    
        current_stylesheet = button.styleSheet()
         
        # Extract the background color, border color, and border-top-left-radius from the current stylesheet
        background_color = current_stylesheet.split("background-color:")[1].split(";")[0].strip()
        border_top_left_radius = current_stylesheet.split("border-top-left-radius:")[1].split(";")[0].strip()
        border_top_right_radius = current_stylesheet.split("border-top-right-radius:")[1].split(";")[0].strip()
        border_bottom_left_radius = current_stylesheet.split("border-bottom-left-radius:")[1].split(";")[0].strip()
        border_bottom_right_radius = current_stylesheet.split("border-bottom-right-radius:")[1].split(";")[0].strip()    
        
        # Reapply the extracted styles along with the new text color
        new_stylesheet = f"""
            background-color: {background_color};
            border: 2px solid {text_color};
            border-top-left-radius: {border_top_left_radius};
            border-top-right-radius: {border_top_right_radius};
            border-bottom-left-radius: {border_bottom_left_radius};
            border-bottom-right-radius: {border_bottom_right_radius};
            color: {text_color};
        """
        button.setStyleSheet(new_stylesheet)
        
        # update to database online
        locker_sensor("_" + button.text(),status)
        
    def door_sensor_locker(self):
        pins_to_check = {
            26: self._20, 
            19: self._21, 
            13: self._16, 
            6: self._12, 
            5: self._7, 
            11: self._8
        }
        for pin, button in pins_to_check.items():
            self.change_status(status=door_status(pin), button=button)

       


