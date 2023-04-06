import cv2
import numpy as np
import dlib 

# Initialize the camera
cap = cv2.VideoCapture(0)

face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')


blink_counter = 0

# Define the eye landmarks as a tuple of (x,y) coordinates
LEFT_EYE_LANDMARKS = (
    (36, 37),
    (37, 38),
    (38, 39),
    (39, 40),
    (40, 41),
    (36, 41)
)

RIGHT_EYE_LANDMARKS = (
    (36, 37),
    (37, 38),
    (38, 39),
    (39, 40),
    (40, 41),
    (36, 41)
)

# Define function to calculate eye aspect ratio (EAR)
def eye_aspect_ratio(eye):
    
    # Compute the euclidean distances between the two sets of
    # vertical eye landmarks (x, y)-coordinates
    A = np.linalg.norm(eye[1] - eye[5]) # 0 4
    B = np.linalg.norm(eye[2] - eye[4]) # 1 3

    # Compute the euclidean distance between the horizontal
    # eye landmark (x, y)-coordinates
    C = np.linalg.norm(eye[0] - eye[3])

    # Calculate the eye aspect ratio
    ear = (A + B) / (2.0 * C)

    return ear

blink = False

# Create a function to track eye motion
def track_eye(frame):
    global blink_counter,blink
    

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect the face in the frame
    faces = face_cascade.detectMultiScale(gray,
                                          scaleFactor=1.1, 
                                          minNeighbors=20, 
                                          minSize=(150, 150), 
                                          flags=cv2.CASCADE_SCALE_IMAGE)
    


    # Loop through all the detected faces
    if len(faces) == 1:

        x, y, w, h = faces[0]
        
        # Draw a rectangle around the face
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        


        # Crop the region of interest (ROI) containing the face
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        # Detect the eyes in the ROI
        eyes = eye_cascade.detectMultiScale(roi_gray,scaleFactor = 1.1,minNeighbors=20,flags=cv2.CASCADE_SCALE_IMAGE)

        
            
        # eyes should detected 2
        if len(eyes) == 2:
                
            for (ex,ey,ew,eh) in eyes:
                
                eye_roi_gray = roi_gray[ey:ey+eh, ex:ex+ew]
                eye_roi_color = roi_color[ey:ey+eh, ex:ex+ew]
                
                LEFT_landmarks = np.array([(ex + x, ey + y) for (ex, ey) in LEFT_EYE_LANDMARKS])
 
                ear = eye_aspect_ratio(LEFT_landmarks)
 
                
                cv2.drawContours(roi_color, [LEFT_landmarks], -1, (255, 0, 0), 1)

                cv2.putText(roi_color, "EAR: {:.2f}".format(ear), (10, 30),
                         cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
     
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)
                
                if ear < 0.5:
                    blink = False
                    blink_counter += 1
                # Eye is closed
                # Do something
                else:
                    blink = True
                # Eye is open
                # Do something else
                


        
    # Print blink counter
    cv2.putText(frame, f"blink: {blink_counter}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(frame, f"blinks status: {blink}", (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Return the processed frame
    return frame



# Main loop
while True:
    # Capture a frame from the camera
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    # Process the frame
    processed_frame = track_eye(frame)

    # Display the processed frame
    cv2.imshow('Eye Motion Tracking', processed_frame)

    # Wait for key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
