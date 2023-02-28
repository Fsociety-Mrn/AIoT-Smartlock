# this script  use for training Known_Faces for face recognition

from facenet_pytorch import MTCNN,InceptionResnetV1
import torch
from torchvision import datasets
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
from PIL import Image

# High level Face detection
mtcnn = MTCNN(    
            image_size=160, 
            margin=0, 
            min_face_size=100,
            thresholds=[0.5, 0.6, 0.7],
            select_largest=True) # initializing mtcnn for face detection

# Face recognition
# resnet = torch.jit.load("Model/InceptionResnetV1.pt").eval() # initializing resnet for face img to embeding conversion
resnet = InceptionResnetV1(pretrained='vggface2').eval() 
# check if they are using GPU or Cpu
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

mtcnn.to(device)
resnet.to(device)

dataset=datasets.ImageFolder('Known_Faces') # photos folder path 
label_names = {i:c for c,i in dataset.class_to_idx.items()} # accessing names of peoples from folder names

def collate_fn(x):
    return x[0]


train_transform = transforms.Compose([
    transforms.RandomHorizontalFlip(p=0.5),
    transforms.RandomAffine(degrees=(-10, 10), translate=(0.1, 0.1), scale=(0.9, 1.1)),
    transforms.ColorJitter(brightness=0.1, contrast=0.1, saturation=0.1, hue=0.1),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
])


loader = DataLoader(dataset, collate_fn=collate_fn)

face_list = [] # list of cropped faces from photos folder
name_list = [] # list of names corrospoing to cropped photos
embedding_list = [] # list of embeding matrix after conversion from cropped faces to embedding matrix using resnet

for images, labels in loader:
    
    with torch.no_grad():
        face, prob = mtcnn(images, return_prob=True) 
    
        if face is not None and prob>0.90: # if face detected and porbability > 90%
            emb = resnet(face.unsqueeze(0)) # passing cropped face into resnet model to get embedding matrix
            embedding_list.append(emb.detach()) # resulten embedding matrix is stored in a list
            name_list.append(label_names[labels]) # names are stored in a list
            print("Training...")
        
data = [embedding_list, name_list]
torch.save(data, 'Model/data.pt') # saving data.pt file