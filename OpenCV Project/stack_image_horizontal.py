# Import the OpenCV library for computer vision tasks
import cv2
# Import the NumPy library for numerical operations
import numpy as np

# Read an image file named "cards.jpg" and store it in the variable 'img'
img = cv2.imread("Resources/cards.jpg")

# Create a horizontally stacked image by concatenating the original image with itself
imgHor = np.hstack((img, img))

# Display the horizontally stacked image with the title "Horizontal Image"
cv2.imshow("Horizontal Image", imgHor)

# Wait for a key press before closing the image window
cv2.waitKey(0)
