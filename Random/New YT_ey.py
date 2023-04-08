import torch
import cv2
import dlib
import numpy as np
from scipy.spatial import distance as dist


# Calculate eye aspect ratio
def eye_aspect_ratio(eye):
    
    eye = torch.from_numpy(eye)
    # ------- verticle ------- #
    v1 = torch.dist(eye[1],eye[5])
    v2 = torch.dist(eye[2],eye[4])

    # ------- horizontal ------- #
    h1 = torch.dist(eye[0],eye[3])

    ear = (v1+v2)/h1
    return ear
    
    # A = dist.euclidean(eye[1], eye[5])
    # B = dist.euclidean(eye[2], eye[4])
    # C = dist.euclidean(eye[0], eye[3])
    # ear = (A + B) / (2.0 * C)
    # return ear


# Load the face and landmark detector models
face_detector = dlib.get_frontal_face_detector()
landmark_detector = dlib.shape_predictor('Model/shape_predictor_68_face_landmarks.dat')

# Define the video stream
video_stream = cv2.VideoCapture(0)

# Initialize the blink counter and threshold
blink_counter = 0
blink_threshold = 0.20

# Loop over the frames from the video stream
while True:
    # Read the current frame
    ret, frame = video_stream.read()

    frame = cv2.flip(frame,1)

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_detector(gray, 0)

    # Loop over the detected faces
    for face in faces:
        
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2= face.bottom()
        cv2.rectangle(frame,(x1,y1),(x2,y2),(200),2)
        
        # Detect the facial landmarks
        landmarks = landmark_detector(gray, face)

        # Extract the left and right eye coordinates
        left_eye = []
        right_eye = []
        for i in range(36, 42):
            left_eye.append((landmarks.part(i).x, landmarks.part(i).y))
        for i in range(42, 48):
            right_eye.append((landmarks.part(i).x, landmarks.part(i).y))

        # Calculate the eye aspect ratios
        left_ear = eye_aspect_ratio(left_eye)
        right_ear = eye_aspect_ratio(right_eye)

        # Average the eye aspect ratios
        ear = (left_ear + right_ear) / 2.0

        # Check if the eye aspect ratio is below the blink threshold
        if ear < blink_threshold:
            blink_counter += 1

        # Draw the eyes and blink counter on the frame
        cv2.drawContours(frame, [np.array(left_eye)], 0, (0, 255, 0), 2)
        cv2.drawContours(frame, [np.array(right_eye)], 0, (0, 255, 0), 2)
        cv2.putText(frame, "Blink Counter: {}".format(blink_counter), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                    (0, 0, 255), 2)

    # Show the frame
    cv2.imshow("Eye Blink Detection", frame)

    # Check for key press
    key = cv2.waitKey(1) & 0xFF

    # Break the loop if the 'q' key is pressed
    if key == ord("q"):
        break

# Release the video stream and close all windows
video_stream.release()
cv2.destroyAllWindows()
