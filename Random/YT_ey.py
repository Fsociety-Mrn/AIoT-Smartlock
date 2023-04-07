import cv2
import dlib
import time
from imutils import face_utils
# from scipy.spatial import distance as dist
import torch


cam = cv2.VideoCapture(0)

#------------Variables---------#
blink_thresh=0.3
tt_frame = 3
count=0


#------#
detector = dlib.get_frontal_face_detector()

face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

lm_model = dlib.shape_predictor('Random/shape_predictor_68_face_landmarks.dat')

#--Eye ids ---#
(L_start, L_end) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
print(L_start,L_end)
(R_start, R_end) = face_utils.FACIAL_LANDMARKS_IDXS['right_eye']

ptime = 0

def EAR_cal(eye):
    
    eye = torch.from_numpy(eye).float()
    #----verticle-#
    v1 = torch.dist(eye[1],eye[5])
    v2 = torch.dist(eye[2],eye[4])


    # #-------horizontal----#
    h1 = torch.dist(eye[0],eye[3])

    ear = (v1+v2)/h1
    return ear



while True:

    if cam.get(cv2.CAP_PROP_POS_FRAMES) == cam.get(cv2.CAP_PROP_FRAME_COUNT) :
        cam.set(cv2.CAP_PROP_POS_FRAMES,0)

    _,frame = cam.read()
    frame = cv2.flip(frame,1)
    
    img_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    #--------fps --------#
    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime= ctime
    cv2.putText(frame,f'FPS:{int(fps)}',(50,50),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,200),1)
    
    #-----facedetection----#
    faces = detector(img_gray)
    

        # Detect the face in the frame
    faces = face_cascade.detectMultiScale(img_gray,
                                          scaleFactor=1.1, 
                                          minNeighbors=20, 
                                          minSize=(150, 150), 
                                          flags=cv2.CASCADE_SCALE_IMAGE)
    
    if len(faces) == 1:
        
        
        x, y, w, h = faces[0]
        
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        
        # x1 = face.left()
        # y1 = face.top()
        # x2 = face.right()
        # y2= face.bottom()
        
        
        # cv2.rectangle(frame,(x1,y1),(x2,y2),(200),2)

        #---------Landmarks------#
        rect = dlib.rectangle(x, y, x+w, y+h)
        shapes = lm_model(img_gray,rect)
        shape = face_utils.shape_to_np(shapes)

        #-----Eye landmarks---#
        lefteye = shape[L_start:L_end]
        righteye = shape[R_start:R_end]

        for Lpt,rpt in zip(lefteye,righteye):
            cv2.circle(frame,Lpt,2,(200,200,0),2)
            cv2.circle(frame, rpt, 2, (200, 200, 0), 2)

        left_EAR = EAR_cal(lefteye)
        right_EAR= EAR_cal(righteye)

        avg =( left_EAR+right_EAR)/2

        if avg<blink_thresh :
            count+=1

        cv2.putText(frame, f"blink: {count}", (50, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 200, 0), 2)


    cv2.imshow("Video" ,frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()