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
folder = "Data/MiddleFinger"
counter = 0

# Infinite loop to capture and process video frames
while True:
    # Reading a frame from the webcam
    success, img = cap.read()

    # Detecting hands in the frame
    hands, img = detector.findHands(img)

    # If hands are detected
    if hands:
        # Take the first detected hand
        hand = hands[0]
        x, y, w, h = hand['bbox']

        # Create a white image for cropping and resizing
        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255

        # Crop and resize the hand region based on aspect ratio
        aspectRatio = h / w

        try:
            if aspectRatio > 1:
                # Resize based on height
                k = imgSize / h
                wCal = math.ceil(k * w)
                imgResize = cv2.resize(img[y - offset:y + h + offset, x - offset: x + w + offset], (wCal, imgSize))
                imgResizeShape = imgResize.shape
                wGap = math.ceil((imgSize - wCal) / 2)
                imgWhite[:, wGap:wCal + wGap] = imgResize
            else:
                # Resize based on width
                k = imgSize / w
                hCal = math.ceil(k * h)
                imgResize = cv2.resize(img[y - offset:y + h + offset, x - offset: x + w + offset], (imgSize, hCal))
                imgResizeShape = imgResize.shape
                hGap = math.ceil((imgSize - hCal) / 2)
                imgWhite[hGap:hCal + hGap, :] = imgResize

            # Display cropped and resized images
            cv2.imshow("ImageCrop", imgResize)
            cv2.imshow("ImageWhite", imgWhite)
        except:
            pass



    # Displaying the original frame with hand bounding box
    cv2.imshow("Result", img)

    # Checking for the 's' key press to save the processed image
    key = cv2.waitKey(1)
    if key == ord("s"):
        # Incrementing counter and saving the image with a timestamp
        counter += 1
        cv2.imwrite(f'{folder}/Image_{time.time()}.jpg', imgWhite)
        print(counter)
