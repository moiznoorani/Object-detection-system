import cv2 as cv
import numpy as np

img = cv.imread("photos/cats.jpg")
cv.imshow('cats', img)
#kernel is number of rows and number of columns 
# applied to the middle pixel as a result of the surrounding pixels
# the heigher kernel size we specify the more blur there is going to be
# Averaging
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)

#gaussian blur
#same thing as averaging, instead each surrounding pixel is given a weight 
#the average of the products of the weightgives you the value of the true center.

gausian = cv.GaussianBlur(img,(3,3),0)
cv.imshow('Gaussian Blur', gausian)
#median blur
#instead of finding the average of the surrounding pixels median blur finds the median

median = cv.medianBlur(img,3)
cv.imshow('Median Blur', median)

#bilateral blur
#the most effective/ applies bluring however retains the edges in the image as well
#sigmaspace = how far of a pixel influences the pixel we are looking at
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral Filtering', bilateral)

cv.waitKey(0)