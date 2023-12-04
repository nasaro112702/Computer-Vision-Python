# Import the OpenCV library
import cv2
import cvzone

# Create a VideoCapture object to access the default camera (camera index 0)
cap = cv2.VideoCapture(0)

# Load a PNG image with transparency
imgPNG = cv2.imread("Resources/icon.png", cv2.IMREAD_UNCHANGED)

# Infinite loop to continuously capture frames from the camera
while True:
    # Read a frame from the camera, 'success' indicates if the frame is captured successfully
    success, img = cap.read()

    # Overlay the loaded PNG image onto the captured frame at position [0, 0]
    cvzone.overlayPNG(img, imgPNG, pos=[0, 0])

    # Display the captured frame in a window named "Cam"
    cv2.imshow("Cam", img)

    # Wait for a key press for 1 millisecond (cv2.waitKey(1)) and continue the loop
    cv2.waitKey(1)
