import cv2 as cv
import numpy as np


#detect faces in a video
capture =cv.VideoCapture(1)

while True:
    isTrue, frame = capture.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    face_cascade=cv.CascadeClassifier('haar_frontal_face.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
    for (x,y,w,h) in faces:
        cv.rectangle(frame,(x,y),(x+w,y+h), (0,255,0),thickness=2)
    cv.imshow('webcam 2', frame)
    
    if cv.waitKey(1) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()