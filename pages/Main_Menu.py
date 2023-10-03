from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import socket

class MainWindow(QtWidgets.QFrame):
    def __init__(self,parent=None):
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
        
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        
        # icon
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setAutoFillBackground(False)
        self.label_6.setStyleSheet("")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/background/Images/logo192x192.png"))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.horizontalLayout.addWidget(self.widget)
        
        # second widget
        self.widget_2 = QtWidgets.QWidget(self)
        self.widget_2.setAutoFillBackground(False)
        self.widget_2.setStyleSheet("\n"
        "background-image:url(:/background/Images/background.jpg);\n"
        "background-color:rgb(255, 255, 255);\n"
        "border-bottom-right-radius: 50px;\n"
        "\n"
        "")
        self.widget_2.setObjectName("widget_2")
        
        # # check online status
        # self.checkOnline = QtWidgets.QLabel(self.widget_2)
        # self.checkOnline.setGeometry(QtCore.QRect(15, 20, 131, 31))
        # font = QtGui.QFont()
        # font.setFamily("Segoe UI")
        # font.setPointSize(10)
        # font.setStrikeOut(False)
        # self.checkOnline.setFont(font)
        # self.checkOnline.setStyleSheet("color:  rgba(11, 131, 120, 219)")
        # self.checkOnline.setFrameShape(QtWidgets.QFrame.NoFrame)
        # self.checkOnline.setAlignment(QtCore.Qt.AlignCenter)
        # self.checkOnline.setObjectName("checkOnline")
        

        # facial register
        self.facialRegister = QtWidgets.QPushButton(self.widget_2)
        self.facialRegister.setGeometry(QtCore.QRect(60, 360, 380, 51))
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
        
        # paro paro g
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(140, 25, 211, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setStyleSheet("color:  rgba(11, 131, 120, 219)")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        
        
        # self.onlineStat = QtWidgets.QPushButton(self.widget_2)
        # self.onlineStat.setEnabled(True)
        # self.onlineStat.setGeometry(QtCore.QRect(280, 412, 41, 41))
        # self.onlineStat.setStyleSheet("border-radius: 100px;")
        # self.onlineStat.setText("")
        # icon3 = QtGui.QIcon()
        # icon3.addPixmap(QtGui.QPixmap("Images/online.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self.onlineStat.setIcon(icon3)
        # self.onlineStat.setIconSize(QtCore.QSize(10, 10))
        # self.onlineStat.setObjectName("onlineStat")
        
        
        # settings
        self.settings = QtWidgets.QPushButton(self.widget_2)
        self.settings.setEnabled(True)
        self.settings.setGeometry(QtCore.QRect(440, 10, 51, 51))
        self.settings.setStyleSheet("border-radius: 100px;")
        self.settings.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Images/user-avatar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings.setIcon(icon1)
        self.settings.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.settings.setIconSize(QtCore.QSize(32, 32))
        self.settings.setObjectName("settings")
        
        # turn Off
        self.turnOff = QtWidgets.QPushButton(self.widget_2)
        self.turnOff.setEnabled(True)
        self.turnOff.setGeometry(QtCore.QRect(440, 50, 51, 51))
        self.turnOff.setStyleSheet("border-radius: 100px;")
        self.turnOff.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Images/power-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.turnOff.setIcon(icon1)
        self.turnOff.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.turnOff.setIconSize(QtCore.QSize(32, 32))
        self.turnOff.setObjectName("settings")
        
        # about
        # self.about = QtWidgets.QPushButton(self.widget_2)
        # self.about.setEnabled(True)
        # self.about.setGeometry(QtCore.QRect(10, 410, 41, 41))
        # self.about.setStyleSheet("border-radius: 100px;")
        # self.about.setText("")
        # icon2 = QtGui.QIcon()
        # icon2.addPixmap(QtGui.QPixmap(":/background/Images/info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self.about.setIcon(icon2)
        # self.about.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # self.about.setIconSize(QtCore.QSize(24, 24))
        # self.about.setObjectName("about")
        
        # time
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(55, 80 + 40, 401, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(42)
        font.setStrikeOut(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:  rgba(11, 131, 120, 219)")
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        
        # date
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(90 + 55, 150 + 40, 211, 20))
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
        
        self.closeEvent = self.closeEvent
        self.horizontalLayout.addWidget(self.widget_2)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        
        # main menu
        self.menu = QMenu(self)
        # self.menu.addAction(QAction("Option 1", self, triggered=self.option1_action))
        # self.menu.addAction(QAction("Option 2", self, triggered=self.option2_action))
        # self.menu.addAction(QAction("Option 3", self, triggered=self.option3_action))
        self.menu.addAction(QAction("Update Face Recognition", self, triggered=self.updateFace))
        self.menu.addAction(QAction("turn off", self, triggered=self.closeEvent))

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        
        self.setWindowTitle(_translate("mainMenu", "Frame"))
        
        self.facialRegister.setText(_translate("mainMenu", "Facial Register"))
        self.facialRegister.clicked.connect(self.openFacialRegister)
        
        self.facialLogin.setText(_translate("mainMenu", "Facial Login"))
        self.facialLogin.clicked.connect(self.openFacialLogin)
        
        self.label.setText(_translate("mainMenu", "paro paro g fly high butterfly"))
        
        self.label_2.setText(_translate("mainMenu", "12:00 PM"))
        
        self.label_3.setText(_translate("mainMenu", "Wed,Jun 3 2023"))
        
        # self.checkOnline.setText(_translate("mainMenu", "Online"))
        self.settings.clicked.connect(self.updateFace)
        
        self.turnOff.clicked.connect(self.closeEvent)
    
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
    
    def updateFace(self):
        
        self.facialLogin.setText("Face Recognition is Updating")
        self.facialRegister.setText("Please bear with me")
        self.facialLogin.isEnabled = False
        self.facialRegister.isEnabled = False

        # Delay the creation of the FacialLogin object by 100 milliseconds
        QtCore.QTimer.singleShot(100, self.update_face)
    
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
        self.facialLogin.setText("Facial Login")
        
        self.facialLogin.isEnabled = True
        self.facialRegister.isEnabled = True

    # check time
    def update_time(self):
        current_date = QtCore.QDate.currentDate().toString("ddd, MMM d yyyy")
        
        current_time = QtCore.QTime.currentTime().toString("h:mm AP")
        
        self.check_internet_connection()
        self.label_2.setText(current_time)
        self.label_3.setText(current_date)
        
    # check internet
    def check_internet_connection(self):
        try:
            # Attempt to create a socket connection to a known server (e.g., Google DNS)
            socket.create_connection(("8.8.8.8", 53))
            self.label.setText("<html><head/><body><p>AIoT Smartlock is <Strong>online<strong/></p></body></html>")
            
        except OSError:
            self.label.setText("<html><head/><body><p><Strong>No Internet<strong/> Connection</p></body></html>")
    
    # ===================== open facial Login ===================== #

    def openFacialLogin(self):
        self.facialLogin.setText("Loading..........")
        self.facialLogin.isEnabled = False
        self.facialRegister.isEnabled = False

        # Delay the creation of the FacialLogin object by 100 milliseconds
        QtCore.QTimer.singleShot(100, self.clickFacialLogin)


    def clickFacialLogin(self):

        from pages.Facial_Login import FacialLogin
        print("start loading")

        self.resize(1024, 565)
        Facial_Login = FacialLogin(self)
        Facial_Login.show()
        self.facialLogin.setText("Facial Login")

    #     # ===================== open Facial Register ===================== #

    def openFacialRegister(self):

        self.facialRegister.setText("Loading..............")
        self.facialLogin.isEnabled = False
        self.facialRegister.isEnabled = False

        # Delay the creation of the FacialLogin object by 100 milliseconds
        QtCore.QTimer.singleShot(100, self.clickFacialRegister)

    def clickFacialRegister(self):
        print("start loading")
        from pages.Token_Form import TokenForm
        print("start loading")


        self.resize(1024, 565)
        Token = TokenForm(self)

        Token.show()
        self.facialRegister.setText("Facial Register")

        
        # from pages.Facial_Register import facialRegister
        
        # FacialRegister = facialRegister(self)
        # FacialRegister.show()

    # when close the frame
    def close(self):
        QtWidgets.qApp.quit()

    def closeEvent(self, event):
        # show a message box asking for confirmation
        message_box = QtWidgets.QMessageBox(None)
        message_box.setWindowTitle('AIoT Smartlock')
        message_box.setText("Are you sure you want to exit?")
        message_box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        message_box.setDefaultButton(QtWidgets.QMessageBox.No)

        reply = message_box.exec_()
        # if the user confirms, exit the application
        if reply == QtWidgets.QMessageBox.Yes:
            QtWidgets.qApp.quit()
        else:
            message_box.close()
            
    def showMenu(self):
        self.menu.exec_(self.settings.mapToGlobal(self.settings.rect().bottomLeft()))
