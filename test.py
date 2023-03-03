import os
import torch
import cv2
import torchvision.transforms as transforms
import torchvision.datasets as datasets

from facenet_pytorch import MTCNN
from PIL import Image,ImageOps


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Initialize the MTCNN model
mtcnn = MTCNN(
    image_size=160,
    factor=0.8,
    
    selection_method="probability",
    keep_all=True,
    device=device
    )


def face_scan(input_folder):
    # Loop over input images and extract faces
    for filename in os.listdir(input_folder):
        if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
            
        # Load input image
            image_path = os.path.join(input_folder, filename)
            image = Image.open(image_path)
            image = ImageOps.equalize(image, mask=None)
   
        # detect crop images return probability
            face, prob = mtcnn(image, return_prob=True)
            
            if face is not None and prob > 0.90:
        # Detect faces in image
                boxes, _ = mtcnn.detect(image)

        # # Replace image with cropped face
                if boxes is not None:
            # Get largest face
                    box = boxes[0]
            # Crop face from image
                    face = image.crop(box)
            # Replace input image with cropped face
                    face.save(image_path)
                else:
            # If no faces detected, delete image
                    os.remove(image_path)
                
face_scan('Crop_faces/Francis Maneclang')

