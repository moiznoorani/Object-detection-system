import cv2 as cv

img = cv.imread('photos/cat.jpg')
cv.imshow('Cat', img)


def rescaleFrame(frame, scale = 0.75):
    #images, videos and live videos 
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes (width, height):
    #live video
    capture.set(3,width)
    capture.set(4,height)


resized_img = rescaleFrame(img, 2)
cv.imshow("Resized image", resized_img)

capture = cv.VideoCapture(1)
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, .2)
    cv.imshow("Webcam Feed", frame)
    cv.imshow('webcam resized', frame_resized)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
