# Importing necessary libraries
import cv2
import object_measurement_utility

# Reading an image
img = cv2.imread('Resources/1.jpg')

# Setting up scale and target dimensions for image processing
scale = 2
wP = 210 * scale
hP = 297 * scale

# Getting the height and width of the image
height, width = img.shape[:2]

# Infinite loop for continuous processing
while True:

    # Finding contours in the image using a utility function
    img, conts = object_measurement_utility.getContours(img, minArea=50000, filter=4)

    # Checking if any contours are found
    if len(conts) != 0:
        # Selecting the largest contour
        biggest = conts[0][2]

        # Warping the image to a standard size using the selected contour
        imgWarp = object_measurement_utility.warpIMG(img, biggest, wP, hP)

        # Finding contours in the warped image
        img2, conts2 = object_measurement_utility.getContours(imgWarp,
                                                              minArea=2000,
                                                              filter=4,
                                                              cThr=[50, 50],
                                                              draw=False)

        # Checking if any contours are found in the warped image
        if len(conts2) != 0:
            # Processing each contour in the warped image
            for obj in conts2:
                # Drawing polylines around the contours
                cv2.polylines(img2, [obj[2]], True, (0, 255, 0), 2)

                # Reordering points for accurate distance calculation
                nPoints = object_measurement_utility.reorder(obj[2])

                # Calculating width and height of the object in centimeters
                nW = round(object_measurement_utility.findDistance(nPoints[0][0]//scale, nPoints[1][0]//scale)/10, 1)
                nH = round(object_measurement_utility.findDistance(nPoints[0][0]//scale, nPoints[2][0]//scale)/10, 1)

                # Drawing arrows indicating width and height
                cv2.arrowedLine(img2, (nPoints[0][0][0], nPoints[0][0][1]), (nPoints[1][0][0], nPoints[1][0][1]),
                                (255, 0, 255), 3, 8, 0, 0.05)
                cv2.arrowedLine(img2, (nPoints[0][0][0], nPoints[0][0][1]), (nPoints[2][0][0], nPoints[2][0][1]),
                                (255, 0, 255), 3, 8, 0, 0.05)

                # Extracting object coordinates and displaying width labels
                x, y, w, h = obj[3]
                cv2.putText(img2, '{}cm'.format(nW), (x + 30, y - 10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8,
                            (255, 0, 255), 1)
                cv2.putText(img2, '{}cm'.format(nH), (x - 70, y + h //2), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8,
                            (255, 0, 255), 1)

        # Displaying the processed image with contours
        cv2.imshow('A4 Image', img2)

    # Resizing the original image for better visualization
    img = cv2.resize(img, (int(width * 0.8), int(height * 0.8)))

    # Displaying the original image with contours
    cv2.imshow("Image", img)

    # Waiting for a key press to exit the loop
    cv2.waitKey(1)
