import torchvision.transforms as transforms
from facenet_pytorch import MTCNN
from PIL import Image

# Initialize the MTCNN model
mtcnn = MTCNN(
    image_size=160, 
    margin=14,
    min_face_size=100,
    thresholds=[0.5, 0.6, 0.7],
    factor=0.6,
    keep_all=True,
    select_largest=True
)

from PIL import Image
import os

def face_scan(input_folder):
    # Loop over input images and extract faces
    for filename in os.listdir(input_folder):
        if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
        # Load input image
            image_path = os.path.join(input_folder, filename)
            image = Image.open(image_path)

        # Detect faces in image
            boxes, _ = mtcnn.detect(image)

        # Replace image with cropped face
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
                
face_scan('Crop_faces/Aj de Roque')