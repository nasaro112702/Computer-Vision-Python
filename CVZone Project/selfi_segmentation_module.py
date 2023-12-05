# Import necessary libraries
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import cv2

# Open the default camera (camera index 0)
cap = cv2.VideoCapture(0)

# Set the width and height of the video capture
cap.set(3, 640)
cap.set(4, 480)

# Create a SelfiSegmentation object with the specified model (model=0)
segmentor = SelfiSegmentation(model=0)

# Infinite loop for continuous video capture and segmentation
while True:
    # Read a frame from the camera
    success, img = cap.read()

    # Remove the background using SelfiSegmentation, replacing it with a magenta color
    imgOut = segmentor.removeBG(img, imgBg=(255, 0, 255), cutThreshold=0.1)

    # Stack the original and segmented images side by side for display
    imgStacked = cvzone.stackImages([img, imgOut], cols=2, scale=1)

    # Display the stacked image with the window title "Segmented Image"
    cv2.imshow("Segmented Image", imgStacked)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
