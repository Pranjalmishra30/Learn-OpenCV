import cv2

img=cv2.imread('Images/pentagon.png')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,th=cv2.threshold(gray,200,250,cv2.THRESH_BINARY)
M = cv2.moments(th)
if M["m00"] != 0:
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])

    cv2.circle(img, (cX, cY), 3, (255, 255, 0), -1)
    cv2.imshow("Image", img)
    cv2.waitKey(0)
