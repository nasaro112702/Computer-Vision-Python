# Import necessary libraries
import cv2  # OpenCV library for computer vision
import numpy as np  # NumPy library for numerical operations

# Create a black image with dimensions 512x512 and 3 color channels (RGB)
img = np.zeros((512, 512, 3), np.uint8)

# Draw a circle on the image at coordinates (400, 50) with radius 30,
# color (255, 255, 255) in RGB (white), and thickness 5 pixels
cv2.circle(img, (400, 50), 30, (255, 255, 255), 5)

# Display the image in a window titled "Image"
cv2.imshow("Image", img)

# Wait for a key press before closing the window
cv2.waitKey(0)