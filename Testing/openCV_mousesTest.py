# Testing different click events

import numpy as np
import cv2


def draw_circle(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),50,(20,230,20),2)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),50,(200,230,20),2)

img=cv2.imread('hand.jpeg')
cv2.namedWindow('image')

cv2.setMouseCallback('image',draw_circle)
while True:
    cv2.imshow('image',img)
    var=cv2.waitKey(1)
    if var == ord('q'):
        break
cv2.destroyAllWindows()
