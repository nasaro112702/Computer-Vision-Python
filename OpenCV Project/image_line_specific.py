# Import the OpenCV library and NumPy
import cv2
import numpy as np

# Create a black image (all zeros) with dimensions 512x512 and 3 color channels (RGB)
img = np.zeros((512, 512, 3), np.uint8)

# Draw a green line on the image from point (0,0) to (300,300) with a thickness of 3 pixels
cv2.line(img, (0,0), (300, 300), (0, 255, 0), 3)

# Display the image in a window titled "Image"
cv2.imshow("Image", img)

# Wait for a key press to close the window
cv2.waitKey(0)
