import cv2
import numpy as np
import os

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#CascadeClassifier object and file contains the face features
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap=cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,700)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,700)
path='/home/pranjal/Desktop/RM/RM-Coding-kids/Pranjal/OpenCV/Haar_Cascade_Classifier'
i,j=0,0
while True:
    ret,img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.5,5) #Helps to find the face co-ordinates
                                                    #1.3 is scale factor . Decrease the shape value until the
                                                    #face is found . Smaller the value , greater the accuracy
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2) # Getting the coordinates for the face rectangle
        #Remove comments to use eye detection
        """
        roi_gray=gray[y:y+h,x:x+h]
        roi_color=img[y:y+h,x:x+h]
        eyes=eye_cascade.detectMultiScale(roi_gray,1.3,5)
        for ex,ey,ew,eh in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)
        """

    var=cv2.waitKey(1)
    if var == ord('q'):
        break

    #Saving screenshots for collecting images for dataset
    elif var == ord('p'):
        cv2.imwrite('Face_recognised.jpg',img)
        #cv2.imwrite(os.path.join(path,'face{}{}.png'.format('Pranjal',i)),img)
        i=i+1
    elif var == ord('d'):
        cv2.imwrite(os.path.join(path,'face{}{}.png'.format('Diwij',i)),img)
        j=j+1
    cv2.imshow('face',img)

cap.release()
cv2.destroyAllWindows()
