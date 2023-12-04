# Import the OpenCV library
import cv2

# Read an image file ("my_profile.jpg") from the "Resources" folder
img = cv2.imread("Resources/my_profile.jpg")

# Display the image in a window titled "Output"
cv2.imshow("Output", img)

# Wait for a key press (0 means wait indefinitely until a key is pressed)
cv2.waitKey(0)
