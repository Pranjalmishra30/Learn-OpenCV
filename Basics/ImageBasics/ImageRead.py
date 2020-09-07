import cv2 # Importing openCV library

img = cv2.imread('Basics/Data/messi.jpeg',1) # 0 for grayscale
cv2.imshow('Image',img)

# -------------------- Resizing images --------------------
# resized_img=cv2.resize(img,(650,500))
# cv2.imshow("Resized Image",resized_img)

# -------------------- Changing Colour Spaces -------------
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
hsv  = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow("Gray-Scale",gray)
cv2.imshow("HSV",hsv)


cv2.waitKey(0) # displays image for given millisceconds. if we keep it 0 then it will be open for infinity
cv2.destroyAllWindows()


#-------------EXTRA Info----------------------

# img.shape()- returns the dimensions

# To get BGR value of a pixel
    #color = img[x,y]
    #specify 0,1,2 if you want BGR separately
