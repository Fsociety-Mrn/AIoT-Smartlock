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
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Loop through all the detected faces
    for (x,y,w,h) in faces:
        # Draw a rectangle around the face
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

        # Crop the region of interest (ROI) containing the face
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        # Detect the eyes in the ROI
        eyes = eye_cascade.detectMultiScale(roi_gray)

        # Loop through all the detected eyes
        for (ex,ey,ew,eh) in eyes:
            # Draw a rectangle around the eye
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

            # Extract the region of interest (ROI) containing the eye
            eye_roi = roi_color[ey:ey+eh, ex:ex+ew]

            # Convert the eye ROI to grayscale
            eye_gray = cv2.cvtColor(eye_roi, cv2.COLOR_BGR2GRAY)

            # # Initialize the previous and current points for optical flow calculation
            # if prev_frame is None:
            #     prev_frame = eye_gray
            #     prev_points = cv2.goodFeaturesToTrack(prev_frame, maxCorners=100, qualityLevel=0.3, minDistance=7, blockSize=7)
            #     mask = np.zeros_like(frame)
            # else:
            #     current_frame = eye_gray
            #     current_points, status, error = cv2.calcOpticalFlowPyrLK(prev_frame, current_frame, prev_points, None, **lk_params)

            #     # Select good points
            #     good_new = current_points[status==1]
            #     good_old = prev_points[status==1]

            #     # Draw the optical flow vectors on the frame
            #     for i,(new,old) in enumerate(zip(good_new, good_old)):
            #         a,b = new.ravel()
            #         c,d = old.ravel()
            #         mask = cv2.line(mask, (a,b),(c,d),(0,255,0), 2)
            #         frame = cv2.circle(frame,(a,b),5,(0,0,255),-1)
            #     img = cv2.add(frame, mask)

            #     # Update the previous points and frame
            #     prev_frame = current_frame.copy()
            #     prev_points = good_new.reshape(-1,1,2)

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
