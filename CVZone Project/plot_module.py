from cvzone.PlotModule import LivePlot
from cvzone.FaceDetectionModule import FaceDetector
import cv2
import cvzone
import math

cap = cv2.VideoCapture(0)
detector = FaceDetector(minDetectionCon=0.85, modelSelection=0)

xPlot = LivePlot(w=1200, yLimit=[0, 500], interval=0.01, char='X')
sinPlot = LivePlot(w=1200, yLimit=[-100, 100], interval=0.01, char='S')
xSin = 0

while True:
    success, img = cap.read()

    img, bboxs = detector.findFaces(img, draw=False)
    val = 0

    if bboxs:
        for bbox in bboxs:
            center = bbox["center"]
            x, y, w, h = bbox['bbox']
            score = int(bbox['score'][0] * 100)
            val = center[0]

            cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)
            cvzone.putTextRect(img, f'{score}%', (x, y - 10))
            cvzone.cornerRect(img, (x, y, w, h))
    xSin += 1
    if xSin == 360: xSin = 0
    imgPlotSin = sinPlot.update(int(math.sin(math.radians(xSin)) * 100))
    imgPlot = xPlot.update(val)

    cv2.imshow("Image Plot", imgPlot)
    cv2.imshow("Image Sin Plot", imgPlotSin)

    cv2.imshow("Face Image", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break





