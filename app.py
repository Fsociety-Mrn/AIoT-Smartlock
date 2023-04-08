import cv2
import sys
import time
import dlib
import numpy as np
import torch

from Face_Recognition.JoloRecognition import JoloRecognition as Jolo
from PyQt5 import QtCore,QtGui,QtWidgets

class Ui_SmartAIoT(object):
    def setupUi(self, SmartAIoT):
        
        SmartAIoT.setObjectName("SmartAIoT")
        SmartAIoT.setWindowModality(QtCore.Qt.ApplicationModal)
        SmartAIoT.resize(660, 600)
        SmartAIoT.setStyleSheet("background-color:rgb(255, 255, 255)")
        SmartAIoT.setAnimated(False)
        SmartAIoT.setDocumentMode(True)
        self.SmartAIoT_3 = QtWidgets.QWidget(SmartAIoT)
        self.SmartAIoT_3.setObjectName("SmartAIoT_3")
        
        # label
        self.label = QtWidgets.QLabel(self.SmartAIoT_3)
        self.label.setGeometry(QtCore.QRect(10, 10, 641, 460))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        
        # Timer
        self.timer = QtCore.QTimer(self.SmartAIoT_3)
        self.timer.timeout.connect(self.videoStreaming)
        
        SmartAIoT.setCentralWidget(self.SmartAIoT_3)

        # self.retranslateUi(SmartAIoT)
        QtCore.QMetaObject.connectSlotsByName(SmartAIoT)

        # open cv2
        self.cap = cv2.VideoCapture(1) if cv2.VideoCapture(1).isOpened() else cv2.VideoCapture(0)
        self.cap.set(4,1080)
        # self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 400)
        # self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)

        # face detection
        self.face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        
        # uisng dlib for face detector
        self.dlib_faceDetcetoor = dlib.get_frontal_face_detector()
        
        # using dlib landmark detector
        self.landmark_detector = dlib.shape_predictor('Model/shape_predictor_68_face_landmarks.dat')
        
        # EAR of eye
        self.blink_threshold = 0.3
        self.blink_counter = 0
        self.blink = True
        
        # countdown face detector
        self.last_recognition_time = time.time()
        self.timer.start(30)
        
        # facial data 
        self.matchs = "please blink"
        self.R=255
        self.G=255
        self.B=0
    
    
    # main function
    def retranslateUi(self, SmartAIoT):
        _translate = QtCore.QCoreApplication.translate
        SmartAIoT.setWindowTitle(_translate("SmartAIoT", "Facial Recognition"))
        self.label.setText(_translate("SmartAIoT", "Loading"))
        
    # caluclate of the EAR
    def EAR_cal(self,eye):
      
        eye = torch.from_numpy(np.array(eye)).float()

        # ------- verticle ------- #
        v1 = torch.dist(eye[1],eye[5])
        v2 = torch.dist(eye[2],eye[4])

        # ------- horizontal ------- #
        h1 = torch.dist(eye[0],eye[3])

        ear = (v1+v2)/h1
        return ear
    
    # eye blink
    def Eye_Blink(self,frame = None,gray = None):
        
        

        # face detector using dlib
        faceDlib = self.dlib_faceDetcetoor(gray,0)
            
        for facess in faceDlib:
                    
            left_eye = []
            right_eye = []
                    
            landmarks = self.landmark_detector(gray, facess)
                    
            for i in range(36, 42):
                left_eye.append((landmarks.part(i).x,landmarks.part(i).y))
                    
            for i in range(42, 48):
                right_eye.append((landmarks.part(i).x,landmarks.part(i).y))
                        
            cv2.drawContours(frame, [np.array(left_eye)], 0, (200, 0, 0), 2)
            cv2.drawContours(frame, [np.array(right_eye)], 0, (200, 0, 0), 2)
                
                # calculate the EAR of EYE
            LEFT = self.EAR_cal(left_eye)
            RIGHT = self.EAR_cal(right_eye)
                
            EAR = float((LEFT + RIGHT) / 2.0)
                
            if EAR < self.blink_threshold:
                
                # if eye is once Open
                if self.blink:
                    self.blink_counter += 1
                    self.blink = False
            else:
                # if eye is open
                self.blink = True
            EAR = round(EAR,2)
            
            cv2.putText(frame, "Blink Counter: {}".format(self.blink_counter), (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(200, 200, 0), 2)
            cv2.putText(frame, "EAR: {}".format(EAR), (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(200, 200, 0), 2)
            cv2.putText(frame, "Eye Status: {}".format(self.blink), (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(200, 200, 0), 2)
            
        
  
    # video streaming 
    def videoStreaming(self):

        ret, frame = self.cap.read()
        if ret:
            frame = cv2.flip(frame, 1)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert the frame to RGB
            
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            # face detector using haarcascade
            faces = self.face_detector.detectMultiScale(gray, 
                                                        scaleFactor=1.1, 
                                                        minNeighbors=20, 
                                                        minSize=(100, 100), 
                                                        flags=cv2.CASCADE_SCALE_IMAGE)
            
            current_time = time.time()
            if len(faces) == 1:
         
                x,y,w,h = faces[0]
                
                cv2.rectangle(frame, (x, y), (x+w, y+h), (self.R,self.G , self.B), 2)
                cv2.putText(frame,str(self.matchs),(x,y+h+30),cv2.FONT_HERSHEY_COMPLEX,1,(self.R,self.G,self.B),1)
                
                
                self.Eye_Blink(gray=gray,frame=frame)
                
                
                if self.blink == False:
                    # get the result of Face_Compare script
                    result = Jolo().Face_Compare(frame)
                
                    if result is not None and result[0] == 'No match detected':
                    # do something
                        self.matchs = str(result[0])
                        self.R=255
                        self.G=0
                        self.B=0
                    else:
                        self.matchs = str(result[0])
                        self.R=0
                        self.G=255
                        self.B=0
                    
                # check if ervery 2 sseonfd
                if current_time - self.last_recognition_time >= 5:
                    self.last_recognition_time = current_time
                    
                    # facial data 
                    self.matchs = "please blink"
                    self.R=255
                    self.G=255
                    self.B=0
                    
                # # get the result of Face_Compare script
                #     result = Jolo().Face_Compare(frame)
                
                #     if result is not None and result[0] == 'No match detected':
                #     # do something
                #         self.matchs = str(result[0])
                #         self.R=255
                #         self.G=0
                #         self.B=0
                #     else:
                #         self.matchs = str(result[0])
                #         self.R=0
                #         self.G=255
                #         self.B=0
                        
            elif len(faces) > 1:
                print("more than 1 faces is detected")
            else:
                print("No face is detected")

            
            
            img = QtGui.QImage(frame, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888)  # Convert the frame to a QImage
            self.label.setPixmap(QtGui.QPixmap.fromImage(img))  # Set the label pixmap to the QImage
    

        
    def closeEvent(self, event):
        self.cap.release()  # Release the camera when the application is closed


if __name__ == "__main__":
    
    print("Loading.........")

    app = QtWidgets.QApplication(sys.argv)
    SmartAIoT = QtWidgets.QMainWindow()
    ui = Ui_SmartAIoT()                          
    ui.setupUi(SmartAIoT)
    print("Done loading.")
    SmartAIoT.show()
    sys.exit(app.exec_())
