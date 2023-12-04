# Import the OpenCV library
import cv2

# Open a video file for reading
cap = cv2.VideoCapture("Resources/Presentation1.mp4")

# Loop indefinitely to read frames from the video
while True:
    # Read a frame from the video
    success, img = cap.read()

    # Display the frame in a window named "Video"
    cv2.imshow("Video", img)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
