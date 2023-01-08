import cv2
import mediapipe as mp 
import time

cap = cv2.VideoCapture(0)
#Hand Object
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
#Method for drawing points
mp_draw = mp.solutions.drawing_utils

while True:
    success, image = cap.read()
    #Converting BGR color to RGB
    img_RGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    #Extracting hands
    results = hands.process(img_RGB)
    

    #if landmarks are detected then this block draws it on the screen
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(image, hand_landmarks,mp_hands.HAND_CONNECTIONS)

    #Showing the image
    cv2.imshow("Hand Tracking", image)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cap.destroyAllWindows()