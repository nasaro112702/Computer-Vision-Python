# Import necessary libraries
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import cvzone.FPS

# Get audio devices and set up volume control
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
volRange = volume.GetVolumeRange()
minVol = volRange[0]
maxVol = volRange[1]

# Set up video capture and configure settings
fpsReader = cvzone.FPS.FPS(avgCount=30)
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# Initialize hand detector
detector = HandDetector(staticMode=False, maxHands=2, modelComplexity=1, detectionCon=0.75, minTrackCon=0.5)

# Initialize volume variables
vol = 0
volBar = 400
volPer  = 0

# Main loop
while True:
    # Read frame from the camera
    success, img = cap.read()

    # Update and display FPS
    fps, img = fpsReader.update(img)

    # Detect hands in the frame
    hands, img = detector.findHands(img, draw=True, flipType=True)

    if hands:
        hand = hands[0]
        lmList = hand['lmList']

        if len(lmList) != 0:
            # Calculate the distance between thumb and index finger
            length, info, img = detector.findDistance(lmList[8][0:2], lmList[4][0:2], img, color=(255, 0, 255),
                                                      scale=10)

            # Map the distance to volume values
            vol = np.interp(length, [50, 300], [minVol, maxVol])
            volBar = np.interp(length, [50, 300], [400, 150])
            volPer = np.interp(length, [50, 300], [0, 100])

            # Set the system volume
            volume.SetMasterVolumeLevel(vol, None)

            # Draw a filled circle if fingers are close
            if length < 50:
                cv2.circle(img, (info[4], info[5]), 10, (0, 0, 255), cv2.FILLED)

    # Draw volume control UI
    cv2.rectangle(img, (50, 150), (85, 400), (0, 255, 0), 3)
    cv2.rectangle(img, (50, int(volBar)), (85, 400), (0, 255, 0), cv2.FILLED)
    cv2.putText(img, f'{int(volPer)} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX,
                1, (0, 255, 0), 3)

    # Display the image
    cv2.imshow("Image", img)

    # Wait for a key event
    cv2.waitKey(1)