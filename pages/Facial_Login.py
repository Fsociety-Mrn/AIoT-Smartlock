import cv2
import time
import dlib
import numpy as np
import torch
import os
import uuid
import shutil

from Face_Recognition.JoloRecognition import JoloRecognition as Jolo
from Firebase.Offline import offline_insert,checkLocker
from Raspberry.Raspberry import OpenLockers,gpio_manual

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from pages.Custom_MessageBox import MessageBox

from Firebase.Offline import delete_table,offline_history,offline_insert,create_person_temporarily_banned

class FacialLogin(QtWidgets.QFrame):
    def __init__(self,main_menu):
        super().__init__(main_menu)
        
        self.Light_PIN,self.lights_on = 25, False
        
        self.start_start = time.time()
        
        self.main_menu = main_menu
        
        # for video streaming variable
        self.videoStream = cv2.VideoCapture(1) if cv2.VideoCapture(1).isOpened() else cv2.VideoCapture(0)
        self.videoStream.set(4, 1080)
        
        # Locker Number
        self.LockerNumber = 0
        
        # message box
        self.MessageBox = MessageBox()
        self.MessageBox.setStyleSheet("""
                        QLabel{
                            min-width: 600px; 
                            min-height: 50px; 
                            font-size: 20px;
                            padding-top: 10px; 
                            padding-bottom: 10px; 
                        }
                        QPushButton { 
                            width: 250px; 
                            height: 30px; 
                            font-size: 15px;
                         }
                    """)

        # ========= for facial detection ========= #
        
        # facial status
        self.facial_result = ("","")
        self.result = "","",False,False,None

        # yellow
        self.R,self.G ,self.B = (255,255,0)
     
        # EAR of eye
        self.blink_threshold, self.blink_counter, self.blink, self.last_dilation_time = 0.35,0,False,0
    
        # haar cascade face detection
        self.face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        # dlib face detection
        self.dlib_faceDetcetoor = dlib.get_frontal_face_detector()

        # using dlib landmark detector
        self.landmark_detector = dlib.shape_predictor('Model/shape_predictor_68_face_landmarks.dat')

        # =============================================================================================================== #

        # frame
        self.setObjectName("Facial Login")
        self.resize(1024, 565)
        
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
        self.widget.setGeometry(QtCore.QRect(180, 50, 661, 471))
        self.widget.setStyleSheet("border: 2px solid rgb(61, 152, 154) ;\n"
            "border-radius: 50px;")
        self.widget.setObjectName("widget")
        
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 621, 431))
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
        self.status.setGeometry(QtCore.QRect(0, 0, 1021, 51))
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
        self.back.setGeometry(QtCore.QRect(10, 10, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(False)
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
        self.back.setFlat(False)
        self.back.setObjectName("back")
        self.back.clicked.connect(self.back_to_main)
        
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
        icon1.addPixmap(QtGui.QPixmap("Images/lights_on.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Lights.setIcon(icon1)
        self.Lights.setIconSize(QtCore.QSize(42, 42))
        self.Lights.setFlat(False)
        self.Lights.setObjectName("back")
        self.Lights.clicked.connect(self.toggle_light)

        # Timer
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.videoStreaming)
        self.last_recognition_time = time.time()
        self.last_check = time.time()
        self.timer.start()
        
        self.status.raise_()
        self.back.raise_()
        self.widget.raise_()
        
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("facialLogin", "Frame"))
        self.status.setText(_translate("facialLogin", "<html><head/><body><p>Please wait, camera is loading.</p></body></html>"))
        self.back.setText(_translate("facialLogin", "Back "))
        
        gpio_manual(self.Light_PIN,False)
        
    def back_to_main(self):
        self.timer.stop()
        self.videoStream.release()
        cv2.destroyAllWindows()
        
        self.main_menu.upload_banned_person()
        self.main_menu.checkFacialUpdate()
        
        self.close()

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
            icon1.addPixmap(QtGui.QPixmap("Images/lights_on.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

            self.Lights.setIcon(icon1)
            
            gpio_manual(self.Light_PIN,False)
            
            return
        
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Images/lights_off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
  
        self.Lights.setIcon(icon1)
        gpio_manual(self.Light_PIN,True)

    # message box
    def messageBoxShow(self,title=None, text=None, buttons=None):

        # Set the window icon, title, and text
        # self.MessageBox.setIcon(icon)
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
     
    # Function to open the camera
    def openCameraWait(self):
        # Delay the creation of the FacialLogin object by 100 milliseconds
        QtCore.QTimer.singleShot(100, self.openCamera)
    
    def openCamera(self):
        # Open camera capture
        self.videoStream.open(0)
    
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
    
    def delete_folder(self,person):
        try:
            dir = f"spam_detection/{person}"
            shutil.rmtree(dir)
            print(f"Folder '{dir}' deleted successfully.")
        except Exception as e:
            print(f"Error: {dir} : {e}")
            
    # Facial Recognition
    def FacialRecognition(self, frame):
        
        # check spam recognition first
        result = Jolo().spam_detection(image=frame,threshold=0.7)
        person, __, spam_detected, error_occur = result
        
        # verify person is in database
        text,result_ = create_person_temporarily_banned(person,"Facial",False)
        self.result = person,text,result_,spam_detected,error_occur
        
        if spam_detected and error_occur == None and result_:
            self.facial_result = ("Denied",'No match detected')
            return

        # facial recognition
        result = Jolo().FaceCompare(frame)
        
        current_date = QtCore.QDate.currentDate().toString("MMM d yyyy")
        current_time = QtCore.QTime.currentTime().toString("h:mm:ss AP")
        
        self.LockerNumber = checkLocker(str(result[0]))

        if not result[0] == 'No match detected':
            
            self.R,self.G,self.B = (0,255,0)
            self.facial_result = ("Authenticated",result[0])
            
            delete_table("Failed attempt")
            delete_table("Fail History")
            delete_table(Table_Name=person,dir="Firebase/banned_and_temporary_list.json")
            self.delete_folder(person)
            offline_insert(TableName="Facial_update", data={"data" : "Facial Login"})
   
            self.messageBoxShow(
                title="Facial Recognition",
                text="Welcome " + str(result[0]) + "!\nLocker Number: " + str(self.LockerNumber),
                buttons=self.MessageBox.Ok
            )
            
        else:
            self.R,self.G,self.B = (255,0,0)
            self.facial_result = ("Denied",result[0])
            
        offline_history(name=result[0],
            access_type="Facial Login",
            Percentage=result[1],
            date=str(current_date),
            time=str(current_time))
                        
        self.status.setText("Please align your face to the camera")
            
    # spam recognition
    def anti_spam(self,image=None):   
             
        personID,text,result,spam_detected,error_occur = self.result

        if personID == None:
            # Generate a random UUID (version 4)
            unique_id = uuid.uuid4()
    
            # Convert UUID to a hexadecimal string and return the first 8 characters
            personID = "person_" + str(unique_id).upper()[:5]
            
                    
        # insert banned person
        create_person_temporarily_banned(personID,"Facial")
        
        # directory for banned person
        directory = "spam_detection"    
        new_dir = f"{directory}/{personID}"
        
        # if not detected it will create folder
        if not spam_detected and error_occur == None:
            os.makedirs(new_dir, exist_ok=True)
        
        print("folder: ", not os.path.exists(new_dir) )
        
        # if folder is exist 
        if not os.path.exists(new_dir) and not spam_detected:
            os.makedirs(new_dir, exist_ok=True)
            
        # if detected it will save images
        self.LastIn_FirstOut(directory=new_dir, new_image=image,batch=2)
          
        self.messageBoxShow(
            title="Facial Recognition",
            text=text,
            buttons=self.MessageBox.Ok
        )
        
        self.R,self.G,self.B = (255,0,0)
        
        if result == False:
            return text
        
        return self.back_to_main()
         
    # for facial detection
    def curveBox(self,frame=None,p1=None,p2=None,curvedRadius=30,BGR=(255,255,0)):
        B,G,R = BGR

        # upper left curve
        cv2.ellipse(
                img=frame, 
                center=(p1[0] + curvedRadius+15, p1[1] + curvedRadius), 
                axes=(curvedRadius, curvedRadius), 
                angle=180, 
                startAngle=0, 
                endAngle=90, 
                color=(B,G,R), # BGR
                thickness=3)
        
        # bottom left curve
        cv2.ellipse(
                img=frame, 
                center=(p1[0] + curvedRadius+15, p2[1] - curvedRadius-10), 
                axes=(curvedRadius, curvedRadius), 
                angle=90, 
                startAngle=0, 
                endAngle=90, 
                color=(B,G,R), # BGR
                thickness=3)
        
        # upper right curve
        cv2.ellipse(img=frame, 
                center=(p2[0]+curvedRadius-75, p1[1]+curvedRadius), 
                axes=(curvedRadius, curvedRadius), 
                angle=270, 
                startAngle=0, 
                endAngle=90, 
                color=(B,G,R), # BGR
                thickness=3)
                
        # bottom right curve
        cv2.ellipse(
                img=frame, 
                center=(p2[0] - curvedRadius - 15, p2[1] - curvedRadius -10), 
                axes=(curvedRadius, curvedRadius), 
                angle=0, 
                startAngle=0, 
                endAngle=90, 
                color=(B,G,R), # BGR
                thickness=3)

    # for video streaming
    def videoStreaming(self):
        ret, frame = self.videoStream.read()
        
        validation,result = self.facial_result
        
        # if no detected frames
        if not ret:
            self.status.setText("Please wait camera is loading")
            self.video.setPixmap(QtGui.QPixmap(":/background/Images/loading.png"))
            return

        
        # process the frame
        frame = cv2.flip(frame, 1)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
        # load facial detector haar
        faces = self.face_detector.detectMultiScale(gray,
                                                    scaleFactor=1.1,
                                                    minNeighbors=20,
                                                    minSize=(180, 180),
                                                    flags=cv2.CASCADE_SCALE_IMAGE)
        
        current_time = time.time()

        # detect one face only
        if len(faces) == 1:
            
            x, y, w, h = faces[0]
            faceCrop = frame[y:y+h, x:x+w]
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
            # face_gray = cv2.cvtColor(faceCrop, cv2.COLOR_BGR2GRAY) 
            
            # face blurred level
            face_blurred = self.detect_blur_in_face(face_gray=face_gray)
            
            if not face_blurred > 0:
                self.status.setText("Oops! Blurry camera. please clean lens or try face login again; if it persists, contact the admin for help!")
                self.show_frame(frame)
                return
                
            
            # check if user is Authenticated
            if validation == "Authenticated":
                
                self.LastIn_FirstOut(directory=f"Known_Faces/{result}",new_image=faceCrop)
                OpenLockers(name=result,key=self.LockerNumber,value=True)
                self.LockerNumber = 0
                offline_insert(TableName="Facial_update", data={"data" : "Facial Login"})
                
                return self.back_to_main()
            
            # check if user i not authenticated
            if validation == "Denied":
                self.facial_result = False,self.anti_spam(image=faceCrop)
                
            self.single_face_process(
                faces=faces,
                frame=frame,
                face_gray=face_gray,
                faceCrop=faceCrop,
                current_time=current_time
            )
            cv2.putText(frame, "Face blurriness: " + str(face_blurred), (30, 440), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (self.B, self.G, self.R), 1)
        
        # Multiple Face Detected
        elif len(faces) >= 1:
            
            self.B,self.G,self.R = (0,0,255)
            for (x, y, w, h) in faces:
                self.curveBox(frame=frame,p1=(x,y),p2=(x+w,y+h),BGR=(self.B,self.G,self.R))

            self.status.setText("more than 1 faces is detected")

        # No face detected
        else:
            self.status.setText("Align your face to unlock the Locker" if validation == "Authenticated" else "No face is detected")

        self.show_frame(frame)
        
    # =================== Frame and Face detection utility =================== #
    
    # for single face process
    def single_face_process(self,frame,faces, face_gray,current_time,faceCrop):

        x, y, w, h = faces[0]

        # set default color if 5 seconds has pass
        result = current_time - self.last_recognition_time >= 15

        self.B, self.G, self.R = (0, 255, 255) if result else (self.B, self.G, self.R)
        self.last_recognition_time = current_time  if result else self.last_recognition_time

        # set instruction and detect faces
        self.status.setText("please blink at least 2 second")
        self.curveBox(frame=frame,p1=(x,y),p2=(x+w,y+h),BGR=(self.B,self.G,self.R))
                    
        # eye blink status
        if self.eyeBlink(gray=face_gray, frame=faceCrop):
            self.FacialRecognition(frame=faceCrop)
                
    # display the frame on the label
    def show_frame(self,frame):
        height, width, channel = frame.shape
        bytesPerLine = channel * width
        qImg = QtGui.QImage(frame.data, width, height, bytesPerLine, QtGui.QImage.Format_BGR888)
        pixmap = QtGui.QPixmap.fromImage(qImg)
        self.video.setPixmap(pixmap)
    
    # check face blurred level
    def detect_blur_in_face(self,face_gray):
        
        # Calculate the Laplacian
        laplacian = cv2.Laplacian(face_gray, cv2.CV_64F)
    
        # Calculate the variance of the Laplacian
        variance = laplacian.var()
        
        Face_blured = float("{:.2f}".format(variance))
            
        return Face_blured
        
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
            blinks = self.update_blink_count_and_status(ear=ear)

            # display blink count, EAR, and eye status on frame
            self.display_stats_on_frame(frame, ear)
            
            # print(f"left eye:{left_eye} right eye:{right_eye}")

            return blinks

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
        
    def update_blink_count_and_status(self,ear=None,dilate_threshold=0.3):

        if ear < self.blink_threshold:
            
            self.blink = False
            
            # if eye is open
            if self.last_dilation_time is None:
                
                self.last_dilation_time = time.time()
            else:
                current_time = time.time()
                time_since_dilate = current_time - self.last_dilation_time
                
                if time_since_dilate >= dilate_threshold:
                    self.last_dilation_time = None
                    self.blink = False
                    
                    self.blink_counter = self.blink_counter + 1
                    return True
                
                # self.last_dilation_time = None
        else:
            
            # If eye is closed
            self.last_dilation_time = None
            self.blink = True
        return False

    def display_stats_on_frame(self, frame, EAR):
        # cv2.putText(frame, "Blink Counter: {}".format(self.blink_counter), (30, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
        #             (self.B, self.G, self.R),1)
        # cv2.putText(frame, "E.A.R: {}".format(EAR), (30, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (self.B, self.G, self.R), 1)
        cv2.putText(frame, "Eye Status: {}".format("OPEN" if self.blink else "CLOSE"), (30, 420), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (self.B, self.G, self.R),1)
        


