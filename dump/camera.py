import cv2

def set_camera_properties(cap, width, height, fps):
    # Set the resolution
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    # Set the frame rate
    cap.set(cv2.CAP_PROP_FPS, fps)

def capture_frame():
    # Open the camera
    cap = cv2.VideoCapture(0)  # Change the index if you have multiple cameras

    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Failed to open the camera.")
        return

    # Set camera properties (adjust as needed)
    # set_camera_properties(cap, 1920, 1080, 30)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 671)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 361)

    while True:
        # Read a frame from the camera
        ret, frame = cap.read()

        # Check if frame is captured successfully
        if not ret:
            print("Failed to capture frame.")
            break

        # Display the frame
        cv2.imshow("Camera", frame)

        # Wait for the 'q' key to be pressed to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()

# Call the capture_frame function to start capturing frames from the webcam
capture_frame()
