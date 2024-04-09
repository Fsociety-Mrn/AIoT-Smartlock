import torch
import torchvision.transforms as transforms
import math 

from PIL import Image
from torchvision import datasets
from torch.utils.data import DataLoader
from facenet_pytorch import MTCNN,InceptionResnetV1



class JoloRecognition:
    
    def __init__(self):

        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        
        # face detection
        self.mtcnn  = MTCNN(image_size=160, margin=0, min_face_size=50,select_largest=False, device=self.device)
        
        # facial recognition
        self.facenet = InceptionResnetV1(pretrained='vggface2').eval().to(self.device)
        
        # load known faces data
        self.Saved_Data = torch.load('/home/aiotsmartlock/Downloads/AIoT_Smart-lock/Model/data.pt', map_location='cpu')
        self.Embedding_List = self.Saved_Data[0]
        self.Name_List = self.Saved_Data[1]
    
    # convert threshold to percent 
    def __thresh_to_percent(self,face_distance, face_match_threshold):
        if face_distance > face_match_threshold:
            range = (1.0 - face_match_threshold)
            linear_val = (1.0 - face_distance) / (range * 2.0)
            return linear_val
        else:
            range = face_match_threshold
            linear_val = 1.0 - (face_distance / (range * 2.0))
            return linear_val + ((1.0 - linear_val) * math.pow((linear_val - 0.5) * 2, 0.2)) 
            
    def FaceCompare(self, face, threshold=0.7):
        
        try:
    
            with torch.no_grad():
            
                # check if there is detected faces
                face,prob = self.mtcnn(face, return_prob=True)
            
                # check if there is face and probability of 90%
                if face  is not None and prob > 0.90:
                
                    # calculate the face distance
                    emb = self.facenet(face.unsqueeze(0)).detach()

                    # self.Embedding_List is the load data.pt 
                    for idx, emb_db in enumerate(self.Embedding_List):

                        # torch.dist = is use to compare the face detected into batch of faceas in self embediing
                        dist = torch.dist(emb, emb_db).item()
                        
                        # percentage
                        percentage = self.__thresh_to_percent(face_distance=dist,face_match_threshold=threshold)
                        percentage = percentage * 100

                        if dist < threshold:
                            return (self.Name_List[idx], percentage)
                      
                    return ('No match detected', percentage)

                return ('No match detected', None)  
        except:
            return ('No match detected', None)
        

    def __face_encodings(self, image_path):
        
        try:

            with torch.no_grad():
            # Load image using PIL
                image = Image.open(image_path)
                image = image.convert("RGB")  # Ensure image is in RGB mode
            
            # for facial detection level 2 --- Using MTCNN model
                face, prob = self.mtcnn(image, return_prob=True)

            # check if there is a detected face and has probability of 90%
                if face is not None and prob > 0.90:
                # calculate face distance
                    emb = self.facenet(face.unsqueeze(0))
                    return emb
        except Exception as e:
            print("__face_encodings:",e)
            return e
    
    def spam_detection(self, Dataset_Folder="/home/aiotsmartlock/Downloads/AIoT_Smart-lock/spam_detection", image=None,threshold=0.6):
        try:
            
            # face2 = self.__face_encodings(image)
            
            face2, prob = self.mtcnn(image, return_prob=True)
            
             # check if there is a detected face and has probability of 90%
            if face2 is None and prob < 0.90:
                return
            
            face2 = self.facenet(face2.unsqueeze(0))
            
            # define a function to collate data
            def collate_fn(x):
                return x[0]
            
            # locate the dataset of known faces
            dataset = datasets.ImageFolder(Dataset_Folder)

            # load the folder name in dataset
            label_names = {i: c for c, i in dataset.class_to_idx.items()}

            # load the dataset
            loader = DataLoader(
                dataset, 
                batch_size=1, 
                collate_fn=collate_fn, 
                pin_memory=True)

            for images, label in loader:

                with torch.no_grad():

                    # for facial detection level 2 --- Using MTCNN model
                    face, prob = self.mtcnn(images, return_prob=True)

                    # check if there is a detected face and has probability of 90%
                    if face is not None and prob > 0.90:
                        
                        # calculate face distance
                        emb = self.facenet(face.unsqueeze(0))
                        
                        dist = torch.dist(emb, face2).item()
                         
                        if dist < threshold:
                            return (label_names[label], dist,True,None)

            return (None, None,False,None)

        except Exception as e:
            print(f"spam_detection - Error occurred while training the model: {str(e)}")
            return (None, None,False,f"spam_detection: {str(e)}")
        
    # training from dataset
    def Face_Train(self, Dataset_Folder="/home/aiotsmartlock/Downloads/AIoT_Smart-lock/Known_Faces", location="/home/aiotsmartlock/Downloads/AIoT_Smart-lock/Model"):
        try:

            training_batch = 1
            
            # define a function to collate data
            def collate_fn(x):
                return x[0]
            
            # locate the dataset of known faces
            dataset = datasets.ImageFolder(Dataset_Folder)

            # load the folder name in dataset
            label_names = {i: c for c, i in dataset.class_to_idx.items()}

            # load the dataset
            loader = DataLoader(dataset, batch_size=20, collate_fn=collate_fn, pin_memory=True)

            # create empty lists for storing embeddings and names
            name_list = []
            embedding_list = []

            for images, label in loader:

                with torch.no_grad():

                    # for facial detection level 2 --- Using MTCNN model
                    face, prob = self.mtcnn(images, return_prob=True)

                    # check if there is a detected face and has probability of 90%
                    if face is not None and prob > 0.90:
                        
                        # calculate face distance
                        emb = self.facenet(face.unsqueeze(0))

                        embedding_list.append(emb.detach())
                        name_list.append(label_names[label])

                        training_batch +=1

            data = [embedding_list, name_list]

            # save the calculated face distance into data.pt
            torch.save(data, location + '/data.pt')

            return "Successfully trained"

        except Exception as e:
            print(f"Error occurred while training the model: {str(e)}")
            return "Error occurred while training the model"
         
    def face_compare_result(self,face_one,face_two):
        with torch.no_grad():
            
            face1 = self.__face_encodings(face_one)
            face2 = self.__face_encodings(face_two)
            
            # torch.dist = is use to compare the face detected into batch of faceas in self embediing
            dist = torch.dist(face1, face2).item()
            
            print(dist)
            return dist
            
            
# JoloRecognition().face_compare_result(
#     face_one="Known_Faces/FRANZ MANECLANG/1.png",
#     face_two ="Known_Faces/Art Lisboa/7.png"
#     )

# result = JoloRecognition().spam_detection(image="Images/2.png")
# print(result)

# JoloRecognition().Face_Train()
