import cv2 as cv
import numpy as np

#classifier 
#an algorithm that decides that wether an image is positive or negative
#example faces are present or not

img = cv.imread('practice/photos/group 1.jpg')
cv.imshow("group", img)

#gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('GRAY group', gray)

Haar_cascade = cv.CascadeClassifier('haar_frontal_face.xml')
faces = Haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
print(f'number of faces found = {len(faces)}')
for (x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h), (0,255,0),thickness=2)

cv.imshow('detected_faces', img )
cv.waitKey(0)