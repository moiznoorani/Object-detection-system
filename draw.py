import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype = 'uint8')
cv.imshow('Blank',blank)
#1. paint the image a certain color
blank[200:300, 300:400] = 0,0,169
cv.imshow("red", blank)
#2. draw a rectangle 
cv.rectangle(blank,((blank.shape[1]//2)+50,(blank.shape[0]//2)+50),(blank.shape[1]//2,blank.shape[0]//2), (0,255,0), thickness=-1)
cv.imshow("Rectangle", blank)
#3. draw a circle
cv.circle(blank,(250,250), 100 , (0,0,200),thickness=-1)
cv.imshow("Circle", blank)

#4. draw a line

cv.line(blank,(0,0),(250,250), (253,23,250), thickness= 5)
cv.imshow("Line", blank)

#5. write text on an image

cv.putText(blank, 'Hello World! this is a whole fucking paragraph for testing', (0,225), cv.FONT_HERSHEY_TRIPLEX, .5, (0,255,0))
cv.imshow("text", blank)

cv.waitKey(0)

