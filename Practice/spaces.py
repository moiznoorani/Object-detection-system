import cv2 as cv
import matplotlib.pyplot as plt 

img = cv.imread('practice/photos/park.jpg')
cv.imshow('park',img)
# plt.imshow(img)
# plt.show()

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#BGR to HSV

hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv)

# BGR to LAB or l*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
cv.imshow("LAB", lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB", rgb)

#HSV to BGR

HSV_BGR = cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow("HSV_to_BGR", HSV_BGR)

#LAB to BGR
LAB_BGR = cv.cvtColor(lab,cv.COLOR_Lab2BGR)
cv.imshow("LAB_to_BGR", LAB_BGR)

plt.imshow(rgb)
plt.show()



cv.waitKey(0)

