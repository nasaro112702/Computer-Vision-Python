# Import the OpenCV library
import cv2

# Read the image file "my_profile.jpg" from the "Resources" folder
img = cv2.imread("Resources/my_profile.jpg")

# Apply the Canny edge detection algorithm to the image
# with threshold values of 100 and 200
imgCanny = cv2.Canny(img, 100, 200)

# Display the Canny edge-detected image in a window titled "Canny Image"
cv2.imshow("Canny Image", imgCanny)

# Display the original image in a window titled "Original Image"
cv2.imshow("Original Image", img)

# Wait until a key is pressed before closing the image windows
cv2.waitKey(0)