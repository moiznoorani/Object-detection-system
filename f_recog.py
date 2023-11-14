import cv2 as cv
import face_recognition
import numpy as np

# Load a sample picture and learn how to recognize it.
known_image = face_recognition.load_image_file("people/Moiz/IMG_1195.jpeg")
known_face_encoding = face_recognition.face_encodings(known_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [known_face_encoding]
known_face_names = ["Moiz Noorani"]

# Initialize some variables
face_locations = []
face_encodings = []

# Start the webcam
capture = cv.VideoCapture(1)

while True:
    isTrue, frame = capture.read()
    rgb_frame = frame[:, :, ::-1]  # Convert the image from BGR color (which OpenCV uses) to RGB color

    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Loop through each face in this frame of video
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "Unknown"

        # If a match was found in known_face_encodings, use the first one.
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        # Draw a rectangle around the face
        cv.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

        # Draw a label with a name below the face
        cv.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv.FILLED)
        font = cv.FONT_HERSHEY_DUPLEX
        cv.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    # Display the resulting image
    cv.imshow('webcam 2', frame)

    # Hit 'd' on the keyboard to quit!
    if cv.waitKey(1) & 0xFF == ord('d'):
        break

# Release handle to the webcam
cv.waitKey(0)
capture.release()
cv.destroyAllWindows()
