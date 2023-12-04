# Import necessary libraries
import cv2  # OpenCV library for computer vision
import numpy as np  # NumPy library for numerical operations

# Create a black image (all zeros) with a shape of (512, 512, 3) and data type uint8
img = np.zeros((512, 512, 3), np.uint8)

# Draw a red rectangle on the image from point (0, 0) to (250, 350) with a thickness of 2
cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), 2)

# Display the image with the rectangle
cv2.imshow("Image", img)

# Wait for a key press to close the image window
cv2.waitKey(0)
