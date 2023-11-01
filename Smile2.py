import cv2

blue = (255, 0, 0)
red = (0, 0, 255)
green = (0, 255, 0)

video_capture = cv2.VideoCapture(0)

# load the haar cascades face and smile detectors
face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
smile_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")

# loop over the frames
while True:
    # get the next frame from the video and convert it to grayscale
    _, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # apply our face detector to the grayscale frame
    faces = face_detector.detectMultiScale(gray, 1.1, 8)
    
    # go through the face bounding boxes 
    for (x, y, w, h) in faces:
        # draw a rectangle around the face on the frame
        cv2.rectangle(frame, (x, y), (x + w, y + h), blue, 2)
        # get the region of the face
        roi = gray[y:y + h, x:x + w]
        
        # apply our smile detector to the region of the face
        smile_rects, rejectLevels, levelWeights = smile_detector.detectMultiScale3(
                                                        roi, 2.5, 20, outputRejectLevels=True)

        # weaker detections are classified as "Not Smiling"
        # while stronger detection are classified as "Smiling" 
        if len(levelWeights) == 0:
            cv2.putText(frame, "Not Smiling", (20, 20),
		            cv2.FONT_HERSHEY_SIMPLEX, 0.75, red, 3)
        else:
            if max(levelWeights) < 2:
                cv2.putText(frame, "Not Smiling", (20, 20),
		            cv2.FONT_HERSHEY_SIMPLEX, 0.75, red, 3)
            else:
                cv2.putText(frame, "Smiling", (20, 20),
		            cv2.FONT_HERSHEY_SIMPLEX, 0.75, green, 3)
        
    cv2.imshow('Frame', frame)
    # wait for 1 millisecond and if the q key is pressed, we break the loop
    if cv2.waitKey(1) == ord('q'):
        break
    
# release the video capture and close all windows
video_capture.release()
cv2.destroyAllWindows()        