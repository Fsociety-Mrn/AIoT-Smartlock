import cv2
import dlib
import numpy as np

face_detector = dlib.get_frontal_face_detector()
shape_predictor = dlib.shape_predictor('Model/shape_predictor_68_face_landmarks.dat')


cap = cv2.VideoCapture(1)  # You can change 0 to the appropriate camera index or video file path


while True:
    ret, frame = cap.read()

    if not ret:
        break
    
    frame = cv2.flip(frame, 1)

    # Convert the frame to grayscale for face and eye detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_detector(gray)

    for face in faces:
        # Detect landmarks for the face
        landmarks = shape_predictor(gray, face)
        
        # Extract the coordinates of the left and right eyes (landmark points 36 to 41 and 42 to 47)
        left_eye_coords = [[landmarks.part(i).x, landmarks.part(i).y] for i in range(36, 42)]
        right_eye_coords = [[landmarks.part(i).x, landmarks.part(i).y] for i in range(42, 48)]

        # Convert the coordinates to NumPy arrays
        left_eye_coords = np.array(left_eye_coords, dtype=np.int32)
        right_eye_coords = np.array(right_eye_coords, dtype=np.int32)

        # Draw a polygon around the left eye
        cv2.fillPoly(frame, [left_eye_coords], (0, 0, 0))  # Black color for the left eye
        # Draw a polygon around the right eye
        cv2.fillPoly(frame, [right_eye_coords], (0, 0, 0))  # Black color for the right eye

    # Display the frame with eyes detected
    cv2.imshow("Eye Detection", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit the loop
        break

cap.release()
cv2.destroyAllWindows()

