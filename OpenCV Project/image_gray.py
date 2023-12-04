# Import the OpenCV library
import cv2

# Read an image file named "my_profile.jpg" from the "Resources" folder
img = cv2.imread("Resources/my_profile.jpg")

# Convert the colored image to grayscale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Display the grayscale image in a window titled "Gray Image"
cv2.imshow("Gray Image", imgGray)

# Display the original colored image in a window titled "Original Image"
cv2.imshow("Original Image", img)

# Wait for any key press to close the open windows
cv2.waitKey(0)
