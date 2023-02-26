# this script is  use for face recognition

from facenet_pytorch import MTCNN
import torch

# face recognition model
resnet = torch.jit.load("Model/InceptionResnetV1.pt", map_location='cpu').eval()

#  face detection model
mtcnn = MTCNN(image_size=160, margin=0, min_face_size=20) # initializing mtcnn for face detection

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
                if min_dist <= threshold:
                    
                    idx_min = dist_list.index(min_dist)
                    return (name_list[idx_min], min_dist)
                else:
                    return ('Unknown', None)
            else:
                return ('Unknown', None)
        else:
            return ('Unknown', None)
     
    

