# Importing necessary libraries
import cv2  # OpenCV library for computer vision
import numpy as np  # NumPy library for numerical operations

# Reading an image file
img = cv2.imread("Resources/my_profile.jpg")

# Creating a 5x5 kernel of ones with data type uint8
kernel = np.ones((5, 5), np.uint8)

# Applying Canny edge detection to the input image
imgCanny = cv2.Canny(img, 100, 200)

# Dilating the edges in the image using the specified kernel
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)

# Displaying the dilated and Canny-edged images
cv2.imshow("Dilated Image", imgDilation)
cv2.imshow("Canny Image", imgCanny)

# Waiting for a key press to close the displayed images
cv2.waitKey(0)
