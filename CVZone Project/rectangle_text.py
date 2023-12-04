# Importing required libraries
import cv2  # OpenCV library for computer vision
import cvzone  # cvzone is a library built on top of OpenCV for additional functionality

# Initializing video capture from the default camera (camera index 0)
cap = cv2.VideoCapture(0)

# Continuous loop for capturing video frames
while True:
    # Reading a frame from the video capture
    success, img = cap.read()

    # Adding a rectangle around the text "Ryan Elico" at position (200, 300) on the image
    cvzone.putTextRect(img, "Ryan Elico", (200,300))

    # Displaying the modified image in a window named "Cam"
    cv2.imshow("Cam", img)

    # Waiting for a key press event (parameter is in milliseconds, 1 millisecond here)
    cv2.waitKey(1)
