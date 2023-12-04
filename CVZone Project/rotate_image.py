# Import the OpenCV and cvzone libraries
import cv2
import cvzone

# Create a VideoCapture object to access the default camera (camera index 0)
cap = cv2.VideoCapture(0)

# Infinite loop to continuously capture frames from the camera
while True:
    # Read a frame from the camera, 'success' indicates if the frame is captured successfully
    success, img = cap.read()

    # Rotate the captured frame by 60 degrees without keeping the original size
    imgRotated60 = cvzone.rotateImage(img, 60, scale=1, keepSize=False)

    # Rotate the captured frame by 60 degrees and keep the original size
    imgRotated60KeepSize = cvzone.rotateImage(img, 60, scale=1, keepSize=True)

    # Display the original image in a window titled "Original Image"
    cv2.imshow("Original Image", img)

    # Display the image rotated by 60 degrees without keeping the original size
    cv2.imshow("imgRotated60 Image", imgRotated60)

    # Display the image rotated by 60 degrees and keeping the original size
    cv2.imshow("imgRotated60KeepSize Image", imgRotated60KeepSize)

    # Wait for a key press for 1 millisecond (cv2.waitKey(1)) and continue the loop
    cv2.waitKey(1)
