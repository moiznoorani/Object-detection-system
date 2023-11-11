import cv2 as cv
import numpy as np

img = cv.imread('photos/park.jpg')
cv.imshow('park', img)

#Translation

def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    print(img.shape)
    return cv.warpAffine(img, transMat, dimensions)

translated = translate(img, -100,-100)
cv.imshow('translated', translated)

# rotation

def rotate(img,angle, rotation_point = None):
    (height, width) = img.shape[:2]
    rotation_point = (width//2,height//2)
    rotation_mat = cv.getRotationMatrix2D(rotation_point,angle, 1.0)
    dimensions = (width,height)
    return cv.warpAffine(img,rotation_mat,dimensions)

rotated = rotate(img, 130)
cv.imshow("rotated", rotated)
# resizing 
resized = cv.resize(img, (img.shape[1]*4,img.shape[0]*4), interpolation=cv.INTER_CUBIC)
cv.imshow("resized image", resized)
#flipping
fliped = cv.flip(img,-1) 
cv.imshow("flipped image", fliped)
#cropping
croped = img[50:200, 60:200]
cv.imshow("cropped image", croped)

cv.waitKey(0)