import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    #capturing the height and width of the frame.
    width = int(cap.get(3))
    height = int(cap.get(4))

    #Converting the image from BGR to HSV.
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #Defining the color that we want to detect
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])

    #Creating a mask of color to be detected
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    #Creating the final image after selecting the colors of the required pixels
    #using bitwise and operation. 
    result = cv2.bitwise_and(frame, frame, mask=mask)

    #Displaying the final result 
    cv2.imshow('frame', result)
    cv2.imshow('mask', mask)

    #The frame will be closed when the key 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()