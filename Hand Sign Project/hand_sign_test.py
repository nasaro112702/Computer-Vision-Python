# Import necessary libraries
import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math

# Initialize video capture from default camera (0)
cap = cv2.VideoCapture(0)

# Initialize HandDetector to detect hand in the frame
detector = HandDetector(maxHands=1)

# Initialize Classifier with a trained model and labels
classifier = Classifier("Model/keras_model.h5", "Model/labels.txt")

# Set offset and image size for cropping and resizing
offset = 20
imgSize = 300

# Labels for classification
labels = ["A", "B", "C"]

# Main loop for processing video frames
while True:
    # Read a frame from the video capture
    success, img = cap.read()
    imgOutput = img.copy()

    # Detect hands in the frame
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
                prediction, index = classifier.getPrediction(imgWhite, draw=False)
                print(prediction, index)
            else:
                # Resize based on width
                k = imgSize / w
                hCal = math.ceil(k * h)
                imgResize = cv2.resize(img[y - offset:y + h + offset, x - offset: x + w + offset], (imgSize, hCal))
                imgResizeShape = imgResize.shape
                hGap = math.ceil((imgSize - hCal) / 2)
                imgWhite[hGap:hCal + hGap, :] = imgResize
                prediction, index = classifier.getPrediction(imgWhite, draw=False)
                print(prediction, index)

            cvzone.cornerRect(imgOutput, (x, y, w, h), l=30, t=5, rt=1,
                              colorR=(255, 0, 255), colorC=(255, 0, 255))

            cvzone.putTextRect(imgOutput, labels[index], (x + 5, y - 15), scale=1, thickness=1, colorT=(255, 255, 255),
                               colorR=(255, 0, 255), font=cv2.FONT_HERSHEY_COMPLEX,
                               offset=10, border=None, colorB=(0, 255, 0))
            cv2.imshow("ImageWhite", imgWhite)
        except:
            pass




        # # Display cropped and resized images
        # cv2.imshow("ImageCrop", imgResize)
        cv2.imshow("ImageWhite", imgWhite)

    # Display the result image
    cv2.imshow("Result", imgOutput)
    cv2.waitKey(1)
