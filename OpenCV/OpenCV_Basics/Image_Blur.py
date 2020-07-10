import cv2
import matplotlib.pyplot as plt

img=cv2.imread('Images/Donuts.jpeg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) # Matplotlib uses RGB scheme

blur1=cv2.GaussianBlur(img,(5,5),0) # values should be >1 and odd
blur2=cv2.GaussianBlur(img,(9,9),0)
blur3=cv2.GaussianBlur(img,(13,13),0)
blur4=cv2.GaussianBlur(img,(17,17),0)

titles = ['Original','Blur level 1','Blur level 2','Blur level 3','Blur level 4']
images = [img,blur1,blur2,blur3,blur4]

for i in range(5):
    plt.subplot(2,3,i+1),plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
