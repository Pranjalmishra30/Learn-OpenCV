import cv2
import argparse
















#-------------Argument Parser----------------
# import math
# def volume_cone (radius , height):
#     v = (1/3)* math.pi * (radius**2)* height
#     return v
#
# parser = argparse.ArgumentParser(description="Calculate volume of a cone")
# parser.add_argument('-r','--Radius',type=float,help='Radius of cone') # These are now optional arguments
# parser.add_argument('-H','--Height',type=float,help='Height of cone')
# args  = parser.parse_args()
#
# print(volume_cone(args.Radius,args.Height))




#-----------------Opening a video-----------------
# cap = cv2.VideoCapture('videos/Bruno_goal.mp4')
# while cap.isOpened():
#     ret, frame = cap.read()
#     # if frame is read correctly ret is True
#     if not ret:
#         print("Can't receive frame (stream end?). Exiting ...")
#         break
#
#     cv2.imshow('frame', frame)
#     if cv2.waitKey(35) == ord('q'): # keep waitkey high if you want vids at slow motion
#         break
# cap.release()
# cv2.destroyAllWindows()
