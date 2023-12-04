# Importing necessary libraries
import cv2           # OpenCV library for computer vision tasks
import numpy as np   # NumPy library for numerical operations

# Reading an image file
img = cv2.imread("Resources/my_profile.jpg")

# Creating a 5x5 kernel for image processing operations
kernel = np.ones((5, 5), np.uint8)

# Applying Canny edge detection to the image
imgCanny = cv2.Canny(img, 100, 200)

# Dilating the edges to make them thicker
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)

# Eroding the dilated image to refine the edges
imgEroded = cv2.erode(imgDilation, kernel, iterations=1)

# Displaying the processed images
cv2.imshow("Dilated Image", imgDilation)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Eroded Image", imgEroded)

# Waiting for a key press to close the image windows
cv2.waitKey(0)
