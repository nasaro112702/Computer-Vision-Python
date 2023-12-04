# Import the OpenCV library
import cv2

# Read an image file ("my_profile.jpg") from the "Resources" folder
img = cv2.imread("Resources/my_profile.jpg")

# Crop the image by selecting a region of interest (ROI) from coordinates [0:200, 200:500]
imgCrop = img[0:200, 200:500]

# Display the original image in a window titled "Original Image"
cv2.imshow("Original Image", img)

# Display the cropped image in a window titled "Cropped Image"
cv2.imshow("Cropped Image", imgCrop)

# Wait for a key press to close the image windows
cv2.waitKey(0)
