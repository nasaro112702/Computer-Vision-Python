# Import required libraries
import cv2
import numpy as np


# Define a function to stack multiple images horizontally or vertically
def stackImages(scale, imgArray):
    # Get the number of rows and columns in the image array
    rows = len(imgArray)
    cols = len(imgArray[0])

    # Check if the first element in the image array is a list (rows available)
    rowsAvailable = isinstance(imgArray[0], list)

    # Get the width and height of each image in the array
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]

    # Resize images to a specified scale and convert grayscale images to BGR if needed
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                                                None, scale, scale)
                if len(imgArray[x][y].shape) == 2:
                    imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)

        # Create a blank image and horizontally stack the images
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])

        # Vertically stack the horizontally stacked images
        ver = np.vstack(hor)
    else:
        # Resize images in a single row and convert grayscale images to BGR if needed
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2:
                imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)

        # Horizontally stack the images
        hor = np.hstack(imgArray)
        ver = hor

    return ver


# Read an image from file
img = cv2.imread("Resources/cards.jpg")

# Convert the image to grayscale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)

# Stack the original image, grayscale image, and a repeated version of the original image
imgStack = stackImages(0.5, ([img, imgGray, img], [img, img, img]))

# Display the stacked image
cv2.imshow("Stacked Image", imgStack)

# Wait for a key press and then close the window
cv2.waitKey(0)
