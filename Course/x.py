import cv2
import numpy as np

# Read the video stream from the camera
cap = cv2.VideoCapture(0)

# Create a background subtraction object
fgbg = cv2.createBackgroundSubtractorMOG2()

# Create a while loop to continuously read frames from the camera
while True:
    # Read the next frame from the camera
    ret, frame = cap.read()

    # Apply the background subtraction algorithm to the frame
    fgmask = fgbg.apply(frame)

    # Find the contours in the foreground mask
    contours, hierarchy = cv2.findContours(fgmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Sort the contours by area in descending order
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    # Count the number of contours that are larger than a certain threshold
    num_people = 0
    for contour in contours:
        if cv2.contourArea(contour) > 1000:
            num_people += 1

    # Display the number of people on the screen
    cv2.putText(frame, "Number of people: {}".format(num_people), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the frame on the screen
    cv2.imshow("Frame", frame)

    # Check if the user has pressed the "q" key to quit
    if cv2.waitKey(1) == ord("q"):
        break

# Release the camera and close the windows
cap.release()
cv2.destroyAllWindows()