import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# todo: what codec works with osx
#out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

diffFrame = None
lastFrame = None

while (cap.isOpened()):
    ret, frame = cap.read()

    if ret is True:
        # fgmask = fgbg.apply(frame)

        if lastFrame is not None:
            diffFrame = cv2.subtract(frame, lastFrame)
            print("DiffFrame Size:" + str(diffFrame.size))

        # write the flipped frame
        # out.write(diffFrame)

        if diffFrame is not None:
            # cv2.imshow("frame", frame)
            cv2.imshow('diffFrame', diffFrame)

        k = cv2.waitKey(0)
        if k == 27:         # wait for ESC key to exit
            cv2.destroyAllWindows()
        elif k == ord('s'): # wait for 's' key to save and exit
            # Write the image
            # cv2.imwrite('messigray.png',img)
            cv2.destroyAllWindows()

    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
