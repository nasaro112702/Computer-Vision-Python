# Import the OpenCV library
import cv2

# Create a video capture object (0 represents the default camera)
cap = cv2.VideoCapture(0)

# Set the width of the capture frame to 640 pixels
cap.set(3, 640)

# Set the height of the capture frame to 480 pixels
cap.set(4, 480)

# Set the brightness of the capture frame to 100 (scale depends on the camera)
cap.set(10, 100)

# Infinite loop to continuously capture frames from the camera
while True:
    # Read a frame from the camera
    success, img = cap.read()

    # Flip the frame horizontally (mirror effect)
    img = cv2.flip(img, 1)

    # Load the pre-trained face detection classifier
    faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")

    # Convert the frame to grayscale
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale image
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

    # Draw rectangles around the detected faces
    for (x, y, w ,h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Display the frame with detected faces
    cv2.imshow("Detected Face", img)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
