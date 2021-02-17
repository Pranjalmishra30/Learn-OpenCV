import cv2 
import numpy as np
import math as m

def mapInt(input):
    outputRange = [0,500]
    inputRange = [0,255]
    output = outputRange[0] + ((outputRange[1] - outputRange[0])/(inputRange[1] - inputRange[0]))*(input - inputRange[0])
    return int(output)

# no returns, prints details(check print statement) 
# for argument information check documents
def compute(l,r):
    
    if l == r:
        print("invalid input")
        return
    
    f = 241
    radius = 46
    centre = (0,290)
    
    (alpha, beta) = (180 + m.degrees(m.atan2(f,l)), 180 + m.degrees(m.atan2(f,r)))
    theta = (alpha - beta)/2 + beta
    delta1, delta2 = alpha - theta, theta - beta
    dist = ( radius/m.sin(m.radians(delta1)) + radius/m.sin(m.radians(delta2)) ) / 2
    pot1 = ( dist*m.cos(m.radians(theta)), dist*m.sin(m.radians(theta)))
    pot2 = ( 2*centre[0] - pot1[0], 2*centre[1] - pot1[1] )

    # print("distance to target = ", dist, "\nangle to target = ", theta, "\npot 1 coords = ",pot1, "\npot 2 coords = ", pot2 )
    print("angle = ", m.degrees(m.atan2(pot1[0] - centre[0], pot2[1] - centre[1])))


# returns a numpy array ROI
def selectROI(img, ROIrows, ROIcolumns):                      # for a 640x480 image only
    pointA = (int(320 - ROIcolumns/2),int(240 - ROIrows/2)) 
    pointC = (int(319 + ROIcolumns/2),int(239 + ROIrows/2))
    img1 = img.copy()
    ROI = img1[ pointA[1]:pointC[1] + 1, pointA[0]:pointC[0] + 1, : ]
    cv2.line(img, ( 319,235), (319,244), (0,255,0), 1)
    cv2.line(img, ( 320,235), (320,244), (0,255,0), 1)
    cv2.line(img, ( 315,239), (324,239), (0,255,0), 1)
    cv2.line(img, ( 315,240), (324,240), (0,255,0), 1)
    cv2.rectangle(img, pointA, pointC, (0,255,0), 2)
    return ROI

# plots live 1D values
def histoRed(array):
    blankPage = np.zeros((500, np.size(array), 3), np.uint8)
    
    heights = np.array(list(map(mapInt, array)))

    for c in range(0,blankPage.shape[1]):
        blankPage[0:heights[c],c] = ( 0,0,255)
    
    cv2.namedWindow('histogram Red', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('histogram Red', cv2.flip(blankPage,0))  

def histoBlue(array):
    blankPage = np.zeros((500, np.size(array), 3), np.uint8)
    
    heights = np.array(list(map(mapInt, array)))

    for c in range(0,blankPage.shape[1]):
        blankPage[0:heights[c],c] = ( 255,0,0)
    
    cv2.namedWindow('histogram Blue', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('histogram Blue', cv2.flip(blankPage,0))  
# standard stuff
#=========================================
cam = cv2.VideoCapture(0)
if not cam.isOpened():
    print('error opening camera')
    exit(0)
#=========================================

while True: 

    _,rawFrame = cam.read()  # obtain frame from camera in BGR

    displayFrame = rawFrame.copy()            
    ROI = selectROI(displayFrame, 80, 500)
    cv2.imshow('webcam feed', displayFrame)      #display the crosshairs and the drawn ROI box

    YCRCB = cv2.cvtColor( ROI, cv2.COLOR_BGR2YCR_CB)
    red, blue = YCRCB[:,:,1], YCRCB[:,:,2]             #separate 2D arrays for cR and cB
    
    redSum = np.sum(red,0)/red.shape[0]
    blueSum = np.sum(blue,0)/blue.shape[0]

    histoRed(redSum)
    histoBlue(blueSum)

    redAvg = np.sum(redSum)/redSum.shape[0]
    blueAvg = np.sum(blueSum)/blueSum.shape[0]

    for x in range(0,len(redSum)):
        if redSum[x] < redAvg:
            redSum[x] = redAvg
   
    for x in range(0,len(blueSum)):
        if blueSum[x] < blueAvg:
            blueSum[x] = blueAvg
    
    redSlope = np.vstack((np.array(range(0,len(redSum)-1)), redSum[1:len(redSum)] - redSum[0:len(redSum)-1]))

    blueSlope = np.vstack((np.array(range(0,len(redSum)-1)), blueSum[1:len(blueSum)] - blueSum[0:len(blueSum)-1]))

    redSlope = redSlope[:, np.argsort(redSlope)[1]]

    blueSlope = blueSlope[:, np.argsort(blueSlope)[1]]

    lines = ROI.copy()
    for x in [redSlope[0,0], blueSlope[0,0], redSlope[0,-1], blueSlope[0,-1]]:
        lines[:,int(x)] = (0,255,0)
        lines[:,int(x+1)] = (0,255,0)
    cv2.imshow("lines",lines)  
    
    if abs(redSlope[0,0] - redSlope[0,-1]) > abs(blueSlope[0,0] - blueSlope[0,-1]):
        l = redSlope[0,0] + 0.5 - (ROI.shape[1])/2
        r = redSlope[0,-1] + 0.5 - (ROI.shape[1])/2
    else:
        l = blueSlope[0,0] + 0.5 - (ROI.shape[1])/2
        r = blueSlope[0,-1] + 0.5 - (ROI.shape[1])/2

    compute(l,r)



    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()
