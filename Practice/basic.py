import cv2 as cv
img = cv.imread('photos/park.jpg')
cv.imshow("park", img)

# convert to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray park", gray)

#blur
blurred = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow("Blurred Image", blurred)

# edge cascade
canny = cv.Canny(blurred, 125, 175)
cv.imshow("Canny Edge Detection", canny)

# dilating the image
dilated = cv.dilate(canny,(7,7), iterations=3)
cv.imshow("Dilated", dilated)

# eroding 
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow("Eroded", eroded)

# resize and crop the image
resized = cv.resize(img, (1920,1080), interpolation= cv.INTER_CUBIC)
cv.imshow("resized", resized)

# cropping
cropped = img[50:200, 200:400]
cv.imshow("Cropped", cropped)

cv.waitKey(0)