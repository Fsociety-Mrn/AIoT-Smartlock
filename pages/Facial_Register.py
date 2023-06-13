

from PyQt5 import QtCore, QtGui, QtWidgets

from Face_Recognition.JoloRecognition import JoloRecognition as JL

import os
import cv2
import time
import dlib
import torch
import numpy as np
import threading
from PyQt5.QtWidgets import *


class facialRegister(QtWidgets.QFrame):
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

            # EAR of eye
            self.blink_threshold = 0.3
            self.blink_counter = 0
            self.blink = True

            #frame
            self.setObjectName("facialRegistration")
            self.resize(800, 480)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(":/background/Images/logo192x192.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.setWindowIcon(icon)
            self.setStyleSheet("background-color: rgb(231, 229, 213);\n"
            "background-image: url(:/background/Images/background-removebg-preview.png);\n"
            "background-position: center;\n"
            "")

            # user name
            self.Name = QtWidgets.QLabel(self)
            self.Name.setGeometry(QtCore.QRect(0, 10, 211, 41))
            font = QtGui.QFont()
            font.setFamily("Segoe UI")
            font.setPointSize(12)
            font.setBold(True)
            font.setWeight(75)
            self.Name.setFont(font)
            self.Name.setStyleSheet("color: #3D989A")
            self.Name.setAlignment(QtCore.Qt.AlignCenter)
            self.Name.setObjectName("Name")
            
            #camera
            self.widget = QtWidgets.QWidget(self)
            self.widget.setGeometry(QtCore.QRect(140, 60, 511, 351))
            self.widget.setStyleSheet("border: 2px solid rgb(61, 152, 154) ;\n"
            "border-radius: 50px;")
            self.widget.setObjectName("widget")
            
            self.horizontalLayoutWidget = QtWidgets.QWidget(self.widget)
            # self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 631, 321))
            self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 471, 331))
            self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
            self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
            self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            self.horizontalLayout.setObjectName("horizontalLayout")

            # camera video label
            self.video = QtWidgets.QLabel(self.horizontalLayoutWidget)
            self.video.setStyleSheet("border:none;")
            self.video.setText("")
            self.video.setPixmap(QtGui.QPixmap(":/background/Images/loading.png"))
            self.video.setScaledContents(False)
            self.video.setAlignment(QtCore.Qt.AlignCenter)
            self.video.setObjectName("video")
            self.horizontalLayout.addWidget(self.video)
        

            self.captureStat = 1
            # camera capture
            self.label = QtWidgets.QLabel(self)
            self.label.setGeometry(QtCore.QRect(370, 430, 41, 41))
            self.label.setText("")
            self.label.setPixmap(QtGui.QPixmap(":/background/Images/capture.png"))
            self.label.setAlignment(QtCore.Qt.AlignCenter)
            self.label.setObjectName("label")
        
            self.capture = QtWidgets.QLabel(self)
            self.capture.setGeometry(QtCore.QRect(410, 435, 21, 31))
            font = QtGui.QFont()
            font.setFamily("Segoe UI")
            font.setPointSize(12)
            font.setBold(True)
            font.setWeight(75)
            self.capture.setFont(font)
            self.capture.setStyleSheet("color: #3D989A")
            self.capture.setAlignment(QtCore.Qt.AlignCenter)
            self.capture.setObjectName("capture")
            
            # status
            self.status = QtWidgets.QLabel(self)
            self.status.setGeometry(QtCore.QRect(-10, 10, 811, 31))
            font = QtGui.QFont()
            font.setFamily("Segoe UI")
            font.setPointSize(12)
            font.setBold(True)
            font.setWeight(75)
            self.status.setFont(font)
            self.status.setStyleSheet("color: #3D989A")
            self.status.setAlignment(QtCore.Qt.AlignCenter)
            self.status.setObjectName("status")

            # open camera
            self.cap = cv2.VideoCapture(1) if cv2.VideoCapture(1).isOpened() else cv2.VideoCapture(0)
            self.cap.set(4, 1080)
            
            # face detector: Haar, dlib,landmark
            self.face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            self.dlib_faceDetcetoor = dlib.get_frontal_face_detector()
            self.landmark_detector = dlib.shape_predictor('Model/shape_predictor_68_face_landmarks.dat')


            # Timer
            self.timer = QtCore.QTimer(self)
            self.timer.timeout.connect(self.videoStreaming)
            self.last_recognition_time = time.time()
            self.start_start = time.time()
            self.timer.start(30)

            self.retranslateUi()
            QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("facialRegistration", "Frame"))
        self.capture.setText(_translate("facialRegistration", "0"))
        self.status.setText(_translate("facialRegistration", "Please be ready at 5"))
        self.Name.setText(_translate("facialRegistration", "Art Lisboa"))

    # receivce data from Token Form
    def receive(self,data):
        self.Name.setText(data)

    # capture and Train Images
    def captureSave(self, current_time=None, frame=None, cropFrame=None):


        # self.status.setText("Please blink" if self.capture >= 20 else "Face capture left" + str(21 - self.captureStat))
        
        self.capture.setText(str(21-self.captureStat))
        
        if self.captureStat >= 20:
            self.status.setText("Please blink")
            
        # Set time delay to avoid over capturing
        if current_time - self.last_recognition_time <= 0.2:
            return

        self.last_recognition_time = current_time
    
        # Save captured images if capture count is less than 20
        if self.captureStat <= 20:

            path = f"Known_Faces/{self.Name.text()}/{self.captureStat}.png"
            
            cv2.imwrite(path, frame)
            self.captureStat += 1
            self.status.setText("Please align your face properly")
            
            # check if the frame is blured
            # laplacian_var = cv2.Laplacian(cropFrame, cv2.CV_64F).var()
            # print("Blurered level",laplacian_var)
            # if laplacian_var < 100:
            #     self.status.setText("cant capture it is blured")
                
            # else:
            #     cv2.imwrite(path, frame)
            #     self.captureStat += 1
            
            #     self.status.setText("Please align your face properly")
            
            return False
        else:
            return True

    def facialTraining(self):

        # Train the facial recognition model
        message = JL().Face_Train()

        # Show the result
        title = "Facial Registration"
        text = "Facial training complete" if message == "Successfully trained" else message
        icon = self.MessageBox.Information if message == "Successfully trained" else self.MessageBox.Warning
        self.messageBoxShow(title=title, text=text, buttons=self.MessageBox.Ok, icon=icon)


        from pages.Main_Menu import MainWindow
        from pages.Token_Form import TokenForm
        
        print("go back to main menu")

        self.resize(800, 480)
        TokenForm(self).close()
        self.close()
        MainWindow(self).show()

        
        self.cap.release()
        cv2.destroyAllWindows()
        self.close()

    # video Streaming
    def videoStreaming(self):
        ret, notFlip = self.cap.read()

        if not ret:
            self.status.setText("Camera wont load")
            return

        # process the frame
        frame = cv2.flip(notFlip, 1)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    

        # load facial detector haar
        faces = self.face_detector.detectMultiScale(gray,
                                                    scaleFactor=1.1,
                                                    minNeighbors=20,
                                                    minSize=(100, 100),
                                                    flags=cv2.CASCADE_SCALE_IMAGE)
        
        
        # laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()
        # print("bluredness level ", laplacian_var)

        current_time = time.time()
        # check if the frame is dark
        mean_value = cv2.mean(gray)[0]
        
        if current_time - self.start_start <= 6:
            
            self.status.setText(f"please be ready at {int(6)-int(current_time - self.start_start)}")
            
            if len(faces) == 1:  
                x, y, w, h = faces[0]
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                
            height, width, channel = frame.shape
            bytesPerLine = channel * width
            qImg = QtGui.QImage(frame.data, width, height, bytesPerLine, QtGui.QImage.Format_BGR888)
            pixmap = QtGui.QPixmap.fromImage(qImg)
            self.video.setPixmap(pixmap)
            return
        
        # self.start_start = current_time
            
        
        # print("brightness value ", mean_value)
        
        if mean_value < 35:
                
            self.status.setText("It is too dark.")
                    
            height, width, channel = frame.shape
            bytesPerLine = channel * width
            qImg = QtGui.QImage(frame.data, width, height, bytesPerLine, QtGui.QImage.Format_BGR888)
            pixmap = QtGui.QPixmap.fromImage(qImg)
            self.video.setPixmap(pixmap)
            return
        
        # check if the frame is Bright
        if mean_value > 100:
            self.status.setText("It is too bright.")
                
            height, width, channel = frame.shape
            bytesPerLine = channel * width
            qImg = QtGui.QImage(frame.data, width, height, bytesPerLine, QtGui.QImage.Format_BGR888)
            pixmap = QtGui.QPixmap.fromImage(qImg)
            self.video.setPixmap(pixmap)
            return
        

        
        if len(faces) == 1:
            
            x, y, w, h = faces[0]
            

            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            faceCrop = notFlip[y:y+h, x:x+w]
            face_gray = cv2.cvtColor(faceCrop, cv2.COLOR_BGR2GRAY)
            
            statusCap = self.captureSave(current_time=current_time, frame=notFlip,cropFrame=face_gray)
            
            if statusCap:
                if not self.eyeBlink(gray=gray):
                    self.facialTraining()
                    
        elif len(faces) >= 1:
            self.status.setText("Multiple face is detected")
        else:
            self.status.setText("No face is detected")
    
        height, width, channel = frame.shape
        bytesPerLine = channel * width
        qImg = QtGui.QImage(frame.data, width, height, bytesPerLine, QtGui.QImage.Format_BGR888)
        pixmap = QtGui.QPixmap.fromImage(qImg)
        self.video.setPixmap(pixmap)

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

            # =================== for eye blinking detection functions =================== #
    def eyeBlink(self, gray):

        # detect eyes using dlib
        faces = self.dlib_faceDetcetoor(gray, 0)
        # status = None
        for face in faces:
            landmarks = self.landmark_detector(gray, face)

            # extract eye coordinates from facial landmarks
            left_eye, right_eye = self.extract_eye_coordinates(landmarks)

            # calculate eye aspect ratio
            ear = self.calculate_ear(left_eye, right_eye)

            # update blink count and status
            status = self.update_blink_count_and_status(ear)


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

                self.status.setText("Facial Training")
                return False
            else:
                # if eye is open
                self.status.setText("Please Blink")
                self.blink = True
                return True


if __name__ == "__main__":

    import sys,background
    # Create a new QApplication object
    app = QApplication(sys.argv)

    New_menu = facialRegister()
    New_menu.show()

    sys.exit(app.exec_())
