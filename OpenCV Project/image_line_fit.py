# Import necessary libraries
import cv2  # OpenCV library for computer vision
import numpy as np  # NumPy library for numerical operations

# Create a black image (all zeros) with dimensions 512x512 and 3 color channels (RGB)
img = np.zeros((512, 512, 3), np.uint8)

# Draw a green line on the image from top-left corner to bottom-right corner
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)

# Display the image with the drawn line
cv2.imshow("Image", img)

# Wait for a key press to close the image window
cv2.waitKey(0)
