import cv2
import numpy as np
img=cv2.imread('Images/Donuts.jpeg')

blur1=cv2.GaussianBlur(img,(5,5),0) # values should be >1 and odd
blur2=cv2.GaussianBlur(img,(7,7),0)
blur3=cv2.GaussianBlur(img,(9,9),0)
blur4=cv2.GaussianBlur(img,(11,11),0)
cv2.imshow('Original',img)
cv2.imshow('Blur Level 1',blur1)
cv2.imshow('Blur Level 2',blur2)
cv2.imshow('Blur Level 3',blur3)
cv2.imshow('Blur Level 4',blur4)
cv2.waitKey(0)
cv2.destroyAllWindows()
