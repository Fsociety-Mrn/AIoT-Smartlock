import cv2
import dlib
import numpy as np


predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")


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

