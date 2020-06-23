import cv2
import numpy as np

img=cv2.imread('Images/car.jpg')

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,th1=cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY) # pixel below threshold to 0 and above to 255
ret,th2=cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV) # pixel below threshold to 255 and above to 0
ret,th3=cv2.threshold(gray, 150, 255, cv2.THRESH_TRUNC) # pixel above threshold set to threshold and others stay same
ret,th4=cv2.threshold(gray, 150, 255, cv2.THRESH_TOZERO) # pixel below threshold set to 0
ret,th5=cv2.threshold(gray, 150, 255, cv2.THRESH_TOZERO_INV)# pixel below threshold set to 255
cv2.imshow('Original',img)
cv2.imshow('Thresh Level 1',th1)
cv2.imshow('Thresh Level 2',th2)
cv2.imshow('Thresh Level 3',th3)
cv2.imshow('Thresh Level 4',th4)
cv2.imshow('Thresh Level 5',th5)
cv2.waitKey(0)
cv2.destroyAllWindows()
