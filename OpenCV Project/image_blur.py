# Import the OpenCV library
import cv2

# Read an image file ("my_profile.jpg") from the "Resources" folder
img = cv2.imread("Resources/my_profile.jpg")

# Apply a Gaussian blur to the image with a kernel size of (7, 7) and sigma=0
imgBlur = cv2.GaussianBlur(img, (7, 7), 0)

# Display the blurred image in a window titled "Blur Image"
cv2.imshow("Blur Image", imgBlur)

# Display the original image in a window titled "Original Image"
cv2.imshow("Original Image", img)

# Wait until a key is pressed to close the windows
cv2.waitKey(0)
