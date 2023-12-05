# Import the OpenCV library
import cv2
import cvzone
import numpy as np
import math
from cvzone.ClassificationModule import Classifier

# Load the pre-trained face cascade classifier
faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")

# Create a VideoCapture object to access the default camera (camera index 0)
cap = cv2.VideoCapture(0)

# Initialize Classifier with a trained model and labels
classifier = Classifier("Model/keras_model.h5", "Model/labels.txt")

# Initialize an empty array to store labels
labels = []

# Open the file in read mode
with open('Model/labels.txt', 'r') as file:
    # Extract names from each line and append to the array
    labels = [line.split(maxsplit=1)[1].strip() for line in file]

# Infinite loop to continuously capture frames from the camera
while True:
    # Read a frame from the camera, 'success' indicates if the frame is captured successfully
    success, img = cap.read()

    # Convert the image to grayscale
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale image using the cascade classifier
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

    offset = 20
    imgSize = 300

    # Draw rectangles around the detected faces on the original color image
    for (x, y, w, h) in faces:

        # Creating a white image with specified size
        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255

        # Cropping the face region from the frame
        imgCrop = img[y - offset:y + h + offset, x - offset: x + w + offset]

        # Calculating aspect ratio of the hand
        aspectRatio = h / w

        try:
            # Resizing and centering the cropped face image based on aspect ratio
            if aspectRatio > 1:
                k = imgSize / h
                wCal = math.ceil(k * w)
                imgResize = cv2.resize(imgCrop, (wCal, imgSize))
                imgResizeShape = imgResize.shape
                wGap = math.ceil((imgSize - wCal) / 2)
                imgWhite[:, wGap:wCal + wGap] = imgResize
                prediction, index = classifier.getPrediction(imgWhite, draw=False)
                print(prediction, index)
            else:
                k = imgSize / w
                hCal = math.ceil(k * h)
                imgResize = cv2.resize(imgCrop, (imgSize, hCal))
                imgResizeShape = imgResize.shape
                hGap = math.ceil((imgSize - hCal) / 2)
                imgWhite[hGap:hCal + hGap, :] = imgResize
                prediction, index = classifier.getPrediction(imgWhite, draw=False)
                print(prediction, index)
        except:
            pass


        cvzone.cornerRect(img, (x, y, w, h), l=30, t=5, rt=1,
                          colorR=(255, 0, 255), colorC=(255, 0, 255))

        cvzone.putTextRect(img, labels[index], (x + 5, y - 15), scale=1, thickness=1, colorT=(255, 255, 255),
                           colorR=(255, 0, 255), font=cv2.FONT_HERSHEY_COMPLEX,
                           offset=10, border=None, colorB=(0, 255, 0))

        # # Displaying cropped and resized face image
        # cv2.imshow("ImageCrop", imgCrop)
        # # Displaying white image with centered face
        # cv2.imshow("ImageWhite", imgWhite)

    # Display the image with detected faces
    cv2.imshow("Detected Face", img)

    cv2.waitKey(1)