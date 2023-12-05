# Import necessary libraries
import cvzone
from cvzone.FaceDetectionModule import FaceDetector
import cv2

# Open the default camera (0) for capturing video
cap = cv2.VideoCapture(0)

# Create a face detector object with a minimum detection confidence of 50%
detector = FaceDetector(minDetectionCon=0.5, modelSelection=0)

# Infinite loop for continuously processing frames from the camera
while True:
    # Read a frame from the camera
    success, img = cap.read()

    # Use the face detector to find faces in the frame without drawing bounding boxes
    img, bboxs = detector.findFaces(img, draw=False)

    # If faces are detected, loop through each bounding box and process
    if bboxs:
        for bbox in bboxs:
            # Extract information from the bounding box
            center = bbox["center"]
            x, y, w, h = bbox['bbox']
            score = int(bbox['score'][0] * 100)

            # Draw a filled circle at the center of the face
            cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)

            # Display the confidence score above the face
            cvzone.putTextRect(img, f'{score}%', (x, y - 10))

            # Draw a rectangle around the face
            cvzone.cornerRect(img, (x, y, w, h))

    # Display the processed frame with detected faces
    cv2.imshow("Detected Faces", img)

    # Wait for a key press (1 millisecond delay between frames)
    cv2.waitKey(1)
