# Import necessary libraries
from cvzone.HandTrackingModule import HandDetector
import cv2

# Open the video capture (webcam in this case)
cap = cv2.VideoCapture(0)

# Initialize HandDetector with specific settings
detector = HandDetector(staticMode=False, maxHands=2, modelComplexity=1, detectionCon=0.5, minTrackCon=0.5)

# Main loop for capturing and processing video frames
while True:
    # Read a frame from the video capture
    success, img = cap.read()

    # Detect hands in the frame and draw them
    hands, img = detector.findHands(img, draw=True, flipType=True)

    # If hands are detected
    if hands:
        # Process the first detected hand
        hand1 = hands[0]
        lmList1 = hand1['lmList']
        bbox1 = hand1["bbox"]
        center1 = hand1['center']
        handType1 = hand1["type"]

        # Count and print the number of fingers up for the first hand
        fingers1 = detector.fingersUp(hand1)
        print(f'H1 = {fingers1.count(1)}', end=" ")

        # Get the positions of the index and middle fingers for the first hand
        tipOfIndexFinger1 = lmList1[8][0:2]
        tipOfMiddleFinger1 = lmList1[12][0:2]

        # Find and print the distance between the index and middle fingers for the first hand
        length, info, img = detector.findDistance(tipOfIndexFinger1, tipOfMiddleFinger1, img, color=(255, 0, 255), scale=10)

        # If there are two hands detected
        if len(hands) == 2:
            # Process the second detected hand
            hand2 = hands[1]
            lmList2 = hand2["lmList"]
            bbox2 = hand2["bbox"]
            center2 = hand2['center']
            handType2 = hand2["type"]

            # Count and print the number of fingers up for the second hand
            fingers2 = detector.fingersUp(hand2)
            print(f'H2 = {fingers2.count(1)}', end=" ")

            # Get the position of the index finger for the second hand
            tipOfIndexFinger2 = lmList2[8][0:2]

            # Find and print the distance between the index fingers of both hands
            length, info, img = detector.findDistance(tipOfIndexFinger1, tipOfIndexFinger2, img, color=(255, 0, 0), scale=10)

        print(" ")

    # Display the frame with detected hands
    cv2.imshow("Detected Hands", img)

    # Wait for a key press
    cv2.waitKey(1)
