# Import necessary libraries
import cv2
import numpy as np

# Function to stack images horizontally or vertically
def stackImages(scale, imgArray):
    # Get the number of rows and columns in the image array
    rows = len(imgArray)
    cols = len(imgArray[0])
    # Check if the images are stacked vertically or horizontally
    rowsAvailable = isinstance(imgArray[0], list)
    # Get the width and height of the images
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]

    # If images are stacked vertically
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                # Resize images to the same dimensions
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                # Convert grayscale images to BGR
                if len(imgArray[x][y].shape) == 2:
                    imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        # Create a blank image
        imageBlank = np.zeros((height, width, 3), np.uint8)
        # Stack images horizontally
        hor = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        # Stack images vertically
        ver = np.vstack(hor)
    # If images are stacked horizontally
    else:
        for x in range(0, rows):
            # Resize images to the same dimensions
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            # Convert grayscale images to BGR
            if len(imgArray[x].shape) == 2:
                imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        # Stack images horizontally
        hor = np.hstack(imgArray)
        ver = hor
    return ver

# Function to get contours in the image
def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area > 500:
            # Draw contours on the image
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            print(peri)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            print(len(approx))
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)

            # Determine the type of object based on the number of corners
            if objCor == 3:
                objectType = "Tri"
            elif objCor == 4:
                aspRatio = w / float(h)
                if aspRatio > 0.98 and aspRatio < 1.02:
                    objectType = "Square"
                else:
                    objectType = "Rectangle"
            elif objCor > 4:
                objectType = "Circles"
            else:
                objectType = "None"

            # Draw a rectangle around the object and label it
            cv2.rectangle(imgContour, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(imgContour, objectType,
                        (x+(w//2)-10, y+(h//2)-10), cv2.FONT_HERSHEY_COMPLEX, 0.5,
                        (0, 0, 0), 2)

# Path to the image file
path = 'Resources/shapes.png'
# Read the image
img = cv2.imread(path)
imgContour = img.copy()
# Convert the image to grayscale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Apply Gaussian blur to the image
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
# Apply Canny edge detection
imgCanny = cv2.Canny(imgBlur, 50, 50)
# Create a blank image
imgBlank = np.zeros_like(img)
# Find and draw contours on the image
getContours(imgCanny)
# Stack different stages of image processing for display
imgStack = stackImages(0.8, ([img, imgGray, imgBlur],
                             [imgCanny, imgContour, imgBlank]))
# Display the stacked image
cv2.imshow("Stacked Image", imgStack)
cv2.waitKey(0)
