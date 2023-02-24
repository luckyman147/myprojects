import mediapipe as mp 
import cv2
import time
from HandTrackingModule import handDetector
ctime=0
ptime=0
cap = cv2.VideoCapture(0)
detector=handDetector()
while True:
        success, img = cap.read()
        img=detector.findHands(img)
        lmlist=detector.FindPosition(img)
        if len(lmlist)!=0:
            print(lmlist[4])
        ctime=time.time()
        fps=1/(ctime-ptime)
        ptime=ctime
        cv2.putText(img,"fps"+str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,
                    3,(255,0,255),2)
        cv2.imshow('Image', img)
        if cv2.waitKey(1) == ord('q'):
            break
