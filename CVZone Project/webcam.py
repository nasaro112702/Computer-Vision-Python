# Import the OpenCV library
import cv2

# Create a VideoCapture object to access the default camera (camera index 0)
cap = cv2.VideoCapture(0)

# Infinite loop to continuously capture frames from the camera
while True:
    # Read a frame from the camera, 'success' indicates if the frame is captured successfully
    success, img = cap.read()

    # Display the captured frame in a window named "Cam"
    cv2.imshow("Cam", img)

    # Wait for a key press for 1 millisecond (cv2.waitKey(1)) and continue the loop
    cv2.waitKey(1)
