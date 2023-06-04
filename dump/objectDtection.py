import torch
import torchvision
from torchvision.models.detection import ssdlite320_mobilenet_v3_large
from torchvision.transforms import functional as F
import cv2
import time

# Load the pre-trained model
model = ssdlite320_mobilenet_v3_large(pretrained=True)
model.eval()

# Load the labels for the COCO dataset
LABELS = ['background', 'person', 'bicycle', 'car', 'motorcycle', 'airplane',
          'bus', 'train', 'truck', 'boat', 'traffic light', 'fire hydrant',
          'N/A', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog',
          'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'N/A',
          'backpack', 'umbrella', 'N/A', 'N/A', 'handbag', 'tie', 'suitcase',
          'frisbee', 'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat',
          'baseball glove', 'skateboard', 'surfboard', 'tennis racket',
          'bottle', 'N/A', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl',
          'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog',
          'pizza', 'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed',
          'N/A', 'dining table', 'N/A', 'N/A', 'toilet', 'N/A', 'tv', 'laptop',
          'mouse', 'remote', 'keyboard', 'cell phone', 'microwave', 'oven',
          'toaster', 'sink', 'refrigerator', 'N/A', 'book', 'clock', 'vase',
          'scissors', 'teddy bear', 'hair drier', 'toothbrush']

# Initialize variables for tracking object detection
last_detection_time = time.time()
current_object = None

# Define the function for drawing bounding boxes and labels on the image
def draw_boxes(image, boxes, labels):
    for box, label in zip(boxes, labels):
        x1, y1, x2, y2 = box.tolist()  # Convert tensors to lists
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)  # Convert to integers
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(image, LABELS[label], (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        print(LABELS[label])
# Open the video stream
video = cv2.VideoCapture(0)

while video.isOpened():
    # Read the next frame from the video stream
    ret, frame = video.read()
    frame = cv2.flip(frame, 1)

    # Check if the video has reached the end
    if not ret:
        break

    # Convert the frame to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Preprocess the frame
    frame_tensor = F.to_tensor(frame_rgb)

    # Make predictions
    with torch.no_grad():
        predictions = model([frame_tensor])

    # Extract the bounding boxes, labels, and scores from the predictions
    boxes = predictions[0]['boxes']
    labels = predictions[0]['labels']
    scores = predictions[0]['scores']

    # Check if enough time has passed since the last detection
    if time.time() - last_detection_time >= 1:
        # Filter the predictions based on the threshold
        threshold = 0.5
        filtered_boxes = boxes[scores > threshold]
        filtered_labels = labels[scores > threshold]

        # Update the current object with the detected object
        if len(filtered_boxes) > 0:
            current_object = (filtered_boxes[0], filtered_labels[0])
        else:
            current_object = None
        last_detection_time = time.time()

    # Convert the frame back to BGR for visualization
    frame_bgr = cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2BGR)

    # Draw the bounding boxes and labels on the frame
    if current_object is not None:
        draw_boxes(frame_bgr, [current_object[0]], [current_object[1]])

    # Display the resulting frame
    cv2.imshow('Object Detection', frame_bgr)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video stream and close the windows
video.release()
cv2.destroyAllWindows()
