# Import OpenCV library and NumPy
import cv2
import numpy as np

# Create a black image (all zeros) with dimensions 512x512 and 3 color channels (RGB)
img = np.zeros((512, 512, 3), np.uint8)

# Put text "OPENCV" on the image at position (300, 200) using a complex font style,
# with a scale factor of 1, color (0, 150, 0) in BGR format (green), and thickness of 1 pixel
cv2.putText(img, " OPENCV ", (300, 200), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 1)

# Display the image in a window titled "Image"
cv2.imshow("Image", img)

# Wait for any key press to exit the program
cv2.waitKey(0)
