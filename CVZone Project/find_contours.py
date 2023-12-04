# Import necessary libraries
import cv2  # OpenCV for image processing
import cvzone  # cvzone for additional computer vision functions
import numpy as np  # NumPy for numerical operations

# Read an image of shapes
imgShapes = cv2.imread("Resources/shapes.png")

# Apply Canny edge detection to the image
imgCanny = cv2.Canny(imgShapes, 50, 150)

# Dilate the edges to make contours more visible
imgDilated = cv2.dilate(imgCanny, np.ones((5, 5), np.uint8), iterations=1)

# Find contours in the original image based on the dilated edges
imgContours, conFound = cvzone.findContours(imgShapes, imgDilated)

# Display the original image with detected contours
cv2.imshow("Image with Contour", imgContours)

# Wait for a key press to close the image window
cv2.waitKey(0)
