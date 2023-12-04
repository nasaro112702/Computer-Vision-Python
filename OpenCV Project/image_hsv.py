# Import the OpenCV library
import cv2

# Specify the path of the image file
path = "Resources/lambo.jpg"

# Read the image from the specified path
img = cv2.imread(path)

# Convert the image from BGR color space to HSV color space
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Display the original image in a window titled "Original Image"
cv2.imshow("Original Image", img)

# Display the HSV (Hue, Saturation, Value) transformed image in a window titled "HSV Image"
cv2.imshow("HSV Image", imgHSV)

# Wait for a key event (0 means wait indefinitely until a key is pressed)
cv2.waitKey(0)
