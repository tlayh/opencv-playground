import time
import numpy as np
import cv2

cap = cv2.VideoCapture(1)

# Define the codec and create VideoWriter object
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# todo: what codec works with osx
# out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

diffFrame = None
lastFrame = None

face_cascade = cv2.CascadeClassifier('data/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('data/haarcascades/haarcascade_eye.xml')

while cap.isOpened():
    ret, frame = cap.read()
    if ret is True:

        # make the image in grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # detect faces in frame and paint in diffFrame later
        faces = face_cascade.detectMultiScale(gray_frame, 1.3, 5)

        # blur the image
        # frame = cv2.blur(frame, (20, 20))

        if lastFrame is not None:
            diffFrame = cv2.subtract(frame, lastFrame)
            # print("DiffFrame Size:" + str(diffFrame.size))

        if diffFrame is not None:
            # mark faces in diffFrame
            for (x, y, w, h) in faces:
                diffFrame = cv2.rectangle(diffFrame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                roi_color = frame[y:y + h, x:x + w]
                roi_gray = gray_frame[y:y+h, x:x+w]
                eyes = eye_cascade.detectMultiScale(roi_gray)
                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(diffFrame, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

            # print("Showing diffFrame")
            cv2.imshow('diffFrame', diffFrame)

        lastFrame = frame
        time.sleep(.250)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()
