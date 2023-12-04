# Import the OpenCV library
import cv2

# Import the NumPy library with alias np
import numpy as np

# Create a black image with dimensions 512x512 and 3 color channels (RGB)
img = np.zeros((512, 512, 3), np.uint8)

# Set the color of the entire image to blue (255, 0, 0 in BGR format)
img[:] = 255, 0, 0

# Display the image in a window titled "Image"
cv2.imshow("Image", img)

# Wait for a key event; 0 means wait indefinitely until a key is pressed
cv2.waitKey(0)
