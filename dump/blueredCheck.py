import cv2
import numpy as np
import torch
from facenet_pytorch import MTCNN



device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
mtcnn = MTCNN(image_size=160, margin=0, min_face_size=50,select_largest=False, device=device)

def check_face_blurriness(image_path, threshold=100):
    # Load the pre-trained face detector from OpenCV
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Load the image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    
    if len(faces) == 0:
        print("No faces found in the image.")
    else:
        for (x, y, w, h) in faces:
            # Extract the face region
            face = image[y:y+h, x:x+w]

            # Calculate blurriness of the face region
            face_gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
            
            laplacian_var = cv2.Laplacian(face_gray, cv2.CV_64F).var()
            
            print("blureness: " ,laplacian_var)
            if laplacian_var < threshold:
                print("Face is blurry.")
            else:
                print("Face is sharp.")
        
def checkFace(image_path):
    faces = cv2.imread(image_path)
    face,prob = mtcnn(faces, return_prob=True)
    
    print(prob)

# Example usage
image_path = "Known_Faces/chylle guzman/1.png"  # Replace with the path to your image
check_face_blurriness(image_path)
