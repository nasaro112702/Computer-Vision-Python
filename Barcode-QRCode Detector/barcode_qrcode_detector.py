# Import necessary libraries
import cv2  # OpenCV library for computer vision
import numpy as np  # NumPy library for numerical operations
from pyzbar.pyzbar import decode  # pyzbar library for decoding barcodes

# Open a connection to the default camera (camera index 0)
cap = cv2.VideoCapture(0)

# Set the width and height of the video capture
cap.set(3, 640)
cap.set(4, 480)

# Infinite loop for continuous video capture and processing
while True:
    # Read a frame from the video capture
    success, img = cap.read()

    # Decode barcodes in the captured frame
    codes = decode(img)

    # Iterate through each detected barcode
    for barcode in codes:
        # Extract data from the barcode
        myData = barcode.data.decode('utf-8')

        # Get the polygon points of the barcode and reshape them
        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))

        # Draw a polygon around the barcode on the image
        cv2.polylines(img, [pts], True, (255, 0, 255), 5)

        # Get the rectangle points around the barcode
        pts2 = barcode.rect

        # Put the decoded data as text near the barcode on the image
        cv2.putText(img, myData, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255), 2)

    # Display the result (image with drawn polygons and text) in a window
    cv2.imshow('Result', img)

    # Wait for a key event for 1 millisecond (allows the window to be closed)
    cv2.waitKey(1)
