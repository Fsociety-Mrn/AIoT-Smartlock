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
        self.resize(543, 521)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.0965909, y2:0.909, stop:0 rgba(61, 152, 154, 255), stop:1 rgba(12, 14, 36, 255));")

        # video framing
        self.video = QtWidgets.QLabel(self)
        self.video.setGeometry(QtCore.QRect(20, 20, 501, 401))
        self.video.setAlignment(QtCore.Qt.AlignCenter)
        self.video.setObjectName("label")
        self.video.setStyleSheet("color: white;\n""")
        # face status
        self.status = QtWidgets.QLabel(self)
        self.status.setGeometry(QtCore.QRect(10, 420, 511, 41))
        self.status.setAlignment(QtCore.Qt.AlignCenter)
        self.status.setObjectName("label_2")
        self.status.setStyleSheet("color: white;\n""")

        # back to mainmenu button
        self.backToMainMeneButton = QtWidgets.QPushButton(self)
        self.backToMainMeneButton.setGeometry(QtCore.QRect(130, 460, 271, 51))
        self.backToMainMeneButton.setObjectName("pushButton")
        self.backToMainMeneButton.setStyleSheet("color: white;\n""")
        # connect the close event to the method

        # Timer
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.videoStreaming)
        self.last_recognition_time = time.time()
        self.timer.start(30)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Frame", "Frame"))

        # video frame
        self.video.setText(_translate("Frame", "Loading..."))

        # frame status
        self.status.setText(_translate("Frame", "status"))

        # back to main Menu
        self.backToMainMeneButton.setText(_translate("Frame", "back to mainMenu"))
        self.backToMainMeneButton.clicked.connect(self.backTomain)

    def backTomain(self):
        from Main_Menu import MainWindow
        
        print("go back to main menu")

        self.resize(555, 495)
        MainWindow(self).show()

        self.videoStream.release()
        cv2.destroyAllWindows()
        self.close()

    #  for facial recognition
    def FacialRecognition(self, frame):
        result = Jolo().Face_Compare(frame,threshold=0.6)

        if result[0] == 'No match detected':

            self.matchs = str(result[0])
            self.R = 255
            self.G = 0
            self.B = 0
        else:
            self.matchs = str(result[0])
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
            self.video.setText("Camera wont load")
            return
        
        # process the frame
        frame = cv2.flip(frame, 1)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # check if the frame is dark
        mean_value = cv2.mean(gray)[0]

        if mean_value < 50:
            
            self.status.setText("It is too dark.")
            
            # display the frame on the label
            height, width, channel = frame.shape
            bytesPerLine = channel * width
            qImg = QtGui.QImage(frame.data, width, height, bytesPerLine, QtGui.QImage.Format_BGR888)
            pixmap = QtGui.QPixmap.fromImage(qImg)
            self.video.setPixmap(pixmap)
           
            
            
            return
        
        # check if the frame is Bright
        if mean_value > 130:
            
            self.status.setText("It is too bright.")
            
            # display the frame on the label
            height, width, channel = frame.shape
            bytesPerLine = channel * width
            qImg = QtGui.QImage(frame.data, width, height, bytesPerLine, QtGui.QImage.Format_BGR888)
            pixmap = QtGui.QPixmap.fromImage(qImg)
            self.video.setPixmap(pixmap)
    
            return

        # load facial detector haar
        faces = self.face_detector.detectMultiScale(gray,
                                                    scaleFactor=1.1,
                                                    minNeighbors=20,
                                                    minSize=(150, 150),
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
            self.display_stats_on_frame(frame, ear)

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

    import sys,res
    # Create a new QApplication object
    app = QApplication(sys.argv)

    New_menu = FacialLogin()
    New_menu.show()

    sys.exit(app.exec_())
