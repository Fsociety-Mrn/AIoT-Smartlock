import cv2
import time
import dlib
import numpy as np
import torch

from Face_Recognition.JoloRecognition import JoloRecognition as Jolo

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *


class FacialLogin(QtWidgets.QFrame):
    def __init__(self,parent=None):
        super().__init__(parent)
        # for video streaming variable
        self.videoStream = cv2.VideoCapture(1) if cv2.VideoCapture(1).isOpened() else cv2.VideoCapture(0)
        self.videoStream.set(4, 1080)
        
        
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

        # ========= for facial detection ========= #

        
        self.matchs = ""
        
        # grey
        # self.R = 115
        # self.G = 115
        # self.B = 115
        
        # yellow
        self.R = 255
        self.G = 255
        self.B = 0

        # EAR of eye
        self.blink_threshold = 0.3
        self.blink_counter = 0
        self.blink = True

        # haar cascade face detection
        self.face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        # dlib face detection
        self.dlib_faceDetcetoor = dlib.get_frontal_face_detector()

        # using dlib landmark detector
        self.landmark_detector = dlib.shape_predictor('Model/shape_predictor_68_face_landmarks.dat')

        # =============================================================================================================== #

        # frame

        self.setObjectName("Facial Login")
        self.resize(800, 480)
        
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/background/Images/logo192x192.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setStyleSheet("background-color: rgb(231, 229, 213);\n"
            "background-image: url(:/background/Images/background-removebg-preview.png);\n"
            "background-position: center;\n"
            "\n"
            "")
        # video framing
        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(140, 50, 511, 351))
        self.widget.setStyleSheet("border: 2px solid rgb(61, 152, 154) ;\n"
            "border-radius: 50px;")
        self.widget.setObjectName("widget")
        
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 471, 331))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        # video for facial recognition
        self.video = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.video.setFont(font)
        self.video.setStyleSheet("border:none;\n color:  rgba(11, 131, 120, 219);")
        self.video.setText("")
        self.video.setPixmap(QtGui.QPixmap(":/background/Images/loading.png"))
        self.video.setScaledContents(False)
        self.video.setAlignment(QtCore.Qt.AlignCenter)
        self.video.setObjectName("video")
        self.horizontalLayout.addWidget(self.video)
        
        # face status
        self.status = QtWidgets.QLabel(self)
        self.status.setGeometry(QtCore.QRect(0, 0, 801, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.status.setFont(font)
        self.status.setStyleSheet("color:  rgba(11, 131, 120, 219)")
        self.status.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.status.setAlignment(QtCore.Qt.AlignCenter)
        self.status.setObjectName("status")

        # back to mainmenu button
        self.back = QtWidgets.QPushButton(self)
        self.back.setGeometry(QtCore.QRect(0, 0, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.back.setFont(font)
        self.back.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back.setAutoFillBackground(False)
        self.back.setStyleSheet("border:none;\n"
                "color:  rgba(11, 131, 120, 219);\n"
                "padding:10px")
        self.back.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/background/Images/return.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back.setIcon(icon1)
        self.back.setIconSize(QtCore.QSize(42, 42))
        self.back.setObjectName("back")
        self.back.clicked.connect(self.backTomain)
        
        # connect the close event to the method
        
        # pincode
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(290, 410, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setStrikeOut(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:  rgba(11, 131, 120, 219)")
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        # pincode icon
        self.pincode = QtWidgets.QPushButton(self)
        self.pincode.setGeometry(QtCore.QRect(430, 415, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.pincode.setFont(font)
        self.pincode.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pincode.setAutoFillBackground(False)
        self.pincode.setStyleSheet("border: 2px solid #3D989A;\n"
        "border-radius: 20px;\n"
        "color: white;\n"
        "padding:10px;")
        self.pincode.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/background/Images/lock-pattern.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pincode.setIcon(icon2)
        self.pincode.setIconSize(QtCore.QSize(35, 35))
        self.pincode.setObjectName("pincode")
            
        # Timer
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.videoStreaming)
        self.last_recognition_time = time.time()
        self.timer.start(30)

        self.label_2.raise_()
        self.pincode.raise_()
        self.status.raise_()
        self.back.raise_()
        self.widget.raise_()
        
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("facialLogin", "Frame"))
        self.label_2.setText(_translate("facialLogin", "can\'t recognize ?"))
        self.status.setText(_translate("facialLogin", "<html><head/><body><p>Please wait, camera is loading.</p></body></html>"))
        self.back.setText(_translate("facialLogin", "Back "))
        
        self.pincode.clicked.connect(self.pinCodeShow)

    def backTomain(self):
        from pages.Main_Menu import MainWindow
        
        print("go back to main menu")

        self.resize(800, 480)
        MainWindow(self).show()

        self.videoStream.release()
        cv2.destroyAllWindows()
        self.close()

    
    
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
    
    # pincode show
    def pinCodeShow(self):
        Dialog = QDialog(self)
        Dialog.setWindowTitle("Pin Code Dialog")
        Dialog.setModal(True)  # Make the dialog modal
        
        Dialog.resize(461, 307)
        Dialog.setStyleSheet("background-image:url(Images/background-removebg-preview.png);\n"
            "background-color: rgb(231, 229, 213);")
        Dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        Dialog.move(qtRectangle.topLeft())

        # cautions
        label = QtWidgets.QLabel(Dialog)
        label.setGeometry(QtCore.QRect(90, 20, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        label.setFont(font)
        label.setStyleSheet("color: #3D989A;\n")
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setObjectName("label")
        label.setText("Please enter your email and password")
        
        # email 
        username = QtWidgets.QLineEdit(Dialog)
        username.setGeometry(QtCore.QRect(30, 60, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        username.setFont(font)
        username.setStyleSheet("background: transparents;\n"
            "color: #3D989A;\n"
            "background-color: rgb(255, 255, 255);\n"
            "border: 1px solid #3D989A;\n"
            "border-radius: 25px;")
        username.setAlignment(QtCore.Qt.AlignCenter)
        username.setObjectName("username")
        username.setPlaceholderText("Email")
        
        # password
        password = QtWidgets.QLineEdit(Dialog)
        password.setGeometry(QtCore.QRect(30, 120, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        password.setFont(font)
        password.setStyleSheet("background: transparents;\n"
            "color: #3D989A;\n"
            "background-color: rgb(255, 255, 255);\n"
            "border: 1px solid #3D989A;\n"
            "border-radius: 25px;")
        password.setAlignment(QtCore.Qt.AlignCenter)
        password.setObjectName("password")
        password.setPlaceholderText("Password")
        
        # enter button
        enterButton = QtWidgets.QPushButton(Dialog)
        enterButton.setGeometry(QtCore.QRect(120, 190, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        enterButton.setFont(font)
        enterButton.setStyleSheet("border: none;\n"
        "background: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
        "border-radius: 20px;\n"
        "color: white;")
        enterButton.setObjectName("enterButton")
        enterButton.setText("Enter")
        enterButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        
        # cancel button
        cancelButton = QtWidgets.QPushButton(Dialog)
        cancelButton.setGeometry(QtCore.QRect(120, 240, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        cancelButton.setFont(font)
        cancelButton.setStyleSheet("border: 2px solid #3D989A;\n"
            "border-radius: 20px;\n"
            "color: #3D989A;")
        cancelButton.setObjectName("cancelButon")
        cancelButton.setText("Cancel")
        cancelButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        
        # layout = QVBoxLayout(Dialog)
        # Dialog.setLayout(layout)

        # label = QLabel("Enter your pin code:", Dialog)
        # layout.addWidget(label)

        # pincode_edit = QLineEdit(Dialog)
        # layout.addWidget(pincode_edit)

        # button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Dialog)
        # button_box.accepted.connect(Dialog.accept)
        # button_box.rejected.connect(Dialog.reject)
        # layout.addWidget(button_box)
        
        Dialog.exec_()

        # if Dialog.exec_() == QDialog.Accepted:
        #     pin_code = pincode_edit.text()
        #     print("Entered pin code:", pin_code)
        # else:
        #     print("Pin code entry canceled")
    
    #  for facial recognition
    def FacialRecognition(self, frame):
        result = Jolo().Face_Compare(frame)

        if result[0] == 'No match detected':
            print(result[0])
            self.matchs = str(result[0])
            # self.status.setText(result[0])
            self.R = 255
            self.G = 0
            self.B = 0
            
            self.messageBoxShow(
                icon=self.MessageBox.Information,
                title="Facial Recognition",
                text="Access Denied! use pinCode if you cant recognize",
                buttons=self.MessageBox.Ok
            )
            

        else:
            self.matchs = str(result[0])
            
            self.messageBoxShow(
                icon=self.MessageBox.Information,
                title="Facial Recognition",
                text="Access Granted! Art Lisboa",
                buttons=self.MessageBox.Ok
            )
            # self.status.setText(result[0])
            self.R = 0
            self.G = 255
            self.B = 0
            
      
    
    # for facial detection
    def curveBox(self,frame=None,p1=None,p2=None,curvedRadius=30):
    
        # upper left curve
        cv2.ellipse(
                img=frame, 
                center=(p1[0] + curvedRadius+15, p1[1] + curvedRadius), 
                axes=(curvedRadius, curvedRadius), 
                angle=180, 
                startAngle=0, 
                endAngle=90, 
                color=(self.B, self.G, self.R), # BGR
                thickness=3)
        
        # bottom left curve
        cv2.ellipse(
                img=frame, 
                center=(p1[0] + curvedRadius+15, p2[1] - curvedRadius-10), 
                axes=(curvedRadius, curvedRadius), 
                angle=90, 
                startAngle=0, 
                endAngle=90, 
                color=(self.B, self.G, self.R), # BGR
                thickness=3)
        
        # upper right curve
        cv2.ellipse(img=frame, 
                center=(p2[0]+curvedRadius-75, p1[1]+curvedRadius), 
                axes=(curvedRadius, curvedRadius), 
                angle=270, 
                startAngle=0, 
                endAngle=90, 
                color=(self.B, self.G, self.R), # BGR
                thickness=3)
                
        # bottom right curve
        cv2.ellipse(
                img=frame, 
                center=(p2[0] - curvedRadius - 15, p2[1] - curvedRadius -10), 
                axes=(curvedRadius, curvedRadius), 
                angle=0, 
                startAngle=0, 
                endAngle=90, 
                color=(self.B, self.G, self.R), # BGR
                thickness=3)

    # for video streaming
    def videoStreaming(self):
        ret, frame = self.videoStream.read()

        if not ret:
            self.status.setText("Please go back to mainmenu")
            self.video.setText("Camera wont load")
            return
        
        # process the frame
        frame = cv2.flip(frame, 1)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # # check if the frame is dark
        # mean_value = cv2.mean(gray)[0]

        # if mean_value < 80:
            
        #     self.status.setText("It is too dark.")
            
        #     # display the frame on the label
        #     height, width, channel = frame.shape
        #     bytesPerLine = channel * width
        #     qImg = QtGui.QImage(frame.data, width, height, bytesPerLine, QtGui.QImage.Format_BGR888)
        #     pixmap = QtGui.QPixmap.fromImage(qImg)
        #     self.video.setPixmap(pixmap)
           
            
            
        #     return
        
        # # check if the frame is Bright
        # if mean_value > 100:
            
        #     self.status.setText("It is too bright.")
            
        #     # display the frame on the label
        #     height, width, channel = frame.shape
        #     bytesPerLine = channel * width
        #     qImg = QtGui.QImage(frame.data, width, height, bytesPerLine, QtGui.QImage.Format_BGR888)
        #     pixmap = QtGui.QPixmap.fromImage(qImg)
        #     self.video.setPixmap(pixmap)
    
        #     return

        # load facial detector haar
        faces = self.face_detector.detectMultiScale(gray,
                                                    scaleFactor=1.1,
                                                    minNeighbors=20,
                                                    minSize=(100, 100),
                                                    flags=cv2.CASCADE_SCALE_IMAGE)

        current_time = time.time()
        # display the result
        if len(faces) == 1:
            x, y, w, h = faces[0]

            
            self.curveBox(frame=frame,p1=(x,y),p2=(x+w,y+h))
            
            # cv2.rectangle(frame, (x, y), (x + w, y + h), (self.B, self.G, self.R), 2)
            cv2.putText(frame, str(self.matchs), (x, y + h + 30), cv2.FONT_HERSHEY_COMPLEX, 1, (self.B, self.G, self.R),1)

            if not self.eyeBlink(gray=gray, frame=frame):
                self.FacialRecognition(frame=frame)

            # check if ervery 5 second
            if current_time - self.last_recognition_time >= 5:

                self.last_recognition_time = current_time

                self.status.setText("Facial Recognition")
                self.matchs = ""
                
                # self.R = 115
                # self.G = 115
                # self.B = 115
                
                # yellow
                self.R = 255
                self.G = 255
                self.B = 0
            else:
                self.status.setText("Please Blink")

        elif len(faces) >= 1:
            self.status.setText("more than 1 faces is detected")
        else:
            self.status.setText("No face is detected")

        # display the frame on the label
        height, width, channel = frame.shape
        bytesPerLine = channel * width
        qImg = QtGui.QImage(frame.data, width, height, bytesPerLine, QtGui.QImage.Format_BGR888)
        pixmap = QtGui.QPixmap.fromImage(qImg)
        self.video.setPixmap(pixmap)

    # =================== for eye blinking detection functions =================== #
    def eyeBlink(self, gray, frame):

        # detect eyes using dlib
        faces = self.dlib_faceDetcetoor(gray, 0)

        for face in faces:
            landmarks = self.landmark_detector(gray, face)

            # extract eye coordinates from facial landmarks
            left_eye, right_eye = self.extract_eye_coordinates(landmarks)

            # calculate eye aspect ratio
            ear = self.calculate_ear(left_eye, right_eye)

            # update blink count and status
            self.update_blink_count_and_status(ear)

            # display blink count, EAR, and eye status on frame
            # self.display_stats_on_frame(frame, ear)

        return self.blink

    def extract_eye_coordinates(self, landmarks):
        left_eye = []
        right_eye = []

        for i in range(36, 42):
            left_eye.append((landmarks.part(i).x, landmarks.part(i).y))

        for i in range(42, 48):
            right_eye.append((landmarks.part(i).x, landmarks.part(i).y))

        return left_eye, right_eye

    def EAR_cal(self, eye):
        eye = torch.from_numpy(np.array(eye)).float()

        # ------- verticle ------- #
        v1 = torch.dist(eye[1], eye[5])
        v2 = torch.dist(eye[2], eye[4])

        # ------- horizontal ------- #
        h1 = torch.dist(eye[0], eye[3])

        ear = (v1 + v2) / h1
        return ear

    def calculate_ear(self, left_eye, right_eye):

        LEFT = self.EAR_cal(left_eye)
        RIGHT = self.EAR_cal(right_eye)

        EAR = float((LEFT + RIGHT) / 2.0)

        return round(EAR, 2)

    def update_blink_count_and_status(self, ear):
        if ear < self.blink_threshold:

            # if eye is once Open
            if self.blink:
                self.blink_counter += 1
                self.blink = False
        else:
            # if eye is open
            self.blink = True

    def display_stats_on_frame(self, frame, EAR):
        cv2.putText(frame, "Blink Counter: {}".format(self.blink_counter), (80, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                    (200, 200, 0), 2)
        cv2.putText(frame, "EAR: {}".format(EAR), (80, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (200, 200, 0), 2)
        cv2.putText(frame, "Eye Status: {}".format(self.blink), (80, 130), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (200, 200, 0),
                    2)

    # when close the frame


if __name__ == "__main__":

    import sys,background
    # Create a new QApplication object
    app = QApplication(sys.argv)

    New_menu = FacialLogin()
    New_menu.show()

    sys.exit(app.exec_())
