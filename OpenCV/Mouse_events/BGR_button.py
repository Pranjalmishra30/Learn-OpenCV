import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def BGR_button(event,x,y,flags,params):

    if event == cv2.EVENT_LBUTTONDOWN:  #L mouse button double click
        print("X:",x,"Y:",y)
        d = img[x,y]
        print(d)


img =cv2.imread('sample.png',1)
cv2.namedWindow('image')

cv2.setMouseCallback('image',BGR_button)

while True:
    cv2.imshow('image',img)
    var=cv2.waitKey(1)

    if var == ord('q'):
        break
cv2.destroyAllWindows()
