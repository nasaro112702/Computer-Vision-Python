# Import necessary libraries
import cvzone.FPS
import cv2

# Create an FPS (Frames Per Second) reader object with an average count of 30 frames
fpsReader = cvzone.FPS.FPS(avgCount=30)

# Create a VideoCapture object to access the default camera (camera index 0)
cap = cv2.VideoCapture(0)

# Set the frames per second (FPS) of the camera to 60
cap.set(cv2.CAP_PROP_FPS, 60)

# Infinite loop to continuously capture frames from the camera
while True:
    # Read a frame from the camera, 'success' indicates if the frame is captured successfully
    success, img = cap.read()

    # Update the FPS and get the updated frame
    fps, img = fpsReader.update(img)

    # Display the captured frame in a window named "Cam"
    cv2.imshow("Cam", img)

    # Wait for a key press for 1 millisecond (cv2.waitKey(1)) and continue the loop
    cv2.waitKey(1)
