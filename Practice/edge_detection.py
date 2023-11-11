import cv2 as cv
import numpy as np

img = cv.imread('practice/photos/park.jpg')
cv.imshow("Original", img)
#gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray Image", gray)

#Laplacian
#gradients of the grayscale image it gets positive and negative number but images
#cannot have neggative thats why we take the absolute and change it into
#image specific datatype

lap = cv.Laplacian(gray,cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

#sobel
sobelx = cv.Sobel(gray,cv.CV_64F,1,0)
sobely = cv.Sobel(gray,cv.CV_64F,0,1)
combined_sobel = cv.bitwise_or(sobelx,sobely)

cv.imshow('sobelx', sobelx)
cv.imshow('sobely', sobely)
cv.imshow('Combined Sobel', combined_sobel)

#Canny Edge Detection
canny = cv.Canny(gray,150,175)
cv.imshow('Cany Edge', canny)

cv.waitKey(0)