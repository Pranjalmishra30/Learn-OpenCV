import cv2
import numpy as np

cap=cv2.VideoCapture(0)
while(True):
    ret,frame=cap.read()
    #Remove the comment line to use Line,Text,Rectangle or Circle

    #cv2.line(frame,(50,50),(400,50),(255,0,0),10)
    # Line (var of frame,1st end,2nd end,BGR value,thickness)

    font=cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,'Learn OpenCV',(50,50),font,1,(255,255,255),2)
    # (Starting coordinates ,font,font scale , color , thickness)

    #frame=cv2.rectangle(frame,(218,42),(538,368),(0,255,0),3)

    #frame=cv2.circle(frame,(388,254),100,(0,0,255),4) # -1 for filled circle

    cv2.imshow('frame',frame)
    if cv2.waitKey(1)  == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
