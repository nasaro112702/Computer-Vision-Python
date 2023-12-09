# Importing necessary modules
from cvzone.FaceMeshModule import FaceMeshDetector
from cvzone.HandTrackingModule import HandDetector
from cvzone.PoseModule import PoseDetector
import cvzone
import cv2

# Accessing the default camera (index 0)
cap = cv2.VideoCapture(0)

# Creating a FaceMeshDetector object with specified settings
face_detector = FaceMeshDetector(staticMode=False, maxFaces=2, minDetectionCon=0.5, minTrackCon=0.5)

# Initialize HandDetector with specific settings
hand_detector = HandDetector(staticMode=False, maxHands=2, modelComplexity=1, detectionCon=0.5, minTrackCon=0.5)

# Create a PoseDetector object with specified parameters
pose_detector = PoseDetector(staticMode=False,
                        modelComplexity=1,
                        smoothLandmarks=True,
                        enableSegmentation=False,
                        smoothSegmentation=True,
                        detectionCon=0.5,
                        trackCon=0.5)

# Running an infinite loop for continuous video capture and face mesh detection
while True:
    # Reading a frame from the camera
    success, img = cap.read()

    imgNoDraw = img.copy()

    # Detect pose in the frame
    img = pose_detector.findPose(img)

    # Find landmarks and bounding box information
    lmList, bboxInfo = pose_detector.findPosition(img, draw=True, bboxWithHands=False)

    imgPoseOnly = img.copy()

    # Detecting face meshes in the current frame and drawing them
    img, faces = face_detector.findFaceMesh(img, draw=True)

    imgPoseAndFaceOnly = img.copy()

    # Detect hands in the frame and draw them
    hands, img = hand_detector.findHands(img, draw=True, flipType=True)

    # Create a list of images for display
    imgList = [imgNoDraw, imgPoseOnly, imgPoseAndFaceOnly, img]
    stackColumns = 2

    # Stack the images horizontally with a 3-pixel gap and a scale factor of 0.7
    stackImages = cvzone.stackImages(imgList, stackColumns, 0.7)

    cv2.imshow("Result", stackImages)

    # Waiting for a key press to exit the loop
    cv2.waitKey(1)
