# Import the OpenCV library
import cv2
import cvzone

# Create a VideoCapture object to access the default camera (camera index 0)
cap = cv2.VideoCapture(0)

# Infinite loop to continuously capture frames from the camera
while True:
    # Read a frame from the camera, 'success' indicates if the frame is captured successfully
    success, img = cap.read()

    # Convert the color of the image to grayscale
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Resize the image to 10% of its original size
    imgSmall = cv2.resize(img, (0, 0), None, 0.1, 0.1)

    # Resize the image to 3 times its original size
    imgBig = cv2.resize(img, (0, 0), None, 3, 3)

    # Apply Canny edge detection to the grayscale image
    imgCanny = cv2.Canny(imgGray, 50, 150)

    # Convert the color of the image to HSV
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Create a list of images for display
    imgList = [img, imgGray, imgCanny, imgSmall, imgBig, imgHSV]

    # Stack the images horizontally with a 3-pixel gap and a scale factor of 0.7
    stackImages = cvzone.stackImages(imgList, 3, 0.7)

    # Display the stacked images in a window titled "Stacked Images"
    cv2.imshow("Stacked Images", stackImages)

    # Wait for a key press for 1 millisecond (cv2.waitKey(1)) and continue the loop
    cv2.waitKey(1)
