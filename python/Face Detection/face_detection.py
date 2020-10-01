import numpy as np
import cv2

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')      # for detecting face
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # set Width
cap.set(4, 480)  # set Height
while True:      # infinite loop for live webcam
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(20, 20)
    )
    for (x,y,w,h) in faces:     # for making red box after detecting face
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
        roi_color = img[y:y+h, x:x+w]
    cv2.imshow('video', img)    # displaying the image continuously to show live video

    k = cv2.waitKey(100) & 0xff  # Waits for .1(100ms) second before capturing another image
    # to increase time between each capture, increase parameters in waitKey()
    if k == 27:  # Press 'ESC' for exiting program
        break  # breaks out of the loop

cap.release()
cv2.destroyAllWindows()