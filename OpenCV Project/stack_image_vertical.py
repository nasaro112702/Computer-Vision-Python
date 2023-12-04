# Import necessary libraries
import cv2  # OpenCV library for computer vision
import numpy as np  # NumPy library for numerical operations

# Read an image from file
img = cv2.imread("Resources/cards.jpg")

# Stack the image vertically by duplicating it and stacking the copies
imgVer = np.vstack((img, img))

# Display the vertically stacked image
cv2.imshow("Vertical Image", imgVer)

# Wait for a key press to close the image window
cv2.waitKey(0)
