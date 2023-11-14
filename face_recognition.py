import os 
import cv2 as cv
import numpy as np
from deepface import DeepFace
capture = cv.VideoCapture(0, cv.CAP_DSHOW)
capture.set(cv.CAP_PROP_FRAME_WIDTH,720)
capture.set(cv.CAP_PROP_FRAME_HEIGHT,480)

counter = 0

face_match = False

reference_img = cv.imread('reference.jpg')

while True:
    ret, frame = capture.read()
    
    if not ret:
        print("can't read the video file")

dir = r'/Users/moiznoorani/Documents/GitHub/Object-detection-system/people'
people = [ 'Ben affleck' ,'Moiz', 'Robert Downey Junior' , 'tom holland','zendaya']
features = []
labels = []
face_cascade=cv.CascadeClassifier('haar_frontal_face.xml')
def create_train():
    for person in people:
        path = os.path.join(dir, person)
        label = people.index(person)

        for img in os.listdir(path):
            if img != '.DS_Store':
                imagePath = os.path.join(path,img)
                images_array = cv.imread(imagePath)
                gray = cv.cvtColor(images_array, cv.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
                for (x,y,w,h) in faces:
                    faces_ROI = gray[y:y+h, x:x+w]
                    features.append(faces_ROI)
                    labels.append(label)
            else:
                continue



create_train()
face_recognizer = cv.face.LBPHFaceRecognizer_create()
# train the recognizer on features list anf the labels list
face_recognizer.train(np.array(features, dtype = 'object'), np.array(labels, dtype= 'object'))
print("Model Training is done")
np.save('features.npy', features)
np.save('labels.npy', labels)
