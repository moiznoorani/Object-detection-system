import cv2 as cv

cat_img = cv.imread('practice/photos/cat_large.jpg')
cv.imshow("Cat", cat_img)

capture = cv.VideoCapture(1)

while True:
    isTrue, frame = capture.read()
    cv.imshow('webcam', frame)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()