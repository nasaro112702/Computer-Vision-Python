# Importing necessary libraries
import cv2
import numpy as np


# Function to find contours in an image
def getContours(img, cThr=[100, 100], showCanny=False, minArea=1000, filter=0, draw=False):
    # Convert image to grayscale
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Apply Gaussian blur to the grayscale image
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)
    # Use Canny edge detection on the blurred image
    imgCanny = cv2.Canny(imgBlur, cThr[0], cThr[1])

    # Apply dilation and erosion to the Canny image
    kernel = np.ones((5, 5))
    imgDilate = cv2.dilate(imgCanny, kernel, iterations=3)
    imgThre = cv2.erode(imgDilate, kernel, iterations=2)

    # Optionally, show the Canny image
    if showCanny:
        cv2.imshow('Canny', imgThre)

    # Find contours in the thresholded image
    contours, hierarchy = cv2.findContours(imgThre, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Initialize a list to store final contours based on certain conditions
    finalContours = []

    # Iterate through each contour
    for i in contours:
        # Calculate the area of the contour
        area = cv2.contourArea(i)
        # Check if the area is above a specified minimum threshold
        if area > minArea:
            # Approximate the contour to a polygon
            peri = cv2.arcLength(i, True)
            approx = cv2.approxPolyDP(i, 0.02 * peri, True)
            # Get the bounding box around the polygon
            bbox = cv2.boundingRect(approx)

            # Optionally, filter contours based on the number of vertices
            if filter > 0:
                if len(approx) == filter:
                    finalContours.append([len(approx), area, approx, bbox, i])
            else:
                finalContours.append([len(approx), area, approx, bbox, i])

    # Sort the final contours based on area in descending order
    finalContours = sorted(finalContours, key=lambda x: x[1], reverse=True)

    # Optionally, draw the final contours on the original image
    if draw:
        for con in finalContours:
            cv2.drawContours(img, con[4], -1, (0, 0, 255), 3)

    # Return the modified image and the final contours list
    return img, finalContours


# Function to reorder points in a list to form a rectangle
def reorder(myPoints):
    myPointsNew = np.zeros_like(myPoints)
    myPoints = myPoints.reshape((4, 2))
    add = myPoints.sum(1)
    myPointsNew[0] = myPoints[np.argmin(add)]
    myPointsNew[3] = myPoints[np.argmax(add)]
    diff = np.diff(myPoints, axis=1)
    myPointsNew[1] = myPoints[np.argmin(diff)]
    myPointsNew[2] = myPoints[np.argmax(diff)]

    return myPointsNew


# Function to warp an image based on four points
def warpIMG(img, points, w, h, pad=20):
    # Reorder the points to form a rectangle
    points = reorder(points)
    # Define the target points for perspective transformation
    pts1 = np.float32(points)
    pts2 = np.float32([[0, 0], [w, 0], [0, h], [w, h]])
    # Compute the perspective transformation matrix
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    # Apply the perspective transformation to the image
    imgWarp = cv2.warpPerspective(img, matrix, (w, h))
    # Crop the warped image to remove padding
    imgWarp = imgWarp[pad:imgWarp.shape[0] - pad, pad:imgWarp.shape[1] - pad]

    return imgWarp


# Function to calculate Euclidean distance between two points
def findDistance(pts1, pts2):
    return ((pts2[0] - pts1[0]) ** 2 + (pts2[1] - pts1[1]) ** 2) ** 0.5
