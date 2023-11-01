import cv2
import dlib
import numpy as np

# Load the face detector and facial landmark predictor
face_detector = dlib.get_frontal_face_detector()
landmark_predictor = dlib.shape_predictor("Model/shape_predictor_68_face_landmarks.dat")

# Load a pre-trained Haar Cascade for smile detection
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

# Open the webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_detector(gray)

    for face in faces:
        # Get facial landmarks
        landmarks = landmark_predictor(gray, face)

        # Extract points for the mouth region
        points = []
        for i in range(48, 68):  # Mouth region in the 68 landmarks model
            x, y = landmarks.part(i).x, landmarks.part(i).y
            points.append((x, y))

        # Convert the points list to a numpy array
        points = np.array(points)

        # Draw a rectangle around the mouth region
        x, y, w, h = cv2.boundingRect(points)

        # Detect smiles within the mouth region
        roi_gray = gray[y:y + h, x:x + w]
        smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.9, minNeighbors=30, minSize=(50, 50))

        is_smiling = len(smiles) > 0  # Check if any smiles are detected

        # Print whether the person is smiling or not
        if is_smiling:
            cv2.putText(frame, 'Smiling', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
            print("Person is smiling")
        else:
            cv2.putText(frame, 'Not Smiling', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
            print("Person is not smiling")

    # Display the frame
    cv2.imshow('Facial Expression Detection', frame)

    # Exit the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
