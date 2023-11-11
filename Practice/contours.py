import cv2 as cv
import numpy as np 

img = cv.imread('practice/photos/cats.jpg')
cv.imshow("cats", img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
# cv.imshow("Blurred", blur)

canny = cv.Canny(img, 125,175)
cv.imshow("Canny Edges", canny)

ret, thresh = cv.threshold(gray,125,255, cv.THRESH_BINARY)
cv.imshow("Thresh", thresh)

# contours python list of all coordinates of contours found in the image and hierarchies representation of contours
contours, hierarchies = cv.findContours(canny,cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found!')

cv.drawContours(blank,contours, -1 , (0,0,255), 1)
cv.imshow("Contours Drawn", blank)



cv.waitKey(0)