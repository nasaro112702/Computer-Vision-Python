# Import necessary modules
import cvzone.ColorModule
import cv2

# Create a ColorFinder object with a trackbar for adjusting color values
myColorFinder = cvzone.ColorModule.ColorFinder(trackBar=True)

# Open a video capture object for the default camera (index 0)
cap = cv2.VideoCapture(0)

# Set the width and height of the video capture frame
cap.set(3, 640)
cap.set(4, 480)

# Initial HSV color range values for detecting a specific color (orange)
hsvVals = {'hmin': 125, 'smin': 127, 'vmin': 0, 'hmax': 179, 'smax': 255, 'vmax':  139}

# Continuous loop for capturing and processing video frames
while True:
    # Read a frame from the video capture
    success, img = cap.read()

    # Update ColorFinder to find the specified color in the frame
    imgOrange, mask = myColorFinder.update(img, hsvVals)

    # Stack original image, processed image with detected color, and the color mask
    imgStack = cvzone.stackImages([img, imgOrange, mask], 3, 1)

    # Display the stacked images in a window named "Stacked Images"
    cv2.imshow("Stacked Images", imgStack)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
