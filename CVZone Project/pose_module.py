# Import necessary libraries
from cvzone.PoseModule import PoseDetector
import cv2

# Initialize webcam
cap = cv2.VideoCapture(0)

# Create a PoseDetector object with specified parameters
detector = PoseDetector(staticMode=False,
                        modelComplexity=1,
                        smoothLandmarks=True,
                        enableSegmentation=False,
                        smoothSegmentation=True,
                        detectionCon=0.5,
                        trackCon=0.5)

# Main loop for real-time processing
while True:
    # Read a frame from the webcam
    success, img = cap.read()

    # Detect pose in the frame
    img = detector.findPose(img)

    # Find landmarks and bounding box information
    lmList, bboxInfo = detector.findPosition(img, draw=True, bboxWithHands=False)

    # If landmarks are detected
    if lmList:
        # Highlight the center of the bounding box with a circle
        center = bboxInfo["center"]
        cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)

        # Find and display the distance between specific landmarks
        length, img, info = detector.findDistance(lmList[11][0:2],
                                                  lmList[15][0:2],
                                                  img=img,
                                                  color=(255, 0, 0),
                                                  scale=10)

        # Find and display the angle formed by three specific landmarks
        angle, img = detector.findAngle(lmList[11][0:2],
                                        lmList[13][0:2],
                                        lmList[15][0:2],
                                        img=img,
                                        color=(0, 0, 255),
                                        scale=10)

        # Check if the angle is close to 50 degrees with a tolerance of 10 degrees
        isCloseAngle50 = detector.angleCheck(myAngle=angle,
                                             targetAngle=50,
                                             offset=10)

        # Print whether the angle is close to 50 degrees
        print(isCloseAngle50)

    # Display the processed image with pose information
    cv2.imshow("Pose Image", img)

    # Wait for a key event to exit the loop
    cv2.waitKey(1)
