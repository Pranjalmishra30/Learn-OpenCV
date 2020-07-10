import cv2
import matplotlib.pyplot as plt

img=cv2.imread('Images/car.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(gray,cv2.COLOR_BGR2RGB) # Matplotlib uses RGB

ret,th1=cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY) # pixel below threshold to 0 and above to 255
ret,th2=cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV) # pixel below threshold to 255 and above to 0
ret,th3=cv2.threshold(gray, 150, 255, cv2.THRESH_TRUNC) # pixel above threshold set to threshold and others stay same
ret,th4=cv2.threshold(gray, 150, 255, cv2.THRESH_TOZERO) # pixel below threshold set to 0
ret,th5=cv2.threshold(gray, 150, 255, cv2.THRESH_TOZERO_INV)# pixel below threshold set to 255

titles = ['Original','Binary threshold','Inv Binary threshold',
         'Truncate threshold','Tozero threshold','Tozero Inv threshold']
images = [img,th1,th2,th3,th4,th5]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
