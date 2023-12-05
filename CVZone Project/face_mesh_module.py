# Importing necessary modules
from cvzone.FaceMeshModule import FaceMeshDetector
import cv2

# Accessing the default camera (index 0)
cap = cv2.VideoCapture(0)

# Creating a FaceMeshDetector object with specified settings
detector = FaceMeshDetector(staticMode=False, maxFaces=2, minDetectionCon=0.5, minTrackCon=0.5)

# Running an infinite loop for continuous video capture and face mesh detection
while True:
    # Reading a frame from the camera
    success, img = cap.read()

    # Detecting face meshes in the current frame and drawing them
    img, faces = detector.findFaceMesh(img, draw=True)

    # Checking if any faces are detected
    if faces:
        # Looping through each detected face
        for face in faces:
            # Extracting key points for the left eye
            leftEyeUpPoint = face[159]
            leftEyeDownPoint = face[23]

            # Calculating the vertical distance between upper and lower points of the left eye
            leftEyeVerticalDistance, info = detector.findDistance(leftEyeUpPoint, leftEyeDownPoint)

            # Printing the calculated vertical distance of the left eye
            print(leftEyeVerticalDistance)

    # Displaying the frame with the detected face meshes
    cv2.imshow("Detected Mesh", img)

    # Waiting for a key press to exit the loop
    cv2.waitKey(1)
