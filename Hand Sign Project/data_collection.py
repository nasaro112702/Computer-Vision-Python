# Importing necessary libraries
import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import time

# Initializing webcam and hand detector
cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)

# Setting up parameters for image processing
offset = 20
imgSize = 300

# Folder to save captured images
folder = "Data/C"
counter = 0

# Infinite loop to capture and process video frames
while True:
    # Reading a frame from the webcam
    success, img = cap.read()

    # Detecting hands in the frame
    hands, img = detector.findHands(img)

    # If hands are detected
    if hands:
        # Extracting bounding box information for the first detected hand
        hand = hands[0]
        x, y, w, h = hand['bbox']

        # Creating a white image with specified size
        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255

        # Cropping the hand region from the frame
        imgCrop = img[y-offset:y+h+offset, x-offset: x+w+offset]

        # Calculating aspect ratio of the hand
        aspectRatio = h / w

        # Resizing and centering the cropped hand image based on aspect ratio
        if aspectRatio > 1:
            k = imgSize/h
            wCal = math.ceil(k*w)
            imgResize = cv2.resize(imgCrop, (wCal, imgSize))
            imgResizeShape = imgResize.shape
            wGap = math.ceil((imgSize - wCal)/2)
            imgWhite[:, wGap:wCal+wGap] = imgResize
        else:
            k = imgSize / w
            hCal = math.ceil(k * h)
            imgResize = cv2.resize(imgCrop, (imgSize, hCal))
            imgResizeShape = imgResize.shape
            hGap = math.ceil((imgSize - hCal) / 2)
            imgWhite[hGap:hCal + hGap, :] = imgResize

        # Displaying cropped and resized hand image
        cv2.imshow("ImageCrop", imgCrop)
        # Displaying white image with centered hand
        cv2.imshow("ImageWhite", imgWhite)

    # Displaying the original frame with hand bounding box
    cv2.imshow("Result", img)

    # Checking for the 's' key press to save the processed image
    key = cv2.waitKey(1)
    if key == ord("s"):
        # Incrementing counter and saving the image with a timestamp
        counter += 1
        cv2.imwrite(f'{folder}/Image_{time.time()}.jpg', imgWhite)
        print(counter)
