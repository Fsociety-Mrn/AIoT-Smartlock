import cv2

# Initialize the camera
cap = cv2.VideoCapture(0)

face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

prev_frame = None
prev_points = None

# Define the parameters for Lucas-Kanade optical flow
lk_params = dict(winSize=(15,15), maxLevel=4, criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

# Create a function to track eye motion
def track_eye(frame):
    global prev_frame,prev_points
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect the face in the frame
    faces = face_cascade.detectMultiScale(gray,
                                          scaleFactor=1.1, 
                                          minNeighbors=20, 
                                          minSize=(100, 100), 
                                          flags=cv2.CASCADE_SCALE_IMAGE)

    # Loop through all the detected faces
    for (x,y,w,h) in faces:
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

        # Loop through all the detected eyes
        for (ex,ey,ew,eh) in eyes:
            

            # Draw a rectangle around the eye
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

            # Extract the region of interest (ROI) containing the eye
            eye_roi = roi_color[ey:ey+eh, ex:ex+ew]
            rows, cols, _ = eye_roi.shape
            
            # Convert the eye ROI to grayscale
            eye_gray = cv2.cvtColor(eye_roi, cv2.COLOR_BGR2GRAY)
            eye_gray = cv2.GaussianBlur(eye_roi, (3,3),0)
            _, threshold = cv2.threshold(src=eye_gray, 
                                         thresh=3, 
                                         maxval=255, 
                                         type=cv2.THRESH_BINARY)
            
            _, contours, _ = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            for cnt in contours:
                cv2.drawContours(eye_roi,[cnt],-1,(0,0,255),3)           


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
