import cv2 as cv
import numpy as np

img = cv.imread("photos/cats.jpg")
cv.imshow('cats', img)
#kernel is number of rows and number of columns 
# applied to the middle pixel as a result of the surrounding pixels
# Averaging
