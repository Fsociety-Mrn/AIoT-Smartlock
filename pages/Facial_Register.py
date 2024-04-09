from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from Face_Recognition.JoloRecognition import JoloRecognition as JL
from Raspberry.Raspberry import gpio_manual
from Firebase.Offline import delete_table
from pages.Custom_MessageBox import MessageBox

import cv2
import time
import dlib
import torch
import numpy as np
import os
import shutil

class facialRegister(QtWidgets.QFrame):
    def __init__(self,parent=None):
            super().__init__(parent)
            
            self.main_menu = parent
            
            self.Light_PIN,self.lights_on = 25, True
  
            # message box
            self.MessageBox = MessageBox()
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
            self.blink_threshold,self.blink_counter,self.blink = 0.35,0,True

            #frame
            self.setObjectName("facialRegistration")
            self.resize(1024, 565)
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
            self.widget.setGeometry(QtCore.QRect(180, 50, 661, 471))
            self.widget.setStyleSheet("border: 2px solid rgb(61, 152, 154) ;\n"
            "border-radius: 50px;")
            self.widget.setObjectName("widget")
            
            self.horizontalLayoutWidget = QtWidgets.QWidget(self.widget)
            # self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 631, 321))
            self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 621, 431))
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
            
            # Set the default image to your custom image
            self.default_image = QtGui.QPixmap("/home/aiotsmartlock/Downloads/AIoT_Smart-lock/Images/loading.png")

        
            self.captureStat = 1
            # camera capture
            self.label = QtWidgets.QLabel(self)
            self.label.setGeometry(QtCore.QRect(600, 5, 41, 41))
            self.label.setText("")
            self.label.setPixmap(QtGui.QPixmap(":/background/Images/capture.png"))
            self.label.setAlignment(QtCore.Qt.AlignCenter)
            self.label.setObjectName("label")
        
            self.capture = QtWidgets.QLabel(self)
            self.capture.setGeometry(QtCore.QRect(660, 10, 21, 31))
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
            self.status.setGeometry(QtCore.QRect(200, 10, 400, 31))
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
            self.landmark_detector = dlib.shape_predictor('/home/aiotsmartlock/Downloads/AIoT_Smart-lock/Model/shape_predictor_68_face_landmarks.dat')


            # turn on the switch 
            self.Lights = QtWidgets.QPushButton(self)
            self.Lights.setGeometry(QtCore.QRect(910 - 30, 250, 101, 41))
            font = QtGui.QFont()
            font.setFamily("Segoe UI")
            font.setBold(False)
            font.setPointSize(12)
            self.Lights.setFont(font)
            self.Lights.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.Lights.setAutoFillBackground(False)
            self.Lights.setStyleSheet("border:none;\n"
                "color:  rgba(11, 131, 120, 219);\n"
                "padding:10px")
            self.Lights.setText("")
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap("/home/aiotsmartlock/Downloads/AIoT_Smart-lock/Images/lights_on.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.Lights.setIcon(icon1)
            self.Lights.setIconSize(QtCore.QSize(42, 42))
            self.Lights.setFlat(False)
            self.Lights.setObjectName("back")
            self.Lights.clicked.connect(self.toggle_light)

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
        self.status.setText(_translate("facialRegistration", "Please be ready at 16"))
        self.Name.setText(_translate("facialRegistration", "Art Lisboa"))
        gpio_manual(self.Light_PIN,False)
    # =================== for Lights Button =================== #

    def toggle_light(self):
        # Toggle the state of the lights
        self.lights_on = not self.lights_on

        # Update the button text and icon
        self.update_button_icon()

    def update_button_icon(self):
        
        icon1 = QtGui.QIcon()
                
        # Update the button text and icon based on the state of the lights
        if self.lights_on:
            
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap("/home/aiotsmartlock/Downloads/AIoT_Smart-lock/Images/lights_on.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

            self.Lights.setIcon(icon1)
            
            gpio_manual(self.Light_PIN,False)
        else:
            
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap("/home/aiotsmartlock/Downloads/AIoT_Smart-lock/Images/lights_off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
  
            self.Lights.setIcon(icon1)
            gpio_manual(self.Light_PIN,True)

    # receive data from Token Form
    def receive(self,data):
        self.Name.setText(data)

    # capture and Train Images
    def captureSave(self, current_time=None, frame=None, cropFrame=None):

        # self.status.setText("Please blink" if self.capture >= 20 else "Face capture left" + str(21 - self.captureStat))
        self.capture.setText(str(21-self.captureStat))
        
        if self.captureStat >= 20:
            self.status.setText("Please blink")
            
        # Set time delay to avoid over capturing
        if current_time - self.last_recognition_time <= 0.5:
            return

        self.last_recognition_time = current_time
    
        # Save captured images if capture count is less than 20
        if self.captureStat <= 20:

            path = f"/home/aiotsmartlock/Downloads/AIoT_Smart-lock/Known_Faces/{self.Name.text()}/{self.captureStat}.png"

            # check if the frame is blurred
            laplacian_var = cv2.Laplacian(cropFrame, cv2.CV_64F).var()
   
            if laplacian_var < 300:
                self.status.setText("cant capture it is blured")
                
            else:
                try:
                    cv2.imwrite(path, frame)
                    self.captureStat += 1
                except:
                    pass
            
                self.status.setText("Please align your face properly")
            
            return False
        else:
            return True

    def facialTraining(self,image):
        
        # remove folder on banned system
        self.remove_suspended_person(image)
        
        self.timer.stop()
        self.cap.release()
        cv2.destroyAllWindows()

        self.status.setText("Facial training please wait")
        self.video.setPixmap(self.default_image)
        
        self.status.setText("Facial Training please wait")
        
        # Delay the creation of the FacialLogin object by 100 milliseconds
        QtCore.QTimer.singleShot(100, self.startFacialTraining)
        
    def startFacialTraining(self):
                
        # Train the facial recognition model
        JL().Face_Train()
        
        # Show the result
        title = "Facial Registration"
        text = "Successfully trained" 
        icon = self.MessageBox.Information
        self.messageBoxShow(title=title, text=text, buttons=self.MessageBox.Ok, icon=icon)
        
        self.main_menu.backTomain()
        
    def remove_suspended_person(self,image):

        # spam recognition
        result = JL().spam_detection(image=image)
        person = result[0]

        if result[0] == None:
            return
        
        # remove temporary suspended
        delete_table(Table_Name=person,dir="/home/aiotsmartlock/Downloads/AIoT_Smart-lock/Firebase/banned_and_temporary_list.json")
        
        # remove folder
        path = f"/home/aiotsmartlock/Downloads/AIoT_Smart-lock/spam_detection/{person}"
        if os.path.exists(path):
            shutil.rmtree(path)

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
        
        # check time 10 seconds
        current_time = time.time()
        if current_time - self.start_start <= 11:
            
            self.status.setText(f"please be ready at {int(10)-int(current_time - self.start_start)}")
            
            if len(faces) == 1:  
                x, y, w, h = faces[0]
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                
                
            height, width, channel = frame.shape
            bytesPerLine = channel * width
            qImg = QtGui.QImage(frame.data, width, height, bytesPerLine, QtGui.QImage.Format_BGR888)
            pixmap = QtGui.QPixmap.fromImage(qImg)
            self.video.setPixmap(pixmap)
            return

        if len(faces) == 1:
            
            x, y, w, h = faces[0]

            faceCrop = notFlip[y:y+h, x:x+w]
            face_gray = cv2.cvtColor(faceCrop, cv2.COLOR_BGR2GRAY)
            
            # Calculate new width and height
            scale_factor = 1.2
            new_w = int(w * scale_factor)
            new_h = int(h * scale_factor)

            # Adjust x and y to keep the center of the face in the crop
            new_x = max(0, x - (new_w - w) // 2)
            new_y = max(0, y - (new_h - h) // 2)

            # Crop the image with the new dimensions
            faceCrop = frame[new_y-40:new_y+new_h+30, new_x-40:new_x+new_w+30]
            
            # Calculate the Laplacian
            laplacian = cv2.Laplacian(face_gray, cv2.CV_64F)
    
            # Calculate the variance of the Laplacian
            variance = laplacian.var()
            
            Face_percentage = float("{:.2f}".format(100 * (w * h) / (frame.shape[0] * frame.shape[1])))
            Face_blurreness = float("{:.2f}".format(variance))
            
            statusCap = self.captureSave(current_time=current_time, frame=faceCrop,cropFrame=face_gray)
            
            if statusCap:
                if not self.eyeBlink(gray=face_gray):
                    gpio_manual(self.Light_PIN,True)
                    self.facialTraining(image=faceCrop) 
                    
            
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, "Face percentage: " + str(Face_percentage) + "%", (30, 420), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,255), 1)
            # cv2.putText(frame, "Face percentage: " + str("{:.2f}".format(40 + Face_percentage)) + "%", (90, 400), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (self.B, self.G, self.R), 1)
            cv2.putText(frame, "Face Blurreness:" + str(Face_blurreness), (30, 400), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,255), 1)
            
                  
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

        return status

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
