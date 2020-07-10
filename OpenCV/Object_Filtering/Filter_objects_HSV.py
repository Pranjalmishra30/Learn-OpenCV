"""
Universaly HSV range is ([0-359,0-100,0-100])
But in openCV HSV range is ([0-179,0-255,0-255])
So we need to normalize it
1. For H we just need to divide by 2.
    Example-340 in U-HSV will be 170 in cv-HSV
2. For S and V we need to cv-HSV value = U-HSV(%) * 2.55
    Example-55% in U-HSV will be = 55 * 2.55 = 140.25 ~ 140
"""



import cv2
import numpy as np
import os

path='/home/pranjal/Desktop/RM/RM-Coding-kids/Pranjal/OpenCV/Object_Filtering'
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    cv2.GaussianBlur(frame,(11,11),0)
    HSV_frame=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

#For Blue Screw driver head
    #low_blue=np.array([90,80,50]) #just making an array
    #high_blue=np.array([120,255,255])

#For yellow bottle cap
    low_blue=np.array([20,100,100]) #just making an array
    high_blue=np.array([30,255,255])

    mask=cv2.inRange(HSV_frame,low_blue,high_blue) #Thresholding within limits

    kernel = np.ones((5,5),np.uint8)
    img_erosion = cv2.erode(mask, kernel, iterations=1)
    img_dilation = cv2.dilate(img_erosion, kernel, iterations=1)

    res = cv2.bitwise_and(frame,frame,mask= img_dilation)
#Contouring or outlining
    (cnts,_) = cv2.findContours(img_dilation.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(res,cnts,-1,(0,200,0),3)

    for c in cnts:
    # get the bounding rect
        x, y, w, h = cv2.boundingRect(c)
    # draw a green rectangle to visualize the bounding rect
        cv2.rectangle(res, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('C',res)
    var=cv2.waitKey(1)
    if var == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
