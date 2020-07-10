import cv2
import numpy as np
#Simple Video capture from webcam

cap = cv2.VideoCapture(0)
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

#-----------------Opening a video-----------------
# cap = cv2.VideoCapture('#Video_path.mp4') # Make sure to give correct path to the video file
#
# while cap.isOpened():
#     ret, frame = cap.read()
#     # if frame is read correctly ret is True
#     if not ret:
#         print("Can't receive frame (stream end?). Exiting ...")
#         break
#
#     cv2.imshow('frame', frame)
#     if cv2.waitKey(1) == ord('q'): # keep waitkey high if you want vids at slow motion
#         break
# cap.release()
# cv2.destroyAllWindows()
