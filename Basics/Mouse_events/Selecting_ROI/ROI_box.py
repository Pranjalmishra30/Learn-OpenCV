import cv2

refpt = [] #List of refrence points
cropping = False # A boolean variable to toggle b/w box selecting mode

def select_roi (event,x,y,flags,param):
    global refpt , cropping #Global refrences

    if event == cv2.EVENT_LBUTTONDOWN: # When the left mouse button is cliked
        refpt = [(x,y)]
        cropping = True

    elif event == cv2.EVENT_LBUTTONUP: # When the left mouse button is released
        refpt.append((x,y)) # recording the last coordinates
        cropping = False

        cv2.rectangle(img_resized,refpt[0],refpt[1],(0,255,0),2)
        cv2.imshow('frame',img_resized)


img_resized = cv2.imread('Man_United.jpeg')
img_resized = cv2.resize(img,(200,200))

clone = img_resized.copy()
cv2.namedWindow('frame')
cv2.setMouseCallback('frame',select_roi)

while True:
    cv2.imshow('frame',img_resized)
    var = cv2.waitKey(0)

    if var == ord('s'): #For saving image
        cv2.imwrite('Selected_ROI.png',img_resized)
    elif var == ord('q'): #quit the loop
        break

# Optional : to crop the images selected
# if len(refpt)==2:
#     roi = clone[refpt[0][1]:refpt[1][1], refpt[0][0]:refpt[1][0]]
#     cv2.imshow('ROI',roi)
#     cv2.waitKey(0)

cv2.destroyAllWindows()
