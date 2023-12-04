# Import the OpenCV library
import cv2

# Read an image file ("my_profile.jpg") and store it in the variable 'img'
img = cv2.imread("Resources/my_profile.jpg")

# Print the shape (dimensions) of the original image
print(img.shape)

# Resize the image to a new width and height (560, 549) and store it in 'imgResize'
imgResize = cv2.resize(img, (560, 549))

# Print the shape of the resized image
print(imgResize.shape)

# Display the original image in a window titled "Original Image"
cv2.imshow("Original Image", img)

# Display the resized image in a window titled "Resized Image"
cv2.imshow("Resized Image", imgResize)

# Wait for any key press to close the image windows
cv2.waitKey(0)
