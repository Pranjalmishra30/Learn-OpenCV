import cv2
import numpy as np

#Mouse callback function
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),50,(200,100,0),5)


img=cv2.imread('red.jpg',1)  # Making cirle on an image
#img = np.zeros((512,512,3), np.uint8)   # Making circle on a black image

cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle) # Binding the function to window

while True :
    cv2.imshow('image',img)
    if cv2.waitKey(1)  == ord('q'):
        break
cv2.destroyAllWindows()
