import cv2

cap = cv2.VideoCapture('Basics/Data/Highway.mp4') # Make sure to give correct path to the video file

while cap.isOpened():
    ret, frame = cap.read()
    # gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # For making the video GrayScale
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    cv2.imshow('frame', frame)
    # cv2.imshow("gray frame",gray_frame)
    if cv2.waitKey(1) == ord('q'): # keep waitkey high if you want vids at slow motion
        break
cap.release()
cv2.destroyAllWindows()