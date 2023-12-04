# Import necessary libraries
import cv2  # OpenCV library for computer vision
import numpy as np  # NumPy library for numerical operations

# Create a black image (all zeros) with a shape of 512x512 pixels and 3 color channels (RGB)
img = np.zeros((512, 512, 3), np.uint8)

# Change the color of a specific region in the image (from row 100 to 199, and column 200 to 299) to blue (255, 0, 0)
img[100:200, 200:300] = 255, 0, 0

# Display the modified image in a window with the title "Image"
cv2.imshow("Image", img)

# Wait for any key press to close the image window
cv2.waitKey(0)
