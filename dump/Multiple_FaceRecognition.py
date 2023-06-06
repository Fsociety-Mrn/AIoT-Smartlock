import cv2
import torch
from facenet_pytorch import MTCNN
from Face_Recognition.JoloRecognition import JoloRecognition
# Load the pre-trained MTCNN model
mtcnn = MTCNN()









# ================================= face multiple recognition demo ================================= #

# image = cv2.imread('Images/A.jpg')
# image = cv2.imread('Images/B.jpg')
image = cv2.imread('Images/AFJ.jpg')

# Run face detection
boxes, probs = mtcnn.detect(image)

# Draw bounding boxes on the image
c = 0
for box in boxes:
    
    # Extract coordinates of the bounding box
    x1, y1, x2, y2 = int(box[0]), int(box[1]), int(box[2]), int(box[3])
    
    # x, y, w, h = faces[0]
    
    # Crop the face region
    face_image = image[y1:y2, x1:x2]
    
    result = JoloRecognition().Face_Compare(face=face_image)
    
    # Draw bounding box on the image
    cv2.rectangle(image, (x1, y1), (x2, y2), color=(255, 255, 0), thickness=2)

    # label the person
    cv2.putText(image, result[0], (x1, y1+50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255),2)

    
    # # os save
    # cv2.imwrite(f"Images/{c}.png", face_image)
    # c+=1

# resize the image
resized_image = cv2.resize(image, (800, 900))

# Convert the image back to BGR format
image = cv2.cvtColor(resized_image, cv2.COLOR_RGB2BGR)

# Display the image
cv2.imshow('Face Multiple Recognition', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
