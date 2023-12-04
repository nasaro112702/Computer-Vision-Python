# Importing necessary libraries
import cv2        # OpenCV library for computer vision tasks
import numpy as np # NumPy library for numerical operations in Python

# Creating a black image with dimensions 512x512 and 3 channels (RGB) using NumPy
img = np.zeros((512, 512, 3), np.uint8)

# Drawing a filled red rectangle on the black image from (0,0) to (250,350)
cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), cv2.FILLED)

# Displaying the image in a window named "Image"
cv2.imshow("Image", img)

# Waiting for a key press to close the window
cv2.waitKey(0)
