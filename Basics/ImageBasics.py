import cv2
import numpy as np

img = cv2.imread('Images/messi.jpeg',1) # 0 for grayscale

cv2.imshow('image',img)
cv2.waitKey(0) # displays image for given seconds. if we keep it 0 then it will be open for infinity
cv2.destroyAllWindows()

# Resize
    #resized_img=cv2.resize(img,(650,500))

# Changing colour-spaces
    #gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #hsv  = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

# img.shape()- returns the dimensions

# To get BGR value of a pixel
    #color = img[x,y]
    #specify 0,1,2 if you want BGR separately
