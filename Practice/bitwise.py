import cv2 as cv
import numpy as np 

# binary manner pixel is  off= 0 on = 1

blank = np.zeros((400,400), dtype = 'uint8')


rectangle = cv.rectangle(blank.copy(), (30,30), (370,370),255, -1 )
circle = cv.circle(blank.copy(), (200,200), 200, 255,-1)

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)


#bitwise AND --> intersecting
bitwise_AND = cv.bitwise_and(rectangle,circle)
cv.imshow("Bitwise And", bitwise_AND)

#bitwise OR --> non intersecting and intersecting 
bitwise_OR = cv.bitwise_or(rectangle,circle)
cv.imshow("Bitwise OR", bitwise_OR)


#bitwise XOR --> non intersecting 
bitwise_XOR = cv.bitwise_xor(rectangle,circle)
cv.imshow("Bitwise XOR", bitwise_XOR)


#bitwise NOT --> inverts the birany color
bitwise_NOT = cv.bitwise_not( circle)
cv.imshow("Bitwise NOT", bitwise_NOT)

cv.waitKey(0)