import cv2
import numpy as np
import time

fourCC = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourCC, 20, (200, 200))

cap = cv2.VideoCapture(0)
time.sleep(3)

count = 0
background = None  # Initialize background to None

for i in range(60):
    returnV, background = cap.read()

    if not returnV or background is None:
        # Handle the case where the background is not successfully captured
        print("Error capturing background.")
        break

background = np.flip(background, axis=1)

while cap.isOpened():
    returnV, img = cap.read()

    if not returnV:
        break

    count += 1
    img = np.flip(img, axis=1)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0, 120, 50])
    upper_red = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)

    lower_red = np.array([170, 120, 50])
    upper_red = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red, upper_red)

    mask1 += mask2

    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))

    mask2 = cv2.bitwise_not(mask1)
    result1 = cv2.bitwise_and(img, img, mask=mask2)
    result2 = cv2.bitwise_and(background, background, mask=mask1)

    finalOutput = cv2.addWeighted(result1, 1, result2, 1, 0)

    out.write(finalOutput)

    cv2.imshow('Magic!', finalOutput)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
