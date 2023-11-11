import cv2 as cv
import numpy as np

# threshold is binarizing of an image where we take an image and have it be either 0 or 255, black or white

img = cv.imread('practice/photos/park.jpg')
cv.imshow('park', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('gray', gray)

#simple thresholding

thresholding_value = 150
threshold ,  thresh = cv.threshold(gray, thresholding_value , 255, cv.THRESH_BINARY )
cv.imshow("Simple Threshholded", thresh)

# inverse threshold
threshold ,  thresh_inv = cv.threshold(gray, thresholding_value , 255, cv.THRESH_BINARY_INV )
cv.imshow("Simple Threshholded inverse", thresh_inv)

#Adaptive Thresholding
adaptive_threshold = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,11,9)
cv.imshow('Adaptive thresholding', adaptive_threshold)



cv.waitKey(0)