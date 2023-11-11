import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('practice/photos/cats.jpg')
cv.imshow('park',img)

blank = np.zeros(img.shape[:2], dtype = 'uint8')

#grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

circle = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2),100,255,-1)
cv.imshow('Mask',circle)

mask = cv.bitwise_and(gray,circle)
cv.imshow('Mask',mask)
#grayscale histogram
gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256])
plt.figure()
plt.title('grayscale Histogram')
plt.xlabel('bins')
plt.ylabel('# of Pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()


# color histogram
plt.figure()
plt.title('Color histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b','g','r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img],[i],mask,[256],[0,256])
    plt.plot(hist, color = col)
    plt.xlim([0,256])
plt.show()


cv.waitKey(0)
