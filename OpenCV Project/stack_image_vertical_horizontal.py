# Importing required libraries
import cv2
import numpy as np

# Function to stack images horizontally or vertically
def stackImages(scale, imgArray):
    # Get the number of rows and columns in the image array
    rows = len(imgArray)
    cols = len(imgArray[0])
    # Check if images are available in rows
    rowsAvailable = isinstance(imgArray[0], list)
    # Get dimensions of individual images
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]

    # If images are available in rows
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                # Resize each image to a common size
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                                               None, scale, scale)
                # Convert grayscale images to BGR
                if len(imgArray[x][y].shape) == 2:
                    imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        # Create a blank image to use as a base
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        # Horizontally stack images in each row
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        # Vertically stack rows of images
        ver = np.vstack(hor)
    else:
        # If images are available in a single row
        for x in range(0, rows):
            # Resize each image to a common size
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            # Convert grayscale images to BGR
            if len(imgArray[x].shape) == 2:
                imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        # Horizontally stack images
        hor = np.hstack(imgArray)
        ver = hor

    # Return the final stacked image
    return ver


# Read an image from file
img = cv2.imread("Resources/cards.jpg")
# Create an image stack by repeating the same image
imgStack = stackImages(0.5, ([img, img, img], [img, img, img]))
# Display the stacked image
cv2.imshow("Stacked Image", imgStack)
# Wait for a key press
cv2.waitKey(0)
