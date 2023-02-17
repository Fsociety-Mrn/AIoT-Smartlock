# This script use for convert InceptionResnetV1 to pytorch mobile
import torch
from facenet_pytorch import InceptionResnetV1

# face recognition model
resnet = InceptionResnetV1(pretrained='vggface2').eval() # initializing resnet for face img to embeding conversion

# export and resnet
traced_model_resnet = torch.jit.trace(resnet, torch.randn(1, 3, 160, 160))
traced_model_resnet.save("model/InceptionResnetV1.pt")