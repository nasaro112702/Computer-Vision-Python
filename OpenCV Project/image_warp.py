# Import necessary libraries
import cv2
import numpy as np

# Read the input image
img = cv2.imread("Resources/cards.jpg")

# Define the width and height of the output image
width, height = 250, 350

# Define four points in the input image (pts1) and corresponding points in the output image (pts2)
pts1 = np.float32([[111, 219], [287, 188], [154, 482], [352, 440]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

# Compute the perspective transformation matrix using the specified points
matrix = cv2.getPerspectiveTransform(pts1, pts2)

# Apply the perspective transformation to the input image
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

# Display the original and warped images
cv2.imshow("Original Image", img)
cv2.imshow("Warped Image", imgOutput)

# Wait for a key press and then close the windows
cv2.waitKey(0)
