import cv2
import numpy as np
import imutils

img1=cv2.imread('Shapes.png')
gray=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(11,11),0) #The values need to be >1 and odd
ret, th = cv2.threshold(blur,220,255,cv2.THRESH_BINARY_INV)

(cnts,_) = cv2.findContours(th.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img1,cnts,-1,(240,0,159),3)
cv2.imshow('image',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
