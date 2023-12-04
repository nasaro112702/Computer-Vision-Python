# Import OpenCV library for computer vision tasks
import cv2

# Import cvzone library for additional computer vision functionalities
import cvzone

# Create a VideoCapture object to access the default camera (camera index 0)
cap = cv2.VideoCapture(0)

# Infinite loop for continuously capturing and processing video frames
while True:
    # Read a frame from the camera, success is a boolean indicating if the frame was read successfully
    success, img = cap.read()

    # Draw a rectangular shape at the specified position on the image
    cvzone.cornerRect(img, (200, 200, 300, 200))

    # Display the modified image in a window titled "Cam"
    cv2.imshow("Cam", img)

    # Wait for a key event for 1 millisecond, and continue the loop
    cv2.waitKey(1)
