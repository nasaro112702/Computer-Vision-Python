# Import the OpenCV library
import cv2

# Load the pre-trained face cascade classifier
faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")

# Read an image from file
img = cv2.imread('Resources/face.jpg')

# Convert the image to grayscale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces in the grayscale image using the cascade classifier
faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

# Draw rectangles around the detected faces on the original color image
for (x, y, w ,h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Display the image with detected faces
cv2.imshow("Detected Face", img)

# Wait for a key press to close the image window
cv2.waitKey(0)
