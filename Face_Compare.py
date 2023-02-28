# this script is  use for face recognition
from facenet_pytorch import MTCNN
import torch

# face recognition model
resnet = torch.jit.load("Model/InceptionResnetV1.pt", map_location='cpu').eval()

#  face detection model
mtcnn = MTCNN(
    image_size=160, 
    margin=0, 
    min_face_size=100,
    thresholds=[0.5, 0.6, 0.7],
    select_largest=True
    ) # initializing mtcnn for face detection

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
mtcnn.to(device)
resnet.to(device) 

saved_data = torch.load('Model/data.pt', map_location='cpu') # loading data.pt file
embedding_list = saved_data[0] # getting embedding data
name_list = saved_data[1]  # getting list of names
    
def face_match(face, threshold=0.6):
    # Use torch.no_grad() to reduce memory usage for the forward pass
    with torch.no_grad():
        # returns cropped face and probability
        face, prob = mtcnn(face, return_prob=True)
        if face is not None and prob > 0.90:
            emb = resnet(face.unsqueeze(0)).detach() # detach is to make required gradient false
            dist_list = [] # list of matched distances, minimum distance is used to identify the person
            for idx, emb_db in enumerate(embedding_list):
                try:
                    dist = torch.dist(emb, emb_db).item()
                    dist_list.append(dist)
                    
                except:
                    break
            if len(dist_list) > 0:
                min_dist = min(dist_list)
                print(min_dist)
                if min_dist < threshold:
                    
                    idx_min = dist_list.index(min_dist)
                    return (name_list[idx_min], min_dist)
                else:
                    return ('Unknown', None)
            else:
                return ('Unknown', None)
        else:
            return ('Unknown', None)
     

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
    
import cv2

face_scan('Crop_faces/Roger Gajunera')
# face = cv2.imread('Known_Faces/Roger Gajunera/IMG_20230227_202132.jpg')
# print(face_match(face))