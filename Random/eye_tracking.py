import cv2

# Initialize the camera
cap = cv2.VideoCapture(0)

face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')


# Create a function to track eye motion
def track_eye(frame):

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect the face in the frame
    faces = face_cascade.detectMultiScale(gray,
                                          scaleFactor=1.1, 
                                          minNeighbors=20, 
                                          minSize=(100, 100), 
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
        eyes = eye_cascade.detectMultiScale(
            roi_gray,
            scaleFactor = 1.1,
            minNeighbors=20,
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        
        # eyes should detected 2
        if len(eyes) == 2:
    
            # Loop through all the detected eyes
            for (ex,ey,ew,eh) in eyes:
                
                # Draw a rectangle around the eye
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                
                # B G R
                cv2.putText(frame,"Eyes are open.",(x,y+h+30),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
                
        else:
            # B G R
            cv2.putText(frame,"Eyes are closed!",(x,y+h+30),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),1)

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
