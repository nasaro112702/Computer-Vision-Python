# Import the OpenCV library
import cv2

# Create a VideoCapture object to access the camera (camera index 0)
cap = cv2.VideoCapture(0)

# Set the width of the frame
cap.set(3, 640)

# Set the height of the frame
cap.set(4, 480)

# Set the brightness level
cap.set(10, 100)

# Infinite loop to continuously capture frames from the camera
while True:
    # Read a frame from the camera
    success, img = cap.read()

    # Display the captured frame in a window named "Video"
    cv2.imshow("Video", img)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
