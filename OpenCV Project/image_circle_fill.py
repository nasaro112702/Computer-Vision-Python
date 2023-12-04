# Import the OpenCV library and NumPy
import cv2 
import numpy as np 

# Create a black image (all zeros) with dimensions 512x512 and 3 channels (RGB)
img = np.zeros((512, 512, 3), np.uint8)

# Draw a filled white circle on the black image at coordinates (400, 50) with a radius of 30 pixels
cv2.circle(img, (400, 50), 30, (255, 255, 255), cv2.FILLED)

# Display the image in a window titled "Image"
cv2.imshow("Image", img)

# Wait for a key press before closing the window
cv2.waitKey(0)
